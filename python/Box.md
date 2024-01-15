---
layout: default
title:  Box Objects
parent: GeoDesk for Python
nav_order: 3
---


<a id="Box"></a>

# Box Objects

A `Box` represents an axis-aligned bounding box.

<h3 id="Box_Box" class="api"><span class="prefix">geodesk.</span><span class="name">Box</span><span class="paren">(</span><i>coords</i><span class="paren">)</span></h3><div class="api" markdown="1">

</div>
## Properties

<h3 id="Box_shape" class="api"><span class="prefix">Box.</span><span class="name">shape</span></h3><div class="api" markdown="1">

The box as a [`Polygon`](/python\Geometry#Geometry).

</div>
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

<h3 id="Box_buffer" class="api"><span class="prefix">Box.</span><span class="name">buffer</span><span class="paren">(</span><i>units</i>=<span class="default">*distance*</span><span class="paren">)</span></h3><div class="api" markdown="1">

Expands this box in all directions by the given distance. Negative values shrink it (which may result in an empty box).

</div><h3 id="Box_buffered" class="api"><span class="prefix">Box.</span><span class="name">buffered</span><span class="paren">(</span><i>units</i>=<span class="default">*distance*</span><span class="paren">)</span></h3><div class="api" markdown="1">

Same as [`buffer()`](/python\Box#Box_buffer), but returns a copy, leaving this box unmodified.
