---
layout: default
title:  Geometric Primitives
parent: GeoDesk for Python
nav_order: 2
---

> .module geodesk

# Geometric Primitives

> .class Coordinate 

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

> .property x

The Mercator-projected x-ordinate.
 
> .property y

The Mercator-projected y-ordinate.

> .property lon

The coordinate's longitude.

> .property lat

The coordinate's latitude.

> .class Box

## `Box` objects

A `Box` represents an axis-aligned bounding box.

> .method Box(*coords*)

### Properties

### Operators

#### Containment test (`in`)

.operator in (Containment test): *coord_or_box* in *box* 

*coord_or_box* `in` *box*

Returns true  

#### Expansion (`+` or `|`)

#### Intersection (`&`)

### Methods

> .method buffer(*units*=*distance*)

> .method buffered(*units*=*distance*)

