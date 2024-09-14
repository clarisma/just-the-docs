---
layout: default
title:  Formatters
parent: GeoDesk for Python
nav_order: 9
---


<a id="Formatter"></a>

# Formatters

A **Formatter** converts features to a different format, such as [GeoJSON](#geojson) or [Well-Known Text](#well-known-text). A Formatter's output can be customized, then turned into a string or saved to a file.

## Properties

These properties customize the Formatter's output.

<h3 id="Formatter_id" class="api"><span class="prefix">Formatter.</span><span class="name">id</span></h3><div class="api" markdown="1">

Default: `"{T}{id}"`

A function or string template used to generate an ID for each feature (only for GeoJSON),
or `None` to omit feature IDs.

- By default, the generated ID is a string that starts with `N`, `W` or `R` (for *node*, *way* or *relation*), followed by the feature's `id` property (e.g. `N54127`).

- A function must accept a single object (the `Feature`), and must return a number or string
(or an object whose `__str__()` method returns an ID).

- *As of Version {{ site.geodesk_python_version }}, only functions are accepted by `id`. (see [Issue #37](https://github.com/clarisma/geodesk-py/issues/37))*

```python
france("a[leisure=park]").geojson(
    id = lambda f: f.id * 2 + (0 if f.is_way else 1))
    # GeoJSON output with unique IDs, based on the feature's
    # (non-unique) ID, even for ways and odd for relations
    # (since areas can be either)
```

</div><h3 id="Formatter_limit" class="api"><span class="prefix">Formatter.</span><span class="name">limit</span></h3><div class="api" markdown="1">

Default: `None`

If a numeric limit is specified, the Formatter outputs at most *n* features.

</div><h3 id="Formatter_linewise" class="api"><span class="prefix">Formatter.</span><span class="name">linewise</span></h3><div class="api" markdown="1">

Default: `True` for `geojsonl`, otherwise `False`

For GeoJSON, enables line-by-line output of features (Ignored by other Formatters).

{%comment%}

</div><h3 id="Formatter_mercator" class="api"><span class="prefix">Formatter.</span><span class="name">mercator</span></h3><div class="api" markdown="1">

Default: `False`

If set to `True`, outputs Mercator-projected coordinates instead of WGS-84 (degrees longitude/latitude).

~~0.2~~

{%endcomment%}

</div><h3 id="Formatter_precision" class="api"><span class="prefix">Formatter.</span><span class="name">precision</span></h3><div class="api" markdown="1">

Default: `7`

The number of digits after the decimal point for coordinate values (A value of `7` equates to a resolution of about 1 cm).

</div><h3 id="Formatter_pretty" class="api"><span class="prefix">Formatter.</span><span class="name">pretty</span></h3><div class="api" markdown="1">

Default: `False`

If set to `True`, adds tabs and spacing to make the output easier to read.

</div>
## Methods

<h3 id="Formatter_save" class="api"><span class="prefix">Formatter.</span><span class="name">save</span><span class="paren">(</span><i>filename</i><span class="paren">)</span></h3><div class="api" markdown="1">

Writes the output to a file. If *filename* has no extension, a default is used.

```python
streets.geojson.save('london-streets')  # Creates london-streets.geojson
```

</div>
## GeoJSON

**GeoJSON** is a widely used format for representing geographic features. For each `Feature`, the `Formatter` writes its ID, geometry and properties (its OSM tags).

```json
{
    "type": "FeatureCollection",
    "generator": "geodesk-py/0.1.0",
    "features": [
        {
            "type": "Feature",
            "id": "W6001627",
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [-117.280372, 32.8393748], [-117.2803909, 32.8396239],
                    [-117.2803957, 32.839872], ... ]
            },
            "properties": {
                "highway": "secondary",
                "name": "Prospect Street",
                ...
            },
            ...
        }
    ]
}
```

### Line-based variant
{: #geojsonl }

As an alternative to classic GeoJSON, each `Feature` is written on a separate line:

```json
{ "type": "Feature", "id": "W6001627", "geometry": { "type": "LineString", ... }}
{ "type": "Feature", "id": "N596184365", "geometry": { "type": "Point", ... }}
```


## Well-Known Text
{: #wkt }

**Well-Know Text (WKT)** represents the geometric shapes of features (without IDs or tags).

```python
GEOMETRYCOLLECTION(
    LINESTRING(-117.280372 32.8393748, -117.2803909 32.8396239, ...),
    ...)
```

{% comment %}
You can generate WKT directly from a [`Geometry`](/python\Geometry#Geometry) object.
{% endcomment %}
