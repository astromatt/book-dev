************************
Ecosystem Docker Compose
************************


Ecosystem
=========
.. code-block:: yaml
    :caption: ``ecosystem.yaml``

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

    $ docker-compose -f ecosystem.yaml up -d


Jenkins
=======
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
        restart: always
        ports:
          - "8100:8080"
        networks:
          - ecosystem
        volumes:
          - /home/jenkins:/var/jenkins_home/

.. code-block:: console

    $ docker-compose -f jenkins.yaml up


SonarQube
=========
.. code-block:: yaml
    :caption: ``sonarqube.yaml``

    version: '3'

    networks:
      ecosystem:
        driver: bridge

    services:
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

.. code-block:: console

    $ docker-compose -f sonarqube.yaml up


GitLab
======
.. code-block:: yaml
    :caption: ``gitlab.yaml``

    version: '3'

    networks:
      ecosystem:
        driver: bridge

    services:
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

    $ docker-compose -f gitlab.yaml up


Artifactory
===========
.. code-block:: yaml
    :caption: ``artifactory.yaml``

    version: '3'

    networks:
      ecosystem:
        driver: bridge

    services:
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

.. code-block:: console

    $ docker-compose -f artifactory.yaml up
