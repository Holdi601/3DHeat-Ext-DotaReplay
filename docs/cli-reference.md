---
title: Command reference
nav_order: 90
---

# Command reference

Generated from the code by `tools/gen_docs_reference.py`: do not edit by hand.
The other pages explain each command step by step.

## `heat3d-dota-replay`

```text
usage: heat3d-dota-replay [-h] [--version] {list,convert} ...

Dota 2 replays (.dem) into 3DHeat tables

positional arguments:
  {list,convert}
    list          where Dota 2 saves replays, and the replays there
    convert       each replay as 3DHeat tables: <match>.parquet, .match.json and
                  sidecars

options:
  -h, --help      show this help message and exit
  --version       show program's version number and exit
```

## `list`

```text
usage: heat3d-dota-replay list [-h] [--game GAME]

options:
  -h, --help   show this help message and exit
  --game GAME  the Dota 2 folder, `dota 2 beta` or its game/dota (default: found in
               your Steam libraries)
```

## `convert`

```text
usage: heat3d-dota-replay convert [-h] -o OUT [--game GAME] [--hz HZ] [replay ...]

positional arguments:
  replay         a .dem replay or a folder of them (default: Dota 2's replays folder)

options:
  -h, --help     show this help message and exit
  -o, --out OUT  the folder to write to
  --game GAME    the Dota 2 folder, `dota 2 beta` or its game/dota (default: found in
                 your Steam libraries); only used without a replay
  --hz HZ        hero samples a second (default 7.5, every fourth tick)
```

## Output

### `<match>.parquet`

`time`, `tick`, `event`, `slot`, `player`, `hero`, `team`, `life`, `x`, `y`, `z`, `health`, `maxHealth`, `level`, `other`, `value`, `text`, `dirX`, `dirY`, `dirZ`, `mana`, `maxMana`, `xp`, `strength`, `agility`, `intellect`, `armor`, `magicResist`, `moveSpeed`, `damageMin`, `damageMax`, `attackRange`, `healthRegen`, `manaRegen`, `moving`, `abilityPoints`, `recentDamage`, `items`, `cursorX`, `cursorY`.

Footer `heat3d` hints: kind `dota2-replay`, axes {'up': 'z', 'flipX': False, 'flipY': True, 'flipZ': False, 'scale': 1}.

### `<match>.units.parquet`

Footer kind `dota2-replay-units`; extra columns `name`, `class`, `team`, `health`, `owner`, `match`.

### `<match>.combatlog.parquet`

`time`, `tick`, `log_type`, `attacker_name`, `damage_source_name`, `target_name`, `inflictor_name`, `value`, `attacker_is_hero`, `target_is_hero`, `attacker_is_illusion`, `target_is_illusion`, `ability_level`, `gold_reason`, `xp_reason`, `value_name`, `damage_type`, `stun_duration`, `neutral_camp_type`, `neutral_camp_team`, `location_x`, `location_y`, `timestamp_s`, `game_time_s`, `will_reincarnate`, `visible_radiant`, `visible_dire`, `modifier_duration_s`, `modifier_elapsed_duration_s`, `attacker_team`, `target_team`, `source`, `aura_modifier`, `modifier_purged`, `modifier_purged_duration_s`, `rune_type`.

### Kept whole

`<match>.packets.parquet`, `<match>.entities.parquet`, `<match>.strings.parquet`.

### `<match>.match.json`

`format` `heat3d-dota-match`; `selfCheck.completeness` counts what was read and kept, `selfCheck.crossCheck` the scoreboard against the game's own record.
