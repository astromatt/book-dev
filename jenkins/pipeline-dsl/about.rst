************
Pipeline DSL
************



.. figure:: img/ecosystem-jenkins-pipeline.png
    :scale: 50%
    :align: center

    Pipeline model definition plugin


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


Example
=======
.. literalinclude:: code/jenkinsfile-simple.groovy
    :language: groovy
    :caption: Simple


Documentation
=============
* https://jenkins.io/doc/book/pipeline/jenkinsfile/
* https://jenkins.io/doc/pipeline/steps/
* https://jenkins.io/doc/tutorials/building-a-multibranch-pipeline-project/
* http://localhost:8100/pipeline-syntax/
* http://localhost:8100/pipeline-syntax/globals#currentBuild
* http://localhost:8100/pipeline-syntax/globals#env
