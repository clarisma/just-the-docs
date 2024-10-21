---
layout: default
title: The Basics
next: features.md
parent: GeoDesk for C++
nav_order: 2
---
# The Basics

<img class="float" src="/img/tiles4.png" width=280>

The GeoDesk Toolkit allows applications to query Geographic Object Libraries. A GOL is a compact single-file database that supports fast queries of OpenStreetMap features. To build a GOL from OSM data (`.osm.pbf` files such as the [planet file](https://planet.openstreetmap.org/) or [regional extracts](https://download.geofabrik.de/)), you'll need the [GOL command-line utility](/gol) ([download here](https://www.geodesk.com/download)). 

Create a GOL using the [`gol build`](/gol/build) command:

```bash
$ gol build france france-latest.osm.pbf
```

For a country-sized extract, this should take a few minutes on a reasonably modern machine.  

The [`gol query`](/gol/query) command supports basic [GOQL queries](/goql). The GeoDesk Toolkit brings the full range of geospatial capabilities to your applications.

## Supported Platforms

GeoDesk works with 64-bit Windows, Linux and MacOS. To build the library, you'll need a compiler with C++20 support (such as a recent version of MSVC, GCC or Clang). You'll also need CMake version 3.14 or above.

## Building & Including the Library

Incorporating the GeoDesk Toolkit in your own projects is straightforward, as it is a standalone library without external dependencies.

If you are using **CMake**, include GeoDesk via `FetchContent`:

```cmake
include(FetchContent)
FetchContent_Declare(geodesk GIT_REPOSITORY 
    https://github.com/clarisma/libgeodesk.git)
FetchContent_MakeAvailable(geodesk)
```

Use CMake option `BUILD_SHARED_LIBS` to build GeoDesk as a DLL/SO or a statically-linked library:

```cmake
set(BUILD_SHARED_LIBS ON)   # Use a GeoDesk as a DLL/SO
set(BUILD_SHARED_LIBS OFF)  # Link statically
```

GeoDesk provides optional **support for GEOS** (for advanced geometric operations, such as buffering, simplification and convex/concave hulls). Enable it with option `GEODESK_WITH_GEOS`. In this case, you'll also need to specify where GeoDesk can find the headers for the GEOS library (using `GEOS_INCLUDE_PATHS`).  

```cmake
FetchContent_Declare(geos
    GIT_REPOSITORY https://github.com/libgeos/geos.git)
FetchContent_MakeAvailable(geos)

set(GEODESK_WITH_GEOS ON)
set(GEOS_INCLUDE_PATHS "${geos_SOURCE_DIR}/include" "${geos_BINARY_DIR}/capi")
```

Add the GeoDesk **include path** and **link** to its library:

```cmake
target_include_directories(my_program ${geodesk_SOURCE_DIR}/include
target_link_libraries(my_program geodesk)
```

If you've enabled GEOS support, you'll need to link to GEOS as well (You'll need the GEOS C API as well as the main GEOS library):

```cmake
target_link_libraries(my_program geos_c geos)
```

## Header & Namespace

The entire GeoDesk library is available via a single **header**:

```cpp
#include <geodesk/geodesk.h>
```

All classes live in a single **namespace**:

```cpp
using namespace geodesk;
```

## Querying a GOL

To retrieve features from a GOL, create a `Features` object with the file name of the GOL:

```cpp
#include <geodesk/geodesk.h>

using namespace geodesk;

int main()
{
    Features world("path/to/world.gol");     // .gol extension is optional
    ...

```

Apply a filter (for example, all cities with at least one million inhabitants):

```cpp
    Features majorCities = world("n[place=city][population >= 1000000]"); 
```

Iterate over the filtered collection:

```cpp
    for(Feature city: majorCities)
    {
        std::cout << city["name"] << std::endl;
    }     
```

There's no need to close the GOL file explicitly. It will be automatically closed once all `Features` objects that contain the GOL's features (or a subset) have gone out of scope.

**Important**: The objects retrieved from a GOL (such as `Feature`, `Tags` and `TagValue`) are lightweight handles that become invalid once their underlying GOL file is closed.

The following pages cover [features](features) and [queries](queries) in detail. You can also consult the [API Documentation](http://cppdoc.geodesk.com).

## Geometry Primitives

GeoDesk supports basic geometric operations, such as calculating the [area](features#area) or [centroid](features#centroid) of a feature. It also offers primitives such as `Coordinate` (a pair of Cartesian coordinate values) and `Box` (an axis-aligned bounding box).

Coordinates are stored in [Mercator projection](/core-concepts#coordinate-system), but can be converted to and from degrees longitude/latitude as needed.

```cpp
Coordinate myLocation = Coordinate::ofLonLat(2.294, 48.858);    
Coordinate center = feature.centroid();
std::count << feature << " is located at " 
    << center.lat() " << degrees latitude." << std::endl;
    
Box bounds = Box::ofWSEN(2.2, 48.8, 2.5, 48.9);
    // West, South, East, North as longitude/latitude
```
 





