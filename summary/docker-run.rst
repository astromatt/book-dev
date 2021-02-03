********************
Ecosystem Docker Run
********************


.. code-block:: sh

    curl https://get.docker.com |sudo sh
    sudo usermod -aG docker ubuntu   # requires logout


Jenkins
=======
.. code-block:: sh

    docker network create ecosystem
    mkdir -p /home/jenkins
    chmod 777 /home/jenkins
    chmod 666 /var/run/docker.sock
    ln -s /home/jenkins /var/jenkins_home

    docker run \
        --name jenkins \
        --detach \
        --rm \
        --network ecosystem \
        --publish 8080:8080 \
        --volume /home/jenkins:/var/jenkins_home \
        --volume /var/run/docker.sock:/var/run/docker.sock \
        jenkins/jenkins:alpine


SonarQube
=========
.. code-block:: sh

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

.. code-block:: sh

    -e SONAR_JDBC_URL=... \
    -e SONAR_JDBC_USERNAME=... \
    -e SONAR_JDBC_PASSWORD=...

    # SONAR_JDBC_URL=jdbc:postgresql://localhost:5432/sonarqube?currentSchema=my_schema

Sonar Scanner
=============
* ``sonar-project.properties``
* Further Reading: https://dev.astrotech.io/sonarqube/sonarscanner.html
* Further Reading: https://python.astrotech.io/devsecops/ci-cd/static-analysis.html

.. code-block:: properties
    :caption: Java

    ## Sonar Server
    sonar.host.url=http://sonarqube:9000/
    sonar.login=admin
    sonar.password=admin

    ## About Project
    sonar.projectKey=myproject
    sonar.projectName=myproject
    sonar.sourceEncoding=UTF-8

    ## SonarScanner Config
    sonar.verbose=false
    sonar.log.level=INFO
    sonar.showProfiling=false
    sonar.projectBaseDir=/usr/src/
    sonar.working.directory=/tmp/

    ## Build Breaker
    sonar.buildbreaker.skip=false
    sonar.buildbreaker.queryInterval=10000
    sonar.buildbreaker.queryMaxAttempts=1000

    ## Debugging
    # sonar.verbose=true
    # sonar.log.level=DEBUG
    # sonar.showProfiling=true
    # sonar.scanner.dumpToFile=/tmp/sonar-project.properties

    ## Java
    sonar.language=java
    sonar.java.source=8
    sonar.java.binaries=target/classes
    sonar.sources=src/main/java
    sonar.exclusions=**/migrations/**

.. code-block:: properties
    :caption: Python

    ## Sonar Server
    sonar.host.url=http://sonarqube:9000/
    sonar.login=admin
    sonar.password=admin

    ## About Project
    sonar.projectKey=myproject
    sonar.projectName=myproject
    sonar.sourceEncoding=UTF-8

    ## SonarScanner Config
    sonar.verbose=false
    sonar.log.level=INFO
    sonar.showProfiling=false
    sonar.projectBaseDir=/usr/src/
    sonar.working.directory=/tmp/

    ## Build Breaker
    sonar.buildbreaker.skip=false
    sonar.buildbreaker.queryInterval=10000
    sonar.buildbreaker.queryMaxAttempts=1000

    ## Debugging
    # sonar.verbose=true
    # sonar.log.level=DEBUG
    # sonar.showProfiling=true
    # sonar.scanner.dumpToFile=/tmp/sonar-project.properties

    ## Python
    sonar.language=py
    sonar.sources=.
    sonar.inclusions=**/*.py
    sonar.exclusions=**/migrations/**,**/*.pyc,**/__pycache__/**

.. code-block:: sh

    docker run --rm --network ecosystem -v $(pwd):/usr/src sonarsource/sonar-scanner-cli


Docker Registry
===============
.. code-block:: sh

    docker network create ecosystem
    mkdir -p /home/registry
    chmod 777 /home/registry

    docker run \
        --name registry \
        --detach \
        --rm \
        --network ecosystem \
        --publish 5000:5000 \
        --volume /home/registry:/var/lib/registry \
        registry:2


Docker Registry UI
==================
* ``registry-ui.yml``

.. code-block:: yaml

    listen_addr: 0.0.0.0:8888
    base_path: /

    registry_url: http://registry:5000
    verify_tls: true

    # registry_username: user
    # registry_password: pass

    # The same one should be configured on Docker registry as Authorization Bearer token.
    event_listener_token: token
    event_retention_days: 7

    event_database_driver: sqlite3
    event_database_location: data/registry_events.db
    # event_database_driver: mysql
    # event_database_location: user:password@tcp(localhost:3306)/docker_events

    cache_refresh_interval: 10

    # If users can delete tags.
    # If set to False, then only admins listed below.
    anyone_can_delete: false

    # Users allowed to delete tags.
    # This should be sent via X-WEBAUTH-USER header from your proxy.
    admins: []

    # Debug mode. Affects only templates.
    debug: true

    # How many days to keep tags but also keep the minimal count provided no matter how old.
    purge_tags_keep_days: 90
    purge_tags_keep_count: 2

.. code-block:: console

    docker run \
        --name=registry-ui \
        --detach \
        --rm \
        --network ecosystem \
        --publish 8888:8888 \
        --volume $(pwd)/registry-ui.yml:/opt/config.yml:ro \
        quiq/docker-registry-ui


GitLab
======
.. warning:: Machine must have at least 8 GB RAM, otherwise freezes. Amazon ``t2.micro`` is not good.

.. code-block:: sh

    docker network create ecosystem
    mkdir -p /home/gitlab
    chmod 777 /home/gitlab

    docker run \
        --name gitlab \
        --detach \
        --rm \
        --network ecosystem \
        --publish 8022:22 \
        --publish 8000:80 \
        --publish 8443:443 \
        --volume /home/gitlab/config:/etc/gitlab \
        --volume /home/gitlab/logs:/var/log/gitlab \
        --volume /home/gitlab/data:/var/opt/gitlab \
        gitlab/gitlab-ce:latest


Artifactory
===========
.. code-block:: sh

    docker network create ecosystem
    mkdir -p /home/artifactory
    chmod 777 /home/artifactory

    docker run \
        --name artifactory \
        --detach \
        --rm \
        --network ecosystem \
        --publish 8081:8081 \
        --volume /home/artifactory:/var/opt/jfrog/artifactory \
        docker.bintray.io/jfrog/artifactory-oss:latest


Tests
=====
.. code-block:: sh
    :caption: ``make-artifact.sh``

    #!/bin/sh

    REGISTRY='localhost:5000'
    NAME='myapp'
    VERSION="$(git log -1 --format='%h')"

    IMAGE="$REGISTRY/$NAME:$VERSION"

    docker build . -t $IMAGE
    docker push $IMAGE
    docker rmi $IMAGE

.. code-block:: sh
    :caption: ``test-functional.sh``

    #!/bin/sh

    cd example-py-doctest/
    python3 -m doctest -v doctests/*

.. code-block:: sh
    :caption: ``test-integration.sh``

    #!/bin/sh

    pip install -r requirements.txt
    cd example-py-pytest/
    python3 -m pytest

.. code-block:: sh
    :caption: ``test-static.sh``

    #!/bin/sh

    docker run --rm --net ecosystem -v $(pwd):/usr/src sonarsource/sonar-scanner-cli

.. code-block:: sh
    :caption: ``test-unit.sh``

    #!/bin/sh

    cd example-py-unittest
    python3 -m unittest
