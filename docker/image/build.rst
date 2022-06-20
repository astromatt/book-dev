Docker Build
============


Build images
------------
.. code-block:: console

    $ docker build . -t IMAGE_NAME

.. code-block:: console

    $ docker build . -t myimg
    Sending build context to Docker daemon  2.048kB
    Step 1/3 : FROM alpine:latest
     ---> 961769676411
    Step 2/3 : RUN apk add bash
     ---> Running in 5148740edf53
    fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/main/x86_64/APKINDEX.tar.gz
    fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/community/x86_64/APKINDEX.tar.gz
    (1/5) Installing ncurses-terminfo-base (6.1_p20190518-r0)
    (2/5) Installing ncurses-terminfo (6.1_p20190518-r0)
    (3/5) Installing ncurses-libs (6.1_p20190518-r0)
    (4/5) Installing readline (8.0.0-r0)
    (5/5) Installing bash (5.0.0-r0)
    Executing bash-5.0.0-r0.post-install
    Executing busybox-1.30.1-r2.trigger
    OK: 15 MiB in 19 packages
    Removing intermediate container 5148740edf53
     ---> 99ec117fc810
    Step 3/3 : CMD /bin/bash
     ---> Running in 6a1b630dbfae
    Removing intermediate container 6a1b630dbfae
     ---> ce299736b126
    Successfully built ce299736b126
    Successfully tagged myimg:latest

.. code-block:: console

    $ docker build . -t myimg:1.0.0
    Sending build context to Docker daemon  2.048kB
    Step 1/3 : FROM alpine:latest
     ---> 961769676411
    Step 2/3 : RUN apk add bash
     ---> Running in 5148740edf53
    fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/main/x86_64/APKINDEX.tar.gz
    fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/community/x86_64/APKINDEX.tar.gz
    (1/5) Installing ncurses-terminfo-base (6.1_p20190518-r0)
    (2/5) Installing ncurses-terminfo (6.1_p20190518-r0)
    (3/5) Installing ncurses-libs (6.1_p20190518-r0)
    (4/5) Installing readline (8.0.0-r0)
    (5/5) Installing bash (5.0.0-r0)
    Executing bash-5.0.0-r0.post-install
    Executing busybox-1.30.1-r2.trigger
    OK: 15 MiB in 19 packages
    Removing intermediate container 5148740edf53
     ---> 99ec117fc810
    Step 3/3 : CMD /bin/bash
     ---> Running in 6a1b630dbfae
    Removing intermediate container 6a1b630dbfae
     ---> ce299736b126
    Successfully built ce299736b126
    Successfully tagged myimg:1.0.0

.. code-block:: console

    $ docker build . -t myimg
    Sending build context to Docker daemon  2.048kB
    Step 1/3 : FROM alpine:latest
     ---> 961769676411
    Step 2/3 : RUN apk add bash
     ---> Running in 5148740edf53
    fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/main/x86_64/APKINDEX.tar.gz
    fetch http://dl-cdn.alpinelinux.org/alpine/v3.10/community/x86_64/APKINDEX.tar.gz
    (1/5) Installing ncurses-terminfo-base (6.1_p20190518-r0)
    (2/5) Installing ncurses-terminfo (6.1_p20190518-r0)
    (3/5) Installing ncurses-libs (6.1_p20190518-r0)
    (4/5) Installing readline (8.0.0-r0)
    (5/5) Installing bash (5.0.0-r0)
    Executing bash-5.0.0-r0.post-install
    Executing busybox-1.30.1-r2.trigger
    OK: 15 MiB in 19 packages
    Removing intermediate container 5148740edf53
     ---> 99ec117fc810
    Step 3/3 : CMD /bin/bash
     ---> Running in 6a1b630dbfae
    Removing intermediate container 6a1b630dbfae
     ---> ce299736b126
    Successfully built ce299736b126
    Successfully tagged myimg:latest


List images
-----------
.. code-block:: console

    $ docker images


Remove images
-------------
.. code-block:: console

    $ docker rmi IMAGE_NAME_OR_ID


Build Workflow
--------------
#. Write ``Dockerfile``

    .. code-block:: dockerfile

        FROM alpine:latest
        RUN apk add bash
        CMD /bin/bash

#. Build image

    .. code-block:: console

        $ docker build . -t myimg

#. Run image

    .. code-block:: console

        $ docker run -it myimg

#. List images

    .. code-block:: console

        $ docker images



Docker Hub
==========
* https://hub.docker.com/

#. Build

    .. code-block:: console

        $ docker build . -t myimg:1.0.0

#. Tag

    .. code-block:: console

        $ docker tag myimg:1.0.0 myusername/myimg:latest

#. Publish

    .. code-block:: console

        $ docker login
        $ docker push myusername/myimg:latest

#. Clean local build

    .. code-block:: console

        $ docker image remove myimg:1.0.0

#. Run from Hub

    .. code-block:: console

        $ docker run myusername/myimg


Use Cases
=========
* https://github.com/docker-library/python
* https://github.com/docker-library/gcc


Assignments
===========

Create container and run
------------------------
#. Ściągnij repozytorium:

    * Szkolenie z Python: https://github.com/AstroTech/ecosystem-example-python
    * Szkolenie z C: https://github.com/AstroTech/ecosystem-example-c
    * Szkolenie z JAVA: https://github.com/AstroTech/ecosystem-example-java

#. Zbuduj projekt / lub uruchom testy
#. Przygotuj obraz oraz uruchom aplikację wykorzystując ``Docker``
#. Użyj pliku ``Dockerfile`` do opisu środowiska kontenera
