---
layout: default
title:  Features
parent: GeoDesk for Python
nav_order: 3
---

# Features

A **feature** represents a geographic element. This can be a point of interest like a mailbox or a restaurant, a park, a lake, a segment of a road, or a more abstract concept like a bus route.

- **Nodes** represent a simple point feature

- **Ways** are an ordered sequence of nodes, used to represent line strings and
  simple polygons

- **Relations** represent more complex objects, such as polygons with holes, a route or a river system. They may contain nodes, ways or other relations as members. 

```python
>>> city.osm_type
'node'
>>> city.id
1601837931
>>> city.name
'Praha'
>>> city['name:en']
'Prague'
>>> city.population
1275406
>>> city.str('population')
'1275406'
```

## OSM-specific properties

### `Feature.``osm_type` {#Feature_osm_type}
{:.api}

`"node"`, `"way"` or `"relation"`

### `Feature.``id` {#Feature_id}
{:.api}

The feature's numeric OSM identifier. IDs are unique only within the feature type (which means a node and a way may have the same ID). Always `0` if this feature is an anonymous node, otherwise non-zero.

### <code><span style="font-size: 12px">Feature</span>.<b>tags</b></code>

The feature's `Tags` (key/value pair that describe its properties). 

### `Feature.``is_node` {#Feature_is_node} 
{:.api}

`True` if this feature is a node, otherwise `False`.

### `Feature.``is_way` {#Feature_is_way} 
{:.api}

`True` if this feature is a way (linear or area), otherwise `False`.

### `Feature.``is_way` {#Feature_is_way} 
{:.api}

`True` if this feature is a way (linear or area), otherwise `False`.

### `Feature.``is_relation` {#Feature_is_relation}
{:.api}

`True` if this feature is a relation (area or non-area), otherwise `False`.

### `Feature.``is_area` {#Feature_is_area}
{:.api}

`True` if this feature is a way or relation that represents an area, otherwise `False`.

### `Feature.``nodes` {#Feature_nodes}
{:.api}

The nodes of a way, or an empty set if this feature is a node or relation.

### `Feature.``members` {#Feature_members}
{:.api}

The members of a relation, or an empty set if this feature is a node or way.

### `Feature.``parents` {#Feature_parents}
{:.api}

The relations that have this feature as a member, as well as the ways to which a node feature belongs (Use <code><i>node</i>.parents.relations</code> to obtain just the relations to which a node belongs).

### `Feature.``role` {#Feature_role}
{:.api}

The role of this feature if it was returned via a member set (an empty string if this feature has no explicit role within its parent relation), or `None` for a `Feature` that was not returned via a member set.   

## Geometric properties

### `Feature.``bounds` {#Feature_bounds}
{:.api}

The bounding `Box` of this feature.

### `Feature.``x` {#Feature_x}
{:.api}

The x-coordinate of a node, or the horizontal midpoint of the `bounds` of a way or relation (GeoDesk Mercator projection)

### `Feature.``y` {#Feature_y}
{:.api}

The y-coordinate of a node, or the vertical midpoint of the `bounds` of a way or relation (GeoDesk Mercator projection)

### `Feature.``lon` {#Feature_lon}
{:.api}

`x` in degrees longitude (WGS-84)

### `Feature.``lat` {#Feature_lat}
{:.api}

`y` in degrees latitude (WGS-84)

### `Feature.``centroid` {#Feature_centroid}
{:.api}

The feature's calculated centroid (`Coordinate`)

### `Feature.``shape` {#Feature_shape}
{:.api}

The Shapely geometry for this feature: 

- `Point` for a node
- `LineString` or `Polygon` for a way
- `Polygon`, `GeometryCollection`, `MultiPoint`, `MultiLineString` or `MultiPolygon` for a relation 

### `Feature.``area` {#Feature_area}
{:.api}

The calculated area (in square meters) if this feature is polygonal, otherwise `0`.

### `Feature.``length` {#Feature_length}
{:.api}

The calculated length (in meters) if this feature is lineal, or its circumference if it is polygonal, otherwise `0`.

TODO: GeometryCollection?

## Formatting

To aid import into GIS applications, features can be converted into different representations. You can also visualize a feature on a map. See [Formats](formats) and [Maps](maps) to learn how output can be customized. 

### `Feature.``geojson` {#Feature_geojson}
{:.api}

The [GeoJSON](https://geojson.org/) representation of this feature.

### `Feature.``wkt` {#Feature_wkt}
{:.api}

The feature's geometry as [Well-Known Text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry).

### `Feature.``map` {#Feature_map}
{:.api}

A [`Map`](maps) displaying this feature. 

## Tag methods

### `Feature.``str`(*key*) {#Feature_str}
{:.api}

Returns the value of the given tag key as a string, or an empty string if the feature doesn't have the requested tag.

### `Feature.``num`(*key*) {#Feature_num}
{:.api}

Returns the value of the given tag as an `int` or `float`, or `0` if the feature doesn't have the requested tag.

