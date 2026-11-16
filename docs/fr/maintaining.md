---
title: "Maintenance de ces documents"
nav_order: 91
lang: "fr"
source: maintaining.md
source_hash: "00d3ace33ccf"
nav_exclude: true
search_exclude: true
---
# Maintenance de ces documents {#maintaining-these-docs}

Une liste de contrôle pour chaque version, pour que les pages ne retardent jamais sur le code.

1. **Régénérer la référence.** `python tools/gen_docs_reference.py` réécrit
   [Référence des commandes](../cli-reference.md) à partir du `--help` du programme et de
   ses colonnes de sortie. `python tools/gen_docs_reference.py --check` se termine avec le code 1 quand
   la page versionnée est périmée.
2. **Lister ce qui a changé.** `git log v<VERSION>..HEAD --oneline`, où
   `<VERSION>` est la dernière version publiée (le fichier `VERSION` à la publication).
   Donnez à chaque nouvelle fonctionnalité, option et colonne de sortie une place sur une page, et une
   ligne dans la section **Docs** de [`CHANGELOG.md`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/CHANGELOG.md).
3. **Relecture indépendante.** Quelqu'un qui n'a pas écrit les pages lit le
   README et chaque page modifiée, images comprises, trois fois : comme un
   débutant qui n'a jamais utilisé de terminal, comme un enfant de 8 ans, et comme un
   expert qui vérifie chaque option contre `--help`. Les exemples n'utilisent que des noms et
   des chiffres inventés.
4. **Corriger** tout ce que la relecture trouve.
5. **Traductions.** Chaque page traduite enregistre le hash de la page anglaise
   dont elle est issue. Retraduisez les pages dont la source anglaise a changé,
   puis relisez chaque langue : texte clair, étiquettes de schémas correctes, les mêmes
   mots que l'interface traduite du visualiseur.
6. **Lancer les tests** (`pytest`).
7. **Publier** seulement après le feu vert du propriétaire.

## Traductions : les commandes {#translations-the-commands}

Le site doit être traduit dans les 40 langues du visualiseur 3DHeat (pour l'instant : anglais seulement) : l'anglais dans
`docs/`, chaque autre langue dans `docs/<lang>/` avec les mêmes noms de fichiers. `tools/docs_i18n.py` tient les comptes :

```bash
python tools/docs_i18n.py hashes             # après tout changement anglais : enregistrer le hash de chaque page
python tools/docs_i18n.py svg-strings        # après tout changement d'image : les étiquettes à traduire
python tools/docs_i18n.py status             # par langue : pages à jour, périmées, manquantes
python tools/docs_i18n.py todo --lang de     # les pages allemandes à (re)traduire
python tools/docs_i18n.py svg-build --lang de    # les images allemandes depuis docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # marquer les pages allemandes avec le hash anglais
python tools/docs_i18n.py check              # se termine avec le code 1 quand les hashes ou les étiquettes sont périmés
```

Ne traduisez que ce que `todo` liste : gardez le Markdown, les liens, le code, les noms de fichiers et de colonnes tels quels,
traduisez les titres et les descriptions d'images, et utilisez les mots du visualiseur 3DHeat pour ses boutons
et panneaux (son `src/i18n/locales/<lang>/`). Les pages de référence générées et les images de terminal restent
en anglais. Sur le site, une traduction périmée le dit et renvoie à la page anglaise ; une page
manquante retombe sur l'anglais. Le menu de langue de l'en-tête et la redirection de la page d'accueil
selon la langue du navigateur viennent de `docs/_includes/`.
