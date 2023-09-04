---
layout: default
title:  Feature Sets
parent: GeoDesk for Python
nav_order: 4
---
# Feature Sets

A **feature set** represents those `Feature` objects that meet certain critera.

## Filtering features

### By bounding box

`Features.``[`
{:.api}


### By type and tags

### By geometry

### Using filter methods

Apply a [spatial filter](#spatial-filters) or [topological filter](#topological-filters):

```python
states.within(usa)
features("w[highway]").members_of(route66)
```

## `Features` objects

`class geodesk.Features(`*gol* [`,` *url* ]`)`



## Properties

### `Features.``count` {#Features_count}
{:.api}

The total number of features in this set.

### `Features.``area` {#Features_area}
{:.api}

The total area (in square meters) of all areas in this set.

### `Features.``length` {#Features_length}
{:.api}

The total length (in meters) of all features in this set. For areas, their circumference
is used.

## Subsets

### `Features.``nodes` {#Features_nodes}
{:.api}

Only features that are nodes.

### `Features.``ways` {#Feature_ways}
{:.api}

Only features that are ways (including areas that are represented using a closed way).

If you want to restrict the subset to linear ways, use <code><i>features</i>('w')</code>.

### `Features.``relations` {#Feature_relations}
{:.api}

Only features that are relations (including relations that represent areas).

If you want to restrict the subset to non-area relations, use <code><i>features</i>('r')</code>.

## Formatting

### `Features.``geojson` {#Feature_geojson}
{:.api}

The set's features represented as GeoJSON.

### `Features.``map` {#Feature_map}
{:.api}

A [`Map`](maps) that displays the features in this set. Use `show()` to open it in a browser window, or `save()` to write its HTML file. 

```python
restaurants.map.show()
hotels.map.save("hotel-map") # .html by default
hydrants.map(color='red')    # map with fire hydrants marked in red
```

TODO: link to detailed description


## Spatial filters

These methods return a subset of only those features that fulfill a specific spatial relationship with another geometrical object (`Feature`, `Geometry`, `Box` or `Coordinate`). 

### `Feature.``around`(*geom*, *units*=*distance*) {#Feature_around}
{:.api}

Features that lie within the given distance from the centroid of *geom*. 
In lieu of a geometrical object, you can also specify coordinates using 
`x` and `y` (for Mercator-projected coordinates) or `lon` and `lat` (in degrees).
Use `meters`, `feet`, `yards`, `km`, `miles`, `mercator_units` to specify the maximum distance.

Example:

```python
bus_stops.around(restaurant, meters=500) 
features.around(miles=3, lat=40.12, lon=-76.41) 
```

### `Features.``contains`(*geom*) {#Feature_contains}
{:.api}

Features whose geometry *contains* the given geometrical object.

**Note:** If you want to test whether this set includes a particular feature, use <code><i>feature</i> in <i>set</i></code>.

### `Features.``intersects`(*geom*) {#Feature_intersects}
{:.api}

Features whose geometry *intersects* the given shape-like object.


## Topological filters

These methods return a subset of those features that have a specific topological relationship with another `Feature`.

### `Features.``members_of`(*feature*) {#Feature_members_of}
{:.api}

Features that are members of the given relation, or nodes of the given way.

### `Features.``parents_of`(*feature*) {#Feature_parents_of}
{:.api}

Relations that have the given feature as a member, as well as ways to which the given node belongs.

### `Features.``descendants_of`(*feature*) {#Feature_descendants_of}
{:.api}

### `Features.``ancestors_of`(*feature*) {#Feature_ancestors_of}
{:.api}

### `Features.``connected_to`(*feature*) {#Feature_connected_to}
{:.api}



