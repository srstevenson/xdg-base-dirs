# xdg

`xdg` is a tiny Python module which provides the variables defined by the [XDG
Base Directory Specification][spec], to save you from duplicating the same
snippet of logic in every Python utility you write that deals with user cache,
configuration, or data files. It has no external dependencies.

## Installation

To install the latest release from [PyPI], use [pip]:

```bash
pip install xdg
```

In Python projects using [Poetry] or [Pipenv] for dependency management, add
`xdg` as a dependency with `poetry add xdg` or `pipenv install xdg`.
Alternatively, since `xdg` is only a single file you may prefer to just copy
`src/xdg/__init__.py` from the source distribution into your project.

## Usage

```python
from xdg import (XDG_CACHE_HOME, XDG_CONFIG_DIRS, XDG_CONFIG_HOME,
                 XDG_DATA_DIRS, XDG_DATA_HOME, XDG_RUNTIME_DIR)
```

`XDG_CACHE_HOME`, `XDG_CONFIG_HOME`, and `XDG_DATA_HOME` are [`pathlib.Path`
objects][path] containing the value of the environment variable of the same
name, or the default defined in the specification if the environment variable is
unset or empty.

`XDG_CONFIG_DIRS` and `XDG_DATA_DIRS` are lists of `pathlib.Path` objects
containing the value of the environment variable of the same name split on
colons, or the default defined in the specification if the environment variable
is unset or empty.

`XDG_RUNTIME_DIR` is a `pathlib.Path` object containing the value of the
environment variable of the same name, or `None` if the environment variable is
unset.

## Copyright

Copyright © 2016-2019 [Scott Stevenson].

`xdg` is distributed under the terms of the [ISC licence].

[isc licence]: https://opensource.org/licenses/ISC
[path]: https://docs.python.org/3/library/pathlib.html#pathlib.Path
[pip]: https://pip.pypa.io/en/stable/
[pipenv]: https://docs.pipenv.org/
[poetry]: https://poetry.eustace.io/
[pypi]: https://pypi.org/project/xdg/
[scott stevenson]: https://scott.stevenson.io
[spec]: https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
