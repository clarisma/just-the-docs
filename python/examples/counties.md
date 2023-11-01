---
layout: default
title:  U.S. Counties
parent: Examples
grand_parent: GeoDesk for Python
nav_order: 5
---

# Example: U.S. Counties

For many geospatial use cases, getting the boundaries of an administrative area is
often the first step. Let's write a script that allows users to discover the counties
of any U.S. state. We'll display a map like the one below, and we also export the boundaries
as a GeoJSON file.

<img class="figure" src="/img/example-counties-screenshot.png" width="480">

Instead of hard-coding the state's name, we'll allow the user to supply it as a command-line
argument, e.g. `python counties.py Oregon`.

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

