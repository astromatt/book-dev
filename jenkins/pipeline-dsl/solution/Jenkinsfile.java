pipeline {
  agent {
    docker {
      image 'env:java'
      args  '-v /home/jenkins/.m2:/root/.m2'
    }

  }
  stages {
    stage('Build') {
      agent any
      steps {
        sh 'mvn compile'
      }
    }

    stage('Test') {
      parallel {
        stage('Unit Test') {
          steps {
            sh 'mvn test'
          }
        }

        stage('Integration test') {
          steps {
            sh 'mvn verify'
          }
        }

        stage('Static Code Analysis') {
          agent any
          steps {
            sh 'mvn compile'
            sh 'pwd'
            sh 'docker run --rm -v /home/jenkins/workspace/java_master@2:/usr/src -e SONAR_HOST_URL=http://54.217.43.196:9000/ sonarsource/sonar-scanner-cli'
          }
        }

      }
    }

    stage('Install') {
      steps {
        sh 'mvn install'
      }
    }

    stage('Build and relese to re') {
      agent any
      steps {
        sh 'docker build . -t localhost:5000/myapp:$(git log -1 --format="%h")'
        sh 'docker push localhost:5000/myapp:$(git log -1 --format="%h")'
        sh 'docker rm localhost:5000/myapp:$(git log -1 --format="%h")'
      }
    }

  }
}
