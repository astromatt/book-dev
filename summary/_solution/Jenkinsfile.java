pipeline {
  agent {
    docker {
      image 'testenv:java'
      args '-v /home/maven:/root/.m2'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'mvn compile'
      }
    }

    stage('Test') {
      parallel {
        stage('Unit Testing') {
          steps {
            sh 'mvn test'
          }
        }

        stage('Integration testing') {
          steps {
            sh 'mvn verify'
          }
        }

      }
    }

    stage('Deploy') {
      steps {
        sh 'echo "Deploying..."'
      }
    }

    stage('Smoke Test') {
      steps {
        sh 'echo "Smoke Test..."'
      }
    }

  }
}
