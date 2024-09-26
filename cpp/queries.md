---
layout: default
title:  Queries & Collections
next:   utility-classes.md
parent: GeoDesk for C++
nav_order: 4
---
# Queries and Feature Collections

Geospatial applications typically work with subsets of features in a library, such as buildings in a town, or waterways in a particular region. These subsets are represented as **feature collections**, which are the result of **queries**.

- Feature collections are lightweight objects that merely described what should be returned; they don't actually contain any objects and take up minimal space. In other words, query execution is lazy: Features are fetched only once they are needed, in response to iteration or a call to `count()`.

- Feature collections can be **ordered** or **unordered**. Only the [nodes of a way](features#nodes-of-a-way) and the [members of a relation](features#members-of-a-relation) are ordered; all other query results are returned in arbitrary order.

**TODO**

Feature collections behave like Java `Collection` classes, and hence implement `size()`, `isEmpty()`, `contains()` and `toArray()`, as well as the ability to iterate. `Features` also offers these methods:  

- [`toList()`]({{site.javadoc}}feature/Features.html#toList()) creates an `ArrayList` containing all features in the collection.

- [`first()`]({{site.javadoc}}feature/Features.html#toList()) returns the first feature in the collection, or `null` if it is empty.

## Bounding-box queries

<img class="float" src="/img/bboxes.png" width=360>

A **bounding box** (or **bbox**) describes an axis-aligned rectangle. Bounding-box queries are the most common type of spatial queries.

This type of query returns all features whose bounding box intersects with the bounding box of the query. Note that the result set may include features whose geometry itself does not fall inside the query bbox. Bounding-box queries are designed as a fast primary filter, intended to narrow down candidates from millions to a few hundred. To eliminate the false positives, you can then apply a second, stricter (but more computationally expensive) filter.   

- A bounding box may straddle the Antimeridian (+/- 180 degrees longitude). Features that cross the Antimeridian are returned as multiple `Feature` objects representing separate parts to the east and to the west.

A bounding box is represented by the `Box` class, which offers multiple static factory methods. To create a `Box` from coordinates (longitude and latitude), use `ofWSEN()`:

```cpp
Box bbox = Box::ofWSEN(8.42, 53.75, 9.07, 53.98);   // West, South, East, North
```

To obtain the features in a given bbox: 

```cpp
Box bbox = ... 
Features subset = features(bbox);   
```

Instead of explicitly creating a bounding box, you can also use the `bounds()` method of a `Feature`:

```cpp
// All features that may be within 100 meters of the river
return features(river.bounds().bufferMeters(100));   
```

**Note**: If you need to determine which features *definitely* lie within 100 meters, use [`maxMetersFrom()`](#maxmetersfrom).

## Filtering by type and tags

Features in a collection can be filtered by type:

```cpp
Nodes nodes()
Ways ways()
Relations relations()   
```

If you assign a collection to a subtype of `Features`, thye are automatically filtered:

```cpp
Features world = ...
Nodes onlyNodes = world;   // same as world.nodes()
```

You can also specify a query string:

```cpp
nodes("[emergency=fire_hydrant]") // nodes that represent fire hydrants
relations("[route=bicycle]")      // cycling routes  
```

(See [Query Language](/goql) for details)

- Some queries always produce an empty collection. For example, `nodes("a")` is always
  empty: areas can be of type `Way` or `Relation`, but never `Node`.


## Retrieving features

To process all features in a set, simple iterate:

```cpp
for(Feature street : streets) ...
```

To obtain a `std::vector`:

```cpp
std::vector<Feature> list = streets;
```

Or populate an existing `std::vector`:

```cpp
streets.addTo(myVector);
```
To obtain the **first** feature in a set:

```cpp
std::optional<Feature> city = france("n[place=city][name=Paris]").first();
```

Note that only the nodes of ways and members of relations are ordered collections;
all others are unordered sets, which means you'll receive a random feature if there
are more than one. If the collection is empty, `first()` returns `nullopt`.

## Spatial filters

Features can be filtered by their spatial relationship to other geometric objects (typically a `GEOSGeometry` or another `Feature`). 

### containing

Selects features whose geometry **contains** *A*:

- Every point of *A* is a point of the candidate feature, and the interiors of the two geometries have at least one point in common.

```cpp
Features containing(Feature);
Features containing(GEOSGeometry);
Features containingXY(int, int);
Features containingLonLat(double, double);
```

For example:

```cpp
// In which park (if any) is this statue of Claude Monet?
return features("a[leisure=park]")
    .containing(statueOfMonet).first();

// The county, state and country for this point -- should return 
// San Diego County, California, USA (in no particular order)  
return features("a[boundary=administrative][admin_level <= 6]")
    .containingLonLat(-117.25, lat=32.99); 
```

### coveredBy 

Selects features whose geometry is **covered by** *A*:

- No point of the candidate feature's geometry lies outside of *A*.

```cpp
Features coveredBy(Feature);
Features coveredBy(GEOSGeometry);
```

### crossing

Selects features whose geometry **crosses** *A*:

- The geometries of *A* and the candidate feature have some (but not all) interior points in common
- The dimension of the intersection must be less than the maximum dimension of the candidate and *A*.

```cpp
Features crossing(Feature);
Features crossing(GEOSGeometry);
```

For example:

```cpp
// All railway bridges across the Mississippi River
Features railwayBridges = features("w[railway][bridge]");    
return railwayBridges.crossing(mississippi);
```

{%comment%}
### disjointFrom 

Selects features whose geometry is **disjoint** from *A*:

- The geometries of the candidate feature and *A* have no common points at all.

```cpp
Features disjointFrom(Feature)
Features disjointFrom(Geometry)
Features disjointFrom(PreparedGeometry)
```

{%endcomment%}


### intersecting

Selects features whose geometry **intersects** *A*:

- The geometries of *A* and the candidate feature have at least one point in common.

```cpp
Features intersecting(Feature);
Features intersecting(GEOSGeometry);
```

{% comment %}

(Move these to section "Geometric filters|)

### <code>minArea(<i>m</i>)</code> ~~0.2~~

Selects features whose area is at least *m* square meters.

- Because of projection-dependent distortion, this test may not be accurate for large features, 
  especially those far from the Equator that extend north-south. 

### <code>maxArea(<i>m</i>)</code> ~~0.2~~

Selects features whose area is no more than *m* square meters.

- Because of projection-dependent distortion, this test may not be accurate for large features,
  especially those far from the Equator that extend north-south.

{% endcomment %}

### maxMetersFrom

Selects features whose distance to *A* is less or equal to *m* meters (measured between the closest points of the candidate feature and *A*).

```cpp
Features maxMetersFrom(double, Feature);
Features maxMetersFrom(double, GEOSGeometry);
Features maxMetersFromXY(double, int, int);
Features maxMetersFromLonLat(double, double, double);
```

For example:

```cpp
// All bus stops within 500 meters of the given restaurant
Features nearbyBusStops = features("n[highway=bus_stop]")
    .maxMetersFrom(500, restaurant);
 
// All features within 3 km of the given point 
return features.maxMetersFromLonLat(3000, 76.41, 40.12); 
```
{%comment%}
### overlapping

Selects features whose geometry **overlaps** *A*:

- The geometries of *A* and the candidate feature have the same dimension.
 
- *A* and candidate feature each have at least one point not shared by the other.
 
- The intersection of their interiors has the same dimension.

```java
Features overlapping(Feature)
Features overlapping(Geometry)
Features overlapping(PreparedGeometry)
```

### touching

Selects features that **touch** *A*:

- The geometries of *A* and the candidate feature have at least one point in common, but their interiors do not intersect.

```java
Features touching(Feature);
Features touching(Geometry);
Features touching(PreparedGeometry);
```

For example:

```java
Features counties = features.select(
    "a[boundary=administrative][admin_level=6]");
for (Feature county: counties)
{
    System.out.printf("%s has %d neighbors\n",
        county.stringValue("name"), 
        counties.touching(county).count());
}
```

{%endcomment%}

### within

Selects features that lie entirely **within** *A*:

- Every point of the candidate feature is a point in *A*, and their interiors have at least one point in common.

```cpp
Features within(Feature);
Features within(GEOSGeometry);
```


## Topological filters

These methods return a subset of those features that have a specific topological relationship with another `Feature`.

### connectedTo

Selects all features that have at least one node (vertex) in common with the given `Feature` or `Geometry`.

```cpp
Features connectedTo(Feature);
Features connectedTo(GEOSGeometry);
```

### nodesOf

The nodes of the given way. Returns an empty set if the feature is a `Node` or `Relation`.

```cpp
Nodes nodesOf(Feature);
```

### membersOf

Features that are members of the given relation, or nodes of the given way. Returns an empty set if the feature is a `Node`.

```cpp
Features membersOf(Feature);
```

### parentsOf

Relations that have the given feature as a member, as well as ways to which the given node belongs.

```cpp
Features parentsOf(Feature);
```


