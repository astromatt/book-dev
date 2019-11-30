********
Triggers
********


Webhook
=======
* Webhook trigger for GitScm polling


Cron
====
* ``cron()``
* Accepts a cron-style string to define a regular interval at which the Pipeline should be re-triggered

.. code-block:: groovy
    :emphasize-lines: 2

    triggers {
        cron('H */4 * * 1-5')
    }


Poll SCM
========
* ``pollSCM()``
* Build periodically
* Accepts a cron-style string to define a regular interval at which Jenkins should check for new source changes
* If new changes exist, the Pipeline will be re-triggered
* Available since Jenkins 2.22

.. code-block:: groovy
    :emphasize-lines: 2

    triggers {
        pollSCM('H */4 * * 1-5')
    }


Upstream
========
* Build after other projects are built
* ``upstream()``
* Accepts a comma separated string of jobs and a threshold
* When any job in the string finishes with the minimum threshold, the Pipeline will be re-triggered.

.. code-block:: groovy
    :emphasize-lines: 2,3

    triggers {
        upstream(upstreamProjects: 'job1,job2',
                 threshold: hudson.model.Result.SUCCESS)
    }


REST API
========
* Trigger builds remotely (e.g., from scripts via REST API)
* https://wiki.jenkins.io/display/JENKINS/Remote+access+API

.. code-block:: console
    :caption: build trigger via Jenkins API

    curl -X POST http://localhost:8080/job/JOB_NAME/build \
    --user USER:TOKEN \
    --data-urlencode json='{
        "parameter": [
            {"name":"id", "value":"123"},
            {"name":"verbosity", "value":"high"}
        ]}'


Example
=======
.. code-block:: groovy
    :caption: Example Trigger
    :emphasize-lines: 4,5,6

    pipeline {
        agent any

        triggers {
            cron('@daily')
        }

        stages {
            stage("Test") {
                steps {
                    sh 'echo "Testing..."'
                }
            }
        }
    }
