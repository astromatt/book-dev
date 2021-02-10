************
Pipeline DSL
************


Jenkinsfile
===========
* Pipeline model definition
* Add ``Jenkinsfile`` to the repository main folder
* Bundled with Blue Ocean
* ``declarative-linter`` validate before running job
* The first line of a Jenkinsfile should be #!/usr/bin/env groovy
* Automatically create Pipelines for all Branches and Pull Requests
* Code review/iteration on the Pipeline
* Audit trail for the Pipeline
* Single source of truth for the Pipeline, which can be viewed and edited by multiple members of the project.
* https://jenkins.io/solutions/pipeline/

Documentation
=============
* https://jenkins.io/doc/book/pipeline/jenkinsfile/
* https://jenkins.io/doc/pipeline/steps/
* https://jenkins.io/doc/tutorials/building-a-multibranch-pipeline-project/
* http://localhost:8100/pipeline-syntax/
* http://localhost:8100/pipeline-syntax/globals#currentBuild
* http://localhost:8100/pipeline-syntax/globals#env


Examples
========

Single Stage
------------
.. code-block:: groovy
    :caption: Simple

    pipeline {
        agent any

        stages {
            stage('My Stage Name') {
                steps {
                    sh '/bin/echo Working...'
                }
            }
        }
    }

Multi Stage
-----------
.. code-block:: groovy
    :caption: Example

    pipeline {
        agent any

        stages {
            stage('Build') {
                steps {
                    sh '/bin/echo Building...'
                }
            }

            stage('Test') {
                steps {
                    sh '/bin/echo Testing...'
                }
            }

            stage('Deploy') {
                steps {
                    sh '/bin/echo Deploying...'
                }
            }
        }
    }


Further Reading
===============
* https://oss.cloudogu.com/jenkins/pipeline-syntax/html
