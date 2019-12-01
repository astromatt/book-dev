*****
Input
*****

.. code-block:: groovy
    :caption: Input

    pipeline {
        agent {
            docker {
                image 'node:6-alpine'
                args '-p 3000:3000 -p 5000:5000'
            }
        }
        environment {
            CI = 'true'
        }
        stages {
            stage('Build') {
                steps {
                    sh '/usr/bin/npm install'
                }
            }
            stage('Test') {
                steps {
                    sh 'bin/test.sh'
                }
            }
            stage('Deliver for development') {
                when {
                    branch 'development'
                }
                steps {
                    sh 'bin/deliver-for-development.sh'
                    input message: 'Finished using the web site? (Click "Proceed" to continue)'
                    sh 'bin/kill.sh'
                }
            }
            stage('Deploy for production') {
                when {
                    branch 'production'
                }
                steps {
                    sh 'bin/deploy-for-production.sh'
                    input message: 'Finished using the web site? (Click "Proceed" to continue)'
                    sh 'bin/kill.sh'
                }
            }
        }
    }
