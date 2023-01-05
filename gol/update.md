---
layout: default
title: update
parent: GOL Utility
nav-order: 10
---

# `update` ~~0.3~~

Updates a GOL with changes in [OsmChange](https://wiki.openstreetmap.org/wiki/OsmChange) format.

Usage:

    gol update <gol-file> <change-file> [<options>]

- GOLs can only be updated if built with option [`updatable`](build#updatable) 



## Options

{% comment %}
{% include gol/option-area.md %}
{% include gol/option-bbox.md %}
{% endcomment %}

### `-i`, `--index` {#option-index}

Re-creates the [ID indexes](build#id-indexing) to speed up processing.

{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}