---
title: "Mantener estos documentos"
nav_order: 91
lang: "es"
source: maintaining.md
source_hash: "00d3ace33ccf"
nav_exclude: true
search_exclude: true
---
# Mantener estos documentos {#maintaining-these-docs}

Una lista de comprobación para cada versión, para que las páginas nunca se queden atrás del código.

1. **Regenerar la referencia.** `python tools/gen_docs_reference.py` reescribe
   [Referencia de comandos](../cli-reference.md) a partir del `--help` del programa y de sus columnas de salida. `python tools/gen_docs_reference.py --check` sale con 1 cuando la página guardada está desfasada.
2. **Listar qué cambió.** `git log v<VERSION>..HEAD --oneline`, donde
   `<VERSION>` es la última versión publicada (el archivo `VERSION` en la publicación). Dale a cada función nueva, opción y columna de salida un lugar en una página, y una fila en la sección **Docs** de [`CHANGELOG.md`](https://github.com/Holdi601/3DHeat-Ext-DotaReplay/blob/main/CHANGELOG.md).
3. **Revisión independiente.** Alguien que no escribió las páginas lee el
   README y cada página cambiada, también las imágenes, tres veces: como principiante que nunca ha usado una terminal, como un niño de 8 años y como experto que comprueba cada opción contra `--help`. Los ejemplos usan solo nombres y números inventados.
4. **Corregir** lo que encuentre la revisión.
5. **Traducciones.** Cada página traducida guarda el hash de la página inglesa de la que se hizo. Vuelve a traducir las páginas cuyo origen en inglés cambió, y luego revisa cada idioma: texto claro, etiquetas correctas en los diagramas, las mismas palabras que la interfaz traducida del visor.
6. **Ejecutar las pruebas** (`pytest`).
7. **Subir** solo con el visto bueno del propietario.

## Traducciones: los comandos {#translations-the-commands}

El sitio se va a traducir a los 40 idiomas del visor de 3DHeat (hasta ahora: solo inglés): el inglés en
`docs/`, cada otro idioma en `docs/<lang>/` con los mismos nombres de archivo. `tools/docs_i18n.py` lleva la cuenta:

```bash
python tools/docs_i18n.py hashes             # tras cualquier cambio en inglés: registrar el hash de cada página
python tools/docs_i18n.py svg-strings        # tras cualquier cambio en imágenes: las etiquetas a traducir
python tools/docs_i18n.py status             # por idioma: al día, desfasadas, páginas que faltan
python tools/docs_i18n.py todo --lang de     # las páginas en alemán a (re)traducir
python tools/docs_i18n.py svg-build --lang de    # las imágenes en alemán desde docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # marcar las páginas en alemán con el hash del inglés
python tools/docs_i18n.py check              # sale con 1 cuando los hashes o las etiquetas están desfasados
```

Traduce solo lo que lista `todo`: mantén el Markdown, los enlaces, el código y los nombres de archivo y columna tal cual,
traduce los títulos y las descripciones de las imágenes, y usa las palabras propias del visor de 3DHeat para sus botones
y paneles (su `src/i18n/locales/<lang>/`). Las páginas de referencia generadas y las imágenes de terminal se quedan
en inglés. En el sitio, una traducción desfasada lo indica y enlaza la página inglesa; una que falta
recurre al inglés. El menú de idiomas del encabezado y la redirección de la página de inicio según el idioma del navegador
vienen de `docs/_includes/`.
