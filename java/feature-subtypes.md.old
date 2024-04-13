---
layout: default
title:  Feature Subtypes
next:   utility-classes.md
parent: GeoDesk for Java
redirect_from: /feature-subtypes
nav_order: 6
---

<style>
table.types td
{
    vertical-align: middle;
}

table.types th
{
    text-align: left;
}

.center
{
    text-align: center;
}

</style>

# Feature Subtypes

When we talk about **types** of features, there are actually three distinct concepts:

- The **object type**: The GeoDesk API type (derived from [`Feature`]({{site.javadoc}}feature/Feature.html)) that corresponds to the three basic OSM datatypes --- [`Node`]({{site.javadoc}}feature/Node.html), [`Way`]({{site.javadoc}}feature/Way.html) and [`Relation`]({{site.javadoc}}feature/Relation.html)

- The **query type**: The letter code used in [GOQL](goql) queries, which also includes areas

- The **geometry type**: The six JTS [`Geometry`]({{site.javadoc_jts}}geom/Geometry.html) subtypes created by the [`toGeometry()`]({{site.javadoc}}feature/Feature.html#toGeometry())  method


Note that neither OSM nor the GeoDesk API have an "area" type --- an area is represented by a `Way` (for simple polygons without holes) or a `Relation` (which can define more complex polygonal geometries).

This chart illustrates the three type concepts:

<table class="types">
<tr>
<th>Object</th>
<th>Query</th>
<th>Geometry</th>
</tr>
<tr>
<td><code>Node</code></td>
<td class="center"><code>n</code></td>
<td><code>Point</code></td>
</tr>
<tr>
<td rowspan="2"><code>Way</code></td>
<td class="center"><code>w</code></td>
<td><code>LineString</code> or <code>LinearRing</code></td>
</tr>
<tr>
<td class="center" rowspan="2"><code>a</code></td>
<td><code>Polygon</code> <i>(without holes)</i></td>
</tr>
<tr>
<td rowspan="2"><code>Relation</code></td>
<td><code>Polygon</code> <i>(with or without holes)</i> or <code>MultiPolygon</code></td>
</tr>
<tr>
<td class="center"><code>r</code></td>
<td><code>GeometryCollection</code></td>
</tr>
</table>

In this chapter, we'll look at the characteristics and additional methods of the `Node`, `Way` and `Relation` subtypes.

## `Node` {#node}

A feature represented by a single coordinate pair. A [`Node`]({{site.javadoc}}feature/Node.html) can be stand-alone, or form part of a `Way`. If the latter, [`belongsToWay()`]({{site.javadoc}}feature/Node.html#belongsToWay()) returns `true`.

[`parentWays()`]({{site.javadoc}}feature/Node.html#parentWays()) returns all ways to which this node belongs (or an empty collection for a stand-alone node). An optional query string can be passed:

```java
node.parentWays("w[waterway=river,stream]")  // only returns rivers and streams 
```

Sometimes it is more convenient to inverse a query using [`with()`]({{site.javadoc}}feature/Features.html#with(com.geodesk.feature.Feature)): ~~0.2~~

```java
library.ways("w[waterway=river,stream]").with(node)  // same as above  
```


### Anonymous nodes {#anonymous-nodes}

An **anonymous node** has no tags and does not belong to any relations --- it merely serves to define the geometry of a `Way`. By default, feature libraries omit the IDs of such nodes to save space, in which case [`id()`]({{site.javadoc}}feature/Feature.html#id()) returns `0`. 

## `Way` <a id=way></a> {#way}

A linear or simple polygonal geometry, represented by two or more nodes. Linear rings and polygons have a minimum of four nodes (their first and last node are the same). 

[`nodes()`]({{site.javadoc}}feature/Way.html#nodes()) returns an ordered collection of a way's nodes. An optional query string can be passed:

```java
way.nodes("[traffic_calming]")  // only speed bumps etc.
```

Sometimes it is more convenient to inverse a query using [`of()`]({{site.javadoc}}feature/Features.html#of(com.geodesk.feature.Feature)): ~~0.2~~

```java
library.nodes("[traffic_calming]").of(way)  // same as above  
```

A `Way` is iterable:

```java
for(Node node: way) ...
```

- Iteration only retrieves nodes that have tags or are part of a relation; to query *all* nodes, use `nodes()`.

[`toXY()`]({{site.javadoc}}feature/Way.html#toXY()) returns an `int` array with the way's coordinates (X coordinates are stored at even index positions, Y at odd), which is the most space-efficient representation of the Way's geometry.



## `Relation` {#relation}

A `Relation` is used to tie together multiple features to build a larger singular feature (such as a [long river](https://wiki.openstreetmap.org/wiki/Relation:waterway) or a [complex polygon](https://wiki.openstreetmap.org/wiki/Relation:multipolygon)) or to create a new conceptual feature, such as a [bus route](https://wiki.openstreetmap.org/wiki/Relation:route) or [turn restriction](https://wiki.openstreetmap.org/wiki/Relation:restriction).

[`members()`]({{site.javadoc}}feature/Relation.html#members()) returns an ordered collection of a relation's members. There are several related methods that filter members based on their object type, also with an optional query argument:

```java
rel.members()                   // all members
rel.memberNodes()               // only nodes
rel.memberWays("[highway]")     // only roads, paths, etc. 
rel.memberRelations()           // only members that themselves are relations
rel.members("a")                // only areas
rel.members("a[leisure=park]")  // only park areas
```

Note that there is no "memberAreas" method, since areas can be `Way` or `Relation` objects. If you want only polygonal ways or area relations, use `memberWays("a")` / `memberRelations("a")`.

Member queries can also be phrased using [`of()`]({{site.javadoc}}feature/Features.html#of(com.geodesk.feature.Feature)): ~~0.2~~

```java
library.ways().of(rel)  // ways that are members of the given relation   
```


To restrict members to specific roles, use `role` in the query as if it were a tag: ~~0.2~~

```java
rel.memberWays("w[waterway=canal][role='*_stream']")  
    // canals whose role ends with "_stream" ("main_stream", "side_stream") 
```

[`first()`]({{site.javadoc}}feature/Features.html#first()) is useful if you expect at most one member with a given role:

```java
Node capital = rel.memberNodes("[role=admin_centre]").first();
```

A `Relation` is iterable:

```java
for(Feature member: rel) ...
// is equivalent to
for(Feature member: rel.members()) ...
```

- A feature may appear among a relation's members more than once (for example, a bus route may pass a road segment multiple times). Usually, each occurrence will have a different role (e.g. `forward` and `backward`), but there is no rule requiring this.

[`toGeometry()`]({{site.javadoc}}feature/Feature.html#toGeometry()) creates a [`Polygon`]({{site.javadoc_jts}}geom/Polygon.html) or [`MultiPolygon`]({{site.javadoc_jts}}geom/MultiPolygon.html) for area relations, and a [`GeometryCollection`]({{site.javadoc_jts}}geom/GeometryCollection.html) (comprised of the geometries of its members) for all others.


The bounding box of a `Relation` is the union of the bounding boxes of its members.





<a name="member-queries">


