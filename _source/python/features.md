---
layout: default
title:  Feature Objects
parent: GeoDesk for Python
nav_order: 4
---
> .module geodesk
> .class Feature

# Feature Objects

A `Feature` represents a geographic element. This can be a point of interest like a mailbox or a restaurant, a park, a lake, a segment of a road, or an abstract concept like a bus route.

OpenStreetMap uses three types of features:

- *Node* -- a simple point feature

- *Way* -- an ordered sequence of nodes, used to represent line strings and
  simple polygons

- *Relation* -- an object composed of multiple features, such as a polygon with holes, a route or a river system. A relation may contain nodes, ways or other relations as members. 

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

> .property osm_type

`"node"`, `"way"` or `"relation"`

> .property id

The feature's numeric OSM identifier. IDs are unique only within the feature type (which means a node and a way may have the same ID). Always `0` if this feature is an [anonymous node](#anonymous-nodes), otherwise non-zero.

> .property tags

The feature's [`Tags`](#Tags) (key/value pairs that describe its properties). 

> .property is_node

`True` if this feature is a node, otherwise `False`.

> .property is_way

`True` if this feature is a way (linear or area), otherwise `False`.

> .property is_relation

`True` if this feature is a relation (area or non-area), otherwise `False`.

> .property is_area

`True` if this feature is a way or relation that represents an area, otherwise `False`.

> .property nodes

The nodes of a way, or an empty set if this feature is a node or relation.

> .property members

The members of a relation, or an empty set if this feature is a node or way. Features returned from this set (or a subset) have a `role` property with a value other than `None`.

> .property parents

The relations that have this feature as a member, as well as the ways to which a node feature belongs (Use <code><i>node</i>.parents.relations</code> to obtain just the relations to which a node belongs).

> .property role

The role of this feature if it was returned via a member set (an empty string if this feature has no explicit role within its parent relation), or `None` for a `Feature` that was not returned via a member set.   

## Geometric properties

> .property bounds

The bounding [`Box`](#Box) of this feature.

> .property x

The x-coordinate of a node, or the horizontal midpoint of the `bounds` of a way or relation (GeoDesk Mercator projection)

> .property y

The y-coordinate of a node, or the vertical midpoint of the `bounds` of a way or relation (GeoDesk Mercator projection)

> .property lon

`x` in degrees longitude (WGS-84)

> .property lat

`y` in degrees latitude (WGS-84)

> .property centroid

The feature's calculated centroid ([`Coordinate`](#Coordinate))

> .property shape

The Shapely geometry for this feature: 

- `Point` for a node
- `LineString` or `Polygon` for a way
- `Polygon`, `GeometryCollection`, `MultiPoint`, `MultiLineString` or `MultiPolygon` for a relation 

> .property area

The calculated area (in square meters) if this feature is polygonal, otherwise `0`.

> .property length

The calculated length (in meters) if this feature is lineal, or its circumference if it is polygonal, otherwise `0`.

TODO: GeometryCollection?

## Formatting

To aid import into GIS applications, features can be converted into different representations. You can also visualize a feature on a map. See [Formats](formats) and [Maps](maps) to learn how output can be customized. 

> .property geojson

The [GeoJSON](https://geojson.org/) representation of this feature.

> .property wkt

The feature's geometry as [Well-Known Text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry).

> .property map

A [`Map`](#Map) displaying this feature. 

## Tag methods

> .method str(*key*)

Returns the value of the given tag key as a string, or an empty string if this feature doesn't have the requested tag.

> .method num(*key*)
 
Returns the value of the given tag as an `int` or `float`, or `0` if this feature doesn't have the requested tag.

> .class Tags

## `Tags` objects

Iterating a `Tags` object yields key/value tuples:

```python
>>> for key, value in street.tags:
...     print f'{key}={value}'  
('highway', 'residential')
('name', 'Rue de la Eglise')
('maxspeed', 30)
```


## Anonymous nodes

An **anonymous node** has no tags and does not belong to any relations --- it merely serves to define the geometry of a way. By default, feature libraries omit the IDs of such nodes to save space, in which case [`id`](#Feature.id) is `0`.

Anonymous nodes can only be obtained by [`nodes`](#Feature.nodes); they are not part of any other feature sets. The [`parents`](#Feature.parents) property of an anonymous node contains the ways to which this node belongs (always at least one).  

Every anonymous node in a GOL has a unique location. If two or more nodes share the exact latitude and longitude, the untagged ones are tagged `geodesk:duplicate=yes` and retain their ID.
