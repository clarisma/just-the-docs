---
layout: default
title:  Box Objects
parent: GeoDesk for Python
nav_order: 3
---

> .module geodesk
> .class Box

# Box Objects

A `Box` represents an axis-aligned bounding box.

> .method Box(*coords*)

## Properties

> .property shape

The box as a [`Polygon`](#Geometry).

## Operators

`in` checks if a `Box` contains the given `Coordinate` (or another `Box`).

```python
>>> Coordinate(50,100) in Box(10,20,300,200)
True
>>> Box(-20,30,100,50) in Box(10,20,300,200)
False
```

`+` expands a `Box` so it contains a given `Coordinate` (or another `Box`).

```python
>>> b = Box(10,20,300,200)
>>> b + Coordinate(400,300)
Box(10, 20, 400, 300)
```

`|` does the same:

```python
>>> Box(10,20,300,200) | Box(50,70,400,500)
Box(10,20,400,500)
```

`&` returns the intersection of two `Box` objects (or an empty box if they don't intersect).

```python
>>> a = Box(10,20,300,200)
>>> b = Box(50,70,400,500)
>>> a & b
Box(50, 70, 300, 200)
```

Since an empty `Box` is *falsy*, you can use `&` to check if two boxes intersect:

```python
if a & b:
    print("The bounding boxes intersect.")
```

## Methods

> .method buffer(*units*=*distance*)

Expands this box in all directions by the given distance. Negative values shrink it (which may result in an empty box).

> .method buffered(*units*=*distance*)

Same as [`buffer()`](#Box.buffer), but returns a copy, leaving this box unmodified.
