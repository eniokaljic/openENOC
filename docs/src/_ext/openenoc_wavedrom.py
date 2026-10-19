# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: CC-BY-SA-4.0

"""Apply per-lane data styles and multiline labels to WaveDrom diagrams."""

from copy import deepcopy
import json
import math
import re

from sphinxcontrib import wavedrom_render_image
from svgwrite.text import TSpan
from wavedrom import fixQuotes


_wavedrom_render = wavedrom_render_image.render
_WAVEFORM_HEIGHT = 20
_ROW_SPACING = 30
_DEFAULT_FONT_SIZE = 11 * 96 / 72


def _font_size(style):
    """Read a CSS font-size length for calculating text spacing and lane height."""
    if not isinstance(style, str):
        raise ValueError("WaveDrom signal style must be a CSS string")
    size = _DEFAULT_FONT_SIZE
    important = False
    for declaration in style.split(";"):
        property_name, separator, value = declaration.partition(":")
        if not separator or property_name.strip().lower() != "font-size":
            continue
        match = re.fullmatch(
            r"(\d+(?:\.\d+)?|\.\d+)(px|pt)(?:\s*!\s*(important))?", value.strip(), re.I
        )
        if not match or float(match[1]) <= 0:
            raise ValueError("WaveDrom data font-size must be a positive px or pt length")
        if important and not match[3]:
            continue
        size = float(match[1]) * (96 / 72 if match[2].lower() == "pt" else 1)
        important = bool(match[3])
    return size


def _label_height(label, font_size, spacing):
    line_count = len(label.split("\n"))
    required = math.ceil(font_size + 5) + (line_count - 1) * spacing
    extra_rows = max(0, math.ceil((required - _WAVEFORM_HEIGHT) / _ROW_SPACING))
    return _WAVEFORM_HEIGHT + extra_rows * _ROW_SPACING


def _pad_label_lanes(signals, layouts):
    """Reserve native rows for the number of text lines in each lane."""
    padded = []
    for signal in signals:
        if isinstance(signal, list):
            padded.append([signal[0], *_pad_label_lanes(signal[1:], layouts)])
        elif isinstance(signal, dict):
            style = signal.get("style", "")
            font_size = _font_size(style)
            spacing = math.ceil(font_size + 3)
            labels = signal.get("data") or []
            if isinstance(labels, str):
                labels = labels.split()
                signal["data"] = labels
            height = max(
                (
                    _label_height(label, font_size, spacing)
                    for label in labels
                    if isinstance(label, str)
                ),
                default=_WAVEFORM_HEIGHT,
            )
            layouts.append((height, style, spacing))
            padded.append(signal)
            for _ in range((height - _WAVEFORM_HEIGHT) // _ROW_SPACING):
                padded.append({})
                layouts.append((_WAVEFORM_HEIGHT, "", math.ceil(_DEFAULT_FONT_SIZE + 3)))
    return padded


def _stretch_path(data, height):
    """Stretch the skin's coordinate pairs without scaling their stroke widths."""
    tokens = re.findall(r"[A-Za-z]|[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?", data)
    coordinate = 0
    for index, token in enumerate(tokens):
        if token.isalpha():
            if token not in "MmLlCcZz":
                raise ValueError(f"Unsupported WaveDrom skin path command: {token}")
            coordinate = 0
        else:
            if coordinate % 2:
                tokens[index] = f"{float(token) * height / _WAVEFORM_HEIGHT:g}"
            coordinate += 1
    return " ".join(tokens)


def _resized_symbol(symbol, height, drawing, symbols):
    identifier = f"{symbol[1:]}-height-{height}"
    if identifier not in symbols:
        stretched = deepcopy(symbols[symbol[1:]])
        stretched["id"] = identifier
        for element in stretched.elements:
            if element.elementname == "path":
                element.commands = [_stretch_path(element.attribs["d"], height)]
        drawing.defs.add(stretched)
        symbols[identifier] = stretched
    return "#" + identifier


def _resize_lane(lane, height, drawing, symbols):
    elements = [lane]
    while elements:
        element = elements.pop()
        elements.extend(getattr(element, "elements", ()))
        if element.elementname == "use":
            element.set_href(_resized_symbol(element["xlink:href"], height, drawing, symbols))
        elif element.elementname == "text":
            element["y"] = float(element["y"]) + (height - _WAVEFORM_HEIGHT) / 2


def _format_lane_labels(lane, style, spacing):
    formatted = False
    for child in list(lane.elements):
        if child.elementname != "text" or len(child.elements) != 1:
            continue
        label = getattr(child.elements[0], "text", None)
        if not isinstance(label, str):
            continue
        lines = label.split("\n")
        if not style and len(lines) == 1:
            continue
        formatted = True
        if style:
            # Inline CSS takes precedence over the skin's text font-size rule.
            child["style"] = style
        child.elements = [
            TSpan(
                line,
                x=[child["x"]],
                y=[float(child["y"]) + (index - (len(lines) - 1) / 2) * spacing],
            )
            for index, line in enumerate(lines)
        ]
        background = deepcopy(child)
        background["style"] = (
            style.rstrip(";") + ";fill:white;stroke:white;stroke-width:2px;stroke-linejoin:round"
        )
        lane.elements.insert(lane.elements.index(child), background)
    return formatted


def _render_wavedrom_with_label_fonts(source="", output=None, strict_js_features=False):
    specification = json.loads(fixQuotes(source))
    layouts = []
    if specification.get("signal"):
        specification["signal"] = _pad_label_lanes(specification["signal"], layouts)
    drawing = _wavedrom_render(
        json.dumps(specification), [] if output is None else output, strict_js_features
    )
    symbols = {element["id"]: element for element in drawing.defs.elements if "id" in element.attribs}
    elements = [drawing]
    has_formatted_labels = False
    while elements:
        element = elements.pop()
        elements.extend(getattr(element, "elements", ()))
        lane = re.fullmatch(r"(?:wavelane|wavegap)_(\d+)_\d+", element.attribs.get("id", ""))
        if lane and layouts[int(lane[1])][0] > _WAVEFORM_HEIGHT:
            _resize_lane(element, layouts[int(lane[1])][0], drawing, symbols)
        lane_draw = re.fullmatch(r"wavelane_draw_(\d+)_\d+", element.attribs.get("id", ""))
        if lane_draw:
            height, style, spacing = layouts[int(lane_draw[1])]
            has_formatted_labels |= _format_lane_labels(element, style, spacing)
    if has_formatted_labels:
        width = float(drawing["width"]) + 40
        height = float(drawing["height"]) + 10
        drawing["width"] = width
        drawing["height"] = height
        drawing.viewbox(0, 0, width, height)
    return drawing


def setup(app):
    app.setup_extension("sphinxcontrib.wavedrom")
    wavedrom_render_image.render = _render_wavedrom_with_label_fonts
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
