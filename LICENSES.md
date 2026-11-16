# Third-party licences

This tool is MIT licensed ([`LICENSE`](LICENSE)). What it uses, and under which
licence; each package's own source is what counts, not this file.

| Software | Licence | How it is used |
|---|---|---|
| gem-dota | MIT | a dependency, installed by pip: the Source 2 demo parser this tool reads replays through (github.com/whanyu1212/gem-dota); used as a library, none of its code is copied here |
| pandas, protobuf, protoc-wheel-0, python-snappy, zstandard | BSD-3-Clause | what gem-dota brings, installed by pip |
| cramjam, rich | MIT | what gem-dota brings, installed by pip |
| numpy | BSD-3-Clause | a dependency, installed by pip |
| pyarrow | Apache-2.0 | a dependency, installed by pip: writing Parquet |
| pytest | MIT | development only: the tests |

## The replays

3DHeat Dota Replay is not affiliated with or endorsed by Valve. Dota 2 and
related names and trademarks belong to their owners. This repository holds no
replay and no table made from one; the tool reads the replays on the user's own
machine - ones the Dota 2 client saved, or public ones the user downloaded - and
the tables it writes stay there. See [Terms and
licence](https://holdi601.github.io/3DHeat-Ext-DotaReplay/terms.html). Rights
holders: open an issue at
[3DHeat-Ext-DotaReplay/issues](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/issues) -
we respond quickly and remove anything on request.
