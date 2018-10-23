Docker
======

Installing
----------
- `macOS <https://docs.docker.com/docker-for-mac/install/>`_
- `Ubuntu <https://docs.docker.com/engine/getstarted/linux_install_help/>`_
- `Linux <https://docs.docker.com/engine/installation/>`_
- `Windows <https://docs.docker.com/docker-for-windows/>`_

Install from terminal
^^^^^^^^^^^^^^^^^^^^^
* https://get.docker.com

.. code-block:: console

    curl -fsSL get.docker.com -o get-docker.sh
    sh get-docker.sh

Nomenclature
------------
* Container
* Image
* Layer
* LTS version
* Edge version
* Host


CLI - Command Line Interface
----------------------------

Docker Management commands
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

      checkpoint  Manage checkpoints
      config      Manage Docker configs
      container   Manage containers
      image       Manage images
      network     Manage networks
      node        Manage Swarm nodes
      plugin      Manage plugins
      secret      Manage Docker secrets
      service     Manage services
      stack       Manage Docker stacks
      swarm       Manage Swarm
      system      Manage Docker
      trust       Manage trust on Docker images
      volume      Manage volumes

Docker commands
^^^^^^^^^^^^^^^
.. code-block:: text

      attach      Attach local standard input, output, and error streams to a running container
      build       Build an image from a Dockerfile
      commit      Create a new image from a container's changes
      cp          Copy files/folders between a container and the local filesystem
      create      Create a new container
      deploy      Deploy a new stack or update an existing stack
      diff        Inspect changes to files or directories on a container's filesystem
      events      Get real time events from the server
      exec        Run a command in a running container
      export      Export a container's filesystem as a tar archive
      history     Show the history of an image
      images      List images
      import      Import the contents from a tarball to create a filesystem image
      info        Display system-wide information
      inspect     Return low-level information on Docker objects
      kill        Kill one or more running containers
      load        Load an image from a tar archive or STDIN
      login       Log in to a Docker registry
      logout      Log out from a Docker registry
      logs        Fetch the logs of a container
      pause       Pause all processes within one or more containers
      port        List port mappings or a specific mapping for the container
      ps          List containers
      pull        Pull an image or a repository from a registry
      push        Push an image or a repository to a registry
      rename      Rename a container
      restart     Restart one or more containers
      rm          Remove one or more containers
      rmi         Remove one or more images
      run         Run a command in a new container
      save        Save one or more images to a tar archive (streamed to STDOUT by default)
      search      Search the Docker Hub for images
      start       Start one or more stopped containers
      stats       Display a live stream of container(s) resource usage statistics
      stop        Stop one or more running containers
      tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
      top         Display the running processes of a container
      unpause     Unpause all processes within one or more containers
      update      Update configuration of one or more containers
      version     Show the Docker version information
      wait        Block until one or more containers stop, then print their exit codes

Run containers
^^^^^^^^^^^^^^
.. code-block:: console

    docker run bash

* ``-t`` - run pseudo terminal and attach to it
* ``-i`` - interactive, keeps stdin open

.. code-block:: console

    docker run -it bash

* ``ctrl + p + q`` - quit container without stopping it
* ``ctld + d`` - exits and stops the container

.. code-block:: console

    docker run -it ubuntu:latest bash

Show containers
^^^^^^^^^^^^^^^
* show running:

    .. code-block:: console

        docker ps

* Show all containers, even not running:

    .. code-block:: console

        docker ps -a

Attach to running containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Attach to stdout of running container:

    .. code-block:: console

        docker attach CONTAINER_NAME_OR_ID

* Attach to running container and execute bash

    .. code-block:: console

        docker exec -u 0 -it CONTAINER_NAME_OR_ID bash

What application is running inside the container?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    docker top CONTAINER_NAME_OR_ID


Images
------

Build images
^^^^^^^^^^^^
.. code-block:: console

    docker build -t docker .

List images
^^^^^^^^^^^
.. code-block:: console

    docker images

