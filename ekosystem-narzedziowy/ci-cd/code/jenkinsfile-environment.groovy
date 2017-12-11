pipeline {
    agent any

    stages {
        stage('Example') {
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
    }
}


// Environment variables can be overriden and declared locally
pipeline {
    agent any

    environment {
        FOO = "BAZ"
        AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
    }

    stages {
        stage("baz") {
            steps {
                sh 'echo "FOO is $FOO"'
            }
        }

        stage("bar") {
            environment {
                FOO = "BAR"
            }

            steps {
                sh 'echo "FOO is $FOO"'
            }
        }
    }
}
