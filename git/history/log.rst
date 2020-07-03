*******
Git Log
*******


Limiting output
===============
.. code-block:: console

    $ git log -1
    commit 8192e9663597d1a58bb89d09b882372763395175 (HEAD -> master, origin/master, origin/HEAD)
    Author: Matt Harasymczuk <book@astronaut.center>
    Date:   Fri Nov 22 13:33:39 2019 +0100

        DevOps: CI/CD #time 15m

.. code-block:: console

    $ git log --oneline
    8192e96 (HEAD -> master, origin/master, origin/HEAD) DevOps: CI/CD #time 15m
    dafb424 DevOps: CI/CD #time 15m
    ad7a58c DevOps: Docker #time 25m
    f9e70b6 DevOps: Summary and Ecosystem big picture #time 5m
    0adfae7 DevOps: Summary and Ecosystem big picture #time 180m
    947e4ca DevOps: Docker #time 20m
    370a4fa DevOps: Docker #time 10m
    262c3e8 DevOps: Git Flow #time 10m
    38a5c0d DevOps: Process #time 120m
    [...]

.. code-block:: console

    $ git log -n 5 --oneline
    8192e96 (HEAD -> master, origin/master, origin/HEAD) DevOps: CI/CD #time 15m
    dafb424 DevOps: CI/CD #time 15m
    ad7a58c DevOps: Docker #time 25m
    f9e70b6 DevOps: Summary and Ecosystem big picture #time 5m
    0adfae7 DevOps: Summary and Ecosystem big picture #time 180m


Graph
=====
.. code-block:: console

    $ git log --graph
    $ git log -15 --oneline --graph


Format
======
* ``%ae`` - author email
* ``%ad`` - author date
* ``%an`` - author name
* ``%ce`` - committer email
* ``%cd`` - committer date
* ``%cn`` - committer name
* ``%h`` - short hash (8 chars)
* ``%H`` - long hash (40 chars)
* ``%s`` - subject

.. code-block:: console

    $ git log -n5 --format='%h %ae %s'
    8192e96 book@astronaut.center DevOps: CI/CD #time 15m
    dafb424 book@astronaut.center DevOps: CI/CD #time 15m
    ad7a58c book@astronaut.center DevOps: Docker #time 25m
    f9e70b6 book@astronaut.center DevOps: Summary and Ecosystem big picture #time 5m
    0adfae7 book@astronaut.center DevOps: Summary and Ecosystem big picture #time 180m

.. code-block:: console

    $ $ git log -n5 --format='%ad' --date=iso
    2019-11-22 13:33:39 +0100
    2019-11-22 13:19:58 +0100
    2019-11-22 13:16:13 +0100
    2019-11-19 19:53:48 +0100
    2019-11-19 19:48:46 +0100

.. code-block:: console

    $ git log -n5 --format='%ad' --date=relative
    5 days ago
    5 days ago
    5 days ago
    8 days ago
    8 days ago

.. code-block:: console

    $ git log -n10 --format='"%h", "%an", "%ad", "%s"' --date=iso
    "8192e96", "Matt Harasymczuk", "2019-11-22 13:33:39 +0100", "DevOps: CI/CD #time 15m"
    "dafb424", "Matt Harasymczuk", "2019-11-22 13:19:58 +0100", "DevOps: CI/CD #time 15m"
    "ad7a58c", "Matt Harasymczuk", "2019-11-22 13:16:13 +0100", "DevOps: Docker #time 25m"
    "f9e70b6", "Matt Harasymczuk", "2019-11-19 19:53:48 +0100", "DevOps: Summary and Ecosystem big picture #time 5m"
    "0adfae7", "Matt Harasymczuk", "2019-11-19 19:48:46 +0100", "DevOps: Summary and Ecosystem big picture #time 180m"
    "947e4ca", "Matt Harasymczuk", "2019-11-19 13:26:36 +0100", "DevOps: Docker #time 20m"
    "370a4fa", "Matt Harasymczuk", "2019-11-19 12:20:41 +0100", "DevOps: Docker #time 10m"
    "262c3e8", "Matt Harasymczuk", "2019-10-28 08:42:20 +0100", "DevOps: Git Flow #time 10m"
    "38a5c0d", "Matt Harasymczuk", "2019-10-28 08:32:32 +0100", "DevOps: Process #time 120m"
    "ff12d83", "Matt Harasymczuk", "2019-10-15 21:12:53 +0200", "Versioning: GIT #time 3m"

.. code-block:: console

    $ git log --format='"%H", "%an", "%ae", "%ad", "%s"' --date=iso > ~/Desktop/git-log.csv

.. code-block:: console

    $ git log --format='%an' |sort |uniq
    Cosaquee
    Jan Folfas
    Karol Kozakowski
    Matt Harasymczuk
    Przemysław Pytlak
    wasikuss


File Log
========
.. code-block:: console

    $ git log -n5 --oneline README.rst
    8b3440a (HEAD -> master) Change Readme file
    d84da13 Book: Refactor #time 79m
    19cc5df Book: Theme #time 30m
    d84ac63 Book: README #time 5m
    e5c6727 Book: README #time 5m
