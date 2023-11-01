---
layout: default
title:  Museums
parent: Examples
grand_parent: GeoDesk for Python
nav_order: 1
---

# Example: Museums in Paris

In this simple example, we'll list the names of all museums in Paris, as well as all
subway stations within 500 meters:

```python
import geodesk

world = geodesk.Features("france.gol")

paris = world("a[boundary=administrative][admin_level=8][name=Paris]").one
museums = world("na[tourism=museum]")
stations = world("n[railway=station]")

for museum in museums(paris):
    print(f"{museum.name}")
    for station in stations.around(museum, meters=500):
        print(f"- {station.name}")
```

### Notes

