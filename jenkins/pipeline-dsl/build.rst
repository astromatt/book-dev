*****
Build
*****


Example
=======
.. code-block:: groovy
    :caption: Build

    pipeline {
        agent any

        stages {
            stage('Build') {
                steps {
                    sh '/usr/bin/make'
                    archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
                }
            }
        }
    }
