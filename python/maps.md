---
layout: default
title:  Creating Maps
parent: GeoDesk for Python
nav_order: 7
---
# Creating Maps


### `geodesk.``Map`(*attributes*) {#Map}
{:.api}

## Properties

All are mutable.

### `Map.``basemap` {#Map_basemap}
{:.api}

### `Map.``attribution` {#Map_attribution}
{:.api}

### `Map.``leaflet_version` {#Map_leaflet_version}
{:.api}

### `Map.``leaflet_url` {#Map_leaflet_url}
{:.api}

### `Map.``leaflet_stylesheet_url` {#Map_leaflet_stylesheet_url}
{:.api}

### `Map.``min_zoom` {#Map_min_zoom}
{:.api}

### `Map.``max_zoom` {#Map_max_zoom}
{:.api}

## Methods

### `Map.``add`(*item*) {#Map_add}
{:.api}

### `Map.``save`(*filename*) {#Map_save}
{:.api}

Saves the map as an HTML file (If the file name has no extension, `.html` is used).

### `Map.``show`() {#Map_show}
{:.api}

Opens a browser window to display the map. If the map hasn't been explicitly saved to an HTML file, this method creates a temporary file.
