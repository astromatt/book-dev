********************
Ecosystem Docker Run
********************


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
        --publish 8100:8080 \
        --volume /home/jenkins:/var/jenkins_home \
        --volume /var/run/docker.sock:/var/run/docker.sock \
        jenkins/jenkins


SonarQube
=========
.. code-block:: sh

    docker network create ecosystem
    mkdir -p /home/sonarqube/
    chmod 777 /home/sonarqube

    docker run \
        --name sonarqube \
        --detach \
        --rm \
        --network ecosystem \
        --publish 8200:9000 \
        --volume /home/sonarqube/conf:/opt/sonarqube/conf \
        --volume /home/sonarqube/data:/opt/sonarqube/data \
        --volume /home/sonarqube/logs:/opt/sonarqube/logs \
        --volume /home/sonarqube/extensions:/opt/sonarqube/extensions \
        sonarqube


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
        --publish 8300:5000 \
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
        --publish 8422:22 \
        --publish 8480:80 \
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
        --publish 8600:8081 \
        --volume /home/artifactory:/var/opt/jfrog/artifactory \
        docker.bintray.io/jfrog/artifactory-oss:latest
