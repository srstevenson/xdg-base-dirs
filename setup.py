"""Setup module for xdg"""

import os.path
from setuptools import setup


def source_root_dir():
    """Return the path to the root of the source distribution"""
    return os.path.abspath(os.path.dirname(__file__))


def read_long_description():
    """Read from README.rst file in root of source directory"""
    readme = os.path.join(source_root_dir(), 'README.rst')
    with open(readme) as fin:
        return fin.read()


setup(
    name='xdg',
    version='1.0.3',
    description='Variables defined by the XDG Base Directory Specification',
    long_description=read_long_description(),
    url='https://github.com/srstevenson/xdg',
    author='Scott Stevenson',
    author_email='scott@stevenson.io',
    license='ISC',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='xdg base directory specification',
    py_modules=['xdg'],
)
