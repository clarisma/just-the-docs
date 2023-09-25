---
layout: default
title:  Creating a Map
parent: GeoDesk for Python
nav_order: 7
---


<a id="Map"></a>

# Creating a `Map`

The easiest way to visualize features and other geometric objects is to place them on a `Map` (a [Leaflet](https://www.leafletjs.com)-based web map). Create one via the [`map`](/python\features#Feature_map) property of a feature or feature set, or directly:

<h3 id="Map_Map" class="api"><span class="prefix">geodesk.</span><span class="name">Map</span><span class="paren">(</span><i>attributes</i><span class="paren">)</span></h3><div class="api" markdown="1">

The optional *attributes* customize the look and behavior of the map and its elements (described below).

</div>

Using a `Map` is easy: [`add()`](/python\maps#Map_add) elements, then [`save()`](/python\maps#Map_save) it as an HTML file and/or [`show()`](/python\maps#Map_show) it in a browser window:

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

<h3 id="Map_basemap" class="api"><span class="prefix">Map.</span><span class="name">basemap</span></h3><div class="api" markdown="1">

</div><h3 id="Map_attribution" class="api"><span class="prefix">Map.</span><span class="name">attribution</span></h3><div class="api" markdown="1">

</div><h3 id="Map_leaflet_version" class="api"><span class="prefix">Map.</span><span class="name">leaflet_version</span></h3><div class="api" markdown="1">

</div><h3 id="Map_leaflet_url" class="api"><span class="prefix">Map.</span><span class="name">leaflet_url</span></h3><div class="api" markdown="1">

</div><h3 id="Map_leaflet_stylesheet_url" class="api"><span class="prefix">Map.</span><span class="name">leaflet_stylesheet_url</span></h3><div class="api" markdown="1">

</div><h3 id="Map_min_zoom" class="api"><span class="prefix">Map.</span><span class="name">min_zoom</span></h3><div class="api" markdown="1">

</div><h3 id="Map_max_zoom" class="api"><span class="prefix">Map.</span><span class="name">max_zoom</span></h3><div class="api" markdown="1">

</div>
## Methods

<h3 id="Map_add" class="api"><span class="prefix">Map.</span><span class="name">add</span><span class="paren">(</span><i>item</i><span class="paren">)</span></h3><div class="api" markdown="1">

</div><h3 id="Map_save" class="api"><span class="prefix">Map.</span><span class="name">save</span><span class="paren">(</span><i>filename</i><span class="paren">)</span></h3><div class="api" markdown="1">

Saves the map as an HTML file (If the file name has no extension, `.html` is used).

</div><h3 id="Map_show" class="api"><span class="prefix">Map.</span><span class="name">show</span><span class="paren">(</span><span class="paren">)</span></h3><div class="api" markdown="1">

Opens a browser window to display the map. If the map hasn't been explicitly saved to an HTML file, this method creates a temporary file.
