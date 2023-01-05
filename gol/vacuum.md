---
layout: default
title: vacuum
parent: GOL Utility
nav-order: 11
---

# `vacuum` ~~0.2~~

Compacts a feature library by removing empty pages.

Usage:

    gol vacuum <gol-file> [<ratio>] [<options>]

If `<ratio>` is specified, the library is only compacted if the amount of free space
exceeds the given percentage of its total size.

## Options

{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}

