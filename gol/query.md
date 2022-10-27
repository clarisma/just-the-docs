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

The query must be written in [GOQL](../goql), the Geometric Object Query Language. GOQL is very
similar to [MapCSS](https://wiki.openstreetmap.org/wiki/MapCSS/0.2), which is used 
by Mapnik and Overpass to select OSM objects.

For example:

    gol query geodata/france 
      na[amenity=fire_station], n[emergency=fire_hydrant]
      -b=2.2,48.8,2.5,18.9 -f=geojson 
      -u=www.mywebsite.com/myfeatures/france -n

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

### `-f`, <code>--format=<em>&lt;TYPE&gt;</em></code>

The output format of the results:

<table>
  <tr>
    <td><code>count</code></td>
    <td markdown="span">

Prints the *number* of features instead of the features themselves. 
  
  </td>
</tr>
<tr>
    <td><code>csv</code></td>
    <td markdown="1">
Outputs features in table-based form, suitable for import into a spreadsheet 
application or an SQL database.

The first row specifies the header, the following rows each contain a single
feature. Use in conjunction with `--tags` to specify which tags
should be written. 

Columns are separated by a tab character. The first two columns are always
`t` (the OSM type of the element: `N`, `W`, or `R`) and `id` (the OSM id
of the element).

If the `--tags` option is not specified, the only other column is `tags`,
which includes all the features' tags as a comma-separated
lists of key-value pairs.

  </td>
</tr>
<tr>
    <td><code>geojson</code></td>
    <td markdown="span">

Outputs features as [GeoJSON](https://geojson.org).
 
  </td>
</tr>
<tr>
    <td><code>geojsonl</code></td>
    <td markdown="span">

Outputs features as [GeoJSONL](https://stevage.github.io/ndgeojson/) (newline-delimited GeoJSON).

  </td>
</tr>
<tr>
   <td><code>list</code></td>
    <td markdown="span">

Outputs only the IDs, prefixed by the feature's OSM type (`N`, `W` or `R`).
This is the default mode if `--format` is omitted.

  </td>
</tr>
<tr>
  <td><code>map</code></td>
  <td markdown="span">

Generates HTML for a [Leaflet](https://leafletjs.com/)-based map
that presents the query results visually. Use [`--map-url`](#option-map-url) to specify a
basemap.

  </td>
</tr>
<tr>
  <td><code>poly</code></td>
  <td markdown="span">

Outputs features in polygon-file format. Non-polygonal features are omitted.
  
  </td>
</tr>
<tr>
  <td><code>xml</code></td>
  <td markdown="span">

Outputs features in [OSM-XML](https://wiki.openstreetmap.org/wiki/OSM_XML) format.
    
`lon` and `lat` attributes are added to the `nd` elements of ways.

  </td>
</tr>
</table>

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

### `-l`, <code>--limit=<em>&lt;NUMBER&gt;</em></code>

The maximum number of features to be displayed or counted.

### <code>--map-attribution=<em>&lt;TEXT&gt;</em></code>

For `--format=map`, the attribution text to display at the bottom of the map.

<a name="option-map-url">
### <code>--map-url=<em>&lt;URL&gt;</em></code>

For `--format=map`, the URL to use for the base map.

<blockquote class="important" markdown="1">
    
If you are using map tiles provided by a third party, be sure to follow their 
tile usage policy and provide proper attribution (using `--map-attribution`)

</blockquote>

### `-t`, <code>--tags=<em>&lt;LIST&gt;</em></code>

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


The following options only apply to `--format=xml`: ~~0.2~~

- `--node-coords=ATTR`: Specifies which coordinates should be added to the `<nd>` element of ways. `lon,lat` adds longitude and latitude (in degrees) as attributes
  `lon` and `lat`. `x,y` adds the projected Mercator coordinates as attributes
  `x` and `y`.

- `--node-ids`: This option causes unique IDs to be generated for non-feature nodes.


{% include gol/option-new.md %}
{% include gol/option-output.md %}
{% include gol/option-url.md %}
{% include gol/option-wait.md %}


## Tips

Be aware that `>` and `|` have special meanings for the shell (re-directing/piping of the
output stream), so if your query contains these characters, you will need to enclose it in  quotes.

This won't work:

    gol query germany w[highway][maxspeed>100]  

Instead, write:

    gol query germany "w[highway][maxspeed>100]"

To write the output of your query to a file:

    gol query germany "w[highway][maxspeed>100]" -f:csv > fast-roads.csv

