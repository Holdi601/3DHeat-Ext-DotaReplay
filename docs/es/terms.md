---
title: "Condiciones y licencia"
nav_order: 8
lang: "es"
source: terms.md
source_hash: "46ff3a8c7213"
nav_exclude: true
search_exclude: true
---
# Condiciones y licencia {#terms-and-licence}

## Las repeticiones de Valve {#valves-replays}

3DHeat Dota Replay no está afiliado a Valve ni respaldado por Valve. Dota 2 y los nombres y marcas relacionados pertenecen a sus propietarios. Esta herramienta no incluye nada del juego y no habla con ningún servidor: lee archivos de repetición en tu equipo - los que el cliente de Dota 2 guardó para ti, o públicos que descargaste - fuera del juego, y no cambia nada en él. Las repeticiones de Dota 2 no están cifradas. Las tablas que escribe se quedan en tu equipo.

## Un proyecto propio {#its-own-project}

Cada lector de un juego es un pequeño proyecto propio, con su propio archivo de licencia, sus versiones y su gestor de incidencias, así que puede instalarse, actualizarse, mantenerse (o retirarse a petición de un titular de derechos) por sí solo, sin afectar al visor ni a las demás herramientas.

Titulares de derechos: abran una incidencia en [3DHeat-Ext-DotaReplay/issues](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/issues); respondemos con rapidez y retiramos cualquier cosa que se nos pida.

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
