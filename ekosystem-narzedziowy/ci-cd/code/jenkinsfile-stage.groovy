/*
 * It is required whithin the ``pipeline {...}``
 * Cannot have empty ``stages {...}`` block (it has to be at least one stage
 */

pipeline {
    agent any

    stages {
        stage("build") {
            steps {
                echo "hello"
            }
        }
    }

    stages {
        stage("build") {
            steps {
                bat 'set'
            }
        }
    }

}