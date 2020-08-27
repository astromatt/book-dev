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
    chmod 777 /var/run/docker.sock

    docker run \
        --name jenkins \
        --detach \
        --rm \
        --network ecosystem \
        --publish 8080:8080 \
        --volume /home/jenkins:/var/jenkins_home \
        --volume /var/run/docker.sock:/var/run/docker.sock \
        jenkins/jenkins


SonarQube
=========
.. code-block:: sh
    :caption: SonarQube 7.9.x LTS

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

.. code-block:: sh
    :caption: SonarQube 8.2+

    docker network create ecosystem
    mkdir -p /home/sonarqube/
    chmod 777 /home/sonarqube

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


Sonar Scanner
=============
.. code-block:: sh

    docker pull sonarsource/sonar-scanner-cli

.. code-block:: properties
    :caption: ``sonar-project.properties``

    # sonar.host.url=http://localhost:9000

    sonar.projectKey=myproject
    sonar.projectName=myproject
    sonar.projectVersion=1.0
    sonar.projectDescription=My Description

    sonar.links.homepage=https://www.example.com/
    sonar.links.scm=https://github.com/myuser/myproject/
    sonar.links.issue=https://github.com/myuser/myproject/issues
    sonar.links.ci=https://github.com/myuser/myproject/cicd

    sonar.language=java
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true

    sonar.sources=src/main/java
    sonar.exclusions=**/migrations/**
    sonar.java.binaries=target/classes
    sonar.java.source=8

.. code-block:: sh

    export SONARQUBE_URL='http://...:9000'
    docker run --rm -e SONAR_HOST_URL="${SONARQUBE_URL}" -v /home/src-java:/usr/src sonarsource/sonar-scanner-cli


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
