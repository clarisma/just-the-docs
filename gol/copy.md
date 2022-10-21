---
layout: default
title: copy
parent: GOL Utility
nav-order: 2
---

# `copy`

Copies tiles from one library to another.

Usage:

    gol copy <source-gol-file> <target-gol-file> [<options>]

- If an area is specified (using [`--bbox`](#option-bbox) or [`--polygon`]((#option-polygon)), only the tiles touching that area are copied.

- Missing tiles will be imported from a repository, if one is specified via [`--url`](#option-url).

- To create a backup, or to share a library via a network connection or slow/space-restricted media, use [`save`](save). 

## Options

{% include gol/option-bbox.md %}
{% include gol/option-new.md %}
{% include gol/option-polygon.md %}
{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-url.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}

