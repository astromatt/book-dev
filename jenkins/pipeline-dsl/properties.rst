**********
Properties
**********

.. code-block:: groovy
    :caption: Test

    pipeline {
        agent any

        properties {
            // how many builds to keep?
            buildDiscarder(logRotatr(numToKeepStr:'1'))
            disableConcurentBuilds()
        }

        stages {
            stage("name") {

            }
        }
    }
