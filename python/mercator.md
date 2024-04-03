---
layout: default
title:  Mercator Projection
parent: GeoDesk for Python
description: Converting between WGS-84 (longitude/latitude) and Mercator projection
nav_order: 10
---


# Mercator Projection

For most geometric operations, GeoDesk expects coordinates in [Mercator Projection](/core-concepts#coordinate-system). OpenStreetMap and many other geospatial datasets use WGS-84, with coordinates expressed as degrees longitude and latitude. GeoDesk's `Coordinate`, `Box` and `Feature` objects allow you to use both coordinate systems interchangeably, but if you work with Shapely geometries (which are unitless and hence projection-agnostic), you may need to explicitly convert between them.

If you are reading a shapefile with the outlines of census districts, and you want to find all streets within each district using GeoDesk, you will first need to convert them [`to_mercator()`](/python\mercator#to_mercator).

Likewise, if you obtained the outline of a lake from a GOL, then applied a buffer using Shapely, and now need to export the resulting geometry to another GIS tool (which expects WGS-84), you'll need to convert its coordinates with [`from_mercator()`](/python\mercator#from_mercator).

## Converting from WGS-84 to Mercator

<h3 id="to_mercator" class="api"><span class="prefix">geodesk.</span><span class="name">to_mercator</span><span class="paren">(</span><i>geom_or_units</i>, lat=<span class="default">None</span>, y=<span class="default">None</span><span class="paren">)</span></h3><div class="api" markdown="1">

<h3>Geometry</h3>

For a `Geometry` object in WGS-84 (degrees longitude and latitude), returns a new `Geometry` with Mercator-projected coordinates:

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

</div>
## Converting from Mercator to WGS-84

<h3 id="from_mercator" class="api"><span class="prefix">geodesk.</span><span class="name">from_mercator</span><span class="paren">(</span><i>geom_or_length</i>, units=<span class="default">'meters'</span>, lat=<span class="default">None</span>, y=<span class="default">None</span><span class="paren">)</span></h3><div class="api" markdown="1">

<h3>Geometry</h3>

For a `Geometry` object in Mercator projection, returns a new `Geometry` with coordinates in WGS-84 (degrees longitude and latitude).

<h3>Length</h3>

To convert a distance in Mercator units to meters (or other units), specify the desired `unit` (`meters` by default) as well as a latitude value that determines the scale (as `lat` for degrees or `y` as a Mercator-projected equivalent).

The following are valid length units:

- `meters` (`m`)
- `feet` (`ft`)
- `yards` (`yd`)
- `kilometers` (`km`)
- `miles` (`mi`)

{%comment%}
```python
# 300 feet as Mercator units
>>> to_mercator(feet=300, lat=38)  # at 38 degrees latitude
12436
>>> to_mercator(feet=300, lat=65)  # at 65 degrees latitude
23189
```
{%endcomment%}
