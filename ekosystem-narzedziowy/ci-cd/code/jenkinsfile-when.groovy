pipeline {
    agent any
    stages {

        stage('Example Build') {
            when {
                echo 'Should I run?'
                return true
            }

            steps {
                echo 'Hello World'
            }
        }

        stage('Example Deploy') {
            when {
                expression { BRANCH_NAME ==~ /(production|staging)/ }

                anyOf {
                    environment name: 'DEPLOY_TO', value: 'production'
                    environment name: 'DEPLOY_TO', value: 'staging'
                }
            }

            steps {
                echo 'Deploying'
            }
        }
    }
}