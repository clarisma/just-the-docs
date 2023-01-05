---
layout: default
title: query
parent: GOL Utility
nav-order: 6
---

# `query`

Prints all features that match the given query to `stdout`, in a variety of formats.

Usage:

    gol query [<options>] <gol-file> <query>

The query must be written in [GOQL](../goql), the Geo-Object Query Language. GOQL is very
similar to [MapCSS](https://wiki.openstreetmap.org/wiki/MapCSS/0.2), which is used 
by Mapnik and Overpass to select OSM objects.

For example:

    gol query geodata/france 
      na[amenity=fire_station], n[emergency=fire_hydrant]
      -b=2.2,48.8,2.5,18.9 -f=geojson 
      -u=https://www.mywebsite.com/myfeatures/france -n

retrieves all fire stations (which can be nodes or areas) and hydrants
(which only exist as nodes) from the `france.gol` library (stored in the `geodata`
folder). The features must lie fully or partially inside the specified bounding box (a rectangle that covers metropolitan Paris) and are printed to `stdout` as GeoJSON (*see below*).

Tiles that are part of the query area, but that are not already present in the
library, are downloaded from the specified URL. If the library itself does not yet
exist, it is created (option `-n`, or `--new`).

- The path of the library is resolved relative to the current directory. The `.gol`
  file extension may be omitted.

## Options

{% include gol/option-area.md %}
{% include gol/option-bbox.md %}

### `-f`, <code>--format=<em>&lt;TYPE&gt;</em></code> {#option-format}

The [output format](#output-formats) of the results:

`count` | Prints only the *number* of features. 
[`csv`](#format-csv) | Comma-separated values
[`geojson`](#format-geojson) | [GeoJSON](https://geojson.org)
[`geojsonl`](#format-geojsonl) | [GeoJSONL](https://stevage.github.io/ndgeojson/) (newline-delimited GeoJSON)
[`list`](#format-list) | Simple list of IDs (*default*)
[`map`](#format-map) | HTML for a [Leaflet](https://leafletjs.com/)-based map
[`poly`](#format-poly) | [Polygon file](https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format)
[`stats`](#format-stats) | Statistics based on tags and roles
[`xml`](#format-xml) | [OSM-XML](https://wiki.openstreetmap.org/wiki/OSM_XML)


### <code>-f:<em>&lt;OPTION&gt;</em></code>, <code>--format:<em>&lt;OPTION&gt;</em> = <em>&lt;VALUE&gt;</em></code>

[Formatting options](#formatting-options) to customize the output.


{% comment %}

### `--center=bbox|centroid|inside` ~~0.2~~

Defines what is considered the "center" of a feature:

<table>
  <tr>
    <td><code>bbox</code></td>
    <td>
        The center point of the feature's bounding box, which may lie outside the
        feature's geometry. Selecting this option may result in slightly faster 
        queries.
    </td>
  </tr>
  <tr>
    <td><code>centroid</code></td>
    <td>
        The geometric centroid of the feature, which may lie outside the
        feature's geometry (though never outside its bounding box). <em>Default</em> 
    </td>
  </tr>
  <tr>
    <td><code>inside</code></td>
    <td>
        A point that is guaranteed the lie inside the feature (or on it, 
        in case of a Way). 
    </td>
  </tr>
</table>

  This option only matters if the `--tags` option includes `lon`, `lat`, `x` or `y`.

  The center point of a Node is always its coordinate.

{% endcomment %}

### `-l`, <code>--limit=<em>&lt;NUMBER&gt;</em></code> {#option-limit}

The maximum number of features to be displayed or counted.

{% comment %}
- For`-f=stats`, limits the number of rows displayed, without affecting the number of features analyzed by the query.
{% endcomment %} 

### `-t`, <code>--tags=<em>&lt;LIST&gt;</em></code> {#option-tags}

A comma-separated list of OSM keys, which determine the feature tags to be
included in the output.

There are several special keys that only apply to the `csv` output option and produce
additional columns:

<table>
  <tr>
    <td><code>bbox</code></td>
    <td markdown="span">

The bounding-box coordinates of the feature (West, South, East, North).
For `--format=geojson`, this becomes the [`bbox`](https://datatracker.ietf.org/doc/html/rfc7946#section-5) member of the `Feature` object.
 
  </td>
</tr>
<tr>
  <td><code>geom</code></td>
  <td>

The geometry of the feature (as <a href="https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry">well-known text</a>).<br>
          Only applies to <code>--format=csv</code>. 
      </td>
    </tr>
    <tr>
      <td><code>lat</code></td>
      <td>
          The WGS-84 latitude of the feature's <em>center</em> (see <code>--center</code>). 
      </td>
    </tr>
    <tr>
      <td><code>lon</code></td>
      <td>
          The WGS-84 longitude of the feature's <em>center</em> (see <code>--center</code>). 
      </td>
    </tr>
    <tr>
      <td><code>tags</code><br>(or&nbsp;<code>*</code>)</td>
      <td>
          A comma-separated list of key-value pairs, representing the keys of the tags
          that are not already printed in a column of their own. 
       </td>
    </tr>
    <tr>
      <td><code>x</code></td>
      <td>
          The Mercator-projected X coordinate of the feature's <em>center</em> (see <code>--center</code>). 
      </td>
    </tr>
    <tr>
      <td><code>y</code></td>
      <td>
          The Mercator-projected Y coordinate of the feature's <em>center</em> (see <code>--center</code>). 
      </td>
    </tr>
  </table>

  If `--tags` is omitted, all tags are included in the output.

  `--tags` is ignored if the requested output format is `count` or `list`.


{% include gol/option-new.md %}
{% include gol/option-output.md %}

### <code>--precision=<em>0-15</em></code> {#option-precision}

The coordinate precision (digits after the decimal point) to use.

<!--
<div class="language-plaintext highlighter-rouge">
<pre class="highlight"><code>--precision=<em>0-15</em></code></pre></div>
-->

Applies only to `csv`, `geojson`/`geojsonl`, `poly` and `xml`.


{% include gol/option-url.md %}

## Output Formats

Specified by the [`--format`](#option-format) option.

### `-f=csv` {#format-csv}

Outputs features in table-based form, suitable for import into a spreadsheet
application or an SQL database.

The first row contains the header, the following rows each represent a single
feature. Use in conjunction with `--tags` to specify which tags
should be written.

Columns are separated by a tab character. The first two columns are always
`t` (the OSM type of the element: `N`, `W`, or `R`) and `id` (the OSM id
of the element).

If the `--tags` option is not specified, the only other column is `tags`,
which includes all the features' tags as a comma-separated
lists of key-value pairs.

Supported options: `f:id`, `f:sort`


### `-f=geojson` {#format-geojson}

Outputs features as [GeoJSON](https://geojson.org).

Supported options: [`f:id`](#option-f-id)

### `-f=geojsonl` {#format-geojsonl}

Outputs features as [GeoJSONL](https://stevage.github.io/ndgeojson/) (newline-delimited GeoJSON).

Supported options: [`f:id`](#option-f-id)

### `-f=list` {#format-list}

A list of IDs. This is the default if no format is specified.

Supported options: `f:id`

### `-f=map` {#format-map}

Generates HTML for a [Leaflet](https://leafletjs.com/)-based map
that presents the query results visually. 

Formatting options:

[`-f:attribution`](#option-f-attribution) | Attribution text at the bottom of the map
[`-f:basemap`](#option-f-basemap) | Tile server URL for base map
[`-f:color`](#option-f-color) | Color of map markers
[`-f:link`](#option-f-link) | URL to navigate when user clicks on a feature

<blockquote class="important" markdown="1">

If you are using map tiles provided by a third party, be sure to follow their
tile usage policy and provide proper attribution.

</blockquote>

Example:

A map displaying all museums in London, using the [Thunderforest Atlas](https://www.thunderforest.com/maps/atlas/) style (proprietary third-party style, API key and attribution required). The name and opening hours are displayed when the user hovers the cursor over a museum feature, and clicking it will show the feature on OpenStreetMap's Humanitarian layer.

```
gol query world -a=london.poly na[tourism=museum] -f=map 
  -t=name,opening_hours
  -f:attribution="Maps © <a href='*'>Thunderforest</a>, Data © OpenStreetMap contributors"
  -f:basemap="https://tile.thunderforest.com/atlas/{z}/{x}/{y}.png?apikey=<YOUR-KEY-HERE>"
  -f:link=https://www.openstreetmap.org/$type/$id#layers=H 
  > london-museums.html 
```

<em>*) links omitted for brevity</em>



### `-f=poly` {#format-poly}

Outputs features in [polygon-file format](https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format). Non-polygonal features are omitted.
The resulting file can be used for the `--area` option in subsequent queries.

### `-f=stats` {#format-stats}

Generates statistics about tag usage and relation roles. Each row in the report is a permutation of the tag values (whose keys are specified by `--tags`) found among the features that the query selects. The final column contains the number of features, total length or total area, based on [`-f:tally`](#option-f-tally). For `-f:tally=roles`, only relations are analyzed, and the roles of their members are included in each permutation.   

{% comment %}
- Use <code>--limit=<em>n</em></code> to only display the *n* most common permutations.
{% endcomment %}

Formatting options:

[`-f:min-tally`](#option-f-min-tally) | Don't include rows with tally less than this number/precentage
[`-f:split-values`](#option-f-split-values) | Treat value with semicolons as list of individual values (e.g. `japanese;sushi;seafood` would be treated as 3 distinct values)   
[`-f:tally`](#option-f-tally) | Statistics to generate: `count`, `length`, `area` or `roles`
[`-f:unit`](#option-f-unit) | Length/area unit (default: `m`)


#### Examples

Discover the most common types of restaurants in Berlin:

```
gol query germany -a=berlin.poly na[amenity=restaurant] -f=stats -t=cuisine 

cuisine
===========================
-               994   23.3%
italian         731   17.1%
german          288    6.7%
vietnamese      258    6.0%
...
---------------------------
Total         4,269  100.0%
```

Calculate the total length (in kilometers) of all road-like features in France, broken out by `highway` type:

```
gol query world -a=france.poly w[highway] -f=stats -t=highway -f:tally=length -f:unit=km 

highway
===================================
track            647,966 km   29.2%
unclassified     464,661 km   20.9%
tertiary         243,117 km   10.9%
residential      239,686 km   10.8%
...
-----------------------------------
Total          2,221,737 km  100.0%
```

Count the various forms of `opening_hours` for restaurants, cafes and shops, sorted by tag values:

```
gol query germany na[amenity=cafe,restaurant],na[shop] -f=stats 
  -t=amenity,shop,opening_hours -f:sort=tags

shop              amenity     opening_hours
============================================================
-                 cafe        -               15,960    2.9%
-                 restaurant  -               57,931   10.7%
bakery            -           -               19,059    3.5%
butcher           -           -                7,332    1.4%
...
------------------------------------------------------------
Total                                        541,833  100.0%
```

Measure the areas of different types of land use (excluding forests and farmland):

```
gol query world a[landuse != forest,farmland] -f=stats -t=landuse -f:tally=area

landuse
----------------------------
residential   240,312,392 m2  
commercial     80,900,121 m2
...
```

Analyze how often certain roles appear in route relations:

```
gol query world r[route] -f=stats -t=route -f:tally=roles 

route    role
-----------------------------------
train    (empty)     10,745 in  216  
train    stop         8,219 in  211
bicycle  (empty)      4,213 in   68
...
```



### `-f=xml` {#format-xml}

Outputs features in [OSM-XML](https://wiki.openstreetmap.org/wiki/OSM_XML) format.

<blockquote class="important" markdown="1">
Output is not suitable for editing, since the IDs for untagged nodes won't
match the original OSM data (*You can open these XML files in JOSM, but please don't upload them*).
</blockquote>

## Formatting Options

### <code>-f:attribution=<em>&lt;TEXT&gt;</em></code> {#option-f-attribution}

For `--format=map`, the attribution text to display at the bottom of the map. Can be plain text or HTML.


### <code>-f:basemap=<em>&lt;URL&gt;</em></code> {#option-f-basemap}

For `--format=map`, the URL to use for the base map.


### <code>-f:color=<em>&lt;COLOR&gt;</em></code> {#option-f-color}

The color of map markers: a named color (`red`, `green`, etc.) or an HTML color value (e.g. `#FF8835`). 

### <code>-f:id=<em>&lt;OPTION&gt;</em></code> ~~0.2~~ {#option-f-id}

Defines the style of IDs used in [CSV](format-csv), [GeoJSON]((format-geojson)), [GeoJSONL]((format-geojsonl)) and basic lists: 

`none` | Omit the ID of features
`multi4` | OSM ID multiplied by 4 (+1 for ways, +2 for relations)
`multi10` | OSM ID multiplied by 10 (+1 for way, +2 for relations)
`full` | `$type/$id`, e.g. `node/123456`
`short` | `$T$id`, e.g. `N123456`
*custom* | A template that can use `$type`, `$id`, `$t` and `$T`

Keep in mind:

- OSM IDs are only unique within each OSM type (This means there could be a `node` and `way` that share the same ID).
- To avoid ID collisions, use a plain `$id` only if you are querying `n` *or* `w` *or* `r`.
- Areas (`a`) can consist of both `way` and `relation` features, so the OSM type must be incorporated into the ID.

### <code>-f:link=<em>&lt;URL&gt;</em></code> {#option-f-link}

URL to navigate when user clicks on a map feature (defaults to the main OSM website).

- Use the `$type` and `$id` placeholders (`$t` and `$T` for type as a single letter) ~~0.2~~

- Use `-f:link=none` to disable links

### <code>-f:max-width=<em>&lt;NUMBER&gt;</em></code> {#option-f-max-width}

The maximum width (in characters) of the displayed table (used by [`stats`](#format-stats) and [`table`](#format-table)). Default: 100.

### <code>-f:min-tally=<em>&lt;NUMBER&gt;</em>|<em>&lt;PERCENTAGE&gt;</em></code> {#option-f-min-tally}

Instructs [`-f=stats`](#format-stats) to omit tag permutations for which the tally (number of features, length or area) is less than the specified number (or less than the specified percentage of the total tally).

### <code>-f:osm=<em>&lt;OPTIONS&gt;</em></code> {#option-f-osm}

Options for [OSM-XML](#format-xml) output.

### <code>-f:sort=<em>&lt;KEYS&gt;</em>|tags|tally</code> {#option-f-sort}

`keys`, `tally`

### <code>-f:split-values</code> {#option-f-split-values}

Instructs [`-f=stats`](#format-stats) to split up values with semicolons and tally them individually. For example, `cuisine=japanese;sushi;seafood` would generate three separate permutations for the `cuisine` tag. 


### <code>-f:tally=<em>&lt;OPTION&gt;</em></code> {#option-f-tally}

What [`-f=stats`](#format-stats) should calculate:

`area` | the total area of all features in each group
`count` | the number of features in each group (*default*)
`keys` | the keys used by the selected features, as well as their most common values 
`length` | the total length of all features in each group
`roles` | the roles of the relations in each group (total number of members for each role, and count of relations in which the role is used)
`tags` | the tags used by the selected features

### <code>-f:unit=<em>&lt;OPTION&gt;</em></code> {#option-f-unit}

The length/area unit to use for [`-f=stats`](#format-stats):

`m` | (square) meters (*default*)
`km` | (square) kilometers
`ft` | (square) feet
`yd` | (square) yards
`ha` | hectares
`ac` | acres



## Solutions to Common Problems

Be aware that `>` and `|` have special meanings for the shell (re-directing/piping of the
output stream), so if your query contains these characters, you will need to enclose it in  quotes.

This won't work:

    gol query germany w[highway][maxspeed>100]  

Instead, write:

    gol query germany "w[highway][maxspeed>100]"

To write the output of your query to a file:

    gol query germany "w[highway][maxspeed>100]" -f:csv > fast-roads.csv

