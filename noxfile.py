"""Nox configuration."""

import os
import pathlib

import nox

SOURCES = ["noxfile.py", "src", "test"]


def list_source_files() -> list[str]:
    """Expand directories in SOURCES to constituent files."""
    paths = [path for path in SOURCES if pathlib.Path(path).is_file()]
    paths.extend(
        [
            os.fspath(path)
            for source in SOURCES
            for path in pathlib.Path(source).rglob("*.py")
            if pathlib.Path(source).is_dir()
        ]
    )
    return paths


@nox.session
def mypy(session: nox.Session) -> None:
    """Type check code with mypy."""
    session.run(
        "mypy", "--show-error-codes", "--strict", *SOURCES, external=True
    )


@nox.session
def flake8(session: nox.Session) -> None:
    """Lint code with Flake8."""
    session.run("flake8", *SOURCES, external=True)


@nox.session
def pylint(session: nox.Session) -> None:
    """Lint code with Pylint."""
    session.run("pylint", *SOURCES, external=True)


@nox.session
def isort(session: nox.Session) -> None:
    """Check import ordering with isort."""
    session.run("isort", "--check", *SOURCES, external=True)


@nox.session
def black(session: nox.Session) -> None:
    """Check code formatting with black."""
    session.run("black", "--check", *SOURCES, external=True)


@nox.session
def pyupgrade(session: nox.Session) -> None:
    """Check Python syntax with pyupgrade."""

    # pyupgrade does not support passing directories as command line arguments
    # so we must construct a list of input filenames.
    session.run(
        "pyupgrade", "--py310-plus", *list_source_files(), external=True
    )


@nox.session
def pytest(session: nox.Session) -> None:
    """Check code formatting with black."""
    session.run("pytest", "--cov=xdg_base_dirs", "test", external=True)
