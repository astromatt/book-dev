************
Post Actions
************


At the end of pipeline directive


Always
======
* ``always``
* Run the steps in the post section regardless of the completion status of the Pipeline’s or stage’s run.


Changed
=======
* ``changed``
* Only run the steps in post if the current Pipeline’s or stage’s run has a different completion status from its previous run.


Failure
=======
* ``failure``
* Only run the steps in post if the current Pipeline’s or stage’s run has a "failed" status, typically denoted by red in the web UI.


Success
=======
* ``success``
* Only run the steps in post if the current Pipeline’s or stage’s run has a "success" status, typically denoted by blue or green in the web UI.


Unstable
========
* ``unstable``
* Only run the steps in post if the current Pipeline’s or stage’s run has an "unstable" status, usually caused by test failures, code violations, etc. This is typically denoted by yellow in the web UI.


Aborted
=======
* ``aborted``
* Only run the steps in post if the current Pipeline’s or stage’s run has an "aborted" status, usually due to the Pipeline being manually aborted. This is typically denoted by gray in the web UI


Examples
========
.. code-block:: groovy
    :caption: Post

    pipeline {
        agent any

        stages {
            stage('Test') {
                steps {
                    sh '/usr/bin/make check'
                }
            }
        }

        post {

            // evaluated first
            always {
                sh '/bin/echo Done'

                // Lets assume the step was ``sh './gradlew build'``
                archive 'build/libs/**/*.jar'
                junit 'build/reports/**/*.xml'
                deleteDir() /* clean up our workspace */
            }

            sucess {
                sh '/bin/echo Success'
                slackSend channel: '#ops-room',
                          color: 'good',
                          message: "The pipeline ${currentBuild.fullDisplayName} completed successfully."
            }

            failure {
                sh '/bin/echo Failure'
                mail to: 'team@example.com',
                     subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                     body: "Something is wrong with ${env.BUILD_URL}"
            }

            unstable {
                sh '/bin/echo Unstable'
                hipchatSend message: "Attention @here ${env.JOB_NAME} #${env.BUILD_NUMBER} has failed.",
                            color: 'RED'
            }

            changed {
                sh '/bin/echo Status was different in previous build'
            }
        }
    }
