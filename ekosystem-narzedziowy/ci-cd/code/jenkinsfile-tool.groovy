/*
* Requirements
* Do not work with docker
* If you put invalid, it will list valid
* Automaticly installs requirements
*/

pipeline {
    agent any

    tools {
        maven "apache-maven-3.1.0"
        jdk "default"
    }

    stages {
        stage('Test') {

        }
    }
}