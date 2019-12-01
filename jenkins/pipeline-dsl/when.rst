****
When
****


Branch
======
* ``branch()``
* Execute the stage when the branch being built matches the branch pattern given
* Note that this only works on a multibranch Pipelnes

.. code-block:: groovy
    :emphasize-lines: 2

    when {
        branch 'master'
    }


Environment
===========
* ``environment()``
* Execute the stage when the specified environment variable is set to the given value

.. code-block:: groovy
    :emphasize-lines: 2

    when {
        environment(name: 'DEPLOY_TO', value: 'production')
    }


Expression
==========
* ``expression()``
* Execute the stage when the specified Groovy expression evaluates to true

.. code-block:: groovy
    :emphasize-lines: 2

    when {
        expression { return params.DEBUG_BUILD }
    }


Not
===
* ``not()``
* Execute the stage when the nested condition is false. Must contain one condition

.. code-block:: groovy
    :emphasize-lines: 2

    when {
        not { branch 'master' }
    }


All of...
=========
* ``allOf()``
* Execute the stage when all of the nested conditions are true. Must contain at least one condition

.. code-block:: groovy
    :emphasize-lines: 2

    when {
        allOf {
            branch 'master'
            environment(name: 'DEPLOY_TO', value: 'production')
        }
    }


Any of...
=========
* ``anyOf()``
* Execute the stage when at least one of the nested conditions is true. Must contain at least one condition

.. code-block:: groovy
    :emphasize-lines: 2

    when {
        anyOf {
            branch 'master'
            branch 'staging'
        }
    }


Examples
========

Example 1
---------
.. code-block:: groovy
    :emphasize-lines: 6-9

    pipeline {
        agent any

        stages {
            stage('Test') {
                when {
                    sh '/bin/echo Should I test?'
                    return true
                }

                steps {
                    sh '/bin/echo Testing...'
                }
            }
    }

Example 2
---------
.. code-block:: groovy
    :emphasize-lines: 6-15

    pipeline {
        agent any

        stages {
            stage('Deploy') {
                when {
                    expression {
                        BRANCH_NAME ==~ /(production|staging)/
                    }

                    anyOf {
                        environment name: 'DEPLOY_TO', value: 'production'
                        environment name: 'DEPLOY_TO', value: 'staging'
                    }
                }

                steps {
                    sh '/bin/echo Deploying...'
                }
            }
        }
    }

