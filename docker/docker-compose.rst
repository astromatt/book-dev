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

        docker-compose up

#. Run in background (daemon)

    .. code-block:: console

        docker-compose up -d


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
          mynetwork:
            driver: bridge

        services:
          jenkins:
            image: jenkins/jenkins
            container_name: jenkins
            restart: "no"
            ports:
              - "8080:8080"
            networks:
              - mynetwork
            volumes:
              - /home/jenkins:/var/jenkins_home/
              - /var/run/docker.sock:/var/run/docker.sock

#. Run Jenkins in background (daemon)

    .. code-block:: console

        docker-compose up -d

``Django`` application
----------------------
.. code-block:: yaml
    :caption: ``docker-compose.yaml``

    version: '3'

    services:
      db:
        image: postgres
        ports:
          - "5432:5432"

      web:
        build: .
        command: python manage.py runserver 0.0.0.0:8000
        volumes:
          - .:/www
        ports:
          - "8000:8000"
        depends_on:
          - db

.. code-block:: console

    docker-compose up -d

.. code-block:: console

    docker swarm init
    docker stack deploy -c docker-compose.yml my-stack

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
          - "8080:8080"
        networks:
          - ecosystem
        volumes:
          - /home/jenkins:/var/jenkins_home/
        depends_on:
          - sonar
          - gitlab
          - artifactory
        environment:
          - SONAR_PORT=9000

      sonar:
        image: sonarqube
        container_name: sonarqube
        restart: always
        ports:
         - "9000:9000"
         - "9092:9092"
        networks:
          - ecosystem

      gitlab:
        image: gitlab/gitlab-ce:latest
        container_name: gitlab
        restart: always
        volumes:
          - /home/gitlab/config:/etc/gitlab
          - /home/gitlab/logs:/var/log/gitlab
          - /home/gitlab/data:/var/opt/gitlab
        ports:
         - "443:443"
         - "80:80"
         - "2222:22"
        networks:
          - ecosystem

      artifactory:
        image: docker.bintray.io/jfrog/artifactory-oss:latest
        container_name: artifactory
        restart: always
        ports:
          - "8081:8081"
        networks:
          - ecosystem

.. code-block:: console

    docker-compose up -d

Assignments
===========

Docker Compose
--------------
#. Ściągnij repozytorium https://github.com/AstroTech/ecosystem-example-java
#. Zbuduj projekt za pomocą ``mvn install``
#. Przygotuj obraz oraz uruchom aplikację wykorzystując ``Docker``
#. Użyj pliku ``docker-compose.yaml`` do opisu środowiska kontenera
