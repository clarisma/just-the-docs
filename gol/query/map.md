---
layout: default
title: Create Maps
parent: query
grand_parent: GOL Utility
nav_order: 0
---

# Create Maps

Use `gol query` with option `-f=map` to display query results on a [Leaflet](https://leafletjs.com/)-based map.

- Use [`--tags`](/gol/query#option-tags) to specify the tags that are displayed when the user hovers over a feature. 

Formatting options:

[`-f:attribution`](#option-f-attribution) | Attribution text at the bottom of the map
[`-f:basemap`](#option-f-basemap) | Tile server URL for base map
[`-f:color`](#option-f-color) | Color of map markers
[`-f:link`](#option-f-link) | URL to navigate when user clicks on a feature

<blockquote class="important" markdown="1">

If you are using map tiles provided by a third party, be sure to follow their
tile usage policy and provide proper attribution (For the OpenStreetMap default style, please see ([Policy for OSM Tiles](https://operations.osmfoundation.org/policies/tiles/)).

</blockquote>

## Example

A map displaying all museums in London, using the [Thunderforest Atlas](https://www.thunderforest.com/maps/atlas/) style (proprietary third-party style, API key and attribution required). The name and opening hours are displayed when the user hovers the cursor over a museum feature, and clicking it will show the feature on OpenStreetMap's Humanitarian layer.

```
gol query world -a=london.poly na[tourism=museum] -f=map 
  -t=name,opening_hours
  -f:attribution="Maps © <a href='*'>Thunderforest</a>, Data © OpenStreetMap contributors"
  -f:basemap="https://tile.thunderforest.com/atlas/{z}/{x}/{y}.png?apikey=<YOUR-KEY-HERE>"
  -f:link=https://www.openstreetmap.org/$type/$id#layers=H 
  > london-museums.html 
```

<em>*) links omitted for brevity</em>

## Formatting Options

### <code>-f:attribution=<em>&lt;TEXT&gt;</em></code> {#option-f-attribution}

The attribution text to display at the bottom of the map. Can be plain text or HTML, and must be enclosed in double quotes if it contains spaces, pspecial characters or HTML tags.


### <code>-f:basemap=<em>&lt;URL&gt;</em></code> {#option-f-basemap}

The URL to use for the base map.


### <code>-f:color=<em>&lt;COLOR&gt;</em></code> {#option-f-color}

The color of map markers: a named color (`red`, `green`, etc.) or an HTML color value (e.g. `#FF8835`). 

### <code>-f:link=<em>&lt;URL&gt;</em></code> {#option-f-link}

URL to navigate when user clicks on a map feature (defaults to the main OSM website).

- Use the `$type` and `$id` placeholders (`$t` and `$T` for type as a single letter) ~~0.2~~

- Use `-f:link=none` to disable links

