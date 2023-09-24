---
layout: default
title: Quickstart
parent: GeoDesk for Python
nav_order: 1
---
# Quickstart

## Install Python

You probably already have Python installed:

```shell
$ python -V
Python 3.11.5
```

If you don't (or the version is lower than 3.9), [download and install Python](https://www.python.org/downloads/).

## Install GeoDesk

```shell
$ pip install geodesk
```

## Install the GeoDesk GOL Tool

[Download the GOL Tool](https://www.geodesk.com/download) and uncompress the ZIP file in a folder of your choice. You'll need Java: Any JRE will do, as long as it is version 16 or above (We recommend the [Adoptium OpenJDK](https://adoptium.net/)).

## Create a GOL

### Download OpenStreetMap Data

A Geographic Object Library (GOL) contains OpenStreetMap data in the format for GeoDesk. You can create a GOL from any `.osm.pbf` file. We recommend starting with a single-country or state-sized extract. These can be downloaded from various sites such as [GeoFabrik](https://download.geofabrik.de/) or
  [BBBike](https://download.bbbike.org/osm/planet/sub-planet-daily/).

### Run `gol build`

Once you have your `.osm.pbf`, you can create a GOL from it. For example:

```shell
$ gol build france france-latest.osm.pbf
```

On a reasonably modern machine, this should take a few minutes.
