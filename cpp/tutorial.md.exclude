---
layout: default
title: Tutorial
parent: GeoDesk for C++
nav_order: 1
---
# Five-Minute Tutorial

<div class="box note" markdown="1">

This tutorial assumes that you are already familiar with OpenStreetMap and its data model. If not, read our [Introduction to OSM](/intro-to-osm) or visit [the official OSM website](https://wiki.openstreetmap.org/wiki/Develop).

</div>

## Create a Feature Library

- [Download and install](https://www.geodesk.com/download) the GOL command-line utility

- Download some OSM data (in PBF format). We suggest starting with a subset for a single
  country (or smaller part). For example, Germany (file size: 3.5 GB) can be downloaded from
  [GeoFabrik](https://download.geofabrik.de/europe/germany.html) or
  [BBBike](https://download.bbbike.org/osm/planet/sub-planet-daily/). 
 
- Turn the PBF file into a Geographic Object Library:   

  ```
  gol build germany germany-latest.osm.pbf
  ```

  On a multi-core workstation with at least 24 GB of RAM, this should take a few minutes;
  on an 8-GB dual-core laptop, expect 20 minutes or more. The output will look like this:

  ```
  Building germany.gol from germany-latest.osm.pbf using default settings...
  Analyzed germany-latest.osm.pbf in 20s 
  Sorted 86,432,126 features in 1m 13s
  Validated 1023 tiles in 36s
  Compiled 1023 tiles in 1m 24s
  Linked 1023 tiles in 8s
  Build completed in 3m 43s  
  ```
  
## Use Feature Libraries in Java  

Add this **Maven dependency** to your project:

{% include maven.md %}

Import the **GeoDesk packages**:

```java
import com.geodesk.feature.*;
import com.geodesk.geom.*;
```
  
**Open** the library:

```java
FeatureLibrary germany = new FeatureLibrary("germany.gol");   
```

Create a **query**:

```java
Features lighthouses = germany.select("na[man_made=lighthouse][name][height]");   
```
  
This returns a collection of `Feature` objects representing lighthouses that
have names and whose height has been recorded (`na` indicates that we want 
features that are mapped as **n**odes or **a**reas --- see [Geo-Object Query Language](../goql.md)).

Iterate through the features:

```java
for(Feature f: lighthouses)
{
    System.out.format("%s is %f meters tall.\n", 
        f.stringValue("name"), f.doubleValue("height"));      
}   
```
  
Typically we want only a specific subset of the collection. The
most common case is a **bounding-box query**:

```java
Box bbox = Box.ofWSEN(8.42, 53.75, 9.07, 53.98);
    // longitude/latitude West, South, East, North
for(Feature f: lighthouses.in(bbox)) ...
```
{% comment %}
- Instead of a `Box`, `in()` also takes a `Geometry`, `PreparedGeometry` or `Feature`.
{% endcomment %}

Other **filters** include:

- Filter by **type**: `.nodes()`, `.ways()`, `.relations()`
 
- **Spatial predicates**: `.containing(...)`, `intersecting(...)`, `crossing(...)`

Filters can be combined:

```java
roads.ways("[bridge]").in(bbox).crossing(rhineRiver)
```


## Work with individual features

Retrieve a feature's **tags**:

```java
Tags tags = feature.tags();
Map<String,Object> tagMap = feature.tags().toMap();
```

Get a specific **tag value** by key:

```java
feature.stringValue("opening_hours") // returns empty string if tag not present
feature.intValue("maxspeed")         // 0 if tag not present or non-numeric
```

Get its **type** and **ID**:

```java
FeatureType type = feature.type();   // NODE, WAY or RELATION
long osmId = feature.id();     
```

Its **location**:

```java
feature.lon()  // degrees longitude
feature.lat()  // degrees latitude
feature.x()    // Mercator-projected X-coordinate
feature.y()    // Mercator-projected Y-coordinate
```

Its **length** (meters) or **area** (square meters):

```java
feature.length()  // 0 if not linear
feature.area()    // 0 if not an area
```


Its JTS **geometry**:

```java
feature.toGeometry()  // Point for a Node
                      // LineString or LinearRing for a non-area Way
                      // Polygon for a Way that represents an area
                      // Polygon or MultiPolygon for an area Relation
                      // GeometryCollection for all other Relations
```

<!--
This creates:

<table>
<tr>
<td markdown="1">
`Point` 
</td>
<td markdown="1">
for a `Node`
</td>
</tr>
<tr>
<td markdown="1">
`LineString` or `LinearRing`  
</td>
<td markdown="1">
for a non-area `Way`
</td>
</tr>
<tr>
<td markdown="1">
`Polygon`  
</td>
<td markdown="1">
for a `Way` that represents an area
</td>
</tr>
<tr>
<td markdown="1">
`Polygon` or `MultiPolygon`   
</td>
<td markdown="1">
for an area `Relation`
</td>
</tr>
<tr>
<td markdown="1">
`GeometryCollection`   
</td>
<td markdown="1">
for any other kind of `Relation`
</td>
</tr>
</table>
-->

## Ways

Retrieve the **nodes** that make up a way:

```java
way.nodes()             // all nodes    
way.nodes("[barrier]")  // only barriers
```

Or simply iterate the way:

```java
for(var node: way) ... 
```

(Iteration only retrieves nodes that have tags or are part of a relation;
 `nodes()` returns *all* nodes).

Retrieve the ways to which a node belongs:

```java
node.parents().ways()
node.parents("w[highway]")
```


## Relations

Retrieve a relation's **members**:

```java
for(Feature member: rel.members())
```

Or simply iterate:

```java
for(Feature member: rel) ...
```

Discover a member's **role**:

```java
member.role()   // "stop", "main_stream", etc.
```

Get the relations to which a feature belongs:

```java
feature.parents().relations()    
feature.parents("r[route]")
```



## Wrapping up

GeoDesk enables you to:

- Create compact spatial databases ("Feature libraries") based on OpenStreetMap data
- Select features using a powerful [query language](../goql.md) and access their properties
  ("tags") and geometries
- Traverse the relationships between nodes, ways and relations 
- Leverage the [Java Topology Suite](https://github.com/locationtech/jts) for advanced geometric operations

<div class="box note" markdown="1">

# Learn more

- [Full documentation](libraries)
- [GOL utility](/gol) --- customize and maintain feature libraries 
- JavaDocs
- Example code

</div>

