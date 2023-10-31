---
layout: default
title:  Features
next:   feature-subtypes.md
parent: GeoDesk for Java
redirect_from: /features
nav_order: 5
---

# Accessing Individual Features

A [`Feature`]({{site.javadoc}}feature/Feature.html) represents a geographic element. This can be a point of interest like a mailbox or a restaurant, a park, a lake, a segment of a road, or a more abstract concept like a bus route.

`Feature` is the supertype of [`Node`]({{site.javadoc}}feature/Node.html), [`Way`]({{site.javadoc}}feature/Way.html) and [`Relation`]({{site.javadoc}}feature/Relation.html). An object returned by a query is always one of these three subtypes. We'll discuss their additional methods and characteristics [in the next chapter](feature-subtypes).

For now, let's focus on what you can do with features of any type.

## Type, identity and equality

[`type()`]({{site.javadoc}}feature/Feature.html#type()) returns a [`FeatureType`]({{site.javadoc}}feature/FeatureType.html) enum (`NODE`, `WAY` or `RELATION`).

[`id()`]({{site.javadoc}}feature/Feature.html#id()) returns the **OSM identifier** (a `long`). IDs are unique only within the feature type (which means a node and a way may have the same ID).

- You can obtain a unique identifier that incorporates the type by using the [`FeatureId`]({{site.javadoc}}feature/FeatureId.html) utility class.

- `id()` may return `0` for [anonymous nodes](feature-subtypes#anonymous-nodes).

[`role()`]({{site.javadoc}}feature/Feature.html#role()) returns the **role** of the feature within a relation, if it was returned by a [member query](feature-subtypes#member-queries). This method returns `null` for features obtained via any other query (an empty string means the feature is a relation member, but has no assigned role in that particular relation).

`equals()`: Two features are equal if they have the same type and ID. 

- If two `Feature` objects are returned from different member queries, with different roles, they are considered equal as long as the above holds true.

- Anonymous nodes are equal if they have the same location.

- Never rely on `==` for equality. Queries *may* return identical objects for the same
  feature, but are by no means guaranteed to do so (even for the same node in a closed way). 

## Tags

**Tags** are key-value properties of a feature. Tags are stored as strings, but there are convenience methods to turn strings into numeric values.

Get a tag value by key:

```java
feature.stringValue("opening_hours") 
feature.intValue("maxspeed")         
```

- If a tag is not present, [`stringValue()`]({{site.javadoc}}feature/Feature.html#stringValue(java.lang.String)) returns an empty string.

- If a tag is not present, or its value is not a valid number, [`intValue()`]({{site.javadoc}}feature/Feature.html#intValue(java.lang.String)) and [`doubleValue()`]({{site.javadoc}}feature/Feature.html#doubleValue(java.lang.String)) return `0`.

Check for presence of a tag:

```java
if(feature.hasTag("highway")) ...
if(feature.hasTag("shop", "bakery")) ...
```

Get all tags:

```java
Tags tags = feature.tags();
```

[`Tags`]({{site.javadoc}}feature/Tags.html) is a `Consumable`, a special kind of iterator that works like an SQL `ResultSet`:

```java
while(tags.next())
{
    String key = tags.key();
    String value = tags.stringValue();
    int intValue = tags.intValue();
    ...
}
```

`Tags` can be turned into other data structures:

```java
Map<String,Object> tagMap = tags.toMap();
```


## Location and geometry

[`bounds()`]({{site.javadoc}}feature/Feature.html#bounds()) returns a feature's [bounding box]({{site.javadoc}}core/Box.html). This is the smallest axis-aligned rectangle that encloses the feature's geometry.

[`lon()`]({{site.javadoc}}feature/Feature.html#lon()) and [`lat()`]({{site.javadoc}}feature/Feature.html#lat()) return the longitude and latitude of a `Feature`; [`x()`]({{site.javadoc}}feature/Feature.html#x()) and [`y()`]({{site.javadoc}}feature/Feature.html#y()) return its Mercator-projected coordinates.

- For ways and relations, this is the center point of the feature's bounding box (*not* the feature's centroid).

[`toGeometry()`]({{site.javadoc}}feature/Feature.html#toGeometry()) creates a JTS [`Geometry`]({{site.javadoc_jts}}geom/Geometry.html) for this feature:

- [`Point`]({{site.javadoc_jts}}geom/Point.html) for a `Node`
- [`LineString`]({{site.javadoc_jts}}geom/LineString.html) or [`LinearRing`]({{site.javadoc_jts}}geom/LinearRing.html) for a non-area `Way`
- [`Polygon`]({{site.javadoc_jts}}geom/Polygon.html) for a `Way` that represents an area
- [`Polygon`]({{site.javadoc_jts}}geom/Polygon.html) or [`MultiPolygon`]({{site.javadoc_jts}}geom/MultiPolygon.html) for an area `Relation`
- [`GeometryCollection`]({{site.javadoc_jts}}geom/GeometryCollection.html) for any other `Relation`

Use [`isArea()`]({{site.javadoc}}feature/Feature.html#isArea()) to check if the feature represents an area (always `false` for `Node`). 

## Parent relations

Any feature may belong to one or more relations.

[`parentRelations()`]({{site.javadoc}}feature/Feature.html#parentRelations()) returns the relations to which this feature belongs (or an empty collection if it is not part of any relations). An optional query string can be passed:

```java
feature.parentRelations("r[route=bicycle]")  // only returns cycling routes 
```

Sometimes it is more convenient to inverse a query using [`with()`]({{site.javadoc}}feature/Features.html#with(com.geodesk.feature.Feature)): ~~0.2~~

```java
library.relations("r[route=bicycle]").with(feature)  // same as above  
```


[`belongsTo(Feature parent)`]({{site.javadoc}}feature/Feature.html#belongsTo(com.geodesk.feature.Feature)) checks whether this feature belongs to a specific relation (the argument itself is of type `Feature` instead of `Relation`, because this method can also test if a `Node` is part of a `Way`; if `parent` is a `Node`, the result is always `false`).

[`belongsToRelation()`]({{site.javadoc}}feature/Feature.html#belongsToRelation()) checks whether a `Feature` is a member of *any* relation (without the need for querying).

## Placeholder features

A **placeholder feature** is a feature that is not present in a dataset, but is referenced from other features in the same dataset. This commonly happens with regional abstracts: A dataset that covers only Germany may include a relation for a [train route to Paris](https://www.openstreetmap.org/relation/6124730) that goes through Cologne; however, the dataset most likely won't include the train stops in Belgium and France (which are members of that relation). In order to maintain referential integrity, [`gol build`](gol/build) creates placeholders for these missing features.

- [`isPlaceholder()`]({{site.javadoc}}feature/Feature.html#isPlaceholder()) returns `true`.

- [`type()`]({{site.javadoc}}feature/Feature.html#type()) and [`id()`]({{site.javadoc}}feature/Feature.html#id()) are valid.

- [`isArea()`]({{site.javadoc}}feature/Feature.html#isArea()) always returns `false`, even if the feature might actually be an area.

- A placeholder has none of the feature's actual tags, but it may contain synthetic tags such as `geodesk:error=missing` that describe the problem further.

- A placeholder `Way` has no nodes; a placeholder `Relation` has no members.

- [`parentRelations()`]({{site.javadoc}}feature/Feature.html#parentRelations()) returns only relations that are contained in the library.  

- [`toGeometry()`]({{site.javadoc}}feature/Feature.html#toGeometry()) creates an empty `Geometry`.

- All other geometry-related methods return an X-coordinates of `Integer.MIN_VALUE` to indicate that the feature's location is invalid/unknown.
 
- Its length and area are `0`.




