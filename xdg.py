"""XDG Base Directory Specification variables.

XDG_CACHE_HOME, XDG_CONFIG_HOME, and XDG_DATA_HOME are strings
containing the value of the environment variable of the same name, or
the default defined in the specification if the environment variable is
unset or empty.

XDG_CONFIG_DIRS and XDG_DATA_DIRS are lists of strings containing the
value of the environment variable of the same name split on colons, or
the default defined in the specification if the environment variable is
unset or empty.

XDG_RUNTIME_DIR is a string containing the value of the environment
variable of the same name, or None if the environment variable is not
set.
"""

# Copyright © 2016-2018 Scott Stevenson <scott@stevenson.io>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

import os

__all__ = [
    'XDG_CACHE_HOME', 'XDG_CONFIG_DIRS', 'XDG_CONFIG_HOME', 'XDG_DATA_DIRS',
    'XDG_DATA_HOME', 'XDG_RUNTIME_DIR'
]


def _getenv(variable: str, default: str) -> str:
    """Get an environment variable.

    Parameters
    ----------
    variable : str
        The environment variable.
    default : str
        A default value that will be returned if the environment
        variable is unset or empty.

    Returns
    -------
    str
        The value of the environment variable, or the default value.

    """
    return os.environ.get(variable) or default


XDG_CACHE_HOME = _getenv('XDG_CACHE_HOME',
                         os.path.expandvars(os.path.join('$HOME', '.cache')))
XDG_CONFIG_DIRS = _getenv('XDG_CONFIG_DIRS', '/etc/xdg').split(':')
XDG_CONFIG_HOME = _getenv('XDG_CONFIG_HOME',
                          os.path.expandvars(os.path.join('$HOME', '.config')))
XDG_DATA_DIRS = _getenv('XDG_DATA_DIRS',
                        '/usr/local/share/:/usr/share/').split(':')
XDG_DATA_HOME = _getenv('XDG_DATA_HOME',
                        os.path.expandvars(
                            os.path.join('$HOME', '.local', 'share')))
XDG_RUNTIME_DIR = os.getenv('XDG_RUNTIME_DIR')
