/* It is required whithin the ``pipeline {...}``
 * At the begining of pipeline directive:
 * - ``agent any``
 * - ``agent none``
 * - ``agent label:'some-label'``
 * - ``agent docker:"python:3.6.3", dockerArgs:"-v /tmp:/tmp -p 80:80"``
 * - ``agent dockerfile:true, dockerArgs:"-v /tmp:/tmp -p 80:80"`` ## Dockerfile in root of your repo
 * - ``agent dockerfile:"SomeOtherDockerfile", dockerArgs:"-v /tmp:/tmp -p 80:80"``
 */

pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            steps {
                checkout scm
                sh 'make'
                stash includes: '**/target/*.jar', name: 'app'
            }
        }

        stage('Test on Linux') {
            agent {
                label 'linux'
            }
            steps {
                unstash 'app'
                sh 'make check'
            }
            post {
                always {
                    junit '**/target/*.xml'
                }
            }
        }

        stage('Test on Windows') {
            agent {
                label 'windows'
            }
            steps {
                unstash 'app'
                bat 'make check'
            }
            post {
                always {
                    junit '**/target/*.xml'
                }
            }
        }
    }
}