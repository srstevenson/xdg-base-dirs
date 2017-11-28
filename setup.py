"""Setup module for xdg."""

from pathlib import Path

from setuptools import setup


def read_long_description():
    """Read from README.rst file in root of source directory."""
    root = Path(__file__).resolve().parent
    readme = root / 'README.rst'
    return readme.read_text()


setup(
    name='xdg',
    version='2.0.0',
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
        'Programming Language :: Python :: 3.6',
    ],
    keywords='xdg base directory specification',
    py_modules=['xdg'],
)
