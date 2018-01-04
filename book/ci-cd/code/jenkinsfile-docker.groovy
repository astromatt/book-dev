// Docker container declaration
pipeline {
    agent { docker 'python:3.6.3' }

    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}

// Verbose declaration
pipeline {
    agent {
        docker {
            image 'maven:3-alpine'
            label 'my-defined-label'
            args  '-v /tmp:/tmp'
        }
    }

    stages {
        stage('build') {
            steps {
                sh 'mvn --version'
            }
        }
    }
}

// Declaring docker container per build
pipeline {
    agent none

    stages {

        stage('Example Build') {
            agent { docker 'maven:3-alpine' }
            steps {
                echo 'Hello, Maven'
                sh 'mvn --version'
            }
        }

        stage('Example Test') {
            agent { docker 'openjdk:8-jre' }
            steps {
                echo 'Hello, JDK'
                sh 'java -version'
            }
        }
    }
}