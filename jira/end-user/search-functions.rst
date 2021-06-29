Search Functions
================


Rationale
---------
* https://support.atlassian.com/jira-software-cloud/docs/advanced-search-reference-jql-functions/
* https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-functions-reference-939938746.html


Jira Core
---------
.. csv-table:: JQL functions in `Jira Core`
    :header: "Function", "Description"
    :widths: 20, 80

    ``cascadeOption()``,                   "Search for issues that match the selected values of a 'cascading select' custom field"
    ``componentsLeadByUser()``,            "Find issues in components that are led by a specific user"
    ``currentLogin()``,                    "Perform searches based on the time at which the current user's session began"
    ``currentUser()``,                     "Perform searches based on the currently logged-in user"
    ``earliestUnreleasedVersion()``,       "Perform searches based on the earliest unreleased version in a project"
    ``endOfDay()``,                        "Perform searches based on the end of the current day"
    ``endOfMonth()``,                      "Perform searches based on the end of the current month"
    ``endOfWeek()``,                       "Search for issues that are due by the end of the last day of the current week"
    ``endOfYear()``,                       "Perform searches based on the end of the current year"
    ``issueHistory()``,                    "Find issues that you have recently viewed, i.e. issues that are in the 'Recent Issues' section of the 'Issues' drop-down menu"
    ``issuesWithRemoteLinksByGlobalId()``, "Perform searches based on issues that are associated with remote links that have any of the specified global ids"
    ``lastLogin()``,                       "Perform searches based on the time at which the current user's previous session began"
    ``latestReleasedVersion()``,           "Perform searches based on the latest released version (i.e. the most recent version that has been released) of a specified project"
    ``linkedissue``,                       "Searches for epics and subtasks. If the issue is not an epic, the search returns all subtasks for the issue"
    ``linkedIssues()``,                    "Searches for issues that are linked to an issue"
    ``membersOf()``,                       "Perform searches based on the members of a particular group"
    ``now()``,                             "Perform searches based on the current time"
    ``parentEpic()``,                      "Search for issues and sub-tasks that are linked to an epic"
    ``projectsLeadByUser()``,              "Find issues in projects that are led by a specific user"
    ``projectsWhereUserHasPermission()``,  "Find issues in projects where you have a specific permission"
    ``projectsWhereUserHasRole()``,        "Find issues in projects where you have a specific role"
    ``releasedVersions()``,                "Perform searches based on the released versions (i.e. versions that your Jira administrator has released) of a specified project"
    ``standardIssueTypes()``,              "Perform searches based on 'standard' Issue Types, that is, search for issues that are not sub-tasks"
    ``startOfDay()``,                      "Perform searches based on the start of the current day"
    ``startOfMonth()``,                    "Perform searches based on the start of the current month"
    ``startOfWeek()``,                     "Search for new issues created since the start of the first day of the current week"
    ``startOfYear()``,                     "Perform searches based on the start of the current year"
    ``subtaskIssueTypes()``,               "Perform searches based on issues that are sub-tasks"
    ``unreleasedVersions()``,              "Perform searches based on the unreleased versions (i.e. versions that your Jira administrator has not yet released) of a specified project"
    ``updatedBy()``,                       "Search for issues that were updated by a specific user, optionally within the specified time range"
    ``votedIssues()``,                     "Perform searches based on issues for which you have voted"
    ``watchedIssues()``,                   "Perform searches based on issues that you are watching"


Jira Software
-------------
.. csv-table:: JQL functions in `Jira Software`
    :header: "Function", "Description"
    :widths: 20, 80

    ``closedSprints()``, "Search for issues that are assigned to a completed Sprint"
    ``futureSprints()``, "Search for issues that are assigned to a sprint that hasn't been started yet"
    ``openSprints()``,   "Search for issues that are assigned to a sprint that was started, but has not yet been completed"


Jira Service Management
-----------------------
.. csv-table:: JQL functions in `Jira Service Management`
    :header: "Function", "Description"
    :widths: 20, 80

    ``approved()``,            "Search for requests that required approval and have a final decision of approved"
    ``approver()``,            "Search for requests that require or required approval by a user"
    ``breached()``,            "Returns issues that whose most recent SLA has missed its goal"
    ``completed()``,           "Returns issues that have an SLA that has completed at least one cycle"
    ``elapsed()``,             "Returns issues whose SLA clock is at a certain point relative to a cycle's start event"
    ``everbreached()``,        "Returns issues that have missed one of their SLA goals"
    ``myApproval()``,          "Search for requests that require approval or have required approval by the current user"
    ``myPending()``,           "Search for requests that require approval by the current user"
    ``organizationMembers()``, "Search for all requests sent by the members of an organization"
    ``paused()``,              "Returns issues that have an SLA that is paused due to a condition"
    ``pending()``,             "Search for requests that require approval"
    ``pendingBy()``,           "Search for requests that require approval by a certain user"
    ``remaining()``,           "Returns issues whose SLA clock is at a certain point relative to the goal"
    ``running()``,             "Returns issues that have an SLA that is running, regardless of the calendar"
    ``withinCalendarHours()``, "Returns issues that have an SLA that is running according to the SLA calendar"


Examples
--------
.. code-block:: sql

    assignee = currentUser()

.. code-block:: sql

    Sprint IN closedSprints()

.. code-block:: sql

    Sprint IN openSprints()

.. code-block:: sql

    Sprint IN futureSprints()


My issues To Do
---------------
.. code-block:: sql

    assignee = currentUser()
        AND statusCategory != "Done"

.. code-block:: sql

    assignee = currentUser()
        AND statusCategory != "Done"
        ORDER BY priority DESC, key ASC

