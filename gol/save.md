---
layout: default
title: save
parent: GOL Utility
nav-order: 9
---

# `save`

Exports tiles to a folder.

Usage:

    gol save <gol-file> <destination> [<options>]

- If no area is defined (via [`--area`](#option-area) or [`--bbox`](#option-bbox)),
  all tiles are exported.

- Missing tiles will be imported from another repository, if one is specified via [`--url`](#option-url).

## Options

{% include gol/option-area.md %}
{% include gol/option-bbox.md %}
{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-url.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}