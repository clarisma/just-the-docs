---
layout: default
title: query
parent: GOL Utility
nav-order: 6
has_children: true
has_toc: false
permalink: /gol/query
---

# `query`

Prints all features that match the given query to `stdout`, in a variety of formats.

Usage:

    gol query [<options>] <gol-file> <query>

The query must be written in [GOQL](../goql), the Geo-Object Query Language. GOQL is
similar to [MapCSS](https://wiki.openstreetmap.org/wiki/MapCSS/0.2), which is used 
by Mapnik and Overpass to select OSM objects.

For example:

    gol query geodata/france 
      na[amenity=fire_station], n[emergency=fire_hydrant]
      -b=2.2,48.8,2.5,48.9 -f=geojson 
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
`csv` | Comma-separated values
`geojson` / `geojsonl` | GeoJSON ([traditional](https://geojson.org) / [one feature per line](https://stevage.github.io/ndgeojson/))
`list` | Simple list of IDs (*default*)
[`map`](/gol/query/map) | [Leaflet-based map](/gol/query/map)
`poly` | [Polygon file](https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format) (areas only)
[`stats`](/gol/query/stats) | [Statistics](/gol/query/stats) based on tags and roles
`table` | Simple text-based table
`wkt` | Well-known text (geometries only)
`xml` | [OSM-XML](https://wiki.openstreetmap.org/wiki/OSM_XML)


<blockquote class="important" markdown="1">
OSM-XML output is not suitable for editing, since the IDs for untagged nodes won't
match the original OSM data (*You can open these XML files in JOSM, but please don't upload them*).
</blockquote>


### <code>-f:<em>&lt;OPTION&gt;</em></code>, <code>--format:<em>&lt;OPTION&gt;</em> = <em>&lt;VALUE&gt;</em></code>

Formatting options to customize the output. These are primarily used by [`map`](/gol/query/map) and [`stats`](/gol/query/stats). Common options are documented below:

### <code>-f:id=<em>&lt;STYLE&gt;</em></code> ~~0.2~~ {#option-f-id}

Defines the style of IDs used for `csv`, `geojson`/`geojsonl`, `list` and `table`:

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

### <code>-f:max-width=<em>&lt;NUMBER&gt;</em></code> {#option-f-max-width}

The maximum width (in characters) of the displayed table (used by [`stats`](/gol/query/stats) and `table`. Default: 100

### <code>-f:sort=<em>&lt;KEYS&gt;</em>|id</code> ~~0.2~~ {#option-f-sort}

Specifies the sort order of results. By default, results are returned in no particular order.

<blockquote class="note" markdown="1">

Sorting may substantially increase memory consumption (and decrease performance), especially for large result sets (millions of features). 

</blockquote>



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

{% comment %}

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

### `-f=poly` {#format-poly}

Outputs features in [polygon-file format](https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format). Non-polygonal features are omitted.
The resulting file can be used for the `--area` option in subsequent queries.

{% endcomment %}


## Solutions to Common Problems

Be aware that `>` and `|` have special meanings for the shell (re-directing/piping of the
output stream), so if your query contains these characters, you will need to enclose it in  quotes.

**This won't work:**

    gol query germany w[highway][maxspeed>100]  

Instead, write:

    gol query germany "w[highway][maxspeed>100]"

To write the output of your query to a file:

    gol query germany "w[highway][maxspeed>100]" -f:csv > fast-roads.csv

Also, be aware that the shell doesn't play nicely with quotation marks (which are required if literal values in the query contain spaces or punctuation).

**This won't work:**

    gol query uk na[amenity=pub][name="The Howling Hound"]

The shell "eats" the double quotes instead of passing it to the GOL utility, which then reports an error. To avoid this problem, **use single quotes**:

    gol query uk na[amenity=pub][name='The Howling Hound']

If the query string itself contains quotation characters, prefix them with a backslash (`\`):

    gol query uk na[amenity=pub][name='King\'s Crossing']

    gol query uk na[amenity=pub][name='The \"Happy\" Place']

