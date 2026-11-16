---
title: "Convertir: convert"
nav_order: 3
lang: "es"
source: convert.md
source_hash: "58226d5bc388"
nav_exclude: true
search_exclude: true
---
# Convertir: `convert` {#converting-convert}

```bash
heat3d-dota-replay convert [<replay.dem> or <folder> ...] -o <folder> [--game FOLDER] [--hz N]
```

lee cada repetición y la escribe como tablas de 3DHeat en la carpeta `-o`, con el nombre del
id de la partida. Sin repetición, convierte cada `.dem` de la carpeta de repeticiones de Dota
([list](list.md) muestra cuál es). Una carpeta dada convierte cada `.dem` que contiene.
Código: [`heat3d_ext_dota_replay/dota_replay.py`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/heat3d_ext_dota_replay/dota_replay.py).

| Opción | Hace |
|---|---|
| `<replay.dem>` o `<folder>` | qué convertir; se pueden dar varios (por defecto: la carpeta de repeticiones de Dota) |
| `-o`, `--out FOLDER` | dónde van las tablas (obligatorio); se crea si no existe |
| `--game FOLDER` | la carpeta `dota 2 beta`, cuando no se da ninguna repetición y Dota 2 no está en ninguna biblioteca de Steam |
| `--hz N` | muestras de héroe por segundo (por defecto 7.5, cada cuarto de los 30 ticks de la repetición) |

Por cada repetición imprime los dos archivos principales que escribió:

```text
tables\7123456789.parquet
tables\7123456789.match.json
```

Una partida larga tarda uno o dos minutos y cerca de un gigabyte de memoria mientras se lee.

## Qué sale {#what-comes-out}

| Archivo | Contiene |
|---|---|
| `<match>.parquet` | la tabla para abrir: cada héroe 7.5 veces por segundo mientras está vivo (posición, altura, vida, nivel, orientación, maná, experiencia, atributos, armadura, velocidad, daño, objetos, el cursor del jugador), y cada evento donde ocurrió: muertes con el lugar del asesino, caídas de héroes donde cayeron, torres, cuarteles, Roshan y los Tormentors donde cayeron, wards donde se colocaron y donde terminaron, las entradas del registro de combate sobre héroes, avisos en el mapa, dibujos en el mapa y cada orden (mover, atacar, lanzar, comprar, ...) |
| `<match>.units.parquet` | cada otra unidad - criaturas, invocaciones, ilusiones, mensajeros, edificios - una vez por segundo |
| `<match>.combatlog.parquet` | el registro de combate completo, cada campo |
| `<match>.match.json` | la partida: equipos, marcador, ganador, la línea de cada jugador, muertes, objetivos, wards, la selección de héroes, el chat, todo lo demás que extrae gem-dota, la cabecera e información propias del archivo de la repetición, y el registro de fin de partida del juego (`matchDetails`, `matchMetadata`); `selfCheck` indica lo completa que fue la lectura |
| `<match>.packets.parquet`, `<match>.entities.parquet`, `<match>.strings.parquet` | todo lo demás que contiene la repetición, guardado entero: cada fotograma y mensaje de red, cada cambio de propiedad de entidad, cada entrada de tabla de cadenas |

Las posiciones están en las unidades de mundo de Dota (unidades de Hammer): x al este, y al norte, z hacia arriba; el
mapa jugable va aproximadamente de -8200 a 8200 en ambos ejes: las mismas unidades que
informa la integración de estado de partida de Dota 2, así que una repetición y una sesión en vivo coinciden. El tiempo es
el reloj de la partida en segundos: negativo antes del cuerno, quieto mientras está en pausa.
Cada fila tiene un `life`: las vidas de un héroe contadas desde 1, así que una trayectoria termina donde
murió el héroe. Todas las columnas: [Referencia de comandos](../cli-reference.md#output).

## Cargarla en el visor {#loading-it-in-the-viewer}

Abre `<match>.parquet` en el visor con **Archivos…** o suéltalo sobre la ventana.
Su pie le dice al visor los ejes, las unidades y las columnas (jugadores como personas,
equipos, vidas como sesiones, orientación como dirección), así que no hace falta asignar nada. Las
tablas auxiliares se abren igual cuando se eligen por separado. Para el mapa debajo en 3D, crea el nivel de Dota 2 con [3DHeat Dota](https://holdi601.github.io/3DHeat-Ext-Dota/).

## Cómo se comprobó {#how-it-was-checked}

Con la repetición de una partida pública: las muertes, asesinatos, asistencias, nivel, últimos golpes y negaciones
leídos del flujo coinciden con el registro de fin de partida del juego para los diez
jugadores (`selfCheck.crossCheck` en el archivo de la partida guarda la comparación de cada
repetición), y cada mensaje de la tabla de paquetes se vuelve a serializar byte a byte.
Las pruebas usan solo datos inventados.

Un parche nuevo de Dota puede cambiar las entidades de la repetición antes de que gem-dota las siga. Una repetición que gem-dota no puede leer hasta el final se convierte hasta donde llega y se marca como `incomplete` en su archivo de partida.

## Mensajes y código de salida {#messages-and-exit-status}

| Mensaje | Salida | Significa |
|---|---|---|
| dos nombres de archivo por repetición | 0 | hecho |
| `heat3d-dota-replay: no replay (.dem) found in ...` | 2 | no hay nada que convertir donde se buscó |
| `heat3d-dota-replay: <file>: <file> is not a Source 2 demo ...` | 2 | no es una repetición de Dota 2 (un `.dem.bz2` hay que descomprimirlo antes); entre otras que se convirtieron: 1 |
| `heat3d-dota-replay: pip install gem-dota ...` | 2 | gem-dota no está instalado: `python -m pip install gem-dota` |
| `heat3d-dota-replay: <file>: <error>` | 1 | esa repetición falló; las demás se siguen convirtiendo |
