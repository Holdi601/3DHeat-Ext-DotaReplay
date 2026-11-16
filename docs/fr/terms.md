---
title: "Conditions et licence"
nav_order: 8
lang: "fr"
source: terms.md
source_hash: "59d062678c54"
nav_exclude: true
search_exclude: true
---
# Conditions et licence {#terms-and-licence}

## Les replays de Valve {#valves-replays}

Dota 2 et ses replays appartiennent à Valve, qui ne cautionne pas ce projet. Cet
outil ne livre rien du jeu et ne parle à aucun serveur : il lit des fichiers de replay sur
votre machine - ceux que le client Dota 2 a enregistrés pour vous, ou des replays publics
que vous avez téléchargés - en dehors du jeu, et ne modifie rien dans celui-ci. Les replays de Dota 2 ne sont pas chiffrés : OpenDota, Stratz et Dotabuff les lisent depuis dix ans. Les
tables qu'il écrit sont à vous pour les voir ; utiliser l'outil est votre décision, selon les
conditions que vous avez acceptées pour Dota 2 et Steam.

C'est pourquoi c'est un paquet séparé : si Valve demande un jour qu'il disparaisse, il
disparaît seul, et le visualiseur, le Watcher et les autres outils restent.

## gem-dota {#gem-dota}

Le format des replays (démos Source 2 : paquets protobuf compressés et différences
d'entités) est décodé par gem-dota (licence MIT,
[github.com/whanyu1212/gem-dota](https://github.com/whanyu1212/gem-dota)),
que pip installe comme dépendance. Il est utilisé comme bibliothèque ; aucun de ses codes
n'est copié dans cet outil. La partie propre à cet outil lui demande des faits, échantillonne
les héros au cours du même passage, place les événements et écrit les tables. Voir
[`LICENSES.md`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/LICENSES.md).

## Licence et sources {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/LICENSE)).
Demande gem-dota (MIT) et ce qu'il apporte, numpy (BSD-3-Clause) et pyarrow
(Apache-2.0) ; les tests demandent pytest (MIT). Écrit pour ce projet, d'abord dans le
cadre du 3DHeat Watcher ; aucun code n'a été pris à un autre projet.
