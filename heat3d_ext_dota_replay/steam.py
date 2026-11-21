"""Where Steam keeps its games: Steam's own folder and every library listed in its `libraryfolders.vdf`."""

from __future__ import annotations

import os
import re
from pathlib import Path


def steam_root() -> Path | None:
    """Steam's own folder, from the registry or the usual places."""
    if os.name == "nt":
        try:
            import winreg

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam") as k:
                path = Path(winreg.QueryValueEx(k, "SteamPath")[0])
                if path.is_dir():
                    return path
        except OSError:
            pass
    for p in (Path(r"C:\Program Files (x86)\Steam"), Path.home() / ".steam" / "steam", Path.home() / ".local" / "share" / "Steam"):
        if p.is_dir():
            return p
    return None


def steam_libraries() -> list[Path]:
    """Every Steam library's `steamapps/common`, from `libraryfolders.vdf`."""
    from .app import paths

    # Every Steam this user has (native, flatpak, Steam Deck, macOS), then the usual one.
    found = list(paths.steam_libraries())
    root = steam_root()
    if root is not None:
        found.append(root)
        try:
            text = (root / "steamapps" / "libraryfolders.vdf").read_text(encoding="utf-8", errors="replace")
            found += [Path(m.replace("\\\\", "\\")) for m in re.findall(r'"path"\s+"([^"]+)"', text)]
        except OSError:
            pass
    out, seen = [], set()
    for lib in found:
        common = lib / "steamapps" / "common"
        key = str(common).lower()
        if key not in seen and common.is_dir():
            seen.add(key)
            out.append(common)
    return out
