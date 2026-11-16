---
title: Inicio
nav_order: 1
lang: "es"
source: index.md
source_hash: "df20c820922e"
nav_exclude: true
search_exclude: true
permalink: /es/
---
# 3DHeat Dota Replay {#dheat-dota-replay}

**¿Qué es?** Esta herramienta lee repeticiones de Dota 2 (archivos `.dem`) y escribe lo que
pasó en ellas como tablas para el visor [3DHeat](https://github.com/Holdi601/3DHeat)
([documentación](https://holdi601.github.io/3DHeat/)): el recorrido de cada héroe por el
mapa, cada muerte, torre, ward, aviso y orden donde ocurrió, y la partida entera.

**¿Para qué la usaría?** Para ver una partida de Dota 2 - la tuya o cualquier pública - como un
mapa de calor y una repetición sobre el mapa: dónde pasó el héroe la partida, dónde
fueron las peleas, dónde se colocaron los wards.

**Ejemplo:** `heat3d-dota-replay convert 7123456789.dem -o tables` ->
`tables/7123456789.parquet`, la tabla para abrir en el visor, con la partida
y las tablas auxiliares al lado.

## Inicio rápido {#quick-start}

¿Nunca has usado la línea de comandos? Lee primero [Antes de empezar](before-you-start.md).
Necesitas Python 3.10 o posterior y una repetición: descárgala en Dota 2 (los detalles de una
partida, **Download replay**), y aparece en la carpeta de repeticiones de Dota. Ejecuta estos comandos
en la carpeta que clonaste o descomprimiste:

```bash
python -m pip install -e .                  # instala heat3d-dota-replay y gem-dota
heat3d-dota-replay list                     # dónde guarda Dota 2 las repeticiones, las que hay allí
heat3d-dota-replay convert -o tables        # cada repetición de allí, como tablas
```

`list` muestra la carpeta de repeticiones de Dota y una línea por repetición; `convert` muestra los
dos archivos que escribió por cada una, `tables/<match>.parquet` y
`tables/<match>.match.json`. Abre el `.parquet` en el visor con **Archivos…**
o soltándolo sobre la ventana ([Convertir](convert.md#cargarla-en-el-visor)).

## Páginas {#pages}

| Página | Qué contiene |
|---|---|
| [Antes de empezar](before-you-start.md) | Python, una terminal, una primera ejecución |
| [Encontrar repeticiones: list](list.md) | dónde guarda Dota 2 las repeticiones, cómo conseguir una, qué muestra `list` |
| [Convertir: convert](convert.md) | cada opción, las tablas columna por columna, cómo cargarlas, cómo se comprobó |
| [Condiciones y licencia](terms.md) | las repeticiones de Valve, la licencia de gem-dota, por qué es un paquete aparte |
| [Referencia de comandos](../cli-reference.md) | cada opción, generada desde el código |
| [Mantener estos documentos](maintaining.md) | la lista de comprobación de cada versión |

## Relacionado {#related}

- El visor 3DHeat: [github.com/Holdi601/3DHeat](https://github.com/Holdi601/3DHeat),
  documentación en [holdi601.github.io/3DHeat](https://holdi601.github.io/3DHeat/).
- El 3DHeat Watcher ejecuta esta herramienta sobre cada repetición que guarda Dota 2, y descarga
  las repeticiones de partidas públicas por id: [repeticiones de Dota 2 en el Watcher](https://holdi601.github.io/3DHeat-Watcher/game-dota-replays.html).
- El mapa de Dota 2 como nivel 3D bajo estas tablas: [3DHeat Dota](https://holdi601.github.io/3DHeat-Ext-Dota/).

## Las herramientas de 3DHeat {#the-3dheat-tools}

| Herramienta | Qué hace | Código | Documentación |
|---|---|---|---|
| visor 3DHeat | muestra los datos: mapas de calor, análisis de carreras, revisión de partidas | [3DHeat](https://github.com/Holdi601/3DHeat) | [documentación](https://holdi601.github.io/3DHeat/) |
| GameFiles | niveles y circuitos a partir de los archivos propios de un juego | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [documentación](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | telemetría de vueltas, y niveles reconstruidos a partir de vídeo de juego | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [documentación](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | un plugin del editor de Unreal: un nivel como un solo `.glb` | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [documentación](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | demos y mapas de Counter-Strike 2 | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [documentación](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | registra lo que los juegos publican mientras juegas | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [documentación](https://holdi601.github.io/3DHeat-Watcher/) |
| Ext-WarThunder | repeticiones de War Thunder | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [documentación](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| Ext-WoT | repeticiones de World of Tanks | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [documentación](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| Ext-WoWs | repeticiones de World of Warships | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [documentación](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Ext-Squad | demos de servidores de Squad | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [documentación](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| Ext-DCS | mapas de DCS World como niveles 3D | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [documentación](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| Ext-IL2 | mapas de IL-2 Sturmovik como niveles 3D | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [documentación](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Ext-Dota | el mapa de Dota 2 como nivel 3D | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [documentación](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Ext-DotaReplay | repeticiones de Dota 2 como tablas | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [documentación](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Ext-Riot | repeticiones de League of Legends y VALORANT: lo que contienen en abierto | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [documentación](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Ext-Forza | circuitos, carreras y coches de Forza a partir de tu propia instalación | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [documentación](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Ext-Battlefield | niveles de Battlefield (Frostbite) como niveles 3D | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [documentación](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| Ext-BeamNG | circuitos de BeamNG.drive | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [documentación](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| Ext-ACRally | tramos de Assetto Corsa Rally como circuitos | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [documentación](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Ext-Reforger | mundos de Arma Reforger (Enfusion) como niveles 3D | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [documentación](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| Ext-R6 | repeticiones de partidas de Rainbow Six Siege | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [documentación](https://holdi601.github.io/3DHeat-Ext-R6/) |
