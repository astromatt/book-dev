Docker
======

Zadania do rozwiązania
----------------------

Ehlo World
^^^^^^^^^^
- Zainstaluj `Docker`
- Czym różni się `Docker` od `Vagrant`?
- Czy Docker może być na `Windows`?
- Czy Docker może być na `OS X`?
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

