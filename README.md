# xdg

`xdg` is a Python module which provides functions to return paths to the
directories defined by the [XDG Base Directory Specification][spec], to save you
from duplicating the same snippet of logic in every Python utility you write
that deals with user cache, configuration, or data files. It has no external
dependencies.

## Installation

To install the latest release from [PyPI], use [pip]:

```bash
python -m pip install xdg
```

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
)
```

`xdg_cache_home()`, `xdg_config_home()`, and `xdg_data_home()` return
[`pathlib.Path` objects][path] containing the value of the environment variable
named `XDG_CACHE_HOME`, `XDG_CONFIG_HOME`, and `XDG_DATA_HOME` respectively, or
the default defined in the specification if the environment variable is unset or
empty.

`xdg_config_dirs()` and `xdg_data_dirs()` return a list of `pathlib.Path`
objects containing the value, split on colons, of the environment variable named
`XDG_CONFIG_DIRS` and `XDG_DATA_DIRS` respectively, or the default defined in
the specification if the environment variable is unset or empty.

`xdg_runtime_dir()` returns a `pathlib.Path` object containing the value of the
`XDG_RUNTIME_DIR` environment variable, or `None` if the environment variable is
not set.

## Copyright

Copyright © 2016-2020 [Scott Stevenson].

`xdg` is distributed under the terms of the [ISC licence].

[isc licence]: https://opensource.org/licenses/ISC
[path]: https://docs.python.org/3/library/pathlib.html#pathlib.Path
[pip]: https://pip.pypa.io/en/stable/
[pipenv]: https://docs.pipenv.org/
[poetry]: https://python-poetry.org/
[pypi]: https://pypi.org/project/xdg/
[scott stevenson]: https://scott.stevenson.io
[spec]: https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
