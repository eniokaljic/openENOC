<!--
SPDX-FileCopyrightText: 2026 Enio Kaljic
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Hardware Libraries

This directory contains external hardware libraries used by openENOC.

## taxi Submodule

The `taxi` library is included as a Git submodule under:

```text
hw/libs/taxi
```

It is fetched from:

```text
git@github.com:alexforencich/taxi.git
```

After cloning the repository, initialize the submodule from the repository root with:

```sh
git submodule update --init hw/libs/taxi
```

Alternatively, when cloning the repository for the first time, use:

```sh
git clone --recurse-submodules <repository-url>
```

To update the submodule to the commit recorded by the main repository, run:

```sh
git submodule update --init --recursive
```

The submodule should remain checked out at the revision tracked by openENOC unless an intentional library update is being performed.
