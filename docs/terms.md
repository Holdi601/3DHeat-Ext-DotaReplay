---
title: Terms and licence
nav_order: 8
---

# Terms and licence

## Valve's replays

Dota 2 and its replays belong to Valve, who do not endorse this project. This
tool ships nothing of the game and talks to no server: it reads replay files on
your machine - ones the Dota 2 client saved for you, or public ones you
downloaded - outside the game, and changes nothing in it. Dota 2 replays are
not encrypted; OpenDota, Stratz and Dotabuff have read them for a decade. The
tables it writes are yours to view; using the tool is your decision, under the
terms you accepted for Dota 2 and Steam.

That is why it is a separate package: if Valve ever asks for it to go, it
goes alone, and the viewer, the Watcher and the other tools stay.

## gem-dota

The replay format (Source 2 demos: compressed protobuf packets and entity
deltas) is decoded by gem-dota (MIT licence,
[github.com/whanyu1212/gem-dota](https://github.com/whanyu1212/gem-dota)),
which pip installs as a dependency. It is used as a library; none of its code
is copied into this tool. This tool's own part asks it for facts, samples the
heroes on the same pass, places the events and writes the tables. See
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/LICENSES.md).

## Licence and sources

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/LICENSE)).
Needs gem-dota (MIT) and what it brings, numpy (BSD-3-Clause) and pyarrow
(Apache-2.0); the tests need pytest (MIT). Written for this project, first as
part of the 3DHeat Watcher; no code was taken from any other project.
