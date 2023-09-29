---
layout: default
title: Why GeoDesk?
next: core-concepts.md
nav_order: 2
---
# Why GeoDesk?

Since its launch in 2004, a vibrant software ecosystem has emerged around OpenStreetMap. However, geospatial analytics remains a difficult task. Most processing tasks are resource-intensive, requiring high-end workstations and in-depth expertise. The OSM project was meant to democratize geospatial data, but these hurdles discourage many potential adopters.

The crux of the problem is this: That shiny OpenStreetMap file isn't particularly useful until you load it into a database, where you can dissect it with spatial queries. But importing into a traditional SQL-based DBMS turns that already hefty OSM file into a monstrous hulking beast. *You're gonna need a bigger drive!*
And you're going to need tons of patience, because that database import will take many hours even on a beefy machine.

So we went back to the drawing board and reimagined data storage. Instead of using a relational database, GeoDesk stores OSM data in a *Geographic Object Library* (GOL). GOLs have the following advantages:    

- **Compact file size**: GOLs are stored as single files, which are typically only 40 percent larger than the dataset in `.osm.pbf` format. This is a small fraction of the footprint of a traditional database.

- **Lightning-fast queries**: The most common spatial queries perform *fifty times faster* than their SQL equivalents.

- **Designed for OSM**: Unlike most spatial databases, GOLs store not only the geometries of features, but also support OSM concepts like relations.   

- **Simplified distribution** of OSM data: Any GOL can be turned into a compressed tile repository, from which users download only the regions they need. This greatly reduces storage and download costs.  

- **Easy to use**: The GeoDesk API provides a powerful query language based on familiar MapCSS. Results are returned as Java or Python objects --- no need for tedious object-relational mapping. 

- Seamless integration with the [**Java Topology Suite (JTS)**](https://locationtech.github.io/jts/) (and Python's [**Shapely**](https://shapely.readthedocs.io/en/stable/)) for **advanced vector operations**: buffer, generalize, union, convex and concave hulls, triangulation, Voronoi diagrams, and much more.  
 
- **Modest hardware requirements**: GeoDesk performs well on just about any system that can run 64-bit Java or Python.

The [GeoDesk database engine](https://www.github.com/clarisma/geodesk) and the [GOL command-line utility](https://www.github.com/clarisma/gol-tool) are free & open-source.