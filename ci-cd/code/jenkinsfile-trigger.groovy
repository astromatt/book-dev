pipeline {
    agent any

    triggers {
        cron('@daily')
    }

    stages {
        stage("name") {

        }
    }
}