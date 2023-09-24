---
layout: default
title:  Geometric Primitives
parent: GeoDesk for Python
nav_order: 2
---



# Geometric Primitives

<a id="Coordinate"></a>

## `Coordinate` objects

A `Coordinate` object is the most basic geometric element, describing a point on the surface of the Earth. Most GeoDesk functions accept coordinate values as simple `(x,y)` tuples, but using `Coordinate` objects has two advantages: They are more compact, and they convert seamlessly between Mercator projection and longitude/latitude (whereas tuples must use Mercator-projected coordinate values).

Construct coordinates like this:

```python
Coordinate(lon=12.42, lat=48.76)      # longitude & latitude (any order)
Coordinate(x=148176372, y=668142957)  # Mercator-projected x/y position
Coordinate(148176372, 668142957)      # (Mercator projection by default)
```

### Comparing coordinates

Coordinates are equal to a simple tuple that has the same Mercator-projected coordinates:

```python
>>> Coordinate(lon=12.42, lat=48.76) == (148176372, 668142957)
True
```

`Coordinate` objects are hashable and therefore suitable as dictionary keys.

### Properties

<h3 id="Coordinate_x" class="api"><span class="prefix">Coordinate.</span><span class="name">x</span></h3><div class="api" markdown="1">

The Mercator-projected x-ordinate.

</div><h3 id="Coordinate_y" class="api"><span class="prefix">Coordinate.</span><span class="name">y</span></h3><div class="api" markdown="1">

The Mercator-projected y-ordinate.

</div><h3 id="Coordinate_lon" class="api"><span class="prefix">Coordinate.</span><span class="name">lon</span></h3><div class="api" markdown="1">

The coordinate's longitude.

</div><h3 id="Coordinate_lat" class="api"><span class="prefix">Coordinate.</span><span class="name">lat</span></h3><div class="api" markdown="1">

The coordinate's latitude.

<a id="Box"></a>

</div>
## `Box` objects

A `Box` represents an axis-aligned bounding box.

<h3 id="Box_Box" class="api"><span class="prefix">geodesk.</span><span class="name">Box</span><span class="paren">(</span><i>coords</i><span class="paren">)</span></h3><div class="api" markdown="1">

</div>
### Operators

### `+` <span style="color:#e0e0e0">&nbsp;&ndash;</span> Expansion

### `+` (Expansion)

### `+` &nbsp;&ndash;&nbsp; Expansion

### `+` &nbsp;&nbsp;&nbsp; Expansion


### `+` : Expansion

### `&` &nbsp;&ndash; Intersection

<h3 id="Box_buffer" class="api"><span class="prefix">Box.</span><span class="name">buffer</span><span class="paren">(</span><i>units</i>=<span class="default">*distance*</span><span class="paren">)</span></h3><div class="api" markdown="1">

</div><h3 id="Box_buffered" class="api"><span class="prefix">Box.</span><span class="name">buffered</span><span class="paren">(</span><i>units</i>=<span class="default">*distance*</span><span class="paren">)</span></h3><div class="api" markdown="1">

