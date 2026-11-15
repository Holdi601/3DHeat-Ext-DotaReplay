---
title: Before you start
nav_order: 1.5
---

# Before you start

New to the command line? This page takes you from nothing to a first run.
It takes about ten minutes, once.

## 1. Install Python

This tool needs **Python 3.10 or later**.

- **Windows:** download Python from [python.org/downloads](https://www.python.org/downloads/)
  and run the installer. On its first screen, tick **Add python.exe to PATH**,
  then click **Install Now**.
- **macOS and Linux:** Python 3 is often there already. Where these pages say
  `python`, type `python3`.

## 2. Get this tool

Open [github.com/Holdi601/3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay), click the
green **Code** button, then **Download ZIP**, and unzip it into a folder of your
choice. If you use git: `git clone https://github.com/Holdi601/3DHeat-Ext-DotaReplay`.

## 3. Open a terminal in that folder

A terminal is a window where you type commands.

- **Windows:** open the folder in Explorer, click into the address bar, type
  `powershell` and press Enter. A blue or black window opens, already in that
  folder.
- **macOS:** open **Terminal**, type `cd ` (with a space), drag the folder into
  the window and press Enter.

`cd` means "change folder": `cd C:\Tools\3DHeat-Ext-DotaReplay` goes to that folder.

## 4. Install the tool

Type this and press Enter:

```bash
python -m pip install -e .
```

It installs the tool and gem-dota, the replay parser it reads through. You
should see, at the end: `Successfully installed ... gem-dota-... heat3d-ext-dota-replay-...`.

## 5. Get a replay and run it

In Dota 2, open a match's details and click **Download replay** (or Watch >
Replays). Then:

```bash
heat3d-dota-replay list
```

You should see something like:

```text
C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota\replays
  7123456789.dem                   98.1 MB
1 replay(s)
```

Next: [Converting: convert](convert.md).

## How to read the commands on these pages

| You see | It means |
|---|---|
| `<match>` | a placeholder: type your own value instead, without the `< >` |
| `[--hz N]` | optional: leave it out, or type it as shown |
| `# a note` | a comment for you: do not type it |
| `"C:\My Files\x"` | put a path that has spaces in quotes |

## When something goes wrong

| The message | What to do |
|---|---|
| `'python' is not recognized` | Python is not installed, or the PATH box was not ticked: install it again and tick it (or type `py` instead of `python`). |
| `'heat3d-dota-replay' is not recognized` | Run step 4 again in the tool's folder, or type `python -m heat3d_ext_dota_replay` instead of `heat3d-dota-replay`: it does the same. |
| `pip install gem-dota (the Dota 2 replay parser, MIT)` | Step 4 did not install gem-dota: run `python -m pip install gem-dota`. |
| `Dota 2 not found in any Steam library` | Install Dota 2 through Steam, give its folder with `--game`, or give the replay's path to `convert`. |
| `... is not a Source 2 demo` | The file is not a Dota 2 replay; a `.dem.bz2` must be unpacked first. |
| anything else | Read the last line of the message, then open an issue on GitHub with it. |

Every command also ends with an **exit status**: 0 means it worked, 2 that
there was nothing to read (no replay, not a replay, gem-dota missing), 1 that a
replay failed. To see it, type `echo $LASTEXITCODE` in PowerShell or `echo $?`
on macOS and Linux.
