---
layout: default
title:  Geometry Objects
parent: GeoDesk for Python
nav_order: 3
---

# Geometry Objects

GeoDesk uses [Shapely](https://shapely.readthedocs.io/) for a wide variety of geometry operations. Shapely provides a Python interface to the widely-deployed GEOS library.

Shapely/GEOS is a library for *planar geometry* --- it operates on flat 2-D space. The Earth isn't flat, of course, but for most real-life cartographic needs, we can pretend that it is and use simplified geometric techniques. 

Shapely's [`Geometry`](https://shapely.readthedocs.io/en/stable/geometry.htm) class has eight subtypes:

[`Point`](https://shapely.readthedocs.io/en/stable/reference/shapely.Point.html)| A geometry type that represents a single coordinate
[`LineString`](https://shapely.readthedocs.io/en/stable/reference/shapely.LineString.html)| A geometry type composed of one or more line segments.
[`LinearRing`](https://shapely.readthedocs.io/en/stable/reference/shapely.LinearRing.html)| A LineString that forms a closed loop.
[`Polygon`](https://shapely.readthedocs.io/en/stable/reference/shapely.Polygon.html)| A geometry type representing an area that is enclosed by a LinearRing.
[`MultiPoint`](https://shapely.readthedocs.io/en/stable/reference/shapely.MultiPoint.html)| A collection of one or more Points.
[`MultiLineString`](https://shapely.readthedocs.io/en/stable/reference/shapely.MultiLineString.html)| A collection of one or more LineStrings.
[`MultiPolygon`](https://shapely.readthedocs.io/en/stable/reference/shapely.MultiPolygon.html)| A collection of one or more Polygons.
[`GeometryCollection`](https://shapely.readthedocs.io/en/stable/reference/shapely.GeometryCollection.html)| A collection of one or more geometries that may contain more than one type of geometry.




Adapted from [Shapely Documentation](https://shapely.readthedocs.io/) --- &copy; 2007 Sean C. Gillies, 2019 Casper van der Wel, 2007 -- 2022 Shapely Contributors. Licensed under [BSD-3-Clause](https://github.com/shapely/shapely/blob/main/LICENSE.txt)

