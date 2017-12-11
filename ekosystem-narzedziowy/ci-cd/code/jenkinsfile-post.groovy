pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'make check'
            }
        }
    }

    post {

        // evaluated first
        always {
            echo "Done."

            // Lets assume the step was ``sh './gradlew build'``
            archive 'build/libs/**/*.jar'
            junit 'build/reports/**/*.xml'
            deleteDir() /* clean up our workspace */
        }

        sucess {
            echo "Sucess. Will now deploy."
            slackSend channel: '#ops-room',
                      color: 'good',
                      message: "The pipeline ${currentBuild.fullDisplayName} completed successfully."
        }

        failure {
            echo "Failure. Will cleanup."
            mail to: 'team@example.com',
                 subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                 body: "Something is wrong with ${env.BUILD_URL}"
        }

        unstable {
            echo 'I am unstable :/'
            hipchatSend message: "Attention @here ${env.JOB_NAME} #${env.BUILD_NUMBER} has failed.",
                        color: 'RED'
        }

        changed {
            echo 'Things were different before...'
        }
    }
}