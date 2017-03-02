Docker
======

Instalacja
----------

- `macOS <https://docs.docker.com/docker-for-mac/install/>`_
- `Ubuntu <https://docs.docker.com/engine/getstarted/linux_install_help/>`_
- `Linux <https://docs.docker.com/engine/installation/>`_
- `Windows <https://docs.docker.com/docker-for-windows/>`_

CLI - Command Line Interface
----------------------------

Pierwsze polecenia
^^^^^^^^^^^^^^^^^^

.. code-block:: sh

    docker run hello-world
    docker run -it ubuntu bash

Przydatne polecenia
^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

    docker run bash
    docker ps -a
    docker exec -u 0 -it CONTAINER_NAME bash
    docker images
    docker rm IMAGE


Building Images
---------------

.. code-block:: sh

    docker build -t docker .

Container linking
-----------------
Containers can be linked to another container’s ports directly using ``-link remote_name:local_alias`` in the client’s docker run. This will set a number of environment variables that can then be used to connect:

.. code-block:: sh

    docker run --rm -t -i --link pg_test:pg eg_postgresql bash

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
.. code-block:: sh

    docker run -v <host path>:<container path>[:FLAG]

.. code-block:: sh


    docker run --detach -P --name web -v /developer/myproject:/var/www training/webapp python app.py
    docker run --detach -P --name web -v /developer/myproject:/var/www:ro training/webapp python app.py

Tworznie volumenów
^^^^^^^^^^^^^^^^^^
.. code-block:: sh

    docker volume create -d flocker --opt o=size=20GB my-named-volume
    docker run --detach -P -v my-named-volume:/webapp --name web training/webapp python app.py

Mounting files
^^^^^^^^^^^^^^
.. code-block:: sh

    docker run --rm -it -v ~/.bash_history:/root/.bash_history ubuntu /bin/bash

Volume container
^^^^^^^^^^^^^^^^
.. code-block:: sh

    docker create -v /dbdata --name dbstore training/postgres /bin/true
    docker run --detach --volumes-from dbstore --name db1 training/postgres

Docker Hub
----------
- https://hub.docker.com/

.. code-block:: sh

    docker run docker/whalesay cowsay boo

Publikowanie
^^^^^^^^^^^^

.. code-block:: sh

   docker login
   docker tag 7d9495d03763 yourusername/docker-whale:latest
   docker push yourusername/docker-whale

.. code-block:: sh

    docker image remove 7d9495d03763
    docker run yourusername/docker-whale

Dockerfile
^^^^^^^^^^
- https://docs.docker.com/engine/reference/builder/

.. code-block:: dockerfile

    FROM docker/whalesay:latest
    RUN apt-get -y update && apt-get install -y fortunes
    CMD /usr/games/fortune -a | cowsay

.. code-block:: sh

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


.. code-block:: sh

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

.. code-block:: sh

    docker-compose up
    docker-machine ip MACHINE_NAME

Zadania do rozwiązania
----------------------

Ehlo World
^^^^^^^^^^
- Zainstaluj `Docker`
- Czym różni się `Docker` od `Vagrant`?
- Wyświetl `Ehlo World!` z wnętrza kontenera `Docker`
- Wyświetl listę działających kontenerów `Docker`

.. toggle-code-block:: rst
    :label: Pokaż rozwiązanie

    $ apt-get install docker.io

    - `Vagrant` virtualizes Operating System, `Docker` run inside containers on host machine
    - `Docker` uses `Linux` kernel to run and cannot be used on either `Windows` or `OS X`
    - However there's a way to run a virtual machine with `Linux` on `Docker` containers on it (this is how ``boot2docker`` works)

    $ docker run echo 'Ehlo World!'
    $ docker ps

Create container and run
^^^^^^^^^^^^^^^^^^^^^^^^
- Ściągnij repozytorium https://github.com/spring-guides/gs-spring-boot-docker.git
- Zbuduj projekt za pomocą `gradle`
- Uruchom aplikację wykorzystując `Docker`
- Użyj pliku `Dockerfile` do opisu środowiska kontenera

.. toggle-code-block:: sh
    :label: Pokaż rozwiązanie

    git clone https://github.com/spring-guides/gs-spring-boot-docker.git
    cd gs-spring-boot-docker
    gradle build

Dockerfile
^^^^^^^^^^
- Stwórz kontener dla `PostgreSQL`

.. toggle-code-block:: dockerfile
    :label: Pokaż przykładowy ``Dockerfile``

    #
    # example Dockerfile for https://docs.docker.com/examples/postgresql_service/
    #

    FROM ubuntu
    MAINTAINER SvenDowideit@docker.com

    # Add the PostgreSQL PGP key to verify their Debian packages.
    # It should be the same key as https://www.postgresql.org/media/keys/ACCC4CF8.asc
    RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

    # Add PostgreSQL's repository. It contains the most recent stable release
    #     of PostgreSQL, ``9.3``.
    RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list

    # Install ``python-software-properties``, ``software-properties-common`` and PostgreSQL 9.3
    #  There are some warnings (in red) that show up during the build. You can hide
    #  them by prefixing each apt-get statement with DEBIAN_FRONTEND=noninteractive
    RUN apt-get update && apt-get install -y python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3

    # Note: The official Debian and Ubuntu images automatically ``apt-get clean``
    # after each ``apt-get``

    # Run the rest of the commands as the ``postgres`` user created by the ``postgres-9.3`` package when it was ``apt-get installed``
    USER postgres

    # Create a PostgreSQL role named ``docker`` with ``docker`` as the password and
    # then create a database `docker` owned by the ``docker`` role.
    # Note: here we use ``&&\`` to run commands one after the other - the ``\``
    #       allows the RUN command to span multiple lines.
    RUN    /etc/init.d/postgresql start &&\
        psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
        createdb -O docker docker

    # Adjust PostgreSQL configuration so that remote connections to the
    # database are possible.
    RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf

    # And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``
    RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

    # Expose the PostgreSQL port
    EXPOSE 5432

    # Add VOLUMEs to allow backup of config, logs and databases
    VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

    # Set the default command to run when starting the container
    CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]


Docker Compose
^^^^^^^^^^^^^^
- Ściągnij repozytorium https://github.com/spring-guides/gs-spring-boot-docker.git
- Zbuduj projekt za pomocą `gradle`
- Uruchom aplikację wykorzystując `Docker`
- Użyj pliku `docker-compose.yaml` do opisu środowiska kontenera

.. toggle-code-block:: sh
    :label: Pokaż rozwiązanie

    git clone https://github.com/spring-guides/gs-spring-boot-docker.git
    cd gs-spring-boot-docker
    gradle build

