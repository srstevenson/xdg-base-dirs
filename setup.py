"""Setup module for xdg."""

from pathlib import Path

from setuptools import setup


def read_long_description() -> str:
    """Read from README.md file in root of source directory."""
    root = Path(__file__).resolve().parent
    readme = root / 'README.md'
    return readme.read_text(encoding='utf-8')  # pylint: disable=no-member


setup(
    name='xdg',
    version='3.0.2',
    description='Variables defined by the XDG Base Directory Specification',
    long_description=read_long_description(),
    long_description_content_type='text/markdown',
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
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='xdg base directory specification',
    py_modules=['xdg'],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ],
)
