Search Functions
================



Rationale
---------
* `AFTER "date"`
* `BEFORE "date"`
* `BY "username"`
* `DURING ("date1", "date2")`
* `ON "date"`
* `FROM "oldvalue"`
* `TO "newvalue"`


Was
---
.. code-block:: sql

    project = "MYPROJECT"
        AND status WAS "Done"
        AND status != "Done"

.. code-block:: sql

    project = "MYPROJECT"
        AND status WAS "Done"
        AND status != "Done"
        AND updated > -1d

.. code-block:: sql

    status WAS IN ("Done", "Rejected")

.. code-block:: sql

    status WAS NOT "In Progress" BEFORE "2000-01-01"

.. code-block:: sql

    status WAS NOT IN ("Done", "Rejected") BEFORE "2000-01-01"

.. code-block:: sql

    status WAS "Resolved" BY "admin" BEFORE "2000-01-01"

.. code-block:: sql

    status WAS "Resolved" BY "admin" DURING ("2000-01-01", "2000-01-31")


Changed
-------
.. code-block:: sql

    status CHANGED BY currentUser()

.. code-block:: sql

    assignee CHANGED

.. code-block:: sql

    priority CHANGED BY "admin"

.. code-block:: sql

    priority CHANGED BY "admin" AFTER startOfWeek()

.. code-block:: sql

    priority CHANGED BY "admin" AFTER startOfWeek() BEFORE endOfWeek()

.. code-block:: sql

    priority CHANGED BY "admin" DURING ("2000-01-01", "2000-01-31")

.. code-block:: sql

    status CHANGED
        FROM "In Progress"
        TO "Open"

.. code-block:: sql

    status CHANGED
        FROM "In Progress"
        TO "Open"
        BY "admin"

.. code-block:: sql

    status CHANGED
        FROM "In Progress"
        TO "Open"
        BY "admin"
        DURING ("2000-01-01", "2000-01-31")

.. code-block:: sql

    status CHANGED
        FROM "In Progress"
        TO "Open"
        BY "admin"
        AFTER startOfWeek()
        BEFORE endOfWeek()

.. code-block:: sql

    status CHANGED
        FROM "In Progress"
        TO "Open"
        BY membersOf("jira-administrators")
        AFTER startOfWeek()
        BEFORE endOfWeek()


Demonstration
-------------
* History searches
