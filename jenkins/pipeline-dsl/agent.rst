*****
Agent
*****


About
=====
* It is required whithin the ``pipeline {...}``
* At the begining of pipeline directive:

    * ``agent any``
    * ``agent none``
    * ``agent label:'some-label'``
    * ``agent docker:"python:3.6.3", dockerArgs:"-v /tmp:/tmp -p 80:80"``
    * ``agent dockerfile:true, dockerArgs:"-v /tmp:/tmp -p 80:80"``  ## ``Dockerfile`` in root of your repo
    * ``agent dockerfile:"SomeOtherDockerfile", dockerArgs:"-v /tmp:/tmp -p 80:80"``

Examples
========
.. code-block:: groovy
    :caption: Agent

    /*
     * It is required whithin the ``pipeline {...}``
     * Cannot have empty ``stages {...}`` block (it has to be at least one stage
     */

    pipeline {
        agent none

        stages {
            agent { label: 'linux' }
            stage("Build on Linux") {
                steps {
                    sh '/bin/echo Building...'
                }
            }
        }

        stages {
            agent { label: 'windows' }
            stage("Building on Windows") {
                steps {
                    bat 'echo Building...'
                }
            }
        }

    }


.. code-block:: groovy
    :caption: Agent

    pipeline {
        agent none
        stages {
            stage('Build') {
                agent any
                steps {
                    checkout scm
                    sh '/usr/bin/make'
                    stash includes: '**/target/*.jar', name: 'app'
                }
            }

            stage('Test on Linux') {
                agent {
                    label 'linux'
                }
                steps {
                    unstash 'app'
                    sh '/usr/bin/make check'
                }
                post {
                    always {
                        junit '**/target/*.xml'
                    }
                }
            }

            stage('Test on Windows') {
                agent {
                    label 'windows'
                }
                steps {
                    unstash 'app'
                    bat '/usr/bin/make check'
                }
                post {
                    always {
                        junit '**/target/*.xml'
                    }
                }
            }
        }
    }
