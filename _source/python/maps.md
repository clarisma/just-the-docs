---
layout: default
title:  Creating Maps
parent: GeoDesk for Python
nav_order: 7
---
# Creating Maps

> .module geodesk
> .class Map


> .method Map(*attributes*)

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
