# xdg

[![Licence](https://img.shields.io/github/license/srstevenson/xdg?label=Licence&color=blue)](https://github.com/srstevenson/xdg/blob/main/LICENCE)
[![GitHub release](https://img.shields.io/github/v/release/srstevenson/xdg?label=GitHub)](https://github.com/srstevenson/xdg)
[![PyPI version](https://img.shields.io/pypi/v/xdg?label=PyPI)](https://pypi.org/project/xdg/)
[![Python versions](https://img.shields.io/pypi/pyversions/xdg?label=Python)](https://pypi.org/project/xdg/)
[![CI status](https://github.com/srstevenson/xdg/workflows/CI/badge.svg)](https://github.com/srstevenson/xdg/actions)
[![Coverage](https://img.shields.io/codecov/c/gh/srstevenson/xdg?label=Coverage)](https://app.codecov.io/gh/srstevenson/xdg)

`xdg` is a Python module which provides functions to return paths to the
directories defined by the [XDG Base Directory Specification][spec], to save you
from duplicating the same snippet of logic in every Python utility you write
that deals with user cache, configuration, or data files. It has no external
dependencies.

## Installation

To install the latest release from [PyPI], use [pip]:

```bash
python3 -m pip install xdg
```

The latest release of `xdg` currently implements version 0.8 of the
specification, released on 8th May 2021.

In Python projects using [Poetry] or [Pipenv] for dependency management, add
`xdg` as a dependency with `poetry add xdg` or `pipenv install xdg`.
Alternatively, since `xdg` is only a single file you may prefer to just copy
`src/xdg/__init__.py` from the source distribution into your project.

## Usage

```python
from xdg import (
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
not set, or contains a relative path rather than absolute path.

## Copyright

Copyright © 2016-2021 [Scott Stevenson].

`xdg` is distributed under the terms of the [ISC licence].

[isc licence]: https://opensource.org/licenses/ISC
[path]: https://docs.python.org/3/library/pathlib.html#pathlib.Path
[pip]: https://pip.pypa.io/en/stable/
[pipenv]: https://docs.pipenv.org/
[poetry]: https://python-poetry.org/
[pypi]: https://pypi.org/project/xdg/
[scott stevenson]: https://scott.stevenson.io
[spec]:
  https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
