---
layout: default
title:  Transforming Coordinates
parent: GeoDesk for Python
nav_order: 8
---
> .module geodesk

# Transforming Coordinates

> .method to_mercator(*geom_or_units*, lat=None, y=None)

<h3>Geometry</h3>

For a `Geometry` object, returns a new `Geometry` with Mercator-projected coordinates:

```python
>>> to_mercator(LineString([(-110,37),(-109,38)]))
<LINESTRING (-1312351118 475753226, -1300420653 490791663)>
```

<h3>Coordinate sequence</h3>

For a sequence of coordinate values, returns a sequence of `Coordinate` objects. Coordinate values can be specified as `(lon,lat)` tuples or as a flat sequence. To make the coordinate order explict, pass the sequence as the keyword argument `lonlat` or `latlon`:

```python
# Coordinates as (lon, lat) tuples
>>> to_mercator([(-110,37),(-109,38)])
[(-1312351118, 475753226), (-1300420653, 490791663)]

# Coordinates as flat sequence (lon before lat)
>>> to_mercator([-110, 37, -109, 38])
[(-1312351118, 475753226), (-1300420653, 490791663)]

# Use lat/lon order instead
>>> to_mercator(latlon=[(37, -110),(38, -109)])
[(-1312351118, 475753226), (-1300420653, 490791663)]
```

<h3>Length</h3>

To convert a length value to its equivalent Mercator units, specify it using a length unit along with a latitude value that determines the scale (as `lat` for degrees or `y` as a Mercator-projected equivalent). 

The following are valid length units:

- `meters` (`m`)
- `feet` (`ft`)
- `yards` (`yd`)
- `kilometers` (`km`)
- `miles` (`mi`)

```python
# 300 feet as Mercator units 
>>> to_mercator(feet=300, lat=38)  # at 38 degrees latitude
12436
>>> to_mercator(feet=300, lat=65)  # at 65 degrees latitude
23189
``` 

> .method from_mercator(*geom*)
 
