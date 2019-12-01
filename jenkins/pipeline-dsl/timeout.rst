*******
Timeout
*******

.. code-block:: groovy
    :caption: Timeout

    pipeline {
        agent any
        stages {
            stage('Deploy') {
                steps {
                    retry(3) {
                        sh 'bin/long-script.sh'
                    }

                    timeout(time: 3, unit: 'MINUTES') {
                        sh 'bin/health-check.sh'
                    }
                }
            }
        }
    }
