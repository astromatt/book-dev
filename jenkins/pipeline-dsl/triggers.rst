********
Triggers
********

Recap
-----
* Crontab syntax
* https://dev.astrotech.io/linux/system/crontab.html

.. code-block:: text

    SHELL=/bin/sh
    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

    # Example of job definition:
    # .---------------- minute (0 - 59)
    # |  .------------- hour (0 - 23)
    # |  |  .---------- day of month (1 - 31)
    # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
    # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
    # |  |  |  |  |
    # *  *  *  *  * user-name command to be executed
    17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
    25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
    47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
    52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )



Webhook
=======
* Webhook trigger for GitScm polling
* ``<jenkins-url>/git/notifyCommit?url=<clone-url>``

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
                    sh '/bin/echo Testing...'
                }
            }
        }
    }


Assignments
===========

API Trigger
-----------
#. Napisz skrypt ``sh`` wykorzystujący ``curl``
#. Skrypt po odpaleniu ma triggerować build
#. Dodaj skrypt do ``crontab``
#. Skrypt ma się uruchamiać ``@daily``
#. Zwróć uwagę, że ``cron`` ma mniejszą ilość zmiennych środowiskowych (skrypt, który u Ciebie działa, może nie być odpalany przez ``cron``)
