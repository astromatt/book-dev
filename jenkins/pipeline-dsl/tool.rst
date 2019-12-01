****
Tool
****


Examples
========

Example 1
---------
.. code-block:: groovy
    :caption: Tool

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

Example 2
---------
.. code-block:: groovy
    :caption: Tool

    pipeline {
        agent any

        stages {
            stage("simple") {
                steps {

                    // withMaven will discover the generated Maven artifacts, JUnit Surefire & FailSafe & FindBugs reports...
                    // Maven installation declared in the Jenkins "Global Tool Configuration"
                    withMaven(maven: 'mvn_3.0.4') {
                          sh '/usr/bin/mvn clean install'
                     }
                }
            }
        }
    }

