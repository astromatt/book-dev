***
Run
***


Basic usage
===========
* Check ``hostname``
* Check ``PS1`` (bash prompt)
* Will pull automatically
* Will close immediately after executing command

.. code-block:: console

    $ docker run bash

.. code-block:: console

    $ docker run bash echo 'hello'
    hello


Interactive mode
================
* ``-t``, ``--tty`` - Allocate a pseudo-TTY
* ``-i``, ``--interactive`` - Keep STDIN open even if not attached
* ``-it`` - implies both ``-i`` and ``-t``
* ``ctrl + p + q`` - quit container without stopping it
* ``ctrl + d`` - exits and stops the container

.. code-block:: console

    $ docker run -it bash

.. code-block:: console

    $ docker run -it alpine sh


Detach and attach
=================

Detach
------
* ``-d``, ``--detach`` - Run container in background and print container ID

.. code-block:: console

    $ docker run -d -it alpine sh
    b7583714a497ac10fcfa2f514025dc271a9e0d4540684f26f115d5a98b2f87b7

    $ docker run --detach -it alpine sh
    09f99d54cba4162ebea238766d366fe09ad831ca9cc844c1b54f3151dd8aec3b

Attach
------
* Attach to local standard input, output, and error streams of main process
* ``ctrl + p + q`` - quit container without stopping it

.. code-block:: console

    $ docker attach CONTAINER_NAME_OR_ID


Show containers
===============

Show running
------------
.. code-block:: console

    $ docker ps
    CONTAINER ID        IMAGE     COMMAND      CREATED              STATUS              PORTS   NAMES
    09f99d54cba4        alpine    "sh"         About a minute ago   Up About a minute           serene_kare
    b7583714a497        alpine    "sh"         About a minute ago   Up About a minute           cocky_curie

Show all containers
-------------------
* even not running

.. code-block:: console

    $ docker ps -a
    CONTAINER ID        IMAGE     COMMAND      CREATED              STATUS              PORTS   NAMES
    09f99d54cba4        alpine    "sh"         About a minute ago   Up About a minute           serene_kare
    b7583714a497        alpine    "sh"         About a minute ago   Up About a minute           cocky_curie


Name
====
* ``--name`` - Assign a name to the container

.. code-block:: console

    $ docker run -d --name sleeper alpine sleep 50
    b9e2e75cb7727cc43c6daff677b69d2fcae9077717c069190ab7bb3329339c4a

    $ docker ps
    CONTAINER ID        IMAGE     COMMAND      CREATED              STATUS              PORTS   NAMES
    b9e2e75cb772        alpine    "sleep 50"   5 seconds ago        Up 4 seconds                sleeper
    09f99d54cba4        alpine    "sh"         About a minute ago   Up About a minute           serene_kare
    b7583714a497        alpine    "sh"         About a minute ago   Up About a minute           cocky_curie


Environmental variables
=======================

Env
---
* ``-e``, ``--env`` - Set environment variables

.. code-block:: console

    $ docker run -e MY_NAME='Jan Twardowski' alpine env
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    HOSTNAME=f5f93be44865
    MY_NAME=Jan Twardowski
    HOME=/root

.. code-block:: console

    $ docker run -e MY_FIRST_NAME='Jan' -e MY_LAST_NAME='Twardowski' alpine env
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    HOSTNAME=0c9bf0f8ae0e
    MY_FIRST_NAME=Jan
    MY_LAST_NAME=Twardowski
    HOME=/root

Env-file
--------
* ``--env-file`` - Read in a file of environment variables
* ``.env`` name convention
* Add ``.env`` to ``.gitignore``
* ``.env-sample`` in your repository

.. code-block:: text
    :caption: Contents of ``.env`` file

    DATABASE_ENGINE=sqlite3
    DATABASE_HOST=localhost
    DATABASE_PORT=1337
    DATABASE_NAME=/tmp/db.sqlite3
    DATABASE_USER=root
    DATABASE_PASSWORD=mypassword

.. code-block:: console

    $ docker run --env-file=.env alpine env
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    HOSTNAME=bb04daae4875
    HOME=/root
    DATABASE_ENGINE=sqlite3
    DATABASE_HOST=localhost
    DATABASE_PORT=1337
    DATABASE_NAME=/tmp/db.sqlite3
    DATABASE_USER=root
    DATABASE_PASSWORD=mypassword


Expose ports
============
* ``-p``, ``--publish`` - Publish a container's port(s) to the host
* ``-P``, ``--publish-all`` - Publish all exposed ports to random ports

.. code-block:: console

    $ docker run -p 5432:5432 postgres
    $ docker run -p 192.168.56.101:5432:5432 postgres


Limiting resources
==================
* https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details


Assignments
===========

Env
---
#. Stwórz plik ``test.env`` oraz ``prod.env``
#. Zapisz dwie różne konfiguracje bazy danych do obu plików
#. Uruchom kontener z parametrami testowymi
#. Uruchom kontener z parametrami produkcyjnymi

Ehlo World
----------
#. Wyświetl ``Ehlo World!`` z wnętrza kontenera ``alpine``
#. Wyświetl listę działających i zakończonych kontenerów
