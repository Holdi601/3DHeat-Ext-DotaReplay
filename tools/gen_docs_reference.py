"""Write docs/cli-reference.md from the code itself, so the reference cannot drift.

The options come from the program's own `--help`; the tables' columns from the
column names the code writes.

    python tools/gen_docs_reference.py          # rewrite the page
    python tools/gen_docs_reference.py --check  # exit 1 when the page is stale
"""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "cli-reference.md"
COMMAND = "heat3d-dota-replay"
VERBS = ["list", "convert"]


def run(args):
    env = dict(os.environ, HEAT3D_NO_UPDATE="1", COLUMNS="88", PYTHONIOENCODING="utf-8",
               PYTHONPATH=str(ROOT) + os.pathsep + os.environ.get("PYTHONPATH", ""))
    r = subprocess.run([sys.executable, "-m", "heat3d_ext_dota_replay"] + args, capture_output=True, text=True,
                       env=env, encoding="utf-8", cwd=ROOT)
    return (r.stdout or r.stderr).rstrip()


def outputs():
    sys.path.insert(0, str(ROOT))
    from heat3d_ext_dota_replay import dota_keep, dota_replay as d
    cols = lambda names: ", ".join(f"`{c}`" for c in names)
    return ["### `<match>.parquet`", "", cols(d.COLUMNS) + ".", "",
            f"Footer `heat3d` hints: kind `{d.HINTS['kind']}`, axes {d.HINTS['axes']}.", "",
            "### `<match>.units.parquet`", "", f"Footer kind `{d.UNIT_HINTS['kind']}`; extra columns "
            + cols(d.UNIT_HINTS["columns"]["extra"]) + ".", "",
            "### `<match>.combatlog.parquet`", "", cols(("time", *d.COMBAT_FIELDS)) + ".", "",
            "### Kept whole", "", ", ".join(f"`<match>.{n}.parquet`" for n in dota_keep.SIDECARS) + ".", "",
            "### `<match>.match.json`", "", "`format` `heat3d-dota-match`; `selfCheck.completeness` counts what was "
            "read and kept, `selfCheck.crossCheck` the scoreboard against the game's own record.", ""]


def build():
    out = ["---", "title: Command reference", "nav_order: 90", "---", "", "# Command reference", "",
           "Generated from the code by `tools/gen_docs_reference.py`: do not edit by hand.",
           "The other pages explain each command step by step.", "",
           f"## `{COMMAND}`", "", "```text", run(["--help"]), "```", ""]
    for v in VERBS:
        out += [f"## `{v}`", "", "```text", run([v, "--help"]), "```", ""]
    out += ["## Output", ""]
    return "\n".join(out + outputs())


if __name__ == "__main__":
    text = build()
    if "--check" in sys.argv:
        sys.exit(0 if OUT.exists() and OUT.read_text(encoding="utf-8") == text else 1)
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT.relative_to(ROOT))
