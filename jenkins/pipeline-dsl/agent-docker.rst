************
Agent Docker
************


Set-up Environment
==================
* https://youtu.be/TsWkZLLU-s4?t=3653

Install Docker on Jenkins container
-----------------------------------
.. code-block:: console

    $ docker exec -it -u root jenkins sh
    $ curl https://get.docker.com |sh

Jenkins and Docker Daemon
-------------------------
* Cannot run Container inside Container
* Mount ``docker.sock`` from Host to Jenkins container
* Will spawn sibling containers

.. code-block:: console

    $ chmod 777 /var/run/docker.sock
    $ docker run -v /var/run/docker.sock:/var/run/docker.sock ...


Using docker
============
.. code-block:: console

    $ docker pull openjdk:8-jdk
    $ docker pull maven:3-jdk-8
    $ docker pull golang:1.7
    $ docker pull python:3

Pipeline DSL
============
.. literalinclude:: code/jenkinsfile-docker.groovy
    :language: groovy
    :caption: Docker

Example 1
---------
// Docker container declaration
pipeline {
    agent { docker 'python:3.6.3' }

    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}

// Verbose declaration
pipeline {
    agent {
        docker {
            image 'maven:3-alpine'
            label 'my-defined-label'
            args  '-v /tmp:/tmp'
        }
    }

    stages {
        stage('build') {
            steps {
                sh 'mvn --version'
            }
        }
    }
}

// Declaring docker container per build
pipeline {
    agent none

    stages {

        stage('Example Build') {
            agent { docker 'maven:3-alpine' }
            steps {
                echo 'Hello, Maven'
                sh 'mvn --version'
            }
        }

        stage('Example Test') {
            agent { docker 'openjdk:8-jre' }
            steps {
                echo 'Hello, JDK'
                sh 'java -version'
            }
        }
    }
}
