---
layout: default
title: Feature Libraries
next: features.md
parent: GeoDesk for Java
redirect_from: /libraries
nav_order: 2
---
# Feature Libraries

<img class="float" src="/img/tiles4.png" width=280>

A **feature library** stores the worldwide OpenStreetMap dataset (or regional subset) as
a single self-contained `.gol` file. Internally, `.gol` files are divided into **tiles**
that contain the features within specific square bounding boxes.


- Create a feature library from OpenStreetMap data (as `.osm.pbf` file) using [`gol build`](/gol/build).

- Alternatively, import tiles from an existing **feature repository** using [`gol load`](/gol/load).

- A feature library does not need to contain the complete set of tiles, but only those
  that are touched by the bounding boxes of queries. If you neither `build` nor `load`
  your library, you can instruct it to programmatically import tiles as needed (*see below*).

{% comment %}

- Using the [`gol` tool](/gol), you can also [`remove`](/gol/remove) tiles you no longer need (or [`retain`](/gol/retain) only those you do), and compact a library using the [`vacuum`](/gol/vacuum) command. ~~0.2~~ 

{% endcomment %}

## Opening a library

Create a [`FeatureLibrary`]({{site.javadoc}}feature/FeatureLibrary.html) object, with the path of the `.gol` file as argument:

```java
FeatureLibrary world = new FeatureLibrary("world.gol");
```

To automatically download missing tiles as they are needed, specify the URL of the
feature repository as the second constructor argument:

```java
FeatureLibrary world = new FeatureLibrary(
    "world.gol", "https://data.geodesk.com/world");
```

- If the library file does not exist, but you've specified a repository URL, the `.gol`
  file is automatically created. 

- A repository can also reside locally --- in that case, use the `file://` protocol (e.g. `file:///home/george/geodata/planet`)

- `FeatureLibrary` is threadsafe; however, you may only create one instance for the same
  `.gol` file per process (`.gol` files can be safely shared among multiple processes).

## Querying

`FeatureLibrary` offers multiple methods to select the features it contains. See [next chapter](queries) for details.

## Closing a library

Once you are done querying a library, close it to release its resources:

```java
world.close();
```

<a name="caution-closed">
<blockquote class="warning" markdown="1">

### The "GOL-den" Rule

Do not call the methods of any objects (collections, `Feature`, `Tags`) you've retrieved from a `FeatureLibrary` after having closed it. These lightweight objects are little more than pointers into a memory-mapped file --- and closing it renders that memory area invalid. 

**If you violate this rule, you may get undefined results, or even trigger a segmentation fault.**

</blockquote>

## Troubleshooting

{% comment %}

### Fragmentation

After a long period of loading and updating tiles, or when deleting a large set of tiles, a feature library may be taking up more space than necessary (This also happens to other databases, such as Sqlite). Use [`gol vacuum`](/gol/vacuum) to compact it. ~~0.2~~ 

{% endcomment %}

### The Rollback Journal

To prevent the feature library from becoming corrupted in case a process writing to it (by downloading tiles) terminates abnormally (process killed, loss of power, etc.), all write operations maintain a **rollback journal** that enables the file to be restored to a
consistent state the next time it is opened after a crash.

This binary file has the same name as its corresponding library, with `.journal` added to its name.

<blockquote class="warning" markdown="1">

You're unlikely to encounter a journal file during normal operation. However, if you come across it, **do not** delete the journal, and **do not** separate the journal and its corresponding library (by moving/renaming one but not the other). Doing so risks leaving the
library in an inconsistent state.

When in doubt, run [`gol check`](/gol/check).


</blockquote>
