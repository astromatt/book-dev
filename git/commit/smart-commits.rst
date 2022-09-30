*************
Smart Commits
*************

* Log in to Jira Software as a user with administrative permissions.
* Go to Administration > Applications > DVCS accounts.
* Check (or clear) the Smart Commits option for a repository.
* https://support.atlassian.com/bitbucket-cloud/docs/enable-smart-commits/
* https://confluence.atlassian.com/fisheye/using-smart-commits-960155400.html

.. code-block:: sh

    $ git commit -m "MYPROJECT-13 #comment zrobione #time 20m #done"

.. code-block:: text
    :caption: Jira

    MYPROJECT-13 #comment corrected indent issue
    MYPROJECT-13 #time 1w 2d 4h 30m Total work logged
    MYPROJECT-13 #time 360m Total work logged
    MYPROJECT-13 #close Fixed this today
    MYPROJECT-13 #start-progress Fixed this today
    MYPROJECT-13 #start-review Fixed this today
    MYPROJECT-13 #time 2d 5h #comment Task completed ahead of schedule #resolve
    MYPROJECT-13 #comment Imagine that this is a really, and I mean really, long comment #time 2d 5h
    MYPROJECT-13 MYPROJECT-69 MYPROJECT-128 #resolve
    MYPROJECT-13 MYPROJECT-69 MYPROJECT-128 #resolve #time 2d 5h #comment Task completed ahead of schedule

.. code-block:: text
    :caption: Crucible

    Fix a bug +review CR-MYPROJECT
    Fix a bug +review CR-MYPROJECT @mwatney @jtwardowski
    Implement rework on past work +review CR-MYPROJECT-128

.. todo:: Smart commits images


Log Work
========
.. code-block:: text

    #time


Comments
========
.. code-block:: text

    #comment


Jira Workflow Triggers
======================
.. code-block:: text

    #to-test
    #to-review
    #done


Code Review
===========
.. code-block:: text

    +review
