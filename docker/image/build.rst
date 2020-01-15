*****
Build
*****


Images
======

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
==============
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


Dockerfile
==========
* Build an image from a ``Dockerfile``
* https://docs.docker.com/engine/reference/builder/

FROM
----
* The FROM instruction initializes a new build stage and sets the Base Image for subsequent instructions.

.. code-block:: dockerfile

    FROM alpine

.. code-block:: dockerfile

    FROM ubuntu          # links to :latest
    FROM ubuntu:latest   # always current LTS
    FROM ubuntu:rolling  # released every 6 months (also LTS, if it was LTS release)
    FROM ubuntu:devel    # released every 6 months (only devel)

.. code-block:: dockerfile

    FROM python:3.7
    FROM python:latest

.. code-block:: dockerfile

    FROM gcc:8
    FROM gcc:9

.. code-block:: dockerfile

    FROM openjdk:8
    FROM openjdk:8-alpine
    FROM openjdk:12
    FROM openjdk:12-alpine


Execute shell commands
======================
* JSON array syntax

``RUN``
-------
* Will execute any commands in a new layer on top of the current image and commit the results
* The resulting committed image will be used for the next step in the Dockerfile

Example 1
^^^^^^^^^
.. code-block:: dockerfile

    FROM alpine
    RUN /bin/echo 'hello'

.. code-block:: console

    $ docker build . -t myimg
    Sending build context to Docker daemon  4.096kB
    Step 1/2 : FROM alpine
     ---> 961769676411
    Step 2/2 : RUN /bin/echo 'hello'
     ---> Running in c66d9f7f5f4d
    hello
    Removing intermediate container c66d9f7f5f4d
     ---> ea39fac384a4
    Successfully built ea39fac384a4
    Successfully tagged myimg:latest

Example 2
^^^^^^^^^
.. code-block:: dockerfile

    FROM alpine
    RUN apk add bash

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

``ENTRYPOINT``
--------------
* An ``ENTRYPOINT`` helps you to configure a container that you can run as an executable.

.. code-block:: dockerfile

    FROM alpine
    ENTRYPOINT ["/bin/ping"]

.. code-block:: console

    $ docker build . -t myimg
    Sending build context to Docker daemon  4.096kB
    Step 1/2 : FROM alpine
     ---> 961769676411
    Step 2/2 : ENTRYPOINT ["/bin/ping"]
     ---> Using cache
     ---> 2b4aa9975a77
    Successfully built 2b4aa9975a77
    Successfully tagged myimg:latest

    $ docker run -it myimg
    BusyBox v1.30.1 (2019-06-12 17:51:55 UTC) multi-call binary.

    Usage: ping [OPTIONS] HOST

    Send ICMP ECHO_REQUEST packets to network hosts

        -4,-6		Force IP or IPv6 name resolution
        -c CNT		Send only CNT pings
        -s SIZE		Send SIZE data bytes in packets (default 56)
        -i SECS		Interval
        -A		Ping as soon as reply is recevied
        -t TTL		Set TTL
        -I IFACE/IP	Source interface or IP address
        -W SEC		Seconds to wait for the first response (default 10)
                (after all -c CNT packets are sent)
        -w SEC		Seconds until ping exits (default:infinite)
                (can exit earlier with -c CNT)
        -q		Quiet, only display output at start
                and when finished
        -p HEXBYTE	Pattern to use for payload

    $ docker run -it myimg 127.0.0.1
    PING 127.0.0.1 (127.0.0.1): 56 data bytes
    64 bytes from 127.0.0.1: seq=0 ttl=64 time=0.041 ms
    64 bytes from 127.0.0.1: seq=1 ttl=64 time=0.094 ms
    64 bytes from 127.0.0.1: seq=2 ttl=64 time=0.094 ms
    ^C
    --- 127.0.0.1 ping statistics ---
    3 packets transmitted, 3 packets received, 0% packet loss
    round-trip min/avg/max = 0.041/0.076/0.094 ms

``CMD``
-------
* There can only be one ``CMD`` instruction in a Dockerfile
* If you list more than one ``CMD`` then only the last ``CMD`` will take effect
* The main purpose of a ``CMD`` is to provide defaults for an executing container

.. code-block:: dockerfile

    FROM alpine
    CMD ["/bin/ping", "127.0.0.1"]

.. code-block:: console

    $ docker build . -t myimg
    Sending build context to Docker daemon  4.096kB
    Step 1/2 : FROM alpine
     ---> 961769676411
    Step 2/2 : CMD ["/bin/ping", "127.0.0.1"]
     ---> Using cache
     ---> e4992bc1834a
    Successfully built e4992bc1834a
    Successfully tagged myimg:latest

    $ docker run myimg
    PING 127.0.0.1 (127.0.0.1): 56 data bytes
    64 bytes from 127.0.0.1: seq=0 ttl=64 time=0.060 ms
    64 bytes from 127.0.0.1: seq=1 ttl=64 time=0.067 ms
    64 bytes from 127.0.0.1: seq=2 ttl=64 time=0.124 ms
    64 bytes from 127.0.0.1: seq=3 ttl=64 time=0.060 ms
    64 bytes from 127.0.0.1: seq=4 ttl=64 time=0.065 ms
    ^C
    --- 127.0.0.1 ping statistics ---
    5 packets transmitted, 5 packets received, 0% packet loss
    round-trip min/avg/max = 0.060/0.075/0.124 ms

``CMD`` vs ``ENTRYPOINT``
-------------------------
* ``ENTRYPOINT`` will pass ``docker run IMAGE ...`` arguments to entrypoint

``USER``
--------
* Run the rest of the commands as the user

