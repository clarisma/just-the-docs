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

Start working with collections by creating a *root collection*, which contains all features in a given Geographic Object Library:

```cpp
Features(const char* golFileName);
```

From this collection, you can create others:

```cpp
Features france("path/to/france.gol");
...
Features shops = france("na[shop]");
Features thingsInParis = france(paris);  // Feature or geometry 
Features shopsInParis = shops & thingsInParis;
```


## Filtering features

To select a subset of `Features`, add the constraint in parentheses, or apply a filter method. This always creates a new collection, leaving the original `Features` object unmodified.

### By bounding box

Select the features whose bounding boxes intersect the given `Box`:  

<img class="float" src="/img/bboxes.png" width=260>

```cpp
Features france("france.gol");
Box parisBounds = Box::ofWSEN(
    2.2, 48.8, 2.5, 48.9);
Features thingsInParis = france(parisBounds);
```

### By type and tags

Apply a query written in [GOQL (Geographic Object Query Language)](/goql) to select features based on their type and tags:

<img class="float" src="/img/query-type-tags.png" width=260>

```cpp
Features restaurants = world(
    "na[amenity=restaurant]");   
    // nodes and areas
    
Nodes fireHydrants = world(
    "n[emergency=fire_hydrant]");
    // only nodes
    
Ways safeForCycling = world(
    "w[highway=cycleway,path,living_street],"        
    "w[highway][maxspeed < 30]");
    // linear ways
```

### Using filter methods

Apply a [spatial filter](#spatial-filters) or [topological filter](#topological-filters), or a [custom filter](#custom-filters):

```cpp
states.within(usa)
features("w[highway]").membersOf(route66)
parks.filter(MyFilters::containsWaterFountains);
```

### Using set intersection

Select only features that are in *both* sets:

```cpp
Features museums = world("na[tourism=museum]");
Features inParis = world.within(paris);
Features parisMuseums = museums(inParis);
```

Alternatively, you can use the `&` operator:

```cpp
Features parisMuseums = museums & inParis;
```


## Obtaining `Feature` objects

Simply iterate:

```cpp
for(Feature hotel : hotels)
{
    std::cout << hotel["name"] << std::endl;
}
```

Create a `std::vector`, or populate an existing one:

```cpp
std::vector<Feature> list = streets;
streets.addTo(myVector);
```

Check if the set is empty:

```cpp
if (pubs.within(dublin))
    printf("Great, we can grab a beer in this town!");

if (!street.nodes("[traffic_calming=bump]"))
    printf("No speed bumps on this street.");
```

## Obtaining a single `Feature`

### first

Returns the first feature in a collection:

```cpp
std::optional<Feature> city = france("n[place=city][name=Paris]").first();
```

Note that only the nodes of ways and members of relations are ordered collections;
all others are unordered sets, which means you'll receive a random feature if there
are more than one. If the collection is empty, `first()` returns `nullopt`.

### one

Returns the one and only feature of the collection. Throws a `QueryException` if the collection is empty or contains more than one feature.

```cpp
Feature paris = world("n[place=city][name=Paris]").one();
    // will likely throw a QueryException, 
    // because there's also Paris, Texas
```

## Testing for membership

To check if a feature belongs to a given set, use `contains()`:

```cpp
Features sushiRestaurants = 
    world("na[amenity=restaurant][cuisine=sushi]");

if (sushiRestaurants.contains(restaurant))
    std::cout << restaurant["name"] << " serves sushi";
```

## Scalar queries

### count

The total number of features in the collection:

```cpp
printf("%d restaurants found.", restaurants.count());
```

### area

The total area (square meters as `double`) of all areas in this set.

```cpp
printf("London has %f square meters of parks.", 
    parks.within(london).area());
```

### length

The total length (meters as `double`) of all features in this set. For areas, their circumference is used.

```cpp
printf("The French motorway network is %f km long.", 
    france("w[highway=motorway]").length() / 1000);
```

## Spatial filters

Features can be filtered by their spatial relationship to other geometric objects (typically a `GEOSGeometry` or another `Feature`). 

### containing

Selects features whose geometry **contains** *A*:

- Every point of *A* is a point of the candidate feature, and the interiors of the two geometries have at least one point in common.

```cpp
Features containing(Feature);
Features containing(GEOSGeometry);
Features containingXY(Coordinate);
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
    .containingLonLat(-117.25, 32.99); 
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
Features maxMetersFrom(double, Coordinate);
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

## Custom filters

Use `filter()` with your own filter predicate:

```cpp
// Find all parks whose area is at least 1 km²
// (one million square meters)
 
Features parks = world("a[leisure=park]");
Features largeParks = parks.filter([](Feature park)
    { return park.area() > 1'000'000; });
```

**Important**: The predicate must be *threadsafe*, as the query may be executed in parallel.


