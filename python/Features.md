---
layout: default
title:  Sets of Features
parent: GeoDesk for Python
has_toc: false
nav_order: 6
---


<a id="Features"></a>

# Sets of Features

A **feature set** represents those [`Feature`](/python\Feature#Feature) objects that meet certain criteria.

{% comment %}
// > .method Features(*filename*, *url*=None)
{% endcomment %}

<h3 id="Features_Features" class="api"><span class="prefix">geodesk.</span><span class="name">Features</span><span class="paren">(</span><i>filename</i><span class="paren">)</span></h3><div class="api" markdown="1">

Creates a feature set based on a Geographic Object Library.

```python
france = Features("france")   # All features in france.gol
```

</div>
## Filtering features

To select a subset of features, add the constraint in parentheses, or apply a filter method. This always creates a new feature set, leaving the original set unmodified.

### By bounding box

Select the features whose bounding boxes intersect the given [`Box`](/python\Box#Box):

<img class="float" src="/img/bboxes.png" width=260>

```python
paris_bounds = Box(
    west=2.2, south=48.8,
    east=2.5, north=48.9)
features_in_paris = france(paris_bounds)
```

### By type and tags

Apply a query written in [GOQL (Geographic Object Query Language)](../goql) to select features based on their type and tags:

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

Apply a [spatial filter](#spatial-filters), [geometric filter](#geometric-filters) or [topological filter](#topological-filters):

```python
states.within(usa)
features("w[highway]").members_of(route66)
```

### Using set intersection

Select only features that are in *both* sets:

```python
museums  = features("na[tourism=museum]")
in_paris = features.within(paris)
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

## Obtaining a single `Feature`

<h3 id="Features_first" class="api"><span class="prefix">Features.</span><span class="name">first</span></h3><div class="api" markdown="1">

The first feature of the set (or any arbitrary feature if the set is unordered).

`None` if the set is empty.

</div><h3 id="Features_one" class="api"><span class="prefix">Features.</span><span class="name">one</span></h3><div class="api" markdown="1">

The one and only feature of the set.

A `QueryError` is raised if the set is empty or contains more than one feature.

</div>

<br>
Alternatively, use `[0]` to get the first `Feature` of a non-empty set.

A `QueryError` is raised if the set is empty.

```python
first_node = way.nodes[0]
```

## Testing for membership

To check if a feature belongs to a given set, use the `in` operator:

```python
sushi_restaurants = world("na[amenity=restaurant][cuisine=sushi]")

if restaurant in sushi_restaurants:
    print (f"{restaurant.name} serves sushi")
```

## Result properties

These are read-only, and are calculated on each access.

<h3 id="Features_count" class="api"><span class="prefix">Features.</span><span class="name">count</span></h3><div class="api" markdown="1">

The total number of features in this set.

</div><h3 id="Features_area" class="api"><span class="prefix">Features.</span><span class="name">area</span></h3><div class="api" markdown="1">

The total area (in square meters) of all areas in this set.

</div><h3 id="Features_length" class="api"><span class="prefix">Features.</span><span class="name">length</span></h3><div class="api" markdown="1">

The total length (in meters) of all features in this set. For areas, their circumference
is used.

</div><h3 id="Features_shape" class="api"><span class="prefix">Features.</span><span class="name">shape</span></h3><div class="api" markdown="1">

A `GeometryCollection` that contains the shapes of all features in this set.

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

The set's features as GeoJSON ([`Formatter`](Formatter#geojson))

</div><h3 id="Features_geojsonl" class="api"><span class="prefix">Features.</span><span class="name">geojsonl</span></h3><div class="api" markdown="1">

The set's features as GeoJSON, with each feature on a separate line ([`Formatter`](Formatter#geojsonl))

</div><h3 id="Features_map" class="api"><span class="prefix">Features.</span><span class="name">map</span></h3><div class="api" markdown="1">

A [`Map`](/python\Map#Map) that displays the features in this set. Use [`show()`](/python\Map#Map_show) to open it in a browser window, or [`save()`](/python\Map#Map_save) to write its HTML file.

```python
restaurants.map.show()
hotels.map.save("hotel-map") # .html by default
hydrants.map(color='red')    # map with fire hydrants marked in red
```

</div><h3 id="Features_wkt" class="api"><span class="prefix">Features.</span><span class="name">wkt</span></h3><div class="api" markdown="1">

The set's features as Well-Known Text ([`Formatter`](Formatter#wkt))

</div>
## Spatial filters

These methods return a subset of only those features that fulfill a specific spatial relationship with another geometric object ([`Feature`](/python\Feature#Feature), [`Geometry`](/python\Geometry#Geometry), [`Box`](/python\Box#Box) or [`Coordinate`](/python\Coordinate#Coordinate)).

<h3 id="Features_intersecting" class="api"><span class="prefix">Features.</span><span class="name">intersecting</span><span class="paren">(</span><i>geom</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose geometry *intersects* the given geometric object.

</div><h3 id="Features_within" class="api"><span class="prefix">Features.</span><span class="name">within</span><span class="paren">(</span><i>geom</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features that lie entirely inside *geom*.



</div><h3 id="Features_around" class="api"><span class="prefix">Features.</span><span class="name">around</span><span class="paren">(</span><i>geom</i>, <i>units</i>=<span class="default">*distance*</span><span class="paren">)</span></h3><div class="api" markdown="1">

Features that lie within the given distance from the centroid of *geom*.
In lieu of a geometric object, you can also specify coordinates using
`x` and `y` (for Mercator-projected coordinates) or `lon` and `lat` (in degrees).
Use `meters`, `feet`, `yards`, `km`, `miles` or `mercator_units` to specify the maximum distance.

```python
# All bus stops within 500 meters of the given restaurant
features("n[highway=bus_stop]").around(restaurant, meters=500)

# All features within 3 miles of the given point
features.around(miles=3, lat=40.12, lon=-76.41)
```

</div><h3 id="Features_containing" class="api"><span class="prefix">Features.</span><span class="name">containing</span><span class="paren">(</span><i>geom</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose geometry *contains* the given geometric object.

**Note:** If you want to test whether this set includes a particular feature, use <code><i>feature</i> in <i>set</i></code> ([See above](#testing-for-membership))

```python
# In which park (if any) is this statue of Claude Monet?
features("a[leisure=park]").containing(statue_of_monet).first

# The county, state and country for this point -- should return
# San Diego County, California, USA (in no particular order)
features("a[boundary=administrative]"
    "[admin_level <= 6]").containing(Coordinate(lon=-117.25, lat=32.99))
```

{% comment %}
```
# The county, state and country for this point -- should return
# San Diego County, California, USA (in no particular order)
features("a[boundary=administrative]"
    "[admin_level <= 6]").containing(lon=-117.25, lat=32.99)
```
{% endcomment %}

*As of Version {{ site.geodesk_python_version}}, only nodes and `Coordinate`
objects are supported.*

</div><h3 id="Features_crossing" class="api"><span class="prefix">Features.</span><span class="name">crossing</span><span class="paren">(</span><i>geom</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose geometry *crosses* the given geometric object.

```python
# All railway bridges across the Mississippi River
features("w[railway][bridge]").crossing(mississippi)
```

{%comment%}

</div><h3 id="Features_disjoint_from" class="api"><span class="prefix">Features.</span><span class="name">disjoint_from</span><span class="paren">(</span><i>geom</i><span class="paren">)</span><del>0.2</del></h3><div class="api" markdown="1">

Features whose geometry is *disjoint* from the given geometric object.

</div><h3 id="Features_overlapping" class="api"><span class="prefix">Features.</span><span class="name">overlapping</span><span class="paren">(</span><i>geom</i><span class="paren">)</span><del>0.2</del></h3><div class="api" markdown="1">

Features whose geometry *overlaps* the given geometric object.

</div><h3 id="Features_touching" class="api"><span class="prefix">Features.</span><span class="name">touching</span><span class="paren">(</span><i>geom</i><span class="paren">)</span><del>0.2</del></h3><div class="api" markdown="1">

Features whose geometry *touches* the given geometric object.

</div><h3 id="Features_nearest_to" class="api"><span class="prefix">Features.</span><span class="name">nearest_to</span><span class="paren">(</span><i>geom</i>, <i>units</i>=<span class="default">*distance*</span><span class="paren">)</span><del>0.2</del></h3><div class="api" markdown="1">

Features in ascending order of distance to the given geometric object.

- To limit the search radius, specify a maximum distance in the units of your choice: `meters`, `feet`, `yards`, `km`, `miles` or `mercator_units`

```python
features("na[amenity=hospital]").nearest_to(my_location, miles=5)
```

{%endcomment%}


</div>
## Geometric filters

These methods return a subset of those features that have specific geometric properties.

<h3 id="Features_min_area" class="api"><span class="prefix">Features.</span><span class="name">min_area</span><span class="paren">(</span><i>n</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose area is at least *n*, where *n* can be square meters or a specific unit (`meters`, `feet`, `yards`, `km`, `miles` or `mercator_units`).

```python
buildings.min_area(1000)
# Buildings with a footprint of at least a thousand square meters

world("a[place=island]").min_area(miles=500)
# Islands that are at least 500 square miles
```

</div><h3 id="Features_max_area" class="api"><span class="prefix">Features.</span><span class="name">max_area</span><span class="paren">(</span><i>n</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose area is at most *n* (see `min_area` above).

```python
features("a[leisure=pitch][sport=tennis]").max_area(ft=2000)
# Tennis courts that are no more than 2000 quare feet
```

</div><h3 id="Features_min_length" class="api"><span class="prefix">Features.</span><span class="name">min_length</span><span class="paren">(</span><i>n</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose length is at least *n*, where *n* can be meters or a specific unit (`meters`, `feet`, `yards`, `km`, `miles` or `mercator_units`).

```python
features("w[barrier=hedge]").min_length(300)
# Hedges that are at least 300 meters long

rivers.min_length(km=30)
# Rivers whose length is at least 30 kilometers
```

</div><h3 id="Features_max_length" class="api"><span class="prefix">Features.</span><span class="name">max_length</span><span class="paren">(</span><i>n</i><span class="paren">)</span></h3><div class="api" markdown="1">

Features whose length is at most *n* (see `min_length` above).

```python
streets.max_length(2.5)
# Street segments that are 2.5 meters or less
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

{%comment%}

</div><h3 id="Features_descendants_of" class="api"><span class="prefix">Features.</span><span class="name">descendants_of</span><span class="paren">(</span><i>feature</i><span class="paren">)</span><del>0.2</del></h3><div class="api" markdown="1">

</div><h3 id="Features_ancestors_of" class="api"><span class="prefix">Features.</span><span class="name">ancestors_of</span><span class="paren">(</span><i>feature</i><span class="paren">)</span><del>0.2</del></h3><div class="api" markdown="1">

{%endcomment%}

</div><h3 id="Features_connected_to" class="api"><span class="prefix">Features.</span><span class="name">connected_to</span><span class="paren">(</span><i>feature</i><span class="paren">)</span></h3><div class="api" markdown="1">

All features that share a common node with *feature*.

{%comment%}

</div>
## Metadata ~~0.2~~

<h3 id="Features_properties" class="api"><span class="prefix">Features.</span><span class="name">properties</span></h3><div class="api" markdown="1">

</div><h3 id="Features_copyright" class="api"><span class="prefix">Features.</span><span class="name">copyright</span></h3><div class="api" markdown="1">

</div><h3 id="Features_license" class="api"><span class="prefix">Features.</span><span class="name">license</span></h3><div class="api" markdown="1">

The license under which this dataset is made available.

</div><h3 id="Features_license_url" class="api"><span class="prefix">Features.</span><span class="name">license_url</span></h3><div class="api" markdown="1">

The URL where the text of the license can be found.

</div><h3 id="Features_indexed_keys" class="api"><span class="prefix">Features.</span><span class="name">indexed_keys</span></h3><div class="api" markdown="1">

</div><h3 id="Features_tiles" class="api"><span class="prefix">Features.</span><span class="name">tiles</span></h3><div class="api" markdown="1">

{%endcomment%}
