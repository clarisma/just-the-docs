---
layout: default
title:  Mailboxes
parent: Examples
grand_parent: GeoDesk for Python
nav_order: 4
---

# Example: Mailbox Collection Times

The OpenStreetMap database contains far more information than what is visible on the map.



```python
import geodesk
from collections import Counter

world = geodesk.Features("world.gol")
post_boxes = world("na[amenity=post_box]")

count = Counter([box.collection_times for box in post_boxes])
most_common = count.most_common(10)

for collection_times, occurrences in most_common:
    print(f"{occurrences:>10} : {collection_times}")
```

### Notes

