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


Building Images
---------------

.. code-block:: sh

    docker build -t docker .

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

.. code-block:: dockerfile

    FROM docker/whalesay:latest
    RUN apt-get -y update && apt-get install -y fortunes
    CMD /usr/games/fortune -a | cowsay

.. code-block:: sh

    docker build -t docker-whale .
    docker images
    docker run docker-whale


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

