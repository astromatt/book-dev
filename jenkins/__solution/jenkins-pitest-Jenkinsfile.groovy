pipeline {
    agent any

    stages {
        stage("Mutatory Testing") {
            steps {
                sh "mvn org.pitest:pitest-maven:mutationCoverage"
            }
        }
    }
}
