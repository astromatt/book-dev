pipeline {
    agent any

    stages {
        stage("simple") {
            steps {

                // withMaven will discover the generated Maven artifacts, JUnit Surefire & FailSafe & FindBugs reports...
                // Maven installation declared in the Jenkins "Global Tool Configuration"
                withMaven(maven: 'mvn_3.0.4') {
                      sh "mvn clean install"
                 }
            }
        }
    }
}

