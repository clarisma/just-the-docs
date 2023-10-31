---
layout: default
title: Quickstart
parent: GeoDesk for Python
nav_order: 1
---
# Quickstart

## Install Python

You probably already have Python installed:

```console
$ python -V
Python 3.11.5
```

If you don't (or the version is lower than 3.7), [download and install Python](https://www.python.org/downloads/).

## Install GeoDesk

```console
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

```console
$ gol build france france-latest.osm.pbf
```

On a reasonably modern machine, this should take a few minutes.

## Ready to go!

Start the interactive Python shell:

```console
$ python
```

First, we'll import the GeoDesk module:

```python
>>> from geodesk import *
```

Then we open the GOL (the `.gol` file extension is optional):

```python
>>> france = Features("france")
```

`france` contains all the features in France: buildings, rivers and roads, parks and power lines, down to picnic benches and garbage bins.

For now, we're just interested in museums:

```python
>>> museums = france("na[tourism=museum]")
```

How many are there?

```python
>>> museums.count
4495
```

Wow, lots of culture and history in France!

Let's focus on the ones in Paris. To do so, we need to get the city itself. OpenStreetMap data contains *administrative areas*. These form a hierarchy, from country (level 2) to individual neighborhoods (level 11). Level 8 is for cities:

```python
>>> paris = france("a[boundary=administrative][admin_level=8][name=Paris]").one
```

Now we can get all museums in Paris:

```python
>>> paris_museums = museums.within(paris)
```

Let's put them on a map, which we'll open in a browser:

```python
>>> paris_museums.map.show()
```

Let's show the opening hours in an overlay (a *tool tip*), and open the museum's website when the user clicks on its marker. While we're at it, let's pick a marker color that's a bit more *artistique*.

```python
>>> map = Map()
>>> map.tooltip = "{name}<br>{opening_hours}"
>>> map.link = "{website}"
>>> map.add(paris_museums, color="purple")
>>> map.show()
```

*Et voila!*

Go ahead and add restaurants. Or parks. Or metro stops.

```python
>>> map.add("na[amenity=restaurant]", color="orange")
>>> map.add("a[leisure=park]", color="green")
>>> map.add("n[railway=station][station=subway]", color="red")
```

Of course, this is merely an *amuse-bouche* to whet your appetite. With a few lines of Python code, you can quickly dig through this vast and ever-growing goldmine of geospatial data.



