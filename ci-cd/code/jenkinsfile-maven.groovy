pipeline {
    agent any

    stages {
        stage("simple") {
            steps {

                // withMaven will discover the generated Maven artifacts, JUnit Surefire & FailSafe & FindBugs reports...
                withMaven(
                    // Maven installation declared in the Jenkins "Global Tool Configuration"
                    maven: 'mvn_3.0.4',

                    // Maven settings and global settings can also be defined in Jenkins Global Tools Configuration
                    mavenSettingsConfig: 'my-maven-settings',
                 ) {

                      // Run the maven build with previously declared context
                      sh "mvn clean install"

                 }
            }
        }
    }
}

