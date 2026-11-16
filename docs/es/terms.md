---
title: "Condiciones y licencia"
nav_order: 8
lang: "es"
source: terms.md
source_hash: "59d062678c54"
nav_exclude: true
search_exclude: true
---
# Condiciones y licencia {#terms-and-licence}

## Las repeticiones de Valve {#valves-replays}

Dota 2 y sus repeticiones son de Valve, que no respalda este proyecto. Esta
herramienta no incluye nada del juego y no habla con ningún servidor: lee archivos de repetición en
tu equipo - los que el cliente de Dota 2 guardó para ti, o públicos que descargaste -
fuera del juego, y no cambia nada en él. Las repeticiones de Dota 2 no están cifradas; OpenDota, Stratz y Dotabuff las leen desde hace una década. Las tablas que escribe son tuyas para verlas; usar la herramienta es decisión tuya, bajo las condiciones que aceptaste para Dota 2 y Steam.

Por eso es un paquete aparte: si Valve algún día pide que se retire, se retira solo, y el visor, el Watcher y las demás herramientas se quedan.

## gem-dota {#gem-dota}

El formato de repetición (demos de Source 2: paquetes protobuf comprimidos y cambios de entidades) lo decodifica gem-dota (licencia MIT,
[github.com/whanyu1212/gem-dota](https://github.com/whanyu1212/gem-dota)),
que pip instala como dependencia. Se usa como biblioteca; ninguno de su código
se copia en esta herramienta. La parte propia de esta herramienta le pide datos, muestrea a los
héroes en la misma pasada, coloca los eventos y escribe las tablas. Ver
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/LICENSES.md).

## Licencia y fuentes {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/LICENSE)).
Necesita gem-dota (MIT) y lo que trae, numpy (BSD-3-Clause) y pyarrow
(Apache-2.0); las pruebas necesitan pytest (MIT). Escrita para este proyecto, primero como
parte del 3DHeat Watcher; no se tomó código de ningún otro proyecto.
