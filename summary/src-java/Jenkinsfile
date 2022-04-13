pipeline {
  docker {
    image 'myapp:cicd'
  }

  stages {
    stage('Environment') {
      steps {
        sh 'hostname'
        sh 'id'
        sh 'ifconfig'
        sh 'ping -c1 dev.astrotech.io'
        sh 'cat /etc/os-release'
        sh 'uname -a'
        sh 'env |sort'
        sh 'java -version'
        sh 'mvn --version'
        sh 'pwd'
        sh 'echo $JAVA_HOME'
        sh 'echo $PATH'
      }
    }

    stage('Build') {
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

        stage('Integration Test') {
          steps {
            sh 'mvn verify'
          }
        }

      }
    }

    stage('Static Code Analysis') {
      steps {
        sh 'mvn compile'
        sh 'mvn test'
        sh 'mvn verify'
        sh 'mvn org.pitest:pitest-maven:mutationCoverage'
        sh 'docker run --rm --network ecosystem -v $(pwd):/usr/src sonarsource/sonar-scanner-cli'
      }
    }

    stage('Upload Artifact') {
      steps {
        sh 'docker build . -f Dockerfile.runtime -t localhost:5000/myapp:$(git log -1 --format="%h")'
        sh 'docker push localhost:5000/myapp:$(git log -1 --format="%h")'
        sh 'docker rmi localhost:5000/myapp:$(git log -1 --format="%h")'
      }
    }

  }
  environment {
    JAVA_HOME = '/usr/lib/jvm/java-1.8-openjdk/'
  }
