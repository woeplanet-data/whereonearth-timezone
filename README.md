whereonearth-timezone
==

The short version
--

Where On Earth (WOE) data for timezones smushed up with Eric Muller's
`tz_world_mp` shapefile for timezones. That's fancy talk for "polygons".

The long version
--

_Forking GeoPlanet one place type a time._

This is an active but still experimental project to create a community-driven
project to maintain and update the Creative Commons licensed GeoPlanet dataset.

Rather than create a single repository with every record the plan is to create
smaller datasets organized by placetype in the hopes that they will be more
manageable to download and to update by users interested in particular place types.

Each location (timezone) is stored as a separate GeoJSON file. GeoJSON was
chosen because it has wide support in variety of GIS tools, most programming
languages (and specifically JavaScript), can be edited using any old text editor
(or Github's own "edit this page" functionality) and allows for any number of
custom key/value pairs using the GeoJSON _properties_ dictionary.

The naming convention for records is the timezone's Where On Earth (WOE) ID
followed by a ".json" extension. Records are stored in nested directories that
correspond to their WOE ID. The top level directory would be the first three
digits of a WOE ID, the second level directory would be the following three
digits (four through six) and so on until their are no more digits in the WOE
ID.

This repository includes countries from GeoPlanet (versions 7.3 through 7.6) as
compiled by [woedb](http://woe.spum.org).

A word about Github
--

In the long-run Github may not be the best venue for managing all of these
records. But it's not an entirely crazy idea either so we're going to try it for
a while because it's easy and safe.

To do
--

* Build concordances with Geonames and Wikipedia.

* Merge and update records from the GeoPlanet 7.10 release.

Other WOE repositories
--

* [whereonearth-country](https://github.com/straup/whereonearth-country)

* [whereonearth-state](https://github.com/straup/whereonearth-state)

* [whereonearth-airport](https://github.com/straup/whereonearth-airport)

* [whereonearth-building](https://github.com/straup/whereonearth-building)

See also
--

* [Eric Muller's "tz_world, an efele.net/tz map"](http://efele.net/maps/tz/world/)

* [Yahoo! GeoPlanet Data](http://developer.yahoo.com/geo/geoplanet/data/)

* [Geonames](http://www.geonames.org/)

* [Show Me the GeoJSON](http://straup.github.com/showme-the-geojson/)


