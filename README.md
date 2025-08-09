# xdg-base-dirs

xdg-base-dirs is a Python module that provides functions to return paths to the
directories defined by the [XDG Base Directory Specification][spec], to save you
from duplicating the same snippet of logic in every Python utility you write
that deals with user cache, configuration, or data files. It has no external
dependencies and consists of a single file, making it easy to integrate.

xdg-base-dirs currently implements version 0.8 of the specification, released on
8th May 2021.

> [!NOTE]
>
> xdg-base-dirs was previously named xdg, and was renamed due to an import
> collision with [PyXDG](https://pypi.org/project/pyxdg/). If you used xdg prior
> to the rename, update by changing the dependency name from xdg to
> xdg-base-dirs, and the import from `xdg` to `xdg_base_dirs`.

## Installation

xdg-base-dirs requires Python 3.10 or later. To add xdg-base-dirs as a
dependency to a project managed with [uv], use:

```bash
uv add xdg-base-dirs
```

Alternatively, since xdg-base-dirs is only a single file you may prefer to just
copy `src/xdg_base_dirs/__init__.py` from the source distribution into your
project.

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
`xdg_state_home()` return [`pathlib.Path` objects][pathlib] containing the value
of the environment variable named `XDG_CACHE_HOME`, `XDG_CONFIG_HOME`,
`XDG_DATA_HOME`, and `XDG_STATE_HOME` respectively, or the default defined in
the specification if the environment variable is unset, empty, or contains a
relative path. Only absolute paths are considered valid; any relative path
causes the function to return the specification's default value.

`xdg_config_dirs()` and `xdg_data_dirs()` return a list of `pathlib.Path`
objects containing the values from the colon-separated environment variables
`XDG_CONFIG_DIRS` and `XDG_DATA_DIRS` respectively. These variables define
search paths where multiple directories can be specified. When parsing the
colon-separated values, relative paths are filtered out entirely. If the
environment variable is unset, empty, or contains only relative paths, the
specification's default list is returned instead.

`xdg_runtime_dir()` returns a `pathlib.Path` object containing the value of the
`XDG_RUNTIME_DIR` environment variable, or `None` if the environment variable is
not set or contains a relative path. Unlike the other functions, this returns
`None` rather than a default path because the XDG specification requires this
directory to be provided by the system runtime environment.

All returned paths are used exactly as specified in the environment variables or
defaults, without additional normalisation or resolution of symbolic links. This
preserves the original paths as intended by the system configuration.

## Copyright

Copyright © Scott Stevenson.

xdg-base-dirs is distributed under the terms of the [ISC license].

[isc license]: https://opensource.org/licenses/ISC
[pathlib]: https://docs.python.org/3/library/pathlib.html#pathlib.Path
[spec]: https://specifications.freedesktop.org/basedir-spec/latest/
[uv]: https://docs.astral.sh/uv/
