Docker Usage
============


Search
------
* https://hub.docker.com

.. code-block:: console

    $ docker search NAME


Pulling from Docker Hub
-----------------------
* Only pull
* Will not run

.. code-block:: console

    $ docker pull IMAGE_NAME


Operating system images
-----------------------
.. code-block:: console

    $ docker images |sort
    REPOSITORY   TAG        IMAGE ID       SIZE
    alpine       3.15       0ac33e5f5afa   5.57MB
    alpine       3.16       e66264b98777   5.52MB
    alpine       latest     e66264b98777   5.52MB

    debian       bullseye   4eacea30377a   124MB
    debian       buster     354ff99d6bff   114MB
    debian       latest     4eacea30377a   124MB

    ubuntu       20.04      20fffa419e3a   72.8MB
    ubuntu       22.04      27941809078c   77.8MB
    ubuntu       latest     27941809078c   77.8MB
