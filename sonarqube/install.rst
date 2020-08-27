*****************
SonarQube Install
*****************


SonarQube LTS
=============
* Default evaluation username: admin
* Default evaluation password: admin

.. code-block:: sh
    :caption: SonarQube 7.9.x LTS

    curl https://get.docker.com |sudo sh
    sudo usermod -aG docker ubuntu   # requires logout

    docker network create ecosystem
    mkdir -p /home/sonarqube/
    chmod 777 /home/sonarqube

    docker run \
        --name sonarqube \
        --detach \
        --rm \
        --network ecosystem \
        --publish 9000:9000 \
        --volume /home/sonarqube/conf:/opt/sonarqube/conf \
        --volume /home/sonarqube/data:/opt/sonarqube/data \
        --volume /home/sonarqube/logs:/opt/sonarqube/logs \
        --volume /home/sonarqube/extensions:/opt/sonarqube/extensions \
        sonarqube:lts


SonarQube Latest
================
* Default evaluation username: admin
* Default evaluation password: admin

.. code-block:: sh
    :caption: SonarQube 8.2+

    curl https://get.docker.com |sudo sh
    sudo usermod -aG docker ubuntu   # requires logout

    docker network create ecosystem
    docker volume create --name sonarqube_data
    docker volume create --name sonarqube_extensions
    docker volume create --name sonarqube_logs

    docker run \
        --name sonarqube \
        --detach \
        --rm \
        --network ecosystem \
        --publish 9000:9000 \
        --volume sonarqube_data:/opt/sonarqube/data \
        --volume sonarqube_logs:/opt/sonarqube/logs \
        --volume sonarqube_extensions:/opt/sonarqube/extensions \
        sonarqube

.. note:: For SonarQube 8.2+ make sure you're using volumes as shown with the above commands, and not bind mounts. Using bind mounts prevents plugins and languages from populating correctly. https://docs.sonarqube.org/latest/setup/install-server/#header-3


Database
========
.. code-block:: sh

    SONAR_JDBC_URL=jdbc:postgresql://db:5432/sonarqube
    SONAR_JDBC_USERNAME=postgres
    SONAR_JDBC_PASSWORD=ecosystem

.. code-block:: sh

    sonar.jdbc.url=jdbc:postgresql://db:5432/sonarqube
    sonar.jdbc.username=postgres
    sonar.jdbc.password=ecosystem


Docker Compose
==============
* Default evaluation username: admin
* Default evaluation password: admin

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
          - POSTGRES_PASSWORD=ecosystem

      sonarqube:
        image: sonarqube
        container_name: sonarqube
        restart: always
        ports:
          - "9000:9000"
        networks:
          - ecosystem
        depends_on:
          - db
        volumes:
          - sonarqube_data:/opt/sonarqube/data
          - sonarqube_logs:/opt/sonarqube/logs
          - sonarqube_extensions:/opt/sonarqube/extensions
        environment:
          - sonar.jdbc.url=jdbc:postgresql://db:5432/sonarqube
          - sonar.jdbc.username=postgres
          - sonar.jdbc.password=ecosystem

.. code-block:: console

    $ docker-compose -f sonarqube.yaml up
