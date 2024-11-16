---
layout: default
title:  Features
next:   queries.md
parent: GeoDesk for C++
nav_order: 3
---

# Features

<img class="float" src="/img/basic-features.png" width=320>

A `Feature` represents a geographic element. This can be a point of interest like a mailbox or a restaurant, a park, a lake, a segment of a road, or a more abstract concept like a bus route.

`Feature` has three subtypes that match the types used by OpenStreetMap:

- `Node` -- a simple point feature

- `Way` -- an ordered sequence of nodes, used to represent line strings and
  simple polygons

- `Relation` -- an object composed of multiple features, such as a polygon with holes, a route or a river system. A relation may contain nodes, ways or other relations as members. 
 
Each feature has a **geometry** (`Point`, `LineString`, `Polygon` or a collection type), as well as one or more **tags** (key-value pairs) that describe its details.

`Feature` objects are obtained via [queries](queries). They are lightweight and immutable, suitable for passing by value.

```cpp
void checkMuseums(Feature city)
{
    for (Feature museum : museums.within(city))
    {
        FeatureType type = museum.type();
        int64_t id = museum.id();
        std::string name = museum["name"];
        ...
```


## Type, identity and equality

### type &nbsp;•&nbsp; typeName

`type()` returns a `FeatureType` enum (`NODE`, `WAY` or `RELATION`). 

`typeName()` returns a `const char*` (`"node"`, `"way"` or `"relation"`).

### isNode &nbsp;•&nbsp; isWay &nbsp;•&nbsp; isRelation  

To check if a `Feature` has a certain type, use `isNode()`, `isWay()` or `isRelation()`. 

- You can implicitly cast `Feature` to its sub-type; however, a `std::runtime_error` will be thrown in case of a type mismatch. An attempt to assign a `Node`, `Way` or `Relation` to the wrong type will result in a compile-time error. 

    ```cpp
    if(feature.isNode())
    {
        Node node = feature;      // <-- This is fine
        Way noWay = node;         // <-- This line won't compile     
    }
    else
    {
        // feature is not a Node
        Node willFail = feature;  // <-- throws a runtime_error
    }
    ```

### id

`id()` returns the numeric **OSM identifier**. IDs are unique only within the feature type (which means a node and a way may have the same ID).

{%comment%}
- You can obtain a unique identifier that incorporates the type by using the [`FeatureId`]({{site.javadoc}}feature/FeatureId.html) utility class.
{%endcomment%} 

