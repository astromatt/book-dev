Linux Distributions
===================


Alpine
------
* Advantage: Very small, lots of up-to-date packages
* Size: 5.52 MB
* Release: every 6 months
* Support: for 2 years
* Latest: Edge
* `Docker image <https://hub.docker.com/_/alpine?tab=tags&page=1&ordering=last_updated>`_

.. code-block:: console

    $ docker pull alpine

.. csv-table:: Alpine Versions
    :header-rows: 1

    "Version",  "Release date", "End of support"
    "edge",     "",             ""
    "v3.16",    "2022-05-23",   "2024-05-23"
    "v3.15",    "2021-11-24",   "2023-11-01"
    "v3.14",    "2021-06-15",   "2023-05-01"
    "v3.13",    "2021-01-14",   "2022-11-01"
    "v3.12",    "2020-05-29",   "2022-05-01"
    "v3.11",    "2019-12-29",   "2021-11-01"
    "v3.10",    "2019-06-19",   "2021-05-01"
    "v3.9",     "2019-01-29",   "2020-11-01"
    "v3.8",     "2018-06-26",   "2020-05-01"
    "v3.7",     "2017-11-30",   "2019-11-01"
    "v3.6",     "2017-05-24",   "2019-05-01"
    "v3.5",     "2016-12-22",   "2018-11-01"
    "v3.4",     "2016-05-31",   "2018-05-01"
    "v3.3",     "2015-12-18",   "2017-11-01"
    "v3.2",     "2015-05-26",   "2017-05-01"
    "v3.1",     "2014-12-10",   "2016-11-01"
    "v3.0",     "2014-06-04",   "2016-05-01"
    "v2.7",     "2013-11-08",   "2015-11-01"
    "v2.6",     "2013-05-17",   "2015-05-01"
    "v2.5",     "2012-11-07",   "2014-11-01"
    "v2.4",     "2012-05-02",   "2014-05-01"
    "v2.3",     "2011-11-01",   "2013-11-01"
    "v2.2",     "2011-05-06",   "2013-05-01"
    "v2.1",     "2010-11-01",   "2012-11-01"


Debian
------
* Advantage: stability, very strict rules about free software licenses, no proprietary licences
* Size: 124 MB
* Release: every 2 years
* Support: for 10 years (extended)
* Latest: Sid (unstable)
* `Docker image <https://hub.docker.com/_/debian?tab=tags&page=1&ordering=last_updated>`_
* `Debian version names are from Toy Story <https://www.debian.org/doc/manuals/debian-faq/ch-ftparchives#s-sourceforcodenames>`_
* `Release table <https://en.wikipedia.org/wiki/Debian_version_history#Release_table>`_
* `Release timeline <https://en.wikipedia.org/wiki/Debian_version_history#Release_timeline>`_

.. code-block:: console

    $ docker pull debian

.. csv-table:: Debian Versions
    :header-rows: 1

    "Version", "Code name", "Release date", "End of life", "Toy Story character"
    "",        "Sid",       "unstable",     "",            "The next door neighbour"
    "11",      "Bullseye",  "2021-08-14",   "",            "Woody's horse"
    "10",      "Buster",    "2019-07-06",   "~2022-08",    "Andy's pet dog"
    "9",       "Stretch",   "2017-06-17",   "2027-06-30",  "Rubber octopus from Toy Story 3"
    "8",       "Jessie",    "2015-04-26",   "2025-06-30",  "Jessie the cowgirl"
    "7",       "Wheezy",    "2013-05-04",   "2020-06-30",  "Wheezy the penguin"
    "6.0",     "Squeeze",   "2011-02-06",   "2016-02-29",  "Squeeze toy aliens"
    "5.0",     "Lenny",     "2009-02-14",   "2012-02-06",  "Lenny, the binoculars"
    "4.0",     "Etch",      "2007-04-08",   "2010-02-15",  "Etch, the Etch-A-Sketch"
    "3.1",     "Sarge",     "2005-06-06",   "2008-03-31",  "Sarge from the Bucket O' Soldiers"
    "3.0",     "Woody",     "2002-07-19",   "2006-06-30",  "Woody the cowboy"
    "2.2",     "Potato",    "2000-08-15",   "2003-06-30",  "Mr Potato Head"
    "2.1",     "Slink",     "1999-03-09",   "2000-10-30",  "Slinky Dog"
    "2.0",     "Hamm",      "1998-07-24",   "",            "Hamm (the pig)"
    "1.3",     "Bo",        "1997-06-05",   "",            "Bo Peep"
    "1.2",     "Rex",       "1996-12-12",   "",            "Rex (the T-Rex)"
    "1.1",     "Buzz",      "1996-06-17",   "",            "Buzz Lightyear"


