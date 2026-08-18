<!--
SPDX-FileCopyrightText: 2026 Enio Kaljic
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Hardware Libraries

This directory contains external hardware libraries used by openENOC.

## taxi Submodule

The `taxi` library is included as a Git submodule under:

```text
libs/taxi
```

It is fetched from:

```text
git@github.com:alexforencich/taxi.git
```

After cloning the repository, initialize the submodule from the repository root with:

```sh
git submodule update --init libs/taxi
```

## picorv32 Submodule

The `picorv32` library is included as a Git submodule under:

```text
libs/picorv32
```

It is fetched from:

```text
git@github.com:YosysHQ/picorv32.git
```

After cloning the repository, initialize the submodule from the repository root with:

```sh
git submodule update --init libs/picorv32
```

## Batch Initialization

Alternatively, when cloning the repository for the first time, use:

```sh
git clone --recurse-submodules git@github.com:eniokaljic/openENOC.git
```

To update the submodules to the commits recorded by the main repository, run:

```sh
git submodule update --init --recursive
```

The submodules should remain checked out at the revisions tracked by openENOC
unless an intentional library update is being performed.
