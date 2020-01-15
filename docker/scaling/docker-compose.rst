**************
Docker-compose
**************

* Compose is a tool for defining and running multi-container Docker applications.
* https://docs.docker.com/compose/django/


Docker-compose workflow
=======================
* File name convention ``docker-compose.yaml``
* Name can be any other, but then ``docker-compose -f FILENAME.yaml`` command

#. Create file

    .. code-block:: yaml
        :caption: ``docker-compose.yaml``

        version: '3'

        services:
          alpine:
            image: alpine
            volumes:
              - /home/alpine:/data

#. Run

    .. code-block:: console

        $ docker-compose up

#. Run in background (daemon)

    .. code-block:: console

        $ docker-compose up -d


Network
=======
.. code-block:: yaml

    version: '3'

    networks:
      mynetwork:
        driver: bridge

    services:
      host1:
        image: alpine
        networks:
          - mynetwork

      host2:
        image: alpine
        networks:
          - mynetwork

Examples
========

Jenkins
-------
#. Create file ``jenkins.yaml``

    .. code-block:: yaml
        :caption: ``jenkins.yaml``

        version: '3'

        networks:
          ecosystem:
            driver: bridge

        services:
          jenkins:
            image: jenkins/jenkins
            container_name: jenkins
            restart: "no"
            ports:
              - "8100:8080"
            networks:
              - ecosystem
            volumes:
              - /home/jenkins:/var/jenkins_home/
              - /var/run/docker.sock:/var/run/docker.sock

#. Run Jenkins in background (daemon)

    .. code-block:: console

        $ docker-compose up -d

``Django`` application
----------------------
.. code-block:: yaml
    :caption: ``docker-compose.yaml``

    version: '3'

    networks:
      mynetwork:
        driver: bridge

    services:
      db:
        image: postgres
        networks:
          - mynetwork
        ports:
          - "5432:5432"

      web:
        build: .
        command: python manage.py runserver 0.0.0.0:8000
        networks:
          - mynetwork
        volumes:
          - .:/srv
        ports:
          - "8000:8000"
        depends_on:
          - db

.. code-block:: console

    $ docker-compose up -d

.. code-block:: console

    $ docker swarm init
    $ docker stack deploy -c docker-compose.yml my-stack

CI/CD ecosystem
---------------
.. code-block:: yaml

    version: '3'

    networks:
      ecosystem:
        driver: bridge

    services:
      jenkins:
        image: jenkins/jenkins
        container_name: jenkins
        restart: always
        ports:
          - "8100:8080"
        networks:
          - ecosystem
        volumes:
          - /home/jenkins:/var/jenkins_home/
        depends_on:
          - sonarqube
          - artifactory
          - gitlab

      db:
        image: postgres
        networks:
          - ecosystem
        ports:
          - "5432:5432"
        volumes:
          - /home/postgresql:/var/lib/postgresql/data
        environment:
          - POSTGRES_USER=postgres
          - POSTGRES_PASSWORD=example

      sonarqube:
        image: sonarqube
        container_name: sonarqube
        restart: always
        ports:
          - "8200:9000"
        networks:
          - ecosystem
        depends_on:
          - db
        volumes:
          - /home/sonarqube/conf:/opt/sonarqube/conf
          - /home/sonarqube/data:/opt/sonarqube/data
          - /home/sonarqube/logs:/opt/sonarqube/logs
          - /home/sonarqube/extensions:/opt/sonarqube/extensions
        environment:
          - sonar.jdbc.url=jdbc:postgresql://db:5432/sonarqube
          - sonar.jdbc.username=sonarqube
          - sonar.jdbc.password=sonarqube

      artifactory:
        image: docker.bintray.io/jfrog/artifactory-oss:latest
        container_name: artifactory
        restart: always
        ports:
          - "8300:8081"
        networks:
          - ecosystem
        depends_on:
          - db
        volumes:
          - /home/artifactory:/var/opt/jfrog/artifactory
        environment:
          - DB_TYPE=postgresql
          - DB_HOST=db
          - DB_PORT=5432
          - DB_NAME=artifactory
          - DB_USER=artifactory
          - DB_PASSWORD=artifactory

      gitlab:
        image: gitlab/gitlab-ce:latest
        container_name: gitlab
        restart: always
        volumes:
          - /home/gitlab/config:/etc/gitlab
          - /home/gitlab/logs:/var/log/gitlab
          - /home/gitlab/data:/var/opt/gitlab
        ports:
          - "8400:80"
          - "8422:22"
          - "8443:443"
        networks:
          - ecosystem
        depends_on:
          - db
        environment:
          - DB_ADAPTER=postgresql
          - DB_HOST=db
          - DB_PORT=5432
          - DB_NAME=gitlab
          - DB_USER=gitlab
          - DB_PASS=gitlab

.. code-block:: console

    $ docker-compose up -d


Assignments
===========

Docker Compose
--------------
#. Ściągnij repozytorium https://github.com/AstroTech/ecosystem-example-java
#. Zbuduj projekt za pomocą ``mvn install``
#. Przygotuj obraz oraz uruchom aplikację wykorzystując ``Docker``
#. Użyj pliku ``docker-compose.yaml`` do opisu środowiska kontenera
