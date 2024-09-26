---
layout: default
title:  Queries & Collections
next:   utility-classes.md
parent: GeoDesk for Java
redirect_from: /queries
nav_order: 4
---
# Queries and Feature Collections

Geospatial applications typically work with subsets of features in a library, such as buildings in a town, or waterways in a particular region. These subsets are represented as **feature collections**, which are the result of **queries**.

All feature collections implement the [`Features`]({{site.javadoc}}feature/Features.html) interface, which provides methods to iterate the member features or constrain them further.

- [`FeatureLibrary`]({{site.javadoc}}feature/FeatureLibrary.html) itself is a feature collection, representing all features in the library.

- Feature collections are lightweight objects that merely described what should be returned; they don't actually contain any objects and take up minimal space. In other words, query execution is lazy: Features are fetched only once they are needed, in response to iteration or a call to `toList()`.

  You can assign queries to variables and pass them around, but be aware that once the 
  [underlying library has been closed](libraries#caution-closed), you **must not** call any of their methods (or iterate 
  over them).

- Feature collections can be **ordered** or **unordered**. Only the [nodes of a way](features#nodes-of-a-way) and the [members of a relation](features#members-of-a-relation) are ordered; all other query results are returned in arbitrary order.

Feature collections behave like Java `Collection` classes, and hence implement `size()`, `isEmpty()`, `contains()` and `toArray()`, as well as the ability to iterate. `Features` also offers these methods:  

- [`toList()`]({{site.javadoc}}feature/Features.html#toList()) creates an `ArrayList` containing all features in the collection.

- [`first()`]({{site.javadoc}}feature/Features.html#toList()) returns the first feature in the collection, or `null` if it is empty.

## Bounding-box queries

<img class="float" src="/img/bboxes.png" width=360>

A **bounding box** (or **bbox**) describes an axis-aligned rectangle. Bounding-box queries are the most common type of spatial queries.

This type of query returns all features whose bounding box intersects with the bounding box of the query. Note that the result set may include features whose geometry itself does not fall inside the query bbox. Bounding-box queries are designed as a fast primary filter, intended to narrow down candidates from millions to a few hundred. To eliminate the false positives, you can then apply a second, stricter (but more computationally expensive) filter.   

- A bounding box may straddle the Antimeridian (+/- 180 degrees longitude). Features that
  cross the Antimeridian are returned as multiple `Feature` objects representing separate parts to the east and to the west.

A bounding box is represented by the [`Box`]({{site.javadoc}}core/Box.html) class, which offers multiple static factory methods. To create a `Box` from coordinates (longitude and latitude), use [`ofWSEN()`]({{site.javadoc}}core/Box.html#ofWSEN(double,double,double,double)):

```java
Box bbox = Box.ofWSEN(8.42, 53.75, 9.07, 53.98);   // West, South, East, North
```

To obtain the features in a given bbox, use [`in()`]({{site.javadoc}}feature/Features.html#in(com.geodesk.core.Bounds)): 

```java
Features subset = features.in(bbox);   
```

Instead of explicitly creating a bounding box, you can also use the [`bounds()`]({{site.javadoc}}feature/Feature.html#bounds()) method of a `Feature`:

```java
// All features that may be within 100 meters of the river
return features.in(river.bounds().bufferMeters(100));   
```

**Note**: If you need to determine which features *definitely* lie within 100 meters, use [`maxMetersFrom()`](#maxmetersfrom).

## Filtering by type and tags

Features in a collection can be filtered by type:

```java
Features nodes()
Features ways()
Features relations()   
```

There are also four methods that take a query string:

```java
Features select(String query)
Features nodes(String query)
Features ways(String query)
Features relations(String query)
```

For example:

```java
nodes("[emergency=fire_hydrant]") // nodes that represent fire hydrants
select("na[amenity=pub,cafe]")    // pubs and cafes (nodes and areas)
relations("[route=bicycle]")      // cycling routes  
```

(See [Query Language](/goql) for details)

- Some queries always produce an empty collection. For example, `nodes("a")` is always
  empty: areas can be of type `Way` or `Relation`, but never `Node`.


## Retrieving features

To process all features in a set, simply iterate:

```java
for(Feature street : streets) ...
```

To obtain a `List`:

```java
List<Feature> list = streets.toList();
```

To obtain the **first** feature in a set:

```java
Feature city = france("n[place=city][name=Paris]").first();
```

Note that only the nodes of ways and members of relations are ordered collections;
all others are unordered sets, which means you'll receive a random feature if there
are more than one. If the collection is empty, `first()` returns `null`.

## Spatial filters

Features can be filtered by their spatial relationship to other geometric objects (typically a `Geometry`, `PreparedGeometry` or another `Feature`). 

### containing

Selects features whose geometry **contains** *A*:

- Every point of *A* is a point of the candidate feature, and the interiors of the two geometries have at least one point in common.

```java
Features containing(Feature)
Features containing(Geometry)
Features containing(PreparedGeometry)
Features containingXY(int, int)
Features containingLonLat(double, double)
```

For example:

```java
// In which park (if any) is this statue of Claude Monet?
return features.select("a[leisure=park]")
    .containing(statueOfMonet).first();

// The county, state and country for this point -- should return 
// San Diego County, California, USA (in no particular order)  
return features.select("a[boundary=administrative][admin_level <= 6]")
    .containingLonLat(-117.25, lat=32.99); 
```

### coveredBy 

Selects features whose geometry is **covered by** *A*:

- No point of the candidate feature's geometry lies outside of *A*.

```java
Features coveredBy(Feature)
Features coveredBy(Geometry)
Features coveredBy(PreparedGeometry)
```

### crossing

Selects features whose geometry **crosses** *A*:

- The geometries of *A* and the candidate feature have some (but not all) interior points in common
- The dimension of the intersection must be less than the maximum dimension of the candidate and *A*.

```java
Features crossing(Feature)
Features crossing(Geometry)
Features crossing(PreparedGeometry)
```

For example:

```java
// All railway bridges across the Mississippi River
Features railwayBridges =
    features.select("w[railway][bridge]");    
return railwayBridges.crossing(mississippi);
```

### disjointFrom 

Selects features whose geometry is **disjoint** from *A*:

- The geometries of the candidate feature and *A* have no common points at all.

```java
Features disjointFrom(Feature)
Features disjointFrom(Geometry)
Features disjointFrom(PreparedGeometry)
```

### intersecting

Selects features whose geometry **intersects** *A*:

- The geometries of *A* and the candidate feature have at least one point in common.

```java
Features intersecting(Feature)
Features intersecting(Geometry)
Features intersecting(PreparedGeometry)
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

```java
Features maxMetersFrom(double, Feature)
Features maxMetersFrom(double, Geometry)
Features maxMetersFrom(double, PreparedGeometry)
Features maxMetersFromXY(double, int, int)
Features maxMetersFromLonLat(double, double, double)
```

For example:

```java
// All bus stops within 500 meters of the given restaurant
Features nearbyBusStops = features.select("n[highway=bus_stop]")
    .maxMetersFrom(500, restaurant);
 
// All features within 3 km of the given point 
return features.maxMetersFromLonLat(3000, 76.41, 40.12); 
```

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
Features touching(Feature)
Features touching(Geometry)
Features touching(PreparedGeometry)
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


### within

Selects features that lie entirely **within** *A*:

- Every point of the candidate feature is a point in *A*, and their interiors have at least one point in common.

```java
Features within(Feature)
Features within(Geometry)
Features within(PreparedGeometry)
```


## Topological filters

These methods return a subset of those features that have a specific topological relationship with another `Feature`.

### connectedTo

Selects all features that have at least one node (vertex) in common with the given `Feature` or `Geometry`.

```java
Features connectedTo(Feature)
Features connectedTo(Geometry)
```

### nodesOf

The nodes of the given way. Returns an empty set if the feature is a node or relation.

```java
Features nodesOf(Feature)
```

### membersOf

Features that are members of the given relation, or nodes of the given way. Returns an empty set if the feature is a node.

```java
Features membersOf(Feature)
```

### parentsOf

Relations that have the given feature as a member, as well as ways to which the given node belongs.

```java
Features parentsOf(Feature)
```


