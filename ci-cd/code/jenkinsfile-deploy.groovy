pipeline {
    agent any

    stages {
        stage('Deploy') {
            when { currentBuild.result == 'SUCCESS' }
            steps {
                sh 'make publish'
            }
        }
    }
}