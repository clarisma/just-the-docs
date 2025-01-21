---
layout: default
title: GOL Utility
has_children: true
has_toc: false
nav_order: 8
permalink: /gol
---

# The `gol` Command Line Utility

The `gol` ("Geo-Object Librarian") command-line utility allows you to build, manage and
query [feature libraries](/libraries).

Usage:

    gol <command> <gol-file> [<arguments>] [<options>]

<img class="figure" src="/img/gol-diagram2.png" width=400>

## Commands

<table>
<tr>
<td markdown="1">
[`build`](/gol/build)
</td>
<td markdown="1">
Creates a feature library from OpenStreetMap data.
</td>
</tr>

<tr>
<td markdown="1">
[`check`](/gol/check)
</td>
<td markdown="1">
Verifies the library's integrity.
</td>
</tr>

<!--
<tr>
<td markdown="1">
[`copy`](/gol/copy)
</td>
<td markdown="1">
Copies tiles between libraries.
</td>
</tr>
-->

<tr>
<td markdown="1">
[`help`](/gol/help)
</td>
<td markdown="1">
Displays documentation.
</td>
</tr>

<tr>
<td markdown="1">
[`info`](/gol/info)
</td>
<td markdown="1">
Provides basic file statistics.
</td>
</tr>

<tr>
<td markdown="1">
[`load`](/gol/load)
</td>
<td markdown="1">
Imports tiles for a specific area.
</td>
</tr>

<tr>
<td markdown="1">
[`query`](/gol/query)
</td>
<td markdown="1">
Extracts features.
</td>
</tr>

<!--
<tr>
<td markdown="1">
[`remove`](/gol/remove) ~~0.2~~
</td>
<td markdown="1">
Removes tiles in a specific area.
</td>
</tr>

<tr>
<td markdown="1">
[`retain`](/gol/retain) ~~0.2~~
</td>
<td markdown="1">
Removes tiles *outside* a specific area.
</td>
</tr>
-->

<tr>
<td markdown="1">
[`save`](/gol/save)
</td>
<td markdown="1">
Exports tiles.
</td>
</tr>

<!--
<tr>
<td markdown="1">
[`update`](/gol/update) ~~0.3~~
</td>
<td markdown="1">
Updates the library.
</td>
</tr>
-->

</table>

<!--
<blockquote class="note" markdown="1">
GeoDesk is in **Early Access**. Some commands and options are not yet available in Version {{ site.geodesk_version }}. ~~This~~ marks the targeted version.
</blockquote>
-->


## Common Options

{% include gol/option-area.md %}
{% include gol/option-bbox.md %}
{% include gol/option-new.md %}
{% include gol/option-output.md %}
{% include gol/option-quiet.md %}
{% include gol/option-url.md %}
{% include gol/option-silent.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}
