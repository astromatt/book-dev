****
Test
****

.. code-block:: groovy
    :caption: Test

    pipeline {
        agent any

        stages {
            stage('Test') {
                steps {
                    // `make check` returns non-zero on test failures,
                    // using `true` to allow the Pipeline to continue nonetheless

                    sh '/usr/bin/make check || true'
                    junit '**/target/*.xml'
                }
            }
        }
    }
