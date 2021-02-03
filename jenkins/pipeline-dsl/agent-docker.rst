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

    $ chmod 666 /var/run/docker.sock
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

Example 1
---------
.. code-block:: groovy
    :caption: Docker container declaration
    :emphasize-lines: 2

    pipeline {
        agent { docker 'python:3.7.5' }

        stages {
            stage('build') {
                steps {
                    sh 'python --version'
                }
            }
        }
    }

Example 2
---------
.. code-block:: groovy
    :caption: Verbose declaration
    :emphasize-lines: 2-8

    pipeline {
        agent {
            docker {
                image 'maven:3-alpine'
                label 'my-defined-label'
                args  '-v /home/jenkins/.m2:/home/jenkins/.m2'
            }
        }

        stages {
            stage('Build') {
                steps {
                    sh '/bin/echo "Building..."'
                }
            }
        }
    }

Example 3
---------
.. code-block:: groovy
    :caption: Declaring docker container per build
    :emphasize-lines: 6,13

    pipeline {
        agent none

        stages {
            stage('Build') {
                agent { docker 'maven:3-alpine' }
                steps {
                    sh 'mvn --version'
                }
            }

            stage('Test') {
                agent { docker 'openjdk:8-jre' }
                steps {
                    sh 'java -version'
                }
            }
        }
    }


Assignments
===========

Jenkins Docker Plugin
---------------------
#. Skonfiguruj zadanie aby uruchamiało kontener
#. Zadanie ma provisionować konfigurację wewnątrz kontenera
#. Zadanie ma uruchamiać build wewnątrz kontenera
#. Zadanie ma niszczyć kontener po buildze
