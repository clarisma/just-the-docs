---
layout: default
title:  Coordinate Objects
parent: GeoDesk for Python
nav_order: 2
---


<a id="Coordinate"></a>

# Coordinate Objects

A `Coordinate` object is the most basic geometric element, describing a point on the surface of the Earth. Most GeoDesk functions accept coordinate values as simple `(x,y)` tuples, but using `Coordinate` objects has two advantages: They are more compact, and they convert seamlessly between Mercator projection and longitude/latitude (whereas tuples must use Mercator-projected coordinate values).

Construct coordinates like this:

```python
Coordinate(lon=12.42, lat=48.76)      # longitude & latitude (any order)
Coordinate(x=148176372, y=668142957)  # Mercator-projected x/y position
Coordinate(148176372, 668142957)      # (Mercator projection by default)
```

Coordinates are equal to a simple tuple that has the same Mercator-projected coordinates:

```python
>>> Coordinate(lon=12.42, lat=48.76) == (148176372, 668142957)
True
```

`Coordinate` objects are hashable and therefore suitable as dictionary keys.

## Properties

<h3 id="Coordinate_x" class="api"><span class="prefix">Coordinate.</span><span class="name">x</span></h3><div class="api" markdown="1">

The Mercator-projected x-ordinate.

</div><h3 id="Coordinate_y" class="api"><span class="prefix">Coordinate.</span><span class="name">y</span></h3><div class="api" markdown="1">

The Mercator-projected y-ordinate.

</div><h3 id="Coordinate_lon" class="api"><span class="prefix">Coordinate.</span><span class="name">lon</span></h3><div class="api" markdown="1">

The coordinate's longitude.

</div><h3 id="Coordinate_lat" class="api"><span class="prefix">Coordinate.</span><span class="name">lat</span></h3><div class="api" markdown="1">

The coordinate's latitude.

