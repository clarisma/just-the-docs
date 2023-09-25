---
layout: default
title:  Creating a Map
parent: GeoDesk for Python
nav_order: 7
---

> .module geodesk
> .class Map
 
# Creating a `Map`

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

`basemap` | Tile server URL for the base map (default: OpenStreetMap Carto)
`attribution` | The attribution text to display at the bottom of the map (This is          required if you publicly display your map, and defaults to "&copy; OpenStreetMap") 
`leaflet_version` | The version of the [Leaflet](https://www.leafletjs.com) to use
`leaflet_url` | The URL from which 

## Element Attributes

`stroke` | Whether to draw the element's stoke. Default: `true`. Use `false` if you don't want borders around polygons or circles.
`color` | The stroke color. Default: `"blue"`
`weight` | Stroke width in pixels. Default: 3
`opacity` | Stroke opacity. Default: 1.0
`lineCap` | A string that defines <a href="https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-linecap">shape to be used at the end</a> of the stroke. Default: `"round"`
`lineJoin` | A string that defines <a href="https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-linejoin">shape to be used at the corners</a> of the stroke. Default: `"round"`
`dashOffset` | A string that defines the stroke <a href="https://developer.mozilla.org/docs/Web/SVG/Attribute/stroke-dasharray">dash pattern</a>. Default: `None` (solid line)
`fill` | Whether to fill the element with color. Default: `true`. Use `false` to disable filling polygons or circles	
`fillColor` | Fill color. Defaults to the value of `color`
`fillOpacity` | Fill opacity. Default: 0.2 


Adapted from [Leaflet API Documentation](https://leafletjs.com/reference.html#path) --- &copy; 2010 -- 2013 Volodymyr Agafonkin. Licensed under [BSD-2-Clause](https://github.com/Leaflet/Leaflet/blob/main/LICENSE)


## Properties

All are mutable.

> .property basemap

> .property attribution

> .property leaflet_version

> .property leaflet_url

> .property leaflet_stylesheet_url

> .property min_zoom

> .property max_zoom

## Methods

> .method add(*item*)

> .method save(*filename*)

Saves the map as an HTML file (If the file name has no extension, `.html` is used).

> .method show()

Opens a browser window to display the map. If the map hasn't been explicitly saved to an HTML file, this method creates a temporary file.
