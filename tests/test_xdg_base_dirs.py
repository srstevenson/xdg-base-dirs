import os
from pathlib import Path
from typing import Final

import pytest

import xdg_base_dirs

HOME_DIR: Final = Path("/homedir")


@pytest.mark.parametrize(
    ("env_var", "expected_path"),
    [
        pytest.param(None, HOME_DIR / ".cache", id="unset"),
        pytest.param("", HOME_DIR / ".cache", id="empty"),
        pytest.param("rela/tive", HOME_DIR / ".cache", id="relative"),
        pytest.param("/xdg_cache_home", Path("/xdg_cache_home"), id="absolute"),
    ],
)
def test_xdg_cache_home(
    monkeypatch: pytest.MonkeyPatch, env_var: str | None, expected_path: Path
) -> None:
    monkeypatch.setenv("HOME", os.fspath(HOME_DIR))
    if env_var is None:
        monkeypatch.delenv("XDG_CACHE_HOME", raising=False)
    else:
        monkeypatch.setenv("XDG_CACHE_HOME", env_var)
    assert xdg_base_dirs.xdg_cache_home() == expected_path


@pytest.mark.parametrize(
    ("env_var", "expected_paths"),
    [
        pytest.param(None, [Path("/etc/xdg")], id="unset"),
        pytest.param("", [Path("/etc/xdg")], id="empty"),
        pytest.param("rela/tive:ano/ther", [Path("/etc/xdg")], id="relative"),
        pytest.param(
            "/first:rela/tive:/sec/ond",
            [Path("/first"), Path("/sec/ond")],
            id="absolute",
        ),
    ],
)
def test_xdg_config_dirs(
    monkeypatch: pytest.MonkeyPatch, env_var: str | None, expected_paths: list[Path]
) -> None:
    if env_var is None:
        monkeypatch.delenv("XDG_CONFIG_DIRS", raising=False)
    else:
        monkeypatch.setenv("XDG_CONFIG_DIRS", env_var)
    assert xdg_base_dirs.xdg_config_dirs() == expected_paths


@pytest.mark.parametrize(
    ("env_var", "expected_path"),
    [
        pytest.param(None, HOME_DIR / ".config", id="unset"),
        pytest.param("", HOME_DIR / ".config", id="empty"),
        pytest.param("rela/tive", HOME_DIR / ".config", id="relative"),
        pytest.param("/xdg_config_home", Path("/xdg_config_home"), id="absolute"),
    ],
)
def test_xdg_config_home(
    monkeypatch: pytest.MonkeyPatch, env_var: str | None, expected_path: Path
) -> None:
    monkeypatch.setenv("HOME", os.fspath(HOME_DIR))
    if env_var is None:
        monkeypatch.delenv("XDG_CONFIG_HOME", raising=False)
    else:
        monkeypatch.setenv("XDG_CONFIG_HOME", env_var)
    assert xdg_base_dirs.xdg_config_home() == expected_path


@pytest.mark.parametrize(
    ("env_var", "expected_paths"),
    [
        pytest.param(
            None, [Path("/usr/local/share/"), Path("/usr/share/")], id="unset"
        ),
        pytest.param("", [Path("/usr/local/share/"), Path("/usr/share/")], id="empty"),
        pytest.param(
            "rela/tive:ano/ther",
            [Path("/usr/local/share/"), Path("/usr/share/")],
            id="relative",
        ),
        pytest.param(
            "/first/:rela/tive:/sec/ond/",
            [Path("/first/"), Path("/sec/ond/")],
            id="absolute",
        ),
    ],
)
def test_xdg_data_dirs(
    monkeypatch: pytest.MonkeyPatch, env_var: str | None, expected_paths: list[Path]
) -> None:
    if env_var is None:
        monkeypatch.delenv("XDG_DATA_DIRS", raising=False)
    else:
        monkeypatch.setenv("XDG_DATA_DIRS", env_var)
    assert xdg_base_dirs.xdg_data_dirs() == expected_paths


@pytest.mark.parametrize(
    ("env_var", "expected_path"),
    [
        pytest.param(None, HOME_DIR / ".local" / "share", id="unset"),
        pytest.param("", HOME_DIR / ".local" / "share", id="empty"),
        pytest.param("rela/tive", HOME_DIR / ".local" / "share", id="relative"),
        pytest.param("/xdg_data_home", Path("/xdg_data_home"), id="absolute"),
    ],
)
def test_xdg_data_home(
    monkeypatch: pytest.MonkeyPatch, env_var: str | None, expected_path: Path
) -> None:
    monkeypatch.setenv("HOME", os.fspath(HOME_DIR))
    if env_var is None:
        monkeypatch.delenv("XDG_DATA_HOME", raising=False)
    else:
        monkeypatch.setenv("XDG_DATA_HOME", env_var)
    assert xdg_base_dirs.xdg_data_home() == expected_path


@pytest.mark.parametrize(
    ("env_var", "expected_path"),
    [
        pytest.param(None, None, id="unset"),
        pytest.param("", None, id="empty"),
        pytest.param("rela/tive", None, id="relative"),
        pytest.param("/xdg_runtime_dir", Path("/xdg_runtime_dir"), id="absolute"),
    ],
)
def test_xdg_runtime_dir(
    monkeypatch: pytest.MonkeyPatch, env_var: str | None, expected_path: Path | None
) -> None:
    if env_var is None:
        monkeypatch.delenv("XDG_RUNTIME_DIR", raising=False)
    else:
        monkeypatch.setenv("XDG_RUNTIME_DIR", env_var)
    assert xdg_base_dirs.xdg_runtime_dir() == expected_path


@pytest.mark.parametrize(
    ("env_var", "expected_path"),
    [
        pytest.param(None, HOME_DIR / ".local" / "state", id="unset"),
        pytest.param("", HOME_DIR / ".local" / "state", id="empty"),
        pytest.param("rela/tive", HOME_DIR / ".local" / "state", id="relative"),
        pytest.param("/xdg_state_home", Path("/xdg_state_home"), id="absolute"),
    ],
)
def test_xdg_state_home(
    monkeypatch: pytest.MonkeyPatch, env_var: str | None, expected_path: Path
) -> None:
    monkeypatch.setenv("HOME", os.fspath(HOME_DIR))
    if env_var is None:
        monkeypatch.delenv("XDG_STATE_HOME", raising=False)
    else:
        monkeypatch.setenv("XDG_STATE_HOME", env_var)
    assert xdg_base_dirs.xdg_state_home() == expected_path
