---
layout: default
title:  Query Language
next:   utility-classes.md
redirect_from: 
  - /java/goql
  - /python/goql
nav_order: 4
---

# Geo-Object Query Language (GOQL)

<img class="float" src="/img/query-type-tags.png" width=320>

**GOQL** is a concise syntax for describing queries in terms of **feature type** and **tags**. It is similar to [MapCSS](https://wiki.openstreetmap.org/wiki/MapCSS/0.2), which in turn is modeled after the original CSS (the *Cascading Style Sheets* used with HTML).

A **query** is composed of one or more **selectors**, which work like their CSS counterparts --- but instead of elements and their attributes, they filter features based on their type and tags.

Type must be one or more of the following:

<table>
<tr>
  <td markdown="1">
`n`
  </td>
  <td markdown="1">
**Nodes**
  </td>
</tr>
<tr>
  <td markdown="1">
`w`
  </td>
  <td markdown="1">
**Ways** *(except areas)*
  </td>
</tr>
<tr>
  <td markdown="1">
`a`
  </td>
  <td markdown="1">
**Areas** *(can be ways or relations)*
  </td>
</tr>
<tr>
  <td markdown="1">
`r`
  </td>
  <td markdown="1">
**Relations** *(except areas)*
  </td>
</tr>
<!--
<tr>
  <td markdown="1">
`w+`
  </td>
  <td markdown="1">
Ways (including areas)
  </td>
</tr>
<tr>
  <td markdown="1">
`r+`
  </td>
  <td markdown="1">
Relations (including areas)
  </td>
</tr>
-->
<tr>
  <td markdown="1">
`*`
  </td>
  <td markdown="1">
Any type
  </td>
</tr>
</table>

Type identifiers can be combined. For example, `na` selects both nodes and areas --- this is the most common combo, as points-of-interest in OSM are often represented as points or polygons.

To select all element types, use the wildcard `*`.

To further constrain features, add one or more **tag clauses**, which function like CSS attribute selectors:

```css
na[amenity=restaurant]
```

The above selects all nodes and areas that have an `amenity` tag whose value is `restaurant`. If multiple tag clauses are specified, the feature must fulfill *all* of
them. For example, this query finds all sushi restaurants that offer takeaway and have a website:

```css
na[amenity=restaurant][cusine=sushi][takeaway][website]
```

Tag clauses may appear in any order.

A **unary tag clause** tests for presence of a tag (whose value must not be `no`). Prepend it with `!` to negate it. For example, to find residential streets that are *not* one-way:

```css
w[highway=residential][!oneway]
```

**Strings** that contain characters other than letters, numbers or underscores must be quoted (matching single or double quotes):

```css
na[amenity=pub][name="The King's Head"]
```

For **partial string matches**, use the wildcard `*`:

```css
na[name=The*]       /* "The Best", "Theater"       */
na[name="The *"]    /* "The Best"                  */
na[name=*land]      /* "bland", "New Zealand"      */
na[name=*eat*]      /* "eatery", "Beat", "Theater" */
```

String matching is always **case-sensitive**.

For more sophisticated string matching, use **regular expressions** (using the operator `~` or `!~`):

```css
na[name~".[Ee]at."]      
```

TODO: more RegEx examples


A query can contain **multiple selectors**, separated by commas:

```css
na[amenity=restaurant], na[amenity=pub], na[amenity=cafe]
```

The above can be simplified by specifying **multiple values** in a single tag clause:

```css
na[amenity=restaurant,pub,cafe]
```


## Quick Reference

<table>
<tr>
  <td markdown="1">
`w[highway]`
  </td>
  <td markdown="1">
Linear ways that have a `highway` tag (*except* `highway=no`)
  </td>
</tr>
<tr>
  <td markdown="1">
`w[highway][!oneway]`
  </td>
  <td markdown="1">
Highways that are *not* one-way
  </td>
</tr>
<tr>
  <td markdown="1">
`w[highway][highway!=motorway,primary]`
  </td>
  <td markdown="1">
Highways *except* motorways and primary roads
  </td>
</tr>
<tr>
  <td markdown="1">
`*[!name]`
  </td>
<td markdown="1">
Any feature without a `name` tag
  </td>
</tr>
<tr>
  <td markdown="1">
`r[route][ref][network]`
  </td>
<td markdown="1">
Non-area relations with `route`, `ref` and `network` tags (whose values must not
be `no`)
  </td>
</tr>
<tr>
  <td markdown="1">
`na[amenity=bar,pub,fast_food]`
  </td>
<td markdown="1">
Nodes and areas that are bars, pubs or fast-food restaurants
  </td>
</tr>
<tr>
  <td markdown="1">
`a[leisure=pitch][sport!=soccer]`
  </td>
<td markdown="1">
Sports pitches that aren't soccer fields
  </td>
</tr>
<tr>
  <td markdown="1">
`na[amenity=pub][name="*King*"]`
  </td>
<td markdown="1">
Pubs with `King` in their name (simple string match)
  </td>
</tr>
<tr>
  <td markdown="1">
`na[amenity=pub][name=~".[Kk]ing."]`
  </td>
<td markdown="1">
Regular expression that selects pubs named `The King's Head` as well as `The Barking Dog`
  </td>
</tr>
<tr>
  <td markdown="1">
`na[place=city][population>=1000000]`
  </td>
<td markdown="1">
Cities whose population is at least one million
  </td>
</tr>

</table>

## How to Use GOQL Queries

On the command line (using the [GOL Tool](/gol/query)):

```bash
$ gol query france na[tourism=hotel] 
```

In [Java](/java/queries#filtering-by-type-and-tags):

```java
for(Feature hotel : france.select("na[tourism=hotel]"))
    ...
```

In [Python](/python/Features#by-type-and-tags):

```python
for hotel in france("na[tourism=hotel]"):
    ...
```

In [C++](cpp/queries#by-type-and-tags):

```java
for(Feature hotel : france("na[tourism=hotel]"))
    ...
```
