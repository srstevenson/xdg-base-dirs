"""Test suite for xdg."""

import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Callable

import pytest  # pylint: disable=import-error

# pylint: disable=import-error,unused-import
if TYPE_CHECKING:
    from _pytest.monkeypatch import MonkeyPatch  # noqa
# pylint: enable=import-error,unused-import

HOME_DIR = Path("/homedir")


@pytest.fixture  # type: ignore
def unimport() -> None:
    """Ensure xdg is absent from sys.modules."""
    try:
        del sys.modules["xdg"]
    except KeyError:
        pass


# pylint: disable=no-self-use,redefined-outer-name,unused-argument


class TestXdgCacheHome:
    """Tests for XDG_CACHE_HOME."""

    def test_unset(
        self, monkeypatch: "MonkeyPatch", unimport: Callable
    ) -> None:
        """Test when XDG_CACHE_HOME is unset."""
        monkeypatch.delenv("XDG_CACHE_HOME", raising=False)
        monkeypatch.setenv("HOME", os.fspath(HOME_DIR))
        from xdg import XDG_CACHE_HOME

        assert XDG_CACHE_HOME == HOME_DIR / ".cache"

    def test_empty(
        self, monkeypatch: "MonkeyPatch", unimport: Callable
    ) -> None:
        """Test when XDG_CACHE_HOME is empty."""
        monkeypatch.setenv("HOME", os.fspath(HOME_DIR))
        monkeypatch.setenv("XDG_CACHE_HOME", "")
        from xdg import XDG_CACHE_HOME

        assert XDG_CACHE_HOME == HOME_DIR / ".cache"

    def test_set(self, monkeypatch: "MonkeyPatch", unimport: Callable) -> None:
        """Test when XDG_CACHE_HOME is set."""
        monkeypatch.setenv("XDG_CACHE_HOME", "/xdg_cache_home")
        from xdg import XDG_CACHE_HOME

        assert XDG_CACHE_HOME == Path("/xdg_cache_home")


class TestXdgConfigDirs:
    """Tests for XDG_CONFIG_DIRS."""

    def test_unset(
        self, monkeypatch: "MonkeyPatch", unimport: Callable
    ) -> None:
        """Test when XDG_CONFIG_DIRS is unset."""
        monkeypatch.delenv("XDG_CONFIG_DIRS", raising=False)
        from xdg import XDG_CONFIG_DIRS

        assert XDG_CONFIG_DIRS == [Path("/etc/xdg")]

    def test_empty(
        self, monkeypatch: "MonkeyPatch", unimport: Callable
    ) -> None:
        """Test when XDG_CONFIG_DIRS is empty."""
        monkeypatch.setenv("XDG_CONFIG_DIRS", "")
        from xdg import XDG_CONFIG_DIRS

        assert XDG_CONFIG_DIRS == [Path("/etc/xdg")]

    def test_set(self, monkeypatch: "MonkeyPatch", unimport: Callable) -> None:
        """Test when XDG_CONFIG_DIRS is set."""
        monkeypatch.setenv("XDG_CONFIG_DIRS", "/first:/sec/ond")
        from xdg import XDG_CONFIG_DIRS

        assert XDG_CONFIG_DIRS == [Path("/first"), Path("/sec/ond")]


class TestXdgConfigHome:
    """Tests for XDG_CONFIG_HOME."""

    def test_unset(
        self, monkeypatch: "MonkeyPatch", unimport: Callable
    ) -> None:
        """Test when XDG_CONFIG_HOME is unset."""
        monkeypatch.delenv("XDG_CONFIG_HOME", raising=False)
        monkeypatch.setenv("HOME", os.fspath(HOME_DIR))
        from xdg import XDG_CONFIG_HOME

        assert XDG_CONFIG_HOME == HOME_DIR / ".config"

    def test_empty(
        self, monkeypatch: "MonkeyPatch", unimport: Callable
    ) -> None:
        """Test when XDG_CONFIG_HOME is empty."""
        monkeypatch.setenv("HOME", os.fspath(HOME_DIR))
        monkeypatch.setenv("XDG_CONFIG_HOME", "")
        from xdg import XDG_CONFIG_HOME

        assert XDG_CONFIG_HOME == HOME_DIR / ".config"

    def test_set(self, monkeypatch: "MonkeyPatch", unimport: Callable) -> None:
        """Test when XDG_CONFIG_HOME is set."""
        monkeypatch.setenv("XDG_CONFIG_HOME", "/xdg_config_home")
        from xdg import XDG_CONFIG_HOME

        assert XDG_CONFIG_HOME == Path("/xdg_config_home")


