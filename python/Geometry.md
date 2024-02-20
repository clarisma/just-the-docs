---
layout: default
title:  Geometry Objects
parent: GeoDesk for Python
description: How to create geometric shapes (points, lines, polygons)
nav_order: 4
---


<a id="Geometry"></a>

# Geometry Objects

GeoDesk uses [Shapely](https://shapely.readthedocs.io/) for a wide variety of geometry operations. Shapely provides a Python interface to the widely-deployed GEOS library.

Shapely/GEOS is a library for *planar geometry* --- it operates on flat 2-D space. The Earth isn't flat, of course, but for many real-life cartographic needs, we can pretend that it is and use simplified geometric techniques.

[`Geometry`](https://shapely.readthedocs.io/en/stable/geometry.htm) is the base class of all geometric shapes. It has eight subtypes:

[`Point`](https://shapely.readthedocs.io/en/stable/reference/shapely.Point.html)| A geometry type that represents a single coordinate
[`LineString`](https://shapely.readthedocs.io/en/stable/reference/shapely.LineString.html)| A geometry type composed of one or more line segments.
[`LinearRing`](https://shapely.readthedocs.io/en/stable/reference/shapely.LinearRing.html)| A LineString that forms a closed loop.
[`Polygon`](https://shapely.readthedocs.io/en/stable/reference/shapely.Polygon.html)| A geometry type representing an area that is enclosed by a LinearRing (optionally with holes).
[`MultiPoint`](https://shapely.readthedocs.io/en/stable/reference/shapely.MultiPoint.html)| A collection of one or more Points.
[`MultiLineString`](https://shapely.readthedocs.io/en/stable/reference/shapely.MultiLineString.html)| A collection of one or more LineStrings.
[`MultiPolygon`](https://shapely.readthedocs.io/en/stable/reference/shapely.MultiPolygon.html)| A collection of one or more Polygons.
[`GeometryCollection`](https://shapely.readthedocs.io/en/stable/reference/shapely.GeometryCollection.html)| A collection of one or more geometries that may contain more than one type of geometry.

Shapely is projection-agnostic --- it uses a unit-less plane. However, to work seamlessly with GeoDesk, all geometries must be represented using [Mercator coordinates](/core-concepts#coordinate-system).

## Creating geometries

Geometries can be created directly by specifying their coordinates. You can use simple `(x,y)` tuples, or GeoDesk's [`Coordinate`](/python\Coordinate#Coordinate) objects. Tuples must use Mercator projection, whereas `Coordinate` automatically converts from degrees longitude and latitude.

GeoDesk's [`lonlat()`](/python\Coordinate#lonlat) and [`latlon()`](/python\Coordinate#latlon) functions provide a convenient way to specify coordinates.

```python
>>> Point(10, 20)>
<POINT (10 20)>
>>> Point(Coordinate(lat=40.7, lon=73.9))
<POINT (881661342 532456967)>
>>> Point(latlon(40.7, 73.9))
<POINT (881661342 532456967)>
```

LineStrings and LinearRings use a sequence of coordinates. For a LinearRing, the first and last coordinate must be the same.

```python
>>> LinearRing([c1, c2, c3, c1])
<LINEARRING (485569914 1337015677, 502272564 1474259260, 541643098 1271302994, ...>
>>> LinearRing(lonlat(40.7, 73.9, 42.1, 76.8, 45.4, 72.3, 40.7, 73.9))
<LINEARRING (485569914 1337015677, 502272564 1474259260, 541643098 1271302994, ...>
```

A Polygon is constructed from a LinearRing, and optionally one or more LinearRings that represent its holes.

```python
>>> Polygon(shell, [hole1, hole2])
<POLYGON ((881661342 532456967, 881661498 532456834, 881662912 532457214, ...>
```



Adapted from [Shapely Documentation](https://shapely.readthedocs.io/) --- &copy; 2011 -- 2023 Sean Gillies and Shapely contributors. Licensed under [BSD-3-Clause](https://github.com/shapely/shapely/blob/main/LICENSE.txt)
{:.text-small}
