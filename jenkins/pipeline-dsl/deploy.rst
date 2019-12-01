******
Deploy
******


Example
=======
.. code-block:: groovy
    :caption: Deploy

    pipeline {
        agent any

        stages {
            stage('Deploy') {
                when { currentBuild.result == 'SUCCESS' }
                steps {
                    sh '/usr/bin/make publish'
                }
            }
        }
    }
