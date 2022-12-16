---
layout: default
title: copy
parent: GOL Utility
nav-order: 2
---

# `copy` ~~0.3~~

Copies tiles from one library to another.

Usage:

    gol copy <source-gol-file> <target-gol-file> [<options>]

- If an area is specified (using [`--bbox`](#option-bbox) or [`--area`]((#option-area)), only the tiles touching that area are copied.

- Missing tiles will be imported from a repository, if one is specified via [`--url`](#option-url).

- To create a backup, or to share a library via a network connection or slow/space-restricted media, use [`save`](save). 

- If the source and target GOL contain different versions, the target's version is set to the newer version, and all tiles from the older GOL are marked as stale.

## Options

{% include gol/option-area.md %}
{% include gol/option-bbox.md %}
{% include gol/option-new.md %}
{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-url.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}

