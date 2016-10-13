xdg
===

.. image:: https://img.shields.io/travis/srstevenson/xdg.svg?maxAge=2592000
	   :target: https://travis-ci.org/srstevenson/xdg

.. image:: https://img.shields.io/github/tag/srstevenson/xdg.svg?maxAge=2592000
	   :target: https://github.com/srstevenson/xdg/releases

.. image:: https://img.shields.io/pypi/v/xdg.svg?maxAge=2592000
	   :target: https://pypi.python.org/pypi/xdg/

``xdg`` is a tiny Python module which provides the variables defined by the
`XDG Base Directory Specification`_, to save you from duplicating the same
snippet of logic in every Python utility you write that deals with user cache,
configuration, or data files. It has no external dependencies and supports
Python 2 and 3.

.. _`XDG Base Directory Specification`: https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html

Installation
------------

To install the latest release from `PyPI`_, use `pip`_:

.. code-block:: bash

    pip install xdg

Alternatively, since ``xdg`` is only a single file you may prefer to just copy
``xdg.py`` from the source distribution into your project.

.. _`pip`: https://pip.pypa.io/
.. _`PyPI`: https://pypi.python.org/pypi/xdg

Usage
-----

.. code-block:: python

    from xdg import (XDG_CACHE_HOME, XDG_CONFIG_DIRS, XDG_CONFIG_HOME,
                     XDG_DATA_DIRS, XDG_DATA_HOME, XDG_RUNTIME_DIR)

``XDG_CACHE_HOME``, ``XDG_CONFIG_HOME``, and ``XDG_DATA_HOME`` are strings
containing the value of the environment variable of the same name, or the
default defined in the specification if the environment variable is unset or
empty.

``XDG_CONFIG_DIRS`` and ``XDG_DATA_DIRS`` are lists of strings containing the
value of the environment variable of the same name split on colons, or the
default defined in the specification if the environment variable is unset or
empty.

``XDG_RUNTIME_DIR`` is a string containing the value of the environment
variable of the same name, or ``None`` if the environment variable is unset.

Copyright
---------

Copyright © 2016 `Scott Stevenson`_.

``xdg`` is distributed under the terms of the `ISC licence`_.

.. _`ISC licence`: https://opensource.org/licenses/ISC
.. _`Scott Stevenson`: https://scott.stevenson.io
