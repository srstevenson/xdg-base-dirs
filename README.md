# xdg-base-dirs

[![License](https://img.shields.io/github/license/srstevenson/xdg-base-dirs?label=License&color=blue)](https://github.com/srstevenson/xdg-base-dirs/blob/main/LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/srstevenson/xdg-base-dirs?label=GitHub)](https://github.com/srstevenson/xdg-base-dirs)
[![PyPI version](https://img.shields.io/pypi/v/xdg-base-dirs?label=PyPI)](https://pypi.org/project/xdg-base-dirs/)
[![Python versions](https://img.shields.io/pypi/pyversions/xdg-base-dirs?label=Python)](https://pypi.org/project/xdg-base-dirs/)
[![CI status](https://github.com/srstevenson/xdg-base-dirs/workflows/CI/badge.svg)](https://github.com/srstevenson/xdg-base-dirs/actions)
[![Coverage](https://img.shields.io/codecov/c/gh/srstevenson/xdg-base-dirs?label=Coverage)](https://app.codecov.io/gh/srstevenson/xdg-base-dirs)

`xdg-base-dirs` is a Python module that provides functions to return paths to
the directories defined by the [XDG Base Directory Specification][spec], to save
you from duplicating the same snippet of logic in every Python utility you write
that deals with user cache, configuration, or data files. It has no external
dependencies.

> [!NOTE]
>
> `xdg-base-dirs` was previously named `xdg`, and was renamed due to an import
> collision with [`PyXDG`](https://pypi.org/project/pyxdg/). If you used `xdg`
> prior to the rename, update by changing the dependency name from `xdg` to
> `xdg-base-dirs` and the import from `xdg` to `xdg_base_dirs`.

## Installation

To install the latest release from [PyPI], use [pip]:

```bash
python3 -m pip install xdg-base-dirs
```

The latest release of `xdg-base-dirs` currently implements version 0.8 of the
specification, released on 8th May 2021.

In Python projects using [Poetry] or [PDM] for dependency management, add
`xdg-base-dirs` as a dependency with `poetry add xdg-base-dirs` or
`pdm add xdg-base-dirs`. Alternatively, since `xdg-base-dirs` is only a single
file you may prefer to just copy `src/xdg_base_dirs/__init__.py` from the source
distribution into your project.

## Usage

```python
from xdg_base_dirs import (
    xdg_cache_home,
    xdg_config_dirs,
    xdg_config_home,
    xdg_data_dirs,
    xdg_data_home,
    xdg_runtime_dir,
    xdg_state_home,
)
```

`xdg_cache_home()`, `xdg_config_home()`, `xdg_data_home()`, and
`xdg_state_home()` return [`pathlib.Path` objects][path] containing the value of
the environment variable named `XDG_CACHE_HOME`, `XDG_CONFIG_HOME`,
`XDG_DATA_HOME`, and `XDG_STATE_HOME` respectively, or the default defined in
the specification if the environment variable is unset, empty, or contains a
relative path rather than absolute path.

`xdg_config_dirs()` and `xdg_data_dirs()` return a list of `pathlib.Path`
objects containing the value, split on colons, of the environment variable named
`XDG_CONFIG_DIRS` and `XDG_DATA_DIRS` respectively, or the default defined in
the specification if the environment variable is unset or empty. Relative paths
are ignored, as per the specification.

`xdg_runtime_dir()` returns a `pathlib.Path` object containing the value of the
`XDG_RUNTIME_DIR` environment variable, or `None` if the environment variable is
not set, or contains a relative path rather than an absolute path.

## Copyright

Copyright © [Scott Stevenson].

`xdg-base-dirs` is distributed under the terms of the [ISC license].

[isc license]: https://opensource.org/licenses/ISC
[path]: https://docs.python.org/3/library/pathlib.html#pathlib.Path
[pdm]: https://pdm.fming.dev/
[pip]: https://pip.pypa.io/en/stable/
[poetry]: https://python-poetry.org/
[pypi]: https://pypi.org/project/xdg-base-dirs/
[scott stevenson]: https://scott.stevenson.io
[spec]:
  https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
