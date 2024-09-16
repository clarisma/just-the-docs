---
layout: default
title:  Creating a Map
parent: GeoDesk for Python
description: How to display OpenStreetMap features on a Leaflet map
nav_order: 8
---

> .module geodesk
> .class Map
 
# Creating a `Map`

<img class="float" src="/img/example-counties-screenshot.png" width="320">

The easiest way to visualize features and other geometric objects is to place them on a `Map` (a [Leaflet](https://www.leafletjs.com)-based web map). Create one via the [`map`](#Feature.map) property of a feature or feature set, or directly:

> .method Map(*attributes*)
 
The optional *attributes* customize the look and behavior of the map and its elements (described below).

> .end method

Using a `Map` is easy: [`add()`](#Map.add) elements, then [`save()`](#Map.save) it as an HTML file and/or [`show()`](#Map.show) it in a browser window:

```python
features("na[tourism=hotel]").map.save("hotels")
# (.html file extension by default)

my_map = Map()
my_map.add(features("na[amenity=fire_station]"), color="red")
my_map.add(features("n[emergency=fire_hydrant]"), color="orange")
my_map.show()
```

## Map Attributes

These attributes apply to the map itself. They can be passed as keyword arguments or accessed as properties of the `Map` object. 

`basemap` | Tile server URL for the base map (Default: OpenStreetMap Carto)
`attribution` | Attribution text to display at the bottom of the map (This is          required if you publicly display your map, and defaults to "&copy; OpenStreetMap") 
`leaflet_version` | Version of the [Leaflet](https://www.leafletjs.com) to use
`leaflet_url` | URL from which Leaflet is loaded (By default, Leaflet is loaded from [UNPKG](https://www.unpkg.com/))
`leaflet_stylesheet_url` | URL for a custom CSS file (to customize the appearance of the Leaflet map controls)
`min_zoom` | Minimum zoom level. Default: 0
`max_zoom` | Maximum zoom level: Default: 19

## Element Attributes

These attributes apply to individual map elements. They can be passed as keyword arguments or accessed as properties of the `Map` object (in which case they act as default attributes). 

`tooltip` | Text (HTML) to display when the user places the mouse cursor over an element. Default: `None`
`link` | URL to navigate when the user clicks on an element (*see details below*). Default: `None` 
`stroke` | Whether to draw the element's stoke. Default: `True`. Use `False` if you don't want borders around polygons or circles.
`color` | The stroke color. Default: `"blue"`
`weight` | Stroke width in pixels. Default: 3
`opacity` | Stroke opacity. Default: 1.0
`lineCap` | A string that defines <a href="https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-linecap">shape to be used at the end</a> of the stroke. Default: `"round"`
`lineJoin` | A string that defines <a href="https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-linejoin">shape to be used at the corners</a> of the stroke. Default: `"round"`
`dashArray` | A string that defines the stroke <a href="https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-dasharray">dash pattern</a>. Default: `None` (solid line)
`dashOffset` | A string that defines the [distance into the dash pattern](https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-dashoffset) to start the dash. Default: `None`
`fill` | Whether to fill the element with color. Default: `True`. Use `False` to disable filling polygons or circles	
`fillColor` | Fill color. Defaults to the value of `color`
`fillOpacity` | Fill opacity. Default: 0.2 

(Adapted from [Leaflet API Documentation](https://leafletjs.com/reference.html#path) --- &copy; 2010 -- 2013 Volodymyr Agafonkin. Licensed under [BSD-2-Clause](https://github.com/Leaflet/Leaflet/blob/main/LICENSE))
{:.text-small}

> .property link

You can use template arguments in the `link` property to customize the link for
each individual `Feature`. Any attribute of `Feature` is accepted (including tags).  

To open the feature's website (if it has one):

```python
link="{website}"
```

To display the feature on the official OpenStreetMap website (where you can see more information, such as its revision history):

```python
link="https://www.openstreetmap.org/{osm_type}/{id}"
```

To edit the feature in iD (the default OpenStreetMap editor):

```python
link="https://www.openstreetmap.org/edit?{osm_type}={id}"
```
{%comment%}

## Properties

All are mutable.

> .property basemap

> .property attribution

> .property leaflet_version

> .property leaflet_url

> .property leaflet_stylesheet_url

> .property min_zoom

> .property max_zoom

{%endcomment%}

## Methods

> .method add(*item*, *attributes*=None)

Creates a map marker for the given *item*:

- a geometric object (`Coordinate`, `Box`, `Feature` or `Geometry`)
- any object that has an `add_to_map(Map)` method
- an iterable that contains any of the above (e.g. a feature set)

> .method save(*filename*)

Saves the map as an HTML file (If the file name has no extension, `.html` is used).

> .method show()

Opens a browser window to display the map. If the map hasn't been explicitly saved to an HTML file, this method creates a temporary file.