Ubuntu
------
* Advantage: Based on Debian, lots of up-to-date packages, liberal rules about licenses
* Size: 77.8 MB
* Release: every 6 months (in April and October), LTS every 2 years (in April)
* Support: 10 years (extended)
* Ubuntu version numbers are ``YY.MM`` for example 22.04 (released in April 2022)
* `Docker image <https://hub.docker.com/_/ubuntu?tab=tags&page=1&ordering=last_updated>`_
* `Release cycle <https://ubuntu.com/about/release-cycle>`_
* `Version names <https://wiki.ubuntu.com/DevelopmentCodeNames>`_

.. code-block:: console

    $ docker pull ubuntu:22.04
    $ docker pull ubuntu:latest
    $ docker pull ubuntu          # will pull latest

.. csv-table:: Ubuntu Versions
    :header-rows: 1

    "Version",   "Code name",         "Release date", "End of support"
    "22.10",     "Kinetic Kudu",      "2022-10-20",   "TBA", "N/A"
    "22.04 LTS", "Jammy Jellyfish",   "2022-04-21",   "2032-04-21"
    "21.10",     "Impish Indri",      "2021-10-14",   "2022-07-14"
    "21.04",     "Hirsute Hippo",     "2021-04-22",   "2022-01-20"
    "20.10",     "Groovy Gorilla",    "2020-10-22",   "2021-07-22"
    "20.04 LTS", "Focal Fossa",       "2020-04-23",   "2030-04-23"
    "19.10",     "Eoan Ermine",       "2019-10-17",   "2020-07-17"
    "19.04",     "Disco Dingo",       "2019-04-18",   "2020-01-23"
    "18.10",     "Cosmic Cuttlefish", "2018-10-18",   "2019-07-18"
    "18.04 LTS", "Bionic Beaver",     "2018-04-26",   "2028-04-26"
    "17.10",     "Artful Aardvark",   "2017-10-19",   "2018-07-19"
    "17.04",     "Zesty Zapus",       "2017-04-13",   "2018-01-13"
    "16.10",     "Yakkety Yak",       "2016-10-13",   "2017-07-20"
    "16.04 LTS", "Xenial Xerus",      "2016-04-21",   "2026-04-23"
    "15.10",     "Wily Werewolf",     "2015-10-22",   "2016-07-28"
    "15.04",     "Vivid Vervet",      "2015-04-23",   "2016-02-04"
    "14.10",     "Utopic Unicorn",    "2014-10-23",   "2015-07-23"
    "14.04 LTS", "Trusty Tahr",       "2014-04-17",   "2024-04-25"
    "13.10",     "Saucy Salamander",  "2013-10-17",   "2014-07-17"
    "13.04",     "Raring Ringtail",   "2013-04-25",   "2014-01-27"
    "12.10",     "Quantal Quetzal",   "2012-10-18",   "2014-05-16"
    "12.04 LTS", "Precise Pangolin",  "2012-04-26",   "2019-04-26"
    "11.10",     "Oneiric Ocelot",    "2011-10-13",   "2013-05-09"
    "11.04",     "Natty Narwhal",     "2011-04-28",   "2012-10-28"
    "10.10",     "Maverick Meerkat",  "2010-10-10",   "2012-04-10"
    "10.04 LTS", "Lucid Lynx",        "2010-04-29",   "2015-04-30"
    "9.10",      "Karmic Koala",      "2009-10-29",   "2011-04-30"
    "9.04",      "Jaunty Jackalope",  "2009-04-23",   "2010-10-23"
    "8.10",      "Intrepid Ibex",     "2008-10-30",   "2010-04-30"
    "8.04 LTS",  "Hardy Heron",       "2008-04-24",   "2013-05-09"
    "7.10",      "Gutsy Gibbon",      "2007-10-18",   "2009-04-18"
    "7.04",      "Feisty Fawn",       "2007-04-19",   "2008-10-19"
    "6.10",      "Edgy Eft",          "2006-10-26",   "2008-04-25"
    "6.06 LTS",  "Dapper Drake",      "2006-06-01",   "2011-06-01"
    "5.10",      "Breezy Badger",     "2005-10-13",   "2007-04-13"
    "5.04",      "Hoary Hedgehog",    "2005-04-08",   "2006-10-31"
    "4.10",      "Warty Warthog",     "2004-10-20",   "2006-04-30"

.. figure:: ../_img/release-ubuntu.png
    :scale: 35%
    :align: center

    `Long term support and interim releases <https://ubuntu.com/about/release-cycle>`_


Ubuntu Core
-----------
* Advantage: Ubuntu Core is a minimalistic version of Ubuntu, designed for IoT devices
* Size: 431 MB
* Release: every 2 years
* Support: 10 years (extended)
* https://cdimage.ubuntu.com/ubuntu-core/24/stable/
* https://ubuntu.com/core
