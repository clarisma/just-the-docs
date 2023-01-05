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

### `-f`, `--free` {#option-free}

Displays statistics about the number and sizes of free pages.

### `-i`, `--index` {#option-index}

Provides a detailed analysis of the library's indexes.

*For a large (planet-size) library, this option may require several minutes to execute.* 

{% include gol/option-new.md %}
{% include gol/option-output.md %}
{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}

### `-t`, `--tiles` {#option-tiles}

Displays statistics about the tiles.


{% include gol/option-url.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}
