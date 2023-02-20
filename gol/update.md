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

### `-F`, `--force` {#option-force}

Ignores replication warnings.

By default, `gol update` will only apply changes from an `.osc` file if all of the following are true:

- `create`: Feature must not exist.
- `modify`: Feature must exist.
- `delete`: Feature must exist.

If you specify this option, `create` will overwrite an existing feature, `modify` will create a feature if it doesn't exist, and `delete` will do nothing if the feature does not exist. 

### `-i`, `--index` {#option-index}

Re-creates the [ID indexes](build#id-indexing) to speed up processing.

{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}