Remove images
^^^^^^^^^^^^^
.. code-block:: console

    docker rmi IMAGE

Remove container
^^^^^^^^^^^^^^^^
.. code-block:: console

    docker rm IMAGE


Container linking
-----------------
Containers can be linked to another container’s ports directly using ``-link remote_name:local_alias`` in the client’s docker run. This will set a number of environment variables that can then be used to connect:

.. code-block:: console

    docker run --rm -t -i --link pg_test:pg eg_postgresql bash

Hostname
--------
* ``hostname`` to docker container id

Volumes
-------
A data volume is a specially-designated directory within one or more containers that bypasses the Union File System. Data volumes provide several useful features for persistent or shared data:

    - Volumes are initialized when a container is created. If the container’s base image contains data at the specified mount point, that existing data is copied into the new volume upon volume initialization. (Note that this does not apply when mounting a host directory.)
    - Data volumes can be shared and reused among containers.
    - Changes to a data volume are made directly.
    - Changes to a data volume will not be included when you update an image.
    - Data volumes persist even if the container itself is deleted.

Data volumes are designed to persist data, independent of the container’s life cycle. Docker therefore never automatically deletes volumes when you remove a container, nor will it “garbage collect” volumes that are no longer referenced by a container [Docker]_.

.. note:: You can also use the VOLUME instruction in a Dockerfile to add one or more new volumes to any container created from that image.

.. [Docker] https://docs.docker.com/engine/tutorials/dockervolumes/

Mounting directories
^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    docker run -v <host path>:<container path>[:FLAG]

.. code-block:: console


    docker run --detach -P --name web -v /developer/myproject:/var/www training/webapp python app.py
    docker run --detach -P --name web -v /developer/myproject:/var/www:ro training/webapp python app.py

Tworznie volumenów
^^^^^^^^^^^^^^^^^^
.. code-block:: console

    docker volume create -d flocker --opt o=size=20GB my-named-volume
    docker run --detach -P -v my-named-volume:/webapp --name web training/webapp python app.py

Mounting files
^^^^^^^^^^^^^^
.. code-block:: console

    docker run --rm -it -v ~/.bash_history:/root/.bash_history ubuntu /bin/bash

Volume container
^^^^^^^^^^^^^^^^
.. code-block:: console

    docker create -v /dbdata --name dbstore training/postgres /bin/true
    docker run --detach --volumes-from dbstore --name db1 training/postgres

Visualizing docker container
----------------------------
* https://portainer.io

Docker Hub
----------
- https://hub.docker.com/

.. code-block:: console

    docker run docker/whalesay cowsay boo

Publikowanie
^^^^^^^^^^^^

.. code-block:: console

   docker login
   docker tag 7d9495d03763 yourusername/docker-whale:latest
   docker push yourusername/docker-whale

.. code-block:: console

    docker image remove 7d9495d03763
    docker run yourusername/docker-whale

Searching
^^^^^^^^^
* https://hub.docker.com

.. code-block:: console

    docker search NAME

Pobieranie
^^^^^^^^^^
* Only pull, not run
.. code-block:: console

    docker pull NAME
    docker pull ubuntu  # will pull lates
    docker pull ubuntu:latest
    docker pull ubuntu:18.10

Dockerfile
^^^^^^^^^^
- https://docs.docker.com/engine/reference/builder/

.. code-block:: dockerfile

    FROM docker/whalesay:latest
    RUN apt-get -y update && apt-get install -y fortunes
    CMD /usr/games/fortune -a | cowsay

.. code-block:: console

    docker build -t docker-whale .
    docker images
    docker run docker-whale

.. code-block:: dockerfile

    FROM      ubuntu
    LABEL Description="This image is used to start the foobar executable" Vendor="ACME Products" Version="1.0"
    RUN apt-get update && apt-get install -y inotify-tools nginx apache2 openssh-server

.. code-block:: dockerfile

    FROM ubuntu
    RUN echo foo > bar

    FROM ubuntu
    RUN echo moo > oink