class TestXdgDataDirs:
    """Tests for XDG_DATA_DIRS."""

    def test_unset(
        self, monkeypatch: "MonkeyPatch", unimport: Callable
    ) -> None:
        """Test when XDG_DATA_DIRS is unset."""
        monkeypatch.delenv("XDG_DATA_DIRS", raising=False)
        from xdg import XDG_DATA_DIRS

        assert XDG_DATA_DIRS == [
            Path("/usr/local/share/"),
            Path("/usr/share/"),
        ]

    def test_empty(
        self, monkeypatch: "MonkeyPatch", unimport: Callable
    ) -> None:
        """Test when XDG_DATA_DIRS is empty."""
        monkeypatch.setenv("XDG_DATA_DIRS", "")
        from xdg import XDG_DATA_DIRS

        assert XDG_DATA_DIRS == [
            Path("/usr/local/share/"),
            Path("/usr/share/"),
        ]

    def test_set(self, monkeypatch: "MonkeyPatch", unimport: Callable) -> None:
        """Test when XDG_DATA_DIRS is set."""
        monkeypatch.setenv("XDG_DATA_DIRS", "/first/:/sec/ond/")
        from xdg import XDG_DATA_DIRS

        assert XDG_DATA_DIRS == [Path("/first/"), Path("/sec/ond/")]


class TestXdgDataHome:
    """Tests for XDG_DATA_HOME."""

    def test_unset(
        self, monkeypatch: "MonkeyPatch", unimport: Callable
    ) -> None:
        """Test when XDG_DATA_HOME is unset."""
        monkeypatch.delenv("XDG_DATA_HOME", raising=False)
        monkeypatch.setenv("HOME", os.fspath(HOME_DIR))
        from xdg import XDG_DATA_HOME

        assert XDG_DATA_HOME == HOME_DIR / ".local" / "share"

    def test_empty(
        self, monkeypatch: "MonkeyPatch", unimport: Callable
    ) -> None:
        """Test when XDG_DATA_HOME is empty."""
        monkeypatch.setenv("HOME", os.fspath(HOME_DIR))
        monkeypatch.setenv("XDG_DATA_HOME", "")
        from xdg import XDG_DATA_HOME

        assert XDG_DATA_HOME == HOME_DIR / ".local" / "share"

    def test_set(self, monkeypatch: "MonkeyPatch", unimport: Callable) -> None:
        """Test when XDG_DATA_HOME is set."""
        monkeypatch.setenv("XDG_DATA_HOME", "/xdg_data_home")
        from xdg import XDG_DATA_HOME

        assert XDG_DATA_HOME == Path("/xdg_data_home")


class TestXdgRuntimeDir:
    """Tests for XDG_RUNTIME_DIR."""

    def test_unset(
        self, monkeypatch: "MonkeyPatch", unimport: Callable
    ) -> None:
        """Test when XDG_RUNTIME_DIR is unset."""
        monkeypatch.delenv("XDG_RUNTIME_DIR", raising=False)
        from xdg import XDG_RUNTIME_DIR

        assert XDG_RUNTIME_DIR is None

    def test_empty(
        self, monkeypatch: "MonkeyPatch", unimport: Callable
    ) -> None:
        """Test when XDG_RUNTIME_DIR is empty."""
        monkeypatch.setenv("XDG_RUNTIME_DIR", "")
        from xdg import XDG_RUNTIME_DIR

        assert XDG_RUNTIME_DIR == Path("")

    def test_set(self, monkeypatch: "MonkeyPatch", unimport: Callable) -> None:
        """Test when XDG_RUNTIME_DIR is set."""
        monkeypatch.setenv("XDG_RUNTIME_DIR", "/xdg_runtime_dir")
        from xdg import XDG_RUNTIME_DIR

        assert XDG_RUNTIME_DIR == Path("/xdg_runtime_dir")
