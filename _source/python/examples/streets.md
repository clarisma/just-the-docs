---
layout: default
title:  Streets
parent: Examples
grand_parent: GeoDesk for Python
nav_order: 2
---

# Example: Streets of Berlin

In OpenStreetMap, a single street often comprises multiple *ways*. This segmentation occurs when there are variations in parking regulations, lane structures, or surface quality along its length. This can complicate a straightforward query such as "How long is this street?" --- but the script below makes this a breeze.

In this example, we'll fetch all the streets in Berlin, add up the lengths of their segment, and alphabetize the results. 

```python
import geodesk

germany = geodesk.Features("germany.gol")

berlin = germany("a[boundary=administrative][admin_level=4][name=Berlin]").one
streets = germany("w[highway][name]")

street_lengths = {}
for street in streets(berlin):
    name = street.name
    street_lengths[name] = street_lengths.get(name, 0) + street.length

for name, length in sorted(street_lengths.items()):
    print (f"{name}, {round(length)}")
```

### Notes

- The `highway` tag encompasses "roads" in the broadest possible sense --- from multi-lane 
  freeways to dirt paths. You can narrow down the results by explicitly
  listing the `highway` types, such as `highway=primary,secondary,tertiary,residential` 
 
- We can't use `street_lengths[name] += street.length`, as it requires that the key is
  already present in the dictionary (otherwise, a `KeyError` is raised). The `get()` method 
  doesn't have this restriction and allows us to specify a default value (`0`) 