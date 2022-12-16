---
layout: default
title: info
parent: GOL Utility
nav-order: 4
---

# `info`

Provides general statistics about a library. If a bounding box or polygon are specified,
this command provides additional statistics about that area.

Usage:

    gol info <gol-file> [<options>]  

## Options

{% include gol/option-area.md %}
{% include gol/option-bbox.md %}

### `-i`, `--index` ~~0.2~~ {#option-index}

Provides additional information about the library's indexes.

{% include gol/option-new.md %}
{% include gol/option-output.md %}
{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-url.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}
