---
layout: default
title: Utility Classes
parent: GeoDesk for Java
nav_order: 5
redirect_from: /utility-classes
---

# Utility Classes

## `Box`

An axis-aligned bounding box. 

Note that the constructor is private -- to create `Box` objects, use the static methods (whose names remind you of the proper order of coordinates, and whether they are expected to be in Mercator projection: `ofWSEN`, `ofXYWH`, etc.)

The coordinates of `Box` are always projected. If `minX` is greater than `maxX`, this means that the bounding box crosses the Antimeridian.  

## `MapMaker`

A class that creates [Leaflet](http://www.leafletjs.com)-style maps. It is not intended to be a full-fledged map-making solution, but rather as a way to quickly visualize the results of geospatial operations. Add features and geometries, optionally set their attributes (color, tool tip, etc.), then save the map to an HTML file:

```java
MapMaker map = new MapMaker();
map.add(geometry)
    .tooltip("The crime scene");
map.add(feature)
    .color(red)
    .tooltip("The suspect's house");
map.save("investigation.html");
```

By default, `MapMaker` uses standard-style OpenStreetMap tiles to display the base map, but you can specify another tile source using `tiles()`. 

<blockquote class="important" markdown="1">

If you are publishing maps created by `MapMaker`, be sure to follow the usage policy of the
tile provider ([Policy for OSM Tiles](https://operations.osmfoundation.org/policies/tiles/)) and provide proper `attribution()`.

</blockquote>

## `Measure`

Various methods to measure the length and area of features and geometries, and distances between them. Units are in (square) meters.

Please be aware that these methods base their calculations on the Euclidean plane, which means they are fast, but don't have sufficient accuracy for objects at larger scales. Use them to measure the length of road segments or the area of a city park, but don't rely on them to calculate the land mass of Alaska.  

*(We plan to add alternative methods that support geodetic operations, such as great-circle distance).*    

## `Mercator`

Various methods to convert coordinates between longitude/latitude and the Mercator projection used internally by GeoDesk.