.. code-block:: dockerfile

    FROM debian:stable
    RUN apt-get update && apt-get install -y --force-yes apache2
    EXPOSE 80 443
    VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2"]

    # An ENTRYPOINT allows you to configure a container that will run as an executable.
    ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

Limiting resources
------------------
* https://docs.docker.com/config/containers/resource_constraints/#--memory-swap-details

Docker network
--------------
* https://docs.docker.com/network/bridge/

- ``bridge`` networks are best when you need multiple containers to communicate on the same Docker host.
- ``host`` networks are best when the network stack should not be isolated from the Docker host, but you want other aspects of the container to be isolated.
- ``overlay`` networks are best when you need containers running on different Docker hosts to communicate, or when multiple applications work together using swarm services.
- ``macvlan`` networks are best when you are migrating from a VM setup or need your containers to look like physical hosts on your network, each with a unique MAC address.
- Third-party network plugins allow you to integrate Docker with specialized network stacks.

Create network
^^^^^^^^^^^^^^
.. code-block:: console

    docker network create my-net

Delete network
^^^^^^^^^^^^^^
.. code-block:: console

    docker network rm my-net

Connect running container to network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    docker network connect my-net my-container

Docker-compose
--------------
Compose is a tool for defining and running multi-container Docker applications.

- https://docs.docker.com/compose/django/

:Dockerfile:
    .. code-block:: dockerfile

         FROM python:3.6
         ENV PYTHONUNBUFFERED 1
         RUN mkdir /code
         WORKDIR /code
         ADD requirements.txt /code/
         RUN pip install -r requirements.txt
         ADD . /code/

:docker-compose.yaml:
    .. code-block:: yaml

         version: '2'
         services:
           db:
             image: postgres
           web:
             build: .
             command: python manage.py runserver 0.0.0.0:8000
             volumes:
               - .:/code
             ports:
               - "8000:8000"
             depends_on:
               - db


.. code-block:: console

    docker-compose run web django-admin.py startproject composeexample .
    sudo chown -R $USER:$USER .

:composeexample/settings.py:
    .. code-block:: python

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'postgres',
                'USER': 'postgres',
                'HOST': 'db',
                'PORT': 5432,
            }
        }

.. code-block:: console

    docker-compose up
    docker-machine ip MACHINE_NAME

Where docker store containers
-----------------------------
* ``docker info``
* ``/var/lib/docker/containers``

Kubernetes
----------
* Kubernetes is a framework for building distributed platforms
* Master node
* Cluster
* https://www.youtube.com/watch?v=_vHTaIJm9uY&list=PLF3s2WICJlqOiymMaTLjwwHz-MSVbtJPQ

Deploying
^^^^^^^^^
* Automatic health checks
* Autohealing
* Rollback deployment

Scaling
^^^^^^^
* Services
* Load ballancing
* Same machine or different machines
* Scaling container within Service

Monitoring
^^^^^^^^^^

Zadania do rozwiązania
----------------------

Ehlo World
^^^^^^^^^^
- Zainstaluj `Docker`
- Czym różni się `Docker` od `Vagrant`?
- Wyświetl `Ehlo World!` z wnętrza kontenera `Docker`
- Wyświetl listę działających kontenerów `Docker`

Create container and run
^^^^^^^^^^^^^^^^^^^^^^^^
- Ściągnij repozytorium https://github.com/spring-guides/gs-spring-boot-docker.git
- Zbuduj projekt za pomocą `gradle`
- Uruchom aplikację wykorzystując `Docker`
- Użyj pliku `Dockerfile` do opisu środowiska kontenera

Dockerfile
^^^^^^^^^^
- Stwórz kontener dla `PostgreSQL`

Docker Compose
^^^^^^^^^^^^^^
- Ściągnij repozytorium https://github.com/spring-guides/gs-spring-boot-docker.git
- Zbuduj projekt za pomocą `gradle`
- Uruchom aplikację wykorzystując `Docker`
- Użyj pliku `docker-compose.yaml` do opisu środowiska kontenera