- `id()` may return `0` for [anonymous nodes](features#anonymous-nodes).

### role

`role()` returns the **role** of the feature within a relation, if it was retrieved via a [member query](#members-of-a-relation). This method returns an empty `StringValue` for features obtained via any other query.

### Equality (`==`)

Two features are equal if they have the same type and ID. 

- If two `Feature` objects are returned from different member queries, with different roles, they are considered equal as long as the above holds true.

- Anonymous nodes are equal if they have the same location.


### Anonymous nodes {#anonymous-nodes}

An **anonymous node** has no tags and does not belong to any relations --- it merely serves to define the geometry of a `Way`. By default, feature libraries omit the IDs of such nodes to save space, in which case [`id()`]({{site.javadoc}}feature/Feature.html#id()) returns `0`. 

## Tags

**Tags** are key-value properties of a feature. Tags are have a `TagValue`, which can be implicitly turned into a `std::string`, `std::string_view`, `double`, `int` or `bool`.

Get a tag value by key:

```cpp
TagValue value = feature["opening_hours"]; 
std::string strValue = value;
int maxSpeed = feature["maxspeed"];         
```

- If a tag is not present, the resulting `TagValue` is an empty string.

- TODO: conversions 

Check for presence of a tag:

```cpp
if(feature.hasTag("highway")) ...
if(feature.hasTag("shop", "bakery")) ...
```

Get all tags:

```cpp
Tags tags = feature.tags();
for(Tag tag: tags)
{
    std::cout << tag.key() << " = " << tag.value();
}
```

`Tags` can be turned into other data structures:

```cpp
// A map of key strings (sorted alphabetically) to value strings  
std::map<std::string,std::string> keyValueMap = feature.tags();

// A vector of Tag objects (in storage order)
std::vector<Tag> tagVector = feature.tags();
```


## Location and geometry

### bounds

`bounds()` returns a feature's bounding box (a `Box`). This is the smallest axis-aligned rectangle that encloses the feature's geometry.

### lon &nbsp;•&nbsp; lat  

`lon()` and `lat()` return the longitude and latitude of this feature (WGS-84 degrees)

### x &nbsp;•&nbsp; y &nbsp;•&nbsp; xy

`x()` and `y()` return its [Mercator-projected](/core-concepts#coordinate-system) coordinates (as `int32_t`).  For ways and relations, this is the center point of the feature's bounding box (*not* the feature's [centroid](#centroid)).

`xy()` returns both as a `Coordinate`.

### centroid

`centroid()` calculates the feature's centroid (a `Coordinate`). 

### toGeometry

`toGeometry(GEOSContextHandle_t)` creates a `GEOSGeometry` for this feature:

- `Point` for a Node
- `LineString` or `LinearRing` for a non-area Way
- `Polygon` for a Way that represents an area
- `Polygon` or `MultiPolygon` for an area `Relation`
- `GeometryCollection` for any other `Relation`

<blockquote class="note" markdown="1">

In order to use this method, you will need to enable option `GEODESK_WITH_GEOS` in your CMake project:

```cmake
set(GEODESK_WITH_GEOS ON)
set(GEOS_INCLUDE_PATHS 
    "${geos_SOURCE_DIR}/include" 
    "${geos_BINARY_DIR}/capi")
```
</blockquote>

Example:

```cpp
GEOSContextHandle_t geosContext = initGEOS_r(nullptr, nullptr);
GEOSGeometry* geom = feature.toGeometry(geosContext);
std::cout << "GEOS geometry created successfully." << std::endl;
GEOSGeom_destroy_r(geosContext, geom);
finishGEOS_r(geosContext);
```

### isArea

`isArea()` returns `true` if the feature represents an area (always `false` for `Node`). 

<a id="area"/>
<a id="length"/>

### area &nbsp;•&nbsp; length

`area()` measures the area of the feature (square meters as `double`). 

`length()` measures the length of the feature (meters as `double`). 

## Related features

Use `nodes()`, `members()` and `parents()` to retrieve related features.  

### Nodes of a way

`nodes()` returns an ordered collection of a way's nodes. An optional query string can be passed:

```cpp
return way.nodes("[traffic_calming]")  // only speed bumps etc.
```

You can also invert the query by calling `nodesOf()` on a set of features. This is especially useful if the filter condition is complex, as it makes your code easier to read, and may improve performance in tight loops.

```cpp
// Obtain a set of all crosswalks
Nodes crosswalks = world("n[highway=crossing]");
// Return the crosswalks of the given street  
return crosswalks.nodesOf(street);
```

### Members of a relation

`members()` returns an ordered collection of a relation's members. An optional query string can be passed:

```cpp
route.members("w[highway=primary]") 
    // only members that are primary roads 
```

Member queries can be inverted, as well. The following is equivalent to the above example:

```cpp
Features primaryRoads = world("w[highway=primary]");
return primaryRoads.membersOf(route);
```

### Parents

`parents()` returns the relations to which this feature belongs (or an empty collection if it is not part of any relation), as well as the ways (if any) to which a node belongs. An optional query string can be passed:

```cpp
Relations busRoutes = street.parents("r[route=bus]");  
    // Bus routes which traverse this street 
```

This query can also be inverted using `Features.parentsOf()`:

```cpp
world("r[route=bus]").parentsOf(street)  // same as above  
```

### belongsTo &nbsp;•&nbsp; belongsToRelation

`belongsTo(Feature parent)` checks whether this `Feature` is part of a specific relation, or whether a `Node` belongs to a given `Way`. If `parent` is a `Node`, the result is always `false`.

`belongsToRelation()` checks whether a `Feature` is a member of *any* `Relation`.




