---
layout: default
title:  Sets of Features
parent: GeoDesk for Python
nav_order: 5
---


<a id="Features"></a>

# Feature Sets

A **feature set** represents those [`Feature`](/python\features#Feature) objects that meet certain criteria.

<h3 id="Features_Features" class="api"><span class="prefix">geodesk.</span><span class="name">Features</span><span class="paren">(</span><i>gol</i>, <i>url</i>=<span class="default">None</span><span class="paren">)</span></h3><div class="api" markdown="1">

Creates a feature set based on a Geographic Object Library.

</div>
## Filtering features

To select a subset of features, add the constraint in parentheses, or apply a filter method. This always creates a new feature set, leaving the original set unmodified.

### By bounding box

Select the features whose bounding boxes intersects the given [`Box`](/python\primitives#Box):

<img class="float" src="/img/bboxes.png" width=260>

```python
paris_bounds = Box(
    west=2.2, south=48.8,
    east=2.5, north=48.9)
features_in_paris = features(paris_bounds)
```

### By type and tags

Apply a query written in GOQL (the Geographic Object Query Language) to select features based on their type and tags:

<img class="float" src="/img/query-type-tags.png" width=260>

```python
restaurants = features(
    "na[amenity=restaurant]")
    # nodes and areas

fire_hydrants = features(
    "n[emergency=fire_hydrant]")
    # only nodes

safe_for_cycling = features(
   "w[highway=cycleway,path,living_street],"
   "w[highway][maxspeed < 30]")
   # linear ways
```

### Using filter methods

Apply a [spatial filter](#spatial-filters) or [topological filter](#topological-filters):

```python
states.within(usa)
features("w[highway]").members_of(route66)
```

### Using set intersection

Select only features that are in *both* sets:

```python
museums  = features("na[tourism=museum]")
in_paris = features.within(paris))
paris_museums = museums(in_paris)
```

Alternatively, you can use the `&` operator:

```python
paris_museums = museums & in_paris
```

## Obtaining `Feature` objects

Iterate through the feature set:

```python
>>> for hotel in hotels:
...     print(hotel.name)
Hôtel du Louvre
Ambassadeur
Brit Hotel
```

Turn it into a `list`:

```python
>>> list(hotels)
[way/112112065, relation/1575507, node/3558592188]
```

Check if the set is empty:

```python
if pubs(within_dublin):
    print("Great, we can grab a beer in this town!")

if not street.nodes("[traffic_calming=bump]"):
    print("No speed bumps on this street.")
```

<h3 id="Features_first" class="api"><span class="prefix">Features.</span><span class="name">first</span></h3><div class="api" markdown="1">

The first feature of the set (or any arbitrary feature if the set is unordered).

`None` if the set is empty.

</div><h3 id="Features_one" class="api"><span class="prefix">Features.</span><span class="name">one</span></h3><div class="api" markdown="1">

The one and only feature of the set.

A `QueryError` is raised if the set is empty or contains more than one feature.

</div>
## Properties

<h3 id="Features_count" class="api"><span class="prefix">Features.</span><span class="name">count</span></h3><div class="api" markdown="1">

The total number of features in this set.

</div><h3 id="Features_area" class="api"><span class="prefix">Features.</span><span class="name">area</span></h3><div class="api" markdown="1">

The total area (in square meters) of all areas in this set.

</div><h3 id="Features_length" class="api"><span class="prefix">Features.</span><span class="name">length</span></h3><div class="api" markdown="1">

The total length (in meters) of all features in this set. For areas, their circumference
is used.

</div>
## Subsets

<h3 id="Features_nodes" class="api"><span class="prefix">Features.</span><span class="name">nodes</span></h3><div class="api" markdown="1">

Only features that are nodes.

</div><h3 id="Features_ways" class="api"><span class="prefix">Features.</span><span class="name">ways</span></h3><div class="api" markdown="1">

Only features that are ways (including areas that are represented using a closed way).

If you want to restrict the subset to linear ways, use <code><i>features</i>('w')</code>.

</div><h3 id="Features_relations" class="api"><span class="prefix">Features.</span><span class="name">relations</span></h3><div class="api" markdown="1">

Only features that are relations (including relations that represent areas).

If you want to restrict the subset to non-area relations, use <code><i>features</i>('r')</code>.

</div>
## Formatting

<h3 id="Features_geojson" class="api"><span class="prefix">Features.</span><span class="name">geojson</span></h3><div class="api" markdown="1">

The set's features represented as GeoJSON.

</div><h3 id="Features_map" class="api"><span class="prefix">Features.</span><span class="name">map</span></h3><div class="api" markdown="1">

A [`Map`](/python\maps#Map) that displays the features in this set. Use [`show()`](/python\maps#Map_show) to open it in a browser window, or [`save()`](/python\maps#Map_save) to write its HTML file.

```python
restaurants.map.show()
hotels.map.save("hotel-map") # .html by default
hydrants.map(color='red')    # map with fire hydrants marked in red
```

</div>
## Spatial filters

These methods return a subset of only those features that fulfill a specific spatial relationship with another geometric object ([`Feature`](/python\features#Feature), [`Geometry`](#Geometry), [`Box`](/python\primitives#Box) or [`Coordinate`](/python\primitives#Coordinate)).

<h3 id="Features_around" class="api"><span class="prefix">Features.</span><span class="name">around</span><span class="paren">(</span><i>geom</i>, <i>units</i>=<span class="default">*distance*</span><span class="paren">)</span></h3><div class="api" markdown="1">

Features that lie within the given distance from the centroid of *geom*.
In lieu of a geometric object, you can also specify coordinates using
`x` and `y` (for Mercator-projected coordinates) or `lon` and `lat` (in degrees).
Use `meters`, `feet`, `yards`, `km`, `miles` or `mercator_units` to specify the maximum distance.

Example:

```python
# All bus stops within 500 meters of the given restaurant
features("n[highway=bus_stop]").around(restaurant, meters=500)

# All features within 3 miles of the given point
features.around(miles=3, lat=40.12, lon=-76.41)
```

</div><h3 id="Features_contains" class="api"><span class="prefix">Features.</span><span class="name">contains</span><span class="paren">(</span><i>geom</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose geometry *contains* the given geometric object.

**Note:** If you want to test whether this set includes a particular feature, use <code><i>feature</i> in <i>set</i></code>.

```python
# In which park (if any) is this statue of Claude Monet?
features("a[leisure=park]").contains(statue_of_monet)

# The county, state and country for this point -- should return
# San Diego County, California, USA (in no particular order)
features("a[boundary=administrative]"
    "[admin_level<=6]").contains(lon=-117.25, lat=32.99)
```

</div><h3 id="Features_crosses" class="api"><span class="prefix">Features.</span><span class="name">crosses</span><span class="paren">(</span><i>geom</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose geometry *crosses* the given geometric object.

```python
# All railway bridges across the Mississippi River
features("w[railway][bridge]").crosses(mississippi)
```

</div><h3 id="Features_disjoint" class="api"><span class="prefix">Features.</span><span class="name">disjoint</span><span class="paren">(</span><i>geom</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose geometry is *disjoint* from the given geometric object.

</div><h3 id="Features_intersects" class="api"><span class="prefix">Features.</span><span class="name">intersects</span><span class="paren">(</span><i>geom</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose geometry *intersects* the given geometric object.

</div><h3 id="Features_overlaps" class="api"><span class="prefix">Features.</span><span class="name">overlaps</span><span class="paren">(</span><i>geom</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose geometry *overlaps* the given geometric object.

</div><h3 id="Features_touches" class="api"><span class="prefix">Features.</span><span class="name">touches</span><span class="paren">(</span><i>geom</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose geometry *touches* the given geometric object.

</div><h3 id="Features_nearest_to" class="api"><span class="prefix">Features.</span><span class="name">nearest_to</span><span class="paren">(</span><i>geom</i>, <i>units</i>=<span class="default">*distance*</span><span class="paren">)</span><del>0.2</del></h3><div class="api" markdown="1">

Features in ascending order of distance to the given geometric object.

- To limit the search radius, specify a maximum distance in the units of your choice: `meters`, `feet`, `yards`, `km`, `miles` or `mercator_units`

Example:

```python
features("na[amenity=hospital]").nearest_to(my_location, miles=5)
```


</div>
## Topological filters

These methods return a subset of those features that have a specific topological relationship with another `Feature`.

<h3 id="Features_nodes_of" class="api"><span class="prefix">Features.</span><span class="name">nodes_of</span><span class="paren">(</span><i>feature</i><span class="paren">)</span></h3><div class="api" markdown="1">

The nodes of the given way. Returns an empty set if *feature* is a node or relation.

</div><h3 id="Features_members_of" class="api"><span class="prefix">Features.</span><span class="name">members_of</span><span class="paren">(</span><i>feature</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features that are members of the given relation, or nodes of the given way. Returns an empty set if *feature* is a node.

</div><h3 id="Features_parents_of" class="api"><span class="prefix">Features.</span><span class="name">parents_of</span><span class="paren">(</span><i>feature</i><span class="paren">)</span></h3><div class="api" markdown="1">

Relations that have the given feature as a member, as well as ways to which the given node belongs.

</div><h3 id="Features_descendants_of" class="api"><span class="prefix">Features.</span><span class="name">descendants_of</span><span class="paren">(</span><i>feature</i><span class="paren">)</span><del>0.2</del></h3><div class="api" markdown="1">

</div><h3 id="Features_ancestors_of" class="api"><span class="prefix">Features.</span><span class="name">ancestors_of</span><span class="paren">(</span><i>feature</i><span class="paren">)</span><del>0.2</del></h3><div class="api" markdown="1">

</div><h3 id="Features_connected_to" class="api"><span class="prefix">Features.</span><span class="name">connected_to</span><span class="paren">(</span><i>feature</i><span class="paren">)</span></h3><div class="api" markdown="1">

All features that share a common node with *feature*.


</div>
## Metadata

<h3 id="Features_properties" class="api"><span class="prefix">Features.</span><span class="name">properties</span></h3><div class="api" markdown="1">

</div><h3 id="Features_copyright" class="api"><span class="prefix">Features.</span><span class="name">copyright</span></h3><div class="api" markdown="1">

</div><h3 id="Features_license" class="api"><span class="prefix">Features.</span><span class="name">license</span></h3><div class="api" markdown="1">

The license under which this dataset is made available.

</div><h3 id="Features_license_url" class="api"><span class="prefix">Features.</span><span class="name">license_url</span></h3><div class="api" markdown="1">

The URL where the text of the license can be found.

</div><h3 id="Features_indexed_keys" class="api"><span class="prefix">Features.</span><span class="name">indexed_keys</span></h3><div class="api" markdown="1">

</div><h3 id="Features_tiles" class="api"><span class="prefix">Features.</span><span class="name">tiles</span></h3><div class="api" markdown="1">

