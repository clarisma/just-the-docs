---
layout: default
title:  Feature Objects
parent: GeoDesk for Python
nav_order: 5
---

<a id="Feature"></a>

# Feature Objects

<img class="float" src="/img/basic-features.png" width=320>

A `Feature` represents a geographic element. This can be a point of interest like a mailbox or a restaurant, a park, a lake, a segment of a road, or an abstract concept like a bus route.


OpenStreetMap uses three types of features:

- *Node* -- a simple point feature

- *Way* -- an ordered sequence of nodes, used to represent line strings and
  simple polygons

- *Relation* -- an object composed of multiple features, such as a polygon with holes, a route or a river system. A relation may contain nodes, ways or other relations as members.

Each feature has a geometric **shape** (`Point`, `LineString`, `Polygon` or a collection type), as well as one or more **tags** (key-value pairs) that describe its details. To access a feature's tags, use <code><i>feature</i>["<i>key</i>"]</code>. If the tag key is a valid attribute name (letters and digits only, must start with a letter) and doesn't collide with a property, you can simply use <code><i>feature</i>.<i>key</i></code>.


```python
>>> city["name"]
'Praha'
>>> city.name
'Praha'
>>> city["name:en"]     # must use [] because key contains :
'Prague'
```

Tag values can be strings or numbers, or `None` if the feature doesn't have a tag with the given key. To coerce the value to string or numeric, use [`str()`](#feature.str) (returns an empty string if tag doesn't exist) or [`num()`](/python\Feature#Feature_num) (returns `0` if tag doesn't exist or is non-numeric).

```python
>>> city.population
1275406
>>> city.str("population")
'1275406'
>>> city.num("no_such_tag")
0
```

Use [`tags`](/python\Feature#Feature_tags) to get all tags. A [`Tags`](/python\Feature#Tags) object offers additional options to convert and filter tags.

```python
>>> street.tags
'{"highway": "residential", "name": "Rue des Poulets", "maxspeed": 30}'
>>> street.tags.html
'highway=residential<br>name=Rue des Poulets<br>maxpeed=30'
```

## OSM-specific properties

<h3 id="Feature_osm_type" class="api"><span class="prefix">Feature.</span><span class="name">osm_type</span></h3><div class="api" markdown="1">

`"node"`, `"way"` or `"relation"`

</div><h3 id="Feature_id" class="api"><span class="prefix">Feature.</span><span class="name">id</span></h3><div class="api" markdown="1">

The feature's numeric OSM identifier. IDs are unique only within the feature type (which means a node and a way may have the same ID). Always `0` if this feature is an [anonymous node](#anonymous-nodes), otherwise non-zero.

</div><h3 id="Feature_tags" class="api"><span class="prefix">Feature.</span><span class="name">tags</span></h3><div class="api" markdown="1">

The feature's [`Tags`](/python\Feature#Tags) (key/value pairs that describe its properties).

</div><h3 id="Feature_is_node" class="api"><span class="prefix">Feature.</span><span class="name">is_node</span></h3><div class="api" markdown="1">

`True` if this feature is a node, otherwise `False`.

</div><h3 id="Feature_is_way" class="api"><span class="prefix">Feature.</span><span class="name">is_way</span></h3><div class="api" markdown="1">

`True` if this feature is a way (linear or area), otherwise `False`.

</div><h3 id="Feature_is_relation" class="api"><span class="prefix">Feature.</span><span class="name">is_relation</span></h3><div class="api" markdown="1">

`True` if this feature is a relation (area or non-area), otherwise `False`.

</div><h3 id="Feature_is_area" class="api"><span class="prefix">Feature.</span><span class="name">is_area</span></h3><div class="api" markdown="1">

`True` if this feature is a way or relation that represents an area, otherwise `False`.

</div><h3 id="Feature_nodes" class="api"><span class="prefix">Feature.</span><span class="name">nodes</span></h3><div class="api" markdown="1">

The nodes of a way, or an empty set if this feature is a node or relation.

</div><h3 id="Feature_members" class="api"><span class="prefix">Feature.</span><span class="name">members</span></h3><div class="api" markdown="1">

The members of a relation, or an empty set if this feature is a node or way. Features returned from this set (or a subset) have a `role` property with a value other than `None`.

</div><h3 id="Feature_parents" class="api"><span class="prefix">Feature.</span><span class="name">parents</span></h3><div class="api" markdown="1">

The relations that have this feature as a member, as well as the ways to which a node feature belongs (Use <code><i>node</i>.parents.relations</code> to obtain just the relations to which a node belongs).

</div><h3 id="Feature_role" class="api"><span class="prefix">Feature.</span><span class="name">role</span></h3><div class="api" markdown="1">

The role of this feature if it was returned via a member set (an empty string if this feature has no explicit role within its parent relation), or `None` for a `Feature` that was not returned via a member set.

</div>
## Geometric properties

<h3 id="Feature_bounds" class="api"><span class="prefix">Feature.</span><span class="name">bounds</span></h3><div class="api" markdown="1">

The bounding [`Box`](/python\Box#Box) of this feature.

</div><h3 id="Feature_x" class="api"><span class="prefix">Feature.</span><span class="name">x</span></h3><div class="api" markdown="1">

The x-coordinate of a node, or the horizontal midpoint of the `bounds` of a way or relation (GeoDesk Mercator projection)

</div><h3 id="Feature_y" class="api"><span class="prefix">Feature.</span><span class="name">y</span></h3><div class="api" markdown="1">

The y-coordinate of a node, or the vertical midpoint of the `bounds` of a way or relation (GeoDesk Mercator projection)

</div><h3 id="Feature_lon" class="api"><span class="prefix">Feature.</span><span class="name">lon</span></h3><div class="api" markdown="1">

`x` in degrees longitude (WGS-84)

</div><h3 id="Feature_lat" class="api"><span class="prefix">Feature.</span><span class="name">lat</span></h3><div class="api" markdown="1">

`y` in degrees latitude (WGS-84)

</div><h3 id="Feature_centroid" class="api"><span class="prefix">Feature.</span><span class="name">centroid</span></h3><div class="api" markdown="1">

The feature's calculated centroid ([`Coordinate`](/python\Coordinate#Coordinate))

</div><h3 id="Feature_shape" class="api"><span class="prefix">Feature.</span><span class="name">shape</span></h3><div class="api" markdown="1">

The Shapely [`Geometry`](/python\Geometry#Geometry) of this feature:

- `Point` for a node
- `LineString` or `Polygon` for a way
- `Polygon`, `GeometryCollection`, `MultiPoint`, `MultiLineString` or `MultiPolygon` for a relation

Coordinates are in Mercator projection.

</div><h3 id="Feature_area" class="api"><span class="prefix">Feature.</span><span class="name">area</span></h3><div class="api" markdown="1">

The calculated area (in square meters) if this feature is polygonal, otherwise `0`.

</div><h3 id="Feature_length" class="api"><span class="prefix">Feature.</span><span class="name">length</span></h3><div class="api" markdown="1">

The calculated length (in meters) if this feature is lineal, or its circumference if it is polygonal, otherwise `0`.

{% comment %}
TODO: GeometryCollection?
{% endcomment %}

</div>
## Formatting

To aid import into GIS applications, features can be converted into different representations. You can also visualize a feature on a map. See [Formats](formats) and [Maps](maps) to learn how output can be customized.

<h3 id="Feature_geojson" class="api"><span class="prefix">Feature.</span><span class="name">geojson</span></h3><div class="api" markdown="1">

The [GeoJSON](https://geojson.org/) representation of this feature ([`Formatter`](Formatter#geojson))

</div><h3 id="Feature_wkt" class="api"><span class="prefix">Feature.</span><span class="name">wkt</span></h3><div class="api" markdown="1">

The feature's geometry as [Well-Known Text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) ([`Formatter`](Formatter#wkt))

</div><h3 id="Feature_map" class="api"><span class="prefix">Feature.</span><span class="name">map</span></h3><div class="api" markdown="1">

A [`Map`](/python\Map#Map) displaying this feature.

You can [`add()`](/python\Map#Map_add) more features, [`save()`](/python\Map#Map_save) it or [`show()`](/python\Map#Map_show) it in a browser.

```python
# Mark a route on a map, highlight bike paths in green
route_map = route.map
route_map.add(route.members("w[highway=cycleway]", color="green")
route_map.show()
```

</div>
## Tag methods

<h3 id="Feature_str" class="api"><span class="prefix">Feature.</span><span class="name">str</span><span class="paren">(</span><i>key</i><span class="paren">)</span></h3><div class="api" markdown="1">

Returns the value of the given tag key as a string, or an empty string if this feature doesn't have the requested tag.

</div><h3 id="Feature_num" class="api"><span class="prefix">Feature.</span><span class="name">num</span><span class="paren">(</span><i>key</i><span class="paren">)</span></h3><div class="api" markdown="1">

Returns the value of the given tag as an `int` or `float`, or `0` if this feature doesn't have the requested tag.

{%comment%}

</div><h3 id="Feature_split" class="api"><span class="prefix">Feature.</span><span class="name">split</span><span class="paren">(</span><i>key</i><span class="paren">)</span><del>0.2</del></h3><div class="api" markdown="1">

If a tag contains multiple values separated by `;`, returns a tuple with the individual values. For a single value, returns a single-item tuple. Numbers are always converted to strings. If the tag does not exist, returns an empty tuple.

{%endcomment%}

<a id="Tags"></a>

</div>
## `Tags` objects

Iterating a `Tags` object yields key-value tuples:

```python
>>> for key, value in street.tags:
...     print (f'{key}={value}')
('highway', 'residential')
('name', 'Rue des Poulets')
('maxspeed', 30)
```


## Anonymous nodes

An **anonymous node** has no tags and does not belong to any relations --- it merely serves to define the geometry of a way. By default, feature libraries omit the IDs of such nodes to save space, in which case [`id`](/python\Feature#Feature_id) is `0`.

Anonymous nodes can only be obtained by [`nodes`](/python\Feature#Feature_nodes); they are not part of any other feature sets. The [`parents`](/python\Feature#Feature_parents) property of an anonymous node contains the ways to which this node belongs (always at least one).

Every anonymous node in a GOL has a unique location. If two or more nodes share the exact latitude and longitude, the untagged ones are tagged `geodesk:duplicate=yes` and retain their ID.
