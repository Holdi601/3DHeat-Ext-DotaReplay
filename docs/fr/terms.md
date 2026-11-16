---
title: "Conditions et licence"
nav_order: 8
lang: "fr"
source: terms.md
source_hash: "46ff3a8c7213"
nav_exclude: true
search_exclude: true
---
# Conditions et licence {#terms-and-licence}

## Les replays de Valve {#valves-replays}

3DHeat Dota Replay n'est ni affilié à Valve ni approuvé par Valve. Dota 2 et les noms et
marques associés appartiennent à leurs propriétaires. Cet outil ne livre rien du jeu et ne
parle à aucun serveur : il lit des fichiers de replay sur votre machine - ceux que le
client Dota 2 a enregistrés pour vous, ou des replays publics que vous avez téléchargés -
en dehors du jeu, et ne modifie rien dans celui-ci. Les replays de Dota 2 ne sont pas
chiffrés. Les tables qu'il écrit restent sur votre machine.

## Un projet à part {#its-own-project}

Chaque lecteur de jeu est un petit projet à part, avec son propre fichier de licence, ses
propres versions et son propre suivi des tickets : il peut être installé, mis à jour,
maintenu - ou retiré à la demande d'un ayant droit - seul, sans toucher au visualiseur ni
aux autres outils.

Ayants droit : ouvrez un ticket sur
[3DHeat-Ext-DotaReplay/issues](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/issues) -
nous répondons vite et retirons tout ce qui est demandé.

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
