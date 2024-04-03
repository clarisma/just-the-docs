---
layout: default
title:  Coordinate Objects
parent: GeoDesk for Python
nav_order: 2
---

> .module geodesk
> .class Coordinate

# Coordinate Objects

A `Coordinate` object is the most basic geometric element, describing a point on the surface of the Earth. Most GeoDesk functions accept coordinate values as simple `(x,y)` tuples, but using `Coordinate` objects has two advantages: They are more compact, and they convert seamlessly between Mercator projection and longitude/latitude (whereas tuples must use Mercator-projected coordinate values).   

> .method Coordinate(*coords*)
 
Use positional arguments (`x`/`y` in Mercator projection) or explicit keywords: 

```python
Coordinate(lon=12.42, lat=48.76)      # longitude & latitude (any order)
Coordinate(x=148176372, y=668142957)  # Mercator-projected x/y position
Coordinate(148176372, 668142957)      # (Mercator projection by default)
```

> .end class

> .method lonlat(*coords*)
 
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

> .method latlon(lat, lon)
 
Same as [`lonlat()`](#lonlat), except latitude before longitude.


> .class Coordinate

## Equality and hashing

Coordinates are equal to a simple tuple that has the same Mercator-projected coordinates:

```python
>>> Coordinate(lon=12.42, lat=48.76) == (148176372, 668142957)
True
```

`Coordinate` objects are hashable and therefore suitable as dictionary keys.

## Properties

> .property x

The Mercator-projected x-ordinate.
 
> .property y

The Mercator-projected y-ordinate.

> .property lon

The coordinate's longitude.

> .property lat

The coordinate's latitude.

