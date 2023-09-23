---
layout: default
title: Tutorial
parent: GeoDesk for Python
nav_order: 1
---
# Five-Minute Tutorial

<div class="box note" markdown="1">

This tutorial assumes that you are already familiar with OpenStreetMap and its data model. If not, read our [Introduction to OSM](/intro-to-osm) or visit [the official OSM website](https://wiki.openstreetmap.org/wiki/Develop).

</div>

## Create a Feature Library

- [Download and install](https://www.geodesk.com/download) the GOL command-line utility

- Download some OSM data (in PBF format). We suggest starting with a subset for a single
  country (or smaller part). For example, Germany (file size: 3.5 GB) can be downloaded from
  [GeoFabrik](https://download.geofabrik.de/europe/germany.html) or
  [BBBike](https://download.bbbike.org/osm/planet/sub-planet/).

- Turn the PBF file into a Geographic Object Library:

  ```
  gol build germany germany-latest.osm.pbf
  ```

  On a multi-core workstation with at least 24 GB of RAM, this should take a few minutes;
  on an 8-GB dual-core laptop, expect 20 minutes or more. The output will look like this:

  ```
  Building germany.gol from germany-latest.osm.pbf using default settings...
  Analyzed germany-latest.osm.pbf in 20s
  Sorted 86,432,126 features in 1m 13s
  Validated 1023 tiles in 36s
  Compiled 1023 tiles in 1m 24s
  Linked 1023 tiles in 8s
  Build completed in 3m 43s
  ```

