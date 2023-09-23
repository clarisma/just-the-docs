---
layout: default
title:  Test
parent: GeoDesk for Python
nav_order: 6
---
# Feature Sets

A **feature set** represents those [`Feature`](features) objects that meet certain criteria.

### `geodesk.``Features`(*gol*, *url*=None) {#Features}
{:.api}

Creates a feature set based on a Geographic Object Library.

## Filtering features

### By bounding box

### By type and tags

### By geometry

### Using filter methods

Apply a [spatial filter](#spatial-filters) or [topological filter](#topological-filters):

```python
states.within(usa)
features("w[highway]").members_of(route66)
```

## Obtaining `Feature` objects

Iterate through the feature set, or turn it into a `list`:

```python
>>> for hotel in hotels:
...     print(hotel.name)
...
Hôtel du Louvre
Ambassadeur
Brit Hotel
...
>>> list(hotels)
[way/112112065, relation/1575507, ... , node/3558592188]
```

To check if the set is non-empty:

```python
if pubs(within_dublin):
    print('Great, we can grab a beer in this town!')
```

## Properties

>.api Features.count

The total number of features in this set.

>.api Features.area

The total area (in square meters) of all areas in this set.

### `Features.``length` {#Features_length}
{:.api}

The total length (in meters) of all features in this set. For areas, their circumference
is used.

## Subsets

### `Features.``nodes` {#Features_nodes}
{:.api}

Only features that are nodes.

### `Features.``ways` {#Features_ways}
{:.api}

Only features that are ways (including areas that are represented using a closed way).

If you want to restrict the subset to linear ways, use <code><i>features</i>('w')</code>.

### `Features.``relations` {#Features_relations}
{:.api}

Only features that are relations (including relations that represent areas).

If you want to restrict the subset to non-area relations, use <code><i>features</i>('r')</code>.

## Formatting

### `Features.``geojson` {#Features_geojson}
{:.api}

The set's features represented as GeoJSON.

### `Features.``map` {#Features_map}
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

### `Features.``around`(*geom*, *units*=*distance*) {#Features_around}
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

### `Features.``contains`(*geom*) {#Features_contains}
{:.api}

Features whose geometry *contains* the given geometrical object.

**Note:** If you want to test whether this set includes a particular feature, use <code><i>feature</i> in <i>set</i></code>.

### `Features.``crosses`(*geom*) {#Features_crosses}
{:.api}

Features whose geometry *crosses* the given geometrical object.

### `Features.``disjoint`(*geom*) {#Features_crosses}
{:.api}

Features whose geometry is *disjoint* from the given geometrical object.

### `Features.``intersects`(*geom*) {#Features_intersects}
{:.api}

Features whose geometry *intersects* the given geometrical object.

### `Features.``overlaps`(*geom*) {#Features_overlaps}
{:.api}

Features whose geometry *overlaps* the given geometrical object.

### `Features.``touches`(*geom*) {#Features_touches}
{:.api}

Features whose geometry *touches* the given geometrical object.


## Topological filters

These methods return a subset of those features that have a specific topological relationship with another `Feature`.

### `Features.``members_of`(*feature*) {#Features_members_of}
{:.api}

Features that are members of the given relation, or nodes of the given way.

### `Features.``parents_of`(*feature*) {#Features_parents_of}
{:.api}

Relations that have the given feature as a member, as well as ways to which the given node belongs.

### `Features.``descendants_of`(*feature*) {#Features_descendants_of}
{:.api}

### `Features.``ancestors_of`(*feature*) {#Features_ancestors_of}
{:.api}

### `Features.``connected_to`(*feature*) {#Features_connected_to}
{:.api}


## Metadata

### `Features.``properties` {#Features_properties}
{:.api}

### `Features.``copyright` {#Features_copyright}
{:.api}

### `Features.``license` {#Features_license}
{:.api}

The license under which this dataset is made available. 

### `Features.``license_url` {#Features_license_url}
{:.api}

The URL where the text of the license can be found.

### `Features.``indexed_keys` {#Features_indexed_keys}
{:.api}

### `Features.``tiles` {#Features_tiles}
{:.api}