.. code-block:: sql

    project = "MYPROJECT"
        AND statusCategory != "Done"
        AND sprint IN openSprints()
        AND assignee = currentUser()
        ORDER BY priority DESC, key ASC


Tracking reported issues
------------------------
.. code-block:: sql

    reporter = currentUser()
        AND statusCategory != "Done"
        AND assignee != currentUser()

.. code-block:: sql

    project = "IT Support"
        AND reporter = currentUser()
        AND statusCategory != "Done"


Tracking team members work
--------------------------
.. code-block:: sql

    statusCategory = "In Progress"
        AND assignee IN membersOf("jira-administrators")

.. code-block:: sql

    project = "MYPROJECT"
        AND assignee IN membersOf("jira-administrators")
        AND updated >= -7d

.. code-block:: sql

    assignee IN membersOf("jira-administrators")
        AND updated >= startOfWeek()
        AND updated <= endOfWeek()


Daily
-----
.. code-block:: sql

    project = "MYPROJECT"
        AND sprint IN openSprints()
        AND (Flagged IS NOT EMPTY
             OR statusCategory = "In Progress"
             OR updated >= -1d)

.. code-block:: sql

    project = "MYPROJECT" AND (
        priority = Highest
        OR Flagged IS NOT EMPTY
        OR statusCategory = "In Progress"
        OR statusCategory in ("To Do", "Done")
        AND (updated >= startOfDay(-1d)
            OR (updated <= startOfWeek(1d)
            AND updated >= startOfDay(-3d))))


Time Searches
-------------
.. code-block:: sql

    due >= "2000-01-01" AND due <= "2000-01-31"

.. code-block:: sql

    due >= startOfMonth() AND due <= endOfMonth()

.. code-block:: sql

    due >= startOfMonth(-1w) AND due <= endOfMonth(+2w)

.. code-block:: sql

    due <= now()
        AND statusCategory != "Done"



My issues To Do
---------------
.. code-block:: sql

    assignee = currentUser()
        AND statusCategory != "Done"

.. code-block:: sql

    assignee = currentUser()
        AND statusCategory != "Done"
        ORDER BY priority DESC, key ASC

.. code-block:: sql

    project = "MYPROJECT"
        AND statusCategory != "Done"
        AND sprint IN openSprints()
        AND assignee = currentUser()
        ORDER BY priority DESC, key ASC


Tracking reported issues
------------------------
.. code-block:: sql

    reporter = currentUser()
        AND statusCategory != "Done"
        AND assignee != currentUser()

.. code-block:: sql

    project = "IT Support"
        AND reporter = currentUser()
        AND statusCategory != "Done"


Tracking team members work
--------------------------
.. code-block:: sql

    statusCategory = "In Progress"
        AND assignee IN membersOf("jira-administrators")

.. code-block:: sql

    project = "MYPROJECT"
        AND assignee IN membersOf("jira-administrators")
        AND updated >= -7d

.. code-block:: sql

    assignee IN membersOf("jira-administrators")
        AND updated >= startOfWeek()
        AND updated <= endOfWeek()


Daily
-----
.. code-block:: sql

    project = "MYPROJECT"
        AND sprint IN openSprints()
        AND (Flagged IS NOT EMPTY
             OR statusCategory = "In Progress"
             OR updated >= -1d)

.. code-block:: sql

    project = "MYPROJECT" AND (
        priority = Highest
        OR Flagged IS NOT EMPTY
        OR statusCategory = "In Progress")

.. code-block:: sql

    project = "MYPROJECT" AND (
        priority = Highest
        OR Flagged IS NOT EMPTY
        OR statusCategory = "In Progress"
        OR statusCategory in ("To Do", "Done")
        AND (updated >= startOfDay(-1d)
            OR (updated <= startOfWeek(1d)
            AND updated >= startOfDay(-3d))))


Further Reading
---------------
* https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-939938733.html
* https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-functions-reference-939938746.html


Demonstration
-------------
* Advanced: autocompletion, scalar and list operators, functions


Assignments
-----------

Search Advanced Functions
^^^^^^^^^^^^^^^^^^^^^^^^^
#. Przejdź do wyszukiwania zadań:

    * Cloud: Z menu `Filters` wybrać `Advanced Issue Search`
    * Server: Z menu `Issues` wybrać `Search for Issues`

#. Upewnij się, że jesteś w trybie wyszukiwania: `Advanced`
#. Kliknij link Advanced z paska wyszukiwania
#. To co wpisujesz w tym polu, to tzw. `JQL (Jira Query Language)`
#. W polu wyszukiwania wpisz literę `p` i zobacz co Jira Ci podpowiedziała
#. Wybierz strzałką na klawiaturze pozycję `project` i kliknij enter
#. Z listy wybierz znak równa się ``=``
#. Z listy wybierz nazwę swojego projektu (można najechać i kliknąć myszką)
#. Klikamy enter aby wyszukać, powinno nam to wyświetlić wszystkie zadania z naszego projektu
#. Kliknij w pole wyszukiwania i po fragmencie, który wcześniej był wpisany dodaj spację i zobacz co Ci podpowiada
#. Wybierz ``AND`` i zacznij pisać `status` -> mamy dwie opcje do wyboru: `status` i `statusCategory`
#. Wybierz `statusCategory` -> następnie równa się ``=`` -> `In Progress` i klikamy enter aby wyszukać zadania
#. Edytuj zapytanie i dopisz na koniec: `Epic Link` -> równa się ``=`` -> wybrać Epic `Wyszukiwarka`, ale z Twojego projektu
#. Wyczyść zapytanie
#. w poniższych zapytaniach `MYPROJECT` zamień na klucz swojego projektu
#. Wyszukaj: ``project = MYPROJECT AND fixVersion = earliestUnreleasedVersion()``
#. Wyszukaj: ``assignee = currentUser() and statusCategory != Done``