.. code-block:: dockerfile

    FROM alpine
    USER guest
    RUN /usr/bin/id

.. code-block:: console

    $ docker build . -t myimg
    Sending build context to Docker daemon  4.096kB
    Step 1/3 : FROM alpine
     ---> 961769676411
    Step 2/3 : USER guest
     ---> Running in 3861a8f7079f
    Removing intermediate container 3861a8f7079f
     ---> 89e29c8da805
    Step 3/3 : RUN /usr/bin/id
     ---> Running in c6fcf919ced7
    uid=405(guest) gid=100(users)
    Removing intermediate container c6fcf919ced7
     ---> a569f8c240ab
    Successfully built a569f8c240ab
    Successfully tagged myimg:latest

    $ docker run myimg /usr/bin/id
    uid=405(guest) gid=100(users)


Files and directories
=====================

``COPY``
--------
.. code-block:: dockerfile

    FROM alpine
    COPY requirements.txt /data/

``ADD``
-------
* ``ADD`` allows <src> to be a URL
* If the <src> parameter of ``ADD`` is an archive in a recognised compression format, it will be unpacked

.. code-block:: dockerfile

    FROM alpine
    ADD requirements.txt /data/

``COPY`` vs ``ADD``
-------------------
* Best practices for writing Dockerfile suggests using ``COPY`` where the magic of ``ADD`` is not required

``WORKDIR``
-----------
* The ``WORKDIR`` instruction sets the working directory for any ``RUN``, ``CMD``, ``ENTRYPOINT``, ``COPY`` and ``ADD`` instructions that follow it in the Dockerfile
* Default directory when running container

.. code-block:: dockerfile

    WORKDIR /data

``VOLUME``
----------
* The ``VOLUME`` instruction creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers.

.. code-block:: dockerfile

    VOLUME ["/data"]


Networking
==========

``EXPOSE``
----------
* The ``EXPOSE`` instruction does not actually publish the port
* It functions as a type of documentation between the person who builds the image and the person who runs the container, about which ports are intended to be published

.. code-block:: dockerfile

    FROM alpine
    EXPOSE 80/tcp
    EXPOSE 80/udp
    EXPOSE 443


Environmental variables
=======================

``ENV``
-------
.. code-block:: dockerfile

    ENV <key> <value>
    ENV <key>=<value> ...

.. code-block:: dockerfile

    ENV MY_NAME Jan Twardowski

.. code-block:: console

    $ docker build . -t myimg
    Sending build context to Docker daemon  4.096kB
    Step 1/2 : FROM alpine
     ---> 961769676411
    Step 2/2 : ENV MY_NAME Jan Twardowski
     ---> Running in f6a7217b8b8a
    Removing intermediate container f6a7217b8b8a
     ---> 347cd3b90f0b
    Successfully built 347cd3b90f0b
    Successfully tagged myimg:latest

    $ docker run myimg env
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    HOSTNAME=4c59a9f37394
    MY_NAME=Jan Twardowski
    HOME=/root


Examples
========

Run Django App in container
---------------------------
.. code-block:: dockerfile

    FROM python:3.7

    COPY . /data
    RUN pip install -r /data/requirements.txt
    ENV DEBUG false
    EXPOSE 8000/tcp

    WORKDIR /data
    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

Apache 2
--------
.. code-block:: dockerfile

    FROM debian:stable

    RUN apt update && apt install -y --force-yes apache2
    EXPOSE 80/tcp
    EXPOSE 443/tcp
    VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2"]

    ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

Django app
----------
.. code-block:: dockerfile

    ## Creating image based on official python image
    FROM python:3.7

    ## Sets dumping log messages directly to stream instead of buffering
    ENV PYTHONUNBUFFERED 1

    ## Install system dependencies
    RUN apt update && apt install -y nginx

    ## Change working directory
    WORKDIR /srv

    ## Creating and putting configurations
    COPY habitat /srv/habitat
    COPY manage.py /srv/
    COPY docker-entrypoint.sh /srv/docker-entrypoint.sh
    COPY requirements.txt /srv/requirements.txt
    COPY conf/nginx.conf /etc/nginx/sites-enabled/habitatOS

    ## Installing all python dependencies
    RUN echo "daemon off;" >> /etc/nginx/nginx.conf
    RUN pip install --no-cache-dir -r /srv/requirements.txt

    ## Open ports to outside world
    EXPOSE 80 80/tcp
    EXPOSE 8000 8000/tcp

    ## When container starts, this script will be executed.
    ## Note that it is NOT executed during building
    CMD sh /srv/docker-entrypoint.sh


    ## Run like that
    # docker build . -t habitatos:latest
    # docker run -d --env-file=.env --rm --name habitatOS -p 80:80 habitatos
    # docker run -d --env-file=.env --rm --name habitatOS -p 80:80 -v /Users/matt/Developer/habitatOS/habitat:/srv/habitat habitatos
    # docker exec -it habitatOS bash


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


Assignments
===========

Dockerfile
----------
#. Na bazie czystego Alpine stwórz własny kontener dla ``PostgreSQL``

Create container and run
------------------------
#. Ściągnij repozytorium:

    * Szkolenie z Python: https://github.com/AstroTech/ecosystem-example-python
    * Szkolenie z C: https://github.com/AstroTech/ecosystem-example-c
    * Szkolenie z JAVA: https://github.com/AstroTech/ecosystem-example-java

#. Zbuduj projekt / lub uruchom testy
#. Przygotuj obraz oraz uruchom aplikację wykorzystując ``Docker``
#. Użyj pliku ``Dockerfile`` do opisu środowiska kontenera
