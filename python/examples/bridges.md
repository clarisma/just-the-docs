---
layout: default
title:  Railway Bridges
parent: Examples
grand_parent: GeoDesk for Python
nav_order: 3
---

# Example: Railway Bridges

The [Danube](https://www.openstreetmap.org/relation/89652) is the second-longest river in Europe, flowing from the Black Forest to the Black Sea. What if we wanted to find all the railway bridges that cross it --- but only those in the German state of Bavaria?

This example demonstrates how to combine multiple filters to precisely select the features you want.

```python
import geodesk

features = geodesk.Features("europe.gol")

bavaria = features(
    "a[boundary=administrative][admin_level=4][name:en=Bavaria]").one

danube = features("r[waterway=river][name:en=Danube]").one

rail_bridges = features("w[railway][bridge]")
rail_bridges(bavaria).crosses(danube).map(
    "rail-crossings", color="red", weight=8, opacity=0.5).show()
```

### Notes

- Administrative areas (such as countries and states) in OpenStreetMap form a hierarchy.
  The meaning of `admin_level` varies between countries, but typically follows this scheme:

  2  | country
  4  | state or region
  6  | county (U.S.), *département* (France), *landkreis* (Germany), *provincia* (Italy)
  8  | City
  10 | Village or suburb

- While most water courses are mapped as simple ways (which you can retrieve with `w[waterway]`, larger rivers are typically represented using relations (`r`)
