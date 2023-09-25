---
layout: default
title:  Sets of Features
parent: GeoDesk for Python
nav_order: 5
---

> .module geodesk
> .class Features

# Feature Sets

A **feature set** represents those [`Feature`](#Feature) objects that meet certain criteria.

> .method Features(*gol*, *url*=None)

Creates a feature set based on a Geographic Object Library.

## Filtering features

To select a subset of features, add the constraint in parentheses, or apply a filter method. This always creates a new feature set, leaving the original set unmodified.

### By bounding box

Select the features whose bounding boxes intersects the given [`Box`](#Box):  

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

## Properties

> .property count

The total number of features in this set.

> .property area

The total area (in square meters) of all areas in this set.

> .property length

The total length (in meters) of all features in this set. For areas, their circumference
is used.

## Subsets

> .property nodes

Only features that are nodes.

> .property ways

Only features that are ways (including areas that are represented using a closed way).

If you want to restrict the subset to linear ways, use <code><i>features</i>('w')</code>.

> .property relations

Only features that are relations (including relations that represent areas).

If you want to restrict the subset to non-area relations, use <code><i>features</i>('r')</code>.

## Formatting

> .property geojson

The set's features represented as GeoJSON.

> .property map

A [`Map`](#Map) that displays the features in this set. Use [`show()`](#Map.show) to open it in a browser window, or [`save()`](#Map.save) to write its HTML file. 

```python
restaurants.map.show()
hotels.map.save("hotel-map") # .html by default
hydrants.map(color='red')    # map with fire hydrants marked in red
```

## Spatial filters

These methods return a subset of only those features that fulfill a specific spatial relationship with another geometric object ([`Feature`](#Feature), [`Geometry`](#Geometry), [`Box`](#Box) or [`Coordinate`](#Coordinate)). 

> .method around(*geom*, *units*=*distance*)

Features that lie within the given distance from the centroid of *geom*. 
In lieu of a geometric object, you can also specify coordinates using 
`x` and `y` (for Mercator-projected coordinates) or `lon` and `lat` (in degrees).
Use `meters`, `feet`, `yards`, `km`, `miles` or `mercator_units` to specify the maximum distance.

Example:

```python
bus_stops.around(restaurant, meters=500) 
features.around(miles=3, lat=40.12, lon=-76.41) 
```

> .method contains(*geom*)

Features whose geometry *contains* the given geometric object.

**Note:** If you want to test whether this set includes a particular feature, use <code><i>feature</i> in <i>set</i></code>.

> .method crosses(*geom*)

Features whose geometry *crosses* the given geometric object.

> .method disjoint(*geom*)

Features whose geometry is *disjoint* from the given geometric object.

> .method intersects(*geom*)

Features whose geometry *intersects* the given geometric object.

> .method overlaps(*geom*)

Features whose geometry *overlaps* the given geometric object.

> .method touches(*geom*)

Features whose geometry *touches* the given geometric object.

> .method nearest_to(*geom*, *units*=*distance*) 0.2

Features in ascending order of distance to the given geometric object.

- To limit the search radius, specify a maximum distance in the units of your choice: `meters`, `feet`, `yards`, `km`, `miles` or `mercator_units`   

Example:

```python
features("na[amenity=hospital]").nearest_to(my_location, miles=5)
```


## Topological filters

These methods return a subset of those features that have a specific topological relationship with another `Feature`.

> .method members_of(*feature*)

Features that are members of the given relation, or nodes of the given way. Returns an empty set if *feature* is a node.

> .method parents_of(*feature*)

Relations that have the given feature as a member, as well as ways to which the given node belongs.

> .method descendants_of(*feature*) 0.2

> .method ancestors_of(*feature*) 0.2

> .method connected_to(*feature*) 

All features that share a common node with *feature*. 


## Metadata

> .property properties

> .property copyright

> .property license

The license under which this dataset is made available. 

> .property license_url

The URL where the text of the license can be found.

> .property indexed_keys

> .property tiles

