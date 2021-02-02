***********
Basic Usage
***********


Search
======
* https://hub.docker.com

.. code-block:: console

    $ docker search NAME


Pulling from Docker Hub
=======================
* Only pull
* Will not run

.. code-block:: console

    $ docker pull IMAGE_NAME


Operating system images
=======================

Alpine
------
* Image size is 5.53 MB
* Edge is the newest version
* https://hub.docker.com/_/alpine?tab=tags&page=1&ordering=last_updated

.. code-block:: console

    $ docker pull alpine

Debian
------
* Image size is 114 MB
* Debian version names are from Toy Story
* Sid is always unstable
* https://www.debian.org/releases/
* Version Names - https://www.debian.org/doc/manuals/debian-faq/ch-ftparchives#s-sourceforcodenames
* Docker Hub: https://hub.docker.com/_/debian?tab=tags&page=1&ordering=last_updated
* Release Table: https://en.wikipedia.org/wiki/Debian_version_history#Release_table
* Release Timeline: https://en.wikipedia.org/wiki/Debian_version_history#Release_timeline

.. code-block:: console

    $ docker pull debian

Ubuntu
------
* Image size is 66 MB
* Ubuntu version numbers are YY.MM
* LTS or 'Long Term Support' releases are published every two years in April
* Release Cycle - https://ubuntu.com/about/release-cycle
* Version Names - https://wiki.ubuntu.com/DevelopmentCodeNames
* Docker Hub - https://hub.docker.com/_/ubuntu?tab=tags&page=1&ordering=last_updated

.. figure:: ../_img/release-ubuntu.png
    :scale: 35%
    :align: center

    `Long term support and interim releases <https://ubuntu.com/about/release-cycle>`_

.. code-block:: console

    $ docker pull ubuntu:18.04
    $ docker pull ubuntu:latest
    $ docker pull ubuntu          # will pull latest


Where docker store containers
=============================
* ``/var/lib/docker/containers``

.. code-block:: console

    $ docker info |grep 'Docker Root Dir'
    Docker Root Dir: /var/lib/docker
