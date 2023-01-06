---
id: export-features
layout: default
title: Generate Statistics
parent: query
grand_parent: GOL Utility
nav_order: 1
---

# Generate Statistics

Use `gol query` with option `-f=stats` to generate statistics about tag usage and relation roles. Each row in the report is a permutation of the tag values (whose keys are specified by `--tags`) found among the features that the query selects. The final column contains the number of features, total length or total area, based on [`-f:tally`](#option-f-tally). For `-f:tally=roles`, only relations are analyzed, and the roles of their members are included in each permutation.

{% comment %}
- Use <code>--limit=<em>n</em></code> to only display the *n* most common permutations.
  {% endcomment %}

Formatting options:

[`-f:min-tally`](#option-f-min-tally) | Don't include rows with tally less than this number/precentage
[`-f:sort`](#option-f-sort) | Sort rows alphabetically by keys/values (instead of tally)
[`-f:split-values`](#option-f-split-values) | Treat value with semicolons as list of individual values (e.g. `japanese;sushi;seafood` would be treated as 3 distinct values)   
[`-f:tally`](#option-f-tally) | Statistics to generate: `keys` (default), `tags`, `roles`, `count`, `length` or `area`
[`-f:unit`](#option-f-unit) | Length/area unit (default: `m`)


## Examples

### Common Tags and Values

Find the most frequently-used tags (and values) for power lines in France (default `-f:tally=keys`):

```
gol query france -f=stats w[power=line] 

29,098 features                      /key  /count
=================================================
power                      29,098          100.0%
  = line                   29,098  100.0%  100.0%
voltage                    25,500           87.6%
  = 63000                   8,141   31.9%   28.0%
  = 225000                  7,410   29.1%   25.5%
  = 400000                  5,878   23.1%   20.2%
  = 90000                   3,038   11.9%   10.4%
  = 20000                     294    1.2%    1.0%
operator                   24,089           82.8%
  = RTE                    22,852   94.9%   78.5%
  = Enedis                    355    1.5%    1.2%
cables                     16,572           57.0%
  = 3                      13,707   82.7%   47.1%
  = 6                       2,167   13.1%    7.4%
  = 1                         542    3.3%    1.9%
...
-------------------------------------------------
76 keys with 5,602 values
```

Same as above, but instead organized by most common tags:

```
gol query france -f=stats w[power=line] -f:tally=tags

Key          Value             29,098  /count
=============================================
power      = *                 29,098  100.0%
power      = line              29,098  100.0%
voltage    = *                 25,500   87.6%
operator   = *                 24,089   82.8%
operator   = RTE               22,852   78.5%
cables     = *                 16,572   57.0%
cables     = 3                 13,707   47.1%
line       = *                 13,060   44.9%
line       = bay                8,912   30.6%
...
---------------------------------------------
76 keys      5,602 pairs      133,424   4.6/1
```

(`4.6/1` on the total line means that, on average, there are 4.6 tags per feature)

### Permutations of Tag Values

Discover the most common types of restaurants in Berlin:

```
gol query germany -a=berlin.poly na[amenity=restaurant] 
  -f=stats -f:tally=count -t=cuisine 

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

Count the various forms of `opening_hours` for restaurants, cafes and shops, sorted by tag values. Only include opening hours that are used at least 10 times.

```
gol query germany na[amenity=cafe,restaurant],na[shop]  
  -f=stats -f:tally=count -f:min-tally=10 -f:sort=tags
  -t=amenity,shop,opening_hours  

amenity           shop          opening_hours
==================================================================
cafe        -                   -                   15,960    2.9%
restaurant  -                   -                   57,931   10.7%
-                 bakery        -                   19,059    3.5%
-                 butcher       -                    7,332    1.4%
...
-                 supermarket   Mo-Sa 07:00-20:00    2,843    0.5%
-                 supermarket   Mo-Sa 08:00-20:00    2,804    0.5%
...
------------------------------------------------------------------
Total                                              541,833  100.0%
```

### Length and Area

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

Measure the areas of different types of land use (excluding forests and farmland):

```
gol query world a[landuse != forest,farmland] -f=stats -t=landuse -f:tally=area

landuse
----------------------------
residential   240,312,392 m2  
commercial     80,900,121 m2
...
```

### Roles

Analyze how often certain roles appear in route relations:

```
gol query world r[route] -f=stats -t=route -f:tally=roles 

route           Role         Members in Relations
=========================================================
bus             (empty)    5,052,780 in    36,352   44.8%
hiking          (empty)    1,450,043 in    33,066   12.9%
bicycle         (empty)    1,166,304 in    19,062   10.3%
bus             stop         585,931 in    33,370    5.2%
bus             platform     574,225 in    31,602    5.1%
...
---------------------------------------------------------
Total                     11,274,462 in   122,155  100.0%
```

## Formatting Options

### <code>-f:max-width=<em>&lt;NUMBER&gt;</em></code> {#option-f-max-width}

The maximum width (in characters) of the displayed table (used by [`stats`](#format-stats) and [`table`](#format-table)). Default: 100

### <code>-f:min-tally=<em>&lt;NUMBER&gt;</em>|<em>&lt;PERCENTAGE&gt;</em></code> {#option-f-min-tally}

Omits rows in the report whose subtotal (number of features, length or area) is less than the specified number (or less than the specified percentage of the total). Default: 1%

### <code>-f:sort=<em>&lt;KEYS&gt;</em>|tags|tally</code> {#option-f-sort}

Sorts rows alphabetically by key/value instead of tally.  

### <code>-f:split-values</code> {#option-f-split-values}

Splits up values that contain semicolons and tallies the items individually. For example, `cuisine=japanese;sushi;seafood` would generate three separate tallies for the `cuisine` tag.


### <code>-f:tally=<em>&lt;OPTION&gt;</em></code> {#option-f-tally}

What the report should calculate:

`area` | the total area of all features in each group
`count` | the number of features in each group (*default*)
`keys` | the keys used by the selected features, as well as their most common values
`length` | the total length of all features in each group
`roles` | the roles of the relations in each group (total number of members for each role, and count of relations in which the role is used)
`tags` | the tags used by the selected features

### <code>-f:unit=<em>&lt;OPTION&gt;</em></code> {#option-f-unit}

The length/area unit to use for `-f:tally=length` and `-f:tally=area`:

`m` | (square) meters (*default*)
`km` | (square) kilometers
`ft` | (square) feet
`yd` | (square) yards
`ha` | hectares
`ac` | acres


