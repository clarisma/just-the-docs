---
layout: default
title:  U.S. Counties
parent: Examples
grand_parent: GeoDesk for Python
nav_order: 5
---

# Example: U.S. Counties



```python
import geodesk
import sys

world = geodesk.Features("usa.gol")

state_name = sys.argv[1] # first command-line argument (e.g. "California")
file_name = state_name.lower().replace(' ', '-') + "-counties"

state = world(f"a[boundary=administrative][admin_level=4][name='{state_name}']").one
counties = world("a[boundary=administrative][admin_level=6]").within(state)

counties.map(file_name, tooltip="{name}").show()
counties.geojson.save(file_name)
```

### Notes

