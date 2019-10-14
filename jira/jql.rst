JQL - JIRA Query Language
=========================
- List View, Detail View
- Konfiguracja Kolumn wyszukiwania
- Searching Issues
- Konfiguracja Boardów
- Bulk edit
- Bulk change limit
- Limit wyświetlania wyników dla JQL
- Import / Export CSV
- ``jira.issue.editable = true`` dla statusu Done (Workflow)

.. code-block:: sql

    project = DEMO

.. code-block:: sql

    project = DEMO
        AND status = "To Do"

.. code-block:: sql

    status = "To Do" OR status = "In Progress"

    status IN ("To Do", "In Progress")

    status NOT IN ("To Do", "In Progress")

.. code-block:: sql

    project = DEMO
        AND resolution NOT IN (Fixed, "Won't Fix")

.. code-block:: sql

    statusCategory = "To Do"
    statusCategory NOT IN ("To Do", "In Progress")
    statusCategory != "Done"

.. code-block:: sql

    statusCategory NOT IN (Done, "In Progress")
        AND assignee = currentUser()

.. code-block:: sql

    statusCategory NOT IN (Done, "In Progress")
        AND assignee IN membersOf("jira-administrators")

.. code-block:: sql

    statusCategory NOT IN (Done, "In Progress")
        AND assignee = currentUser()
        ORDER BY priority DESC, key ASC

.. code-block:: sql

    project = DEMO
        AND status WAS Done
        AND status != Done

.. code-block:: sql

    project = DEMO
        AND status WAS Done
        AND status != Done
        AND updated > -1d

.. code-block:: sql

    Sprint IN closedSprints()
    Sprint IN openSprints()
    Sprint IN futureSprints()

.. code-block:: sql

    project = DEMO
        AND sprint in openSprints()
        AND status != Done
        AND updated > -1d

.. code-block:: sql

    Flagged IS NOT EMPTY

.. code-block:: sql

    project = DEMO
        AND sprint IN openSprints()
        AND (statusCategory = "In Progress" OR Flagged is not EMPTY)

        -- opcjonalnie, ze względu na omawianie Waiting i in test itp.
        AND updated >= -1d

.. code-block:: sql

    project = DEMO
        AND sprint IN openSprints()
        AND assignee = currentUser()

.. code-block:: sql

    reporter = currentUser()
        AND statusCategory != Done
        AND assignee != currentUser()

.. code-block:: sql

    project = DEMO
        AND updated >= -7d
        AND assignee IN membersOf("jira-administrators")

.. code-block:: sql

    due >= 2017-03-01 AND due <= 2017-03-31

    due >= startOfMonth() AND due <= endOfMonth()

.. code-block:: sql

    updated >= startOfWeek(-7d) AND updated <= endOfWeek(-7d)

.. code-block:: sql

    due <= now()
        AND statusCategory != Done

.. code-block:: sql

    status WAS NOT "In Progress" BEFORE "2011/02/02"
    status WAS NOT IN ("Resolved","In Progress") BEFORE "2011/02/02"
    status WAS IN ("Resolved","In Progress")
    status WAS "Resolved" BY jsmith DURING ("2010/01/01","2011/01/01")
    status WAS "Resolved" BY jsmith BEFORE "2011/02/02"

.. code-block:: sql

    status changed by currentUser()

.. code-block:: sql

    AFTER "date"
    BEFORE "date"
    BY "username"
    DURING ("date1","date2")
    ON "date"
    FROM "oldvalue"
    TO "newvalue"

.. code-block:: sql

    assignee CHANGED

    priority CHANGED BY freddo BEFORE endOfWeek() AFTER startOfWeek()

    status CHANGED FROM "In Progress" TO "Open"

.. code-block:: sql

    currentLogin()
    lastLogin()
    now()
    startOfDay()
    startOfWeek()
    startOfMonth()
    startOfYear()
    endOfDay()
    endOfWeek()
    endOfMonth()
    endOfYear()

More info: https://confluence.atlassian.com/jira064/advanced-searching-720416661.html

Assignments
-----------

JQL i Wyszukiwanie zadań
^^^^^^^^^^^^^^^^^^^^^^^^
#. wyszukaj wszystkie zadania, które są w statusie "In Progress"
#. wyszukaj zadania, które zostały zaktualizowane od wczoraj
#. wyszukaj zadania, które należą do obecnie otwartego sprintu
#. wyszukaj zadania oflagowane
#. wyszukaj zadania, które należą do osób z grupy jira-administrators
#. wyszukaj zadania, które były przypisane do Ciebie, ale już nie są
#. Wyszukaj wszystkie zadania zaktualizowane przez Ciebie w okresie ostatniego tygodnia

- Pokaż kolumny: Priority, Key, Summary, Original Time Estimate, fixVersion, Epic Name, Status
