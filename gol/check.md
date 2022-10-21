---
id: query
layout: default
title: check
parent: GOL Utility
nav-order: 1
---

# `check`

Verifies the integrity of a library.

- Each `.gol` file maintains a rollback journal whenever it is modified, which enables it
  to return to a consistent state after a process crashes or power is lost. If the 
  `.journal` is moved or deleted, its corresponding library may become corrupt. 
   

Usage:

    gol check <gol-file> [<options>]  

## Options

{% include gol/option-output.md %}
{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}


