---
title: Terms and licence
nav_order: 8
---

# Terms and licence

## Valve's replays

3DHeat Dota Replay is not affiliated with or endorsed by Valve. Dota 2 and
related names and trademarks belong to their owners. This tool ships nothing of
the game and talks to no server: it reads replay files on your machine - ones
the Dota 2 client saved for you, or public ones you downloaded - outside the
game, and changes nothing in it. Dota 2 replays are not encrypted. The tables it
writes stay on your machine.

## Its own project

Each game reader is its own small project with its own licence file, releases
and issue tracker, so it can be installed, updated, maintained - or withdrawn on
a rights holder's request - on its own, without affecting the viewer or the
other tools.

Rights holders: open an issue at
[3DHeat-Ext-DotaReplay/issues](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/issues) -
we respond quickly and remove anything on request.

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
