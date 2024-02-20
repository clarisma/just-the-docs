---
layout: default
title:  Coordinate Objects
parent: GeoDesk for Python
nav_order: 2
---


<a id="Coordinate"></a>

# Coordinate Objects

A `Coordinate` object is the most basic geometric element, describing a point on the surface of the Earth. Most GeoDesk functions accept coordinate values as simple `(x,y)` tuples, but using `Coordinate` objects has two advantages: They are more compact, and they convert seamlessly between Mercator projection and longitude/latitude (whereas tuples must use Mercator-projected coordinate values).

<h3 id="Coordinate_Coordinate" class="api"><span class="prefix">geodesk.</span><span class="name">Coordinate</span><span class="paren">(</span><i>coords</i><span class="paren">)</span></h3><div class="api" markdown="1">

Use positional arguments (`x`/`y` in Mercator projection) or explicit keywords:

```python
Coordinate(lon=12.42, lat=48.76)      # longitude & latitude (any order)
Coordinate(x=148176372, y=668142957)  # Mercator-projected x/y position
Coordinate(148176372, 668142957)      # (Mercator projection by default)
```

</div>

<h3 id="lonlat" class="api"><span class="prefix">geodesk.</span><span class="name">lonlat</span><span class="paren">(</span><i>coords</i><span class="paren">)</span></h3><div class="api" markdown="1">

Creates a single `Coordinate` or a list with multiple `Coordinate` objects.

*coords* can be one of the following:

- Two individual coordinate values

- Multiple coordinate pairs (tuples or other sequence type)

- A sequence of coordinate pairs

- A sequence of individual coordinate values (interpreted as pairs)

Longitude must be specified before latitude.

```python
lonlat(11.81, 51.23)     # Creates single Coordinate

# The following are equivalent (list of 3 Coordinates)
lonlat((11.81,51.23), (7.44,51.71), (9.25, 52.63))
lonlat([11.81,51.23], [7.44,51.71], [9.25, 52.63])
lonlat([ [11.81,51.23], [7.44,51.71], [9.25, 52.63] ])
lonlat(11.81, 51.23, 7.44, 51.71, 9.25, 52.63)
```

</div><h3 id="latlon" class="api"><span class="prefix">geodesk.</span><span class="name">latlon</span><span class="paren">(</span>lat, lon<span class="paren">)</span></h3><div class="api" markdown="1">

Same as [`lonlat()`](#lonlat), except latitude before longitude.


<a id="Coordinate"></a>

</div>
## Equality and hashing

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

