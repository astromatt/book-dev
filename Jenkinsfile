pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Windows') {
          steps {
            sh 'echo \'test\''
            timestamps()
          }
        }
        stage('Linux') {
          steps {
            sh 'echo \'asd\''
          }
        }
      }
    }
    stage('Achive') {
      steps {
        echo 'lllsdasd'
      }
    }
  }
}