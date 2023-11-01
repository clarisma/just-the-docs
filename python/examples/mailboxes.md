---
layout: default
title:  Mailboxes
parent: Examples
grand_parent: GeoDesk for Python
nav_order: 4
---

# Example: Mailbox Collection Times

The OpenStreetMap database contains far more information than what is visible on the map. Take public mailboxes, for instance: Aside from their locations, you can also discover when the letter you've dropped off will be picked up.

What are the most common mailbox collection times? Let's find out:

```python
import geodesk
from collections import Counter

world = geodesk.Features("world.gol")
post_boxes = world("na[amenity=post_box]")

counter = Counter([box.collection_times for box in post_boxes])
most_common = counter.most_common(10)

for collection_times, count in most_common:
    print(f"{count:>10} : {collection_times}")
```

### Notes


