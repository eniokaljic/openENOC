# SPDX-FileCopyrightText: 2026 Tarik Hamedovic
# SPDX-License-Identifier: CC-BY-SA-4.0

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'openENOC'
copyright = '2026, openENOC\'s contributors. For detailed authorship, please refer to the SPDX headers in the source code of individual files'
author = 'openENOC\'s contributors'
release = '0.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_logo = '../images/openENOC.logo.svg'
html_theme_options = {
    'logo_only': True,
}
html_static_path = ['_static']
html_css_files = [
    "custom.css",
]
