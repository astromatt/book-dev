*************************
JQL - JIRA Query Language
*************************


Where to find?
==============
* Issues -> Search for Issues

    * Basic -> Advanced
    * Detail View -> List View


Where is used?
==============
* Searching Issues
* Board Configuration
* Filters for Dashboard
* Filters for Subscriptions
* Bulk edit (to change limit: ``echo 'jira.bulk.edit.limit.issue.count = 1000' >> $JIRA_HOME/jira-config.properties``)
* ``jira.issue.editable = true`` dla statusu Done (Workflow)


Operators
=========
.. csv-table:: Operators
    :header: "Operator", "Description"

    ``=``, "Equals"
    ``==``, "Equals"
    ``!=``, "Not equal (is different than)"
    ``>``, "Greater than"
    ``<``, "Less than"
    ``<=``, "Greater or equal"
    ``>=``, "Less or equal"
    ``~``, "Contains text"


View
====
- Konfiguracja Kolumn wyszukiwania
- Import / Export CSV

    - All fields
    - current fields

- Limit wyświetlania wyników dla JQL (change: General Configuration -> Advanced Settings -> ``jira.search.views.default.max``)


JQL Examples
============
* Operators capital letter

Select issues
-------------
.. code-block:: sql

    project = "MYPROJECT"

.. code-block:: sql

    status = "To Do"

.. code-block:: sql

    assignee = "admin"

.. code-block:: sql

    reporter = "myusername"

.. code-block:: sql

    summary ~ "Hello"

.. code-block:: sql

    assignee != "myusername"

.. code-block:: sql

    statusCategory = "To Do"

.. code-block:: sql

    statusCategory != "Done"

.. code-block:: sql

    Flagged IS NOT EMPTY

Complex queries
---------------

.. code-block:: sql

    status = "To Do" OR status = "In Progress"

.. code-block:: sql

    status IN ("To Do", "In Progress")

.. code-block:: sql

    status NOT IN ("To Do", "In Progress")

.. code-block:: sql

    statusCategory NOT IN ("To Do", "In Progress")

.. code-block:: sql

    project = "MYPROJECT"
        AND status = "To Do"

.. code-block:: sql

    project = "MYPROJECT"
        AND resolution NOT IN ("Fixed", "Won't Fix")

Ordering
--------
.. code-block:: sql

    project = "MYPROJECT"
        ORDER BY priority DESC

.. code-block:: sql

    project = "MYPROJECT"
        ORDER BY priority DESC, key ASC

Functions
---------
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

.. code-block:: sql

    assignee = currentUser()

.. code-block:: sql

    Sprint IN closedSprints()

.. code-block:: sql

    Sprint IN openSprints()

.. code-block:: sql

    Sprint IN futureSprints()

Queries in History
------------------
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

    due >= 2000-01-01 AND due <= 2000-01-31

.. code-block:: sql

    due >= startOfMonth() AND due <= endOfMonth()

.. code-block:: sql

    due <= now()
        AND statusCategory != "Done"

.. code-block:: sql

    status WAS IN ("Resolved","In Progress")

.. code-block:: sql

    status WAS NOT "In Progress" BEFORE "2000/01/01"

.. code-block:: sql

    status WAS NOT IN ("Resolved","In Progress") BEFORE "2000/01/01"

.. code-block:: sql

    status WAS "Resolved" BY "admin" DURING ("2000/01/01","2000/01/01")

.. code-block:: sql

    status WAS "Resolved" BY "admin" BEFORE "2000/01/01"

.. code-block:: sql

    status CHANGED BY currentUser()

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

.. code-block:: sql

    priority CHANGED BY freddo BEFORE endOfWeek() AFTER startOfWeek()

.. code-block:: sql

    status CHANGED FROM "In Progress" TO "Open"


Useful Queries
==============

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
        AND updated >= -7d
        AND assignee IN membersOf("jira-administrators")

.. code-block:: sql

    assignee IN membersOf("jira-administrators")
        AND updated >= startOfWeek(-7d)
        AND updated <= endOfWeek(-7d)

Daily
-----
.. code-block:: sql

    project = "MYPROJECT"
        AND sprint IN openSprints()
        AND (Flagged IS NOT EMPTY
             OR updated >= -1d
             OR statusCategory = "In Progress")


More info
=========
* https://confluence.atlassian.com/jira064/advanced-searching-720416661.html


Assignments
===========

JQL Search View
---------------
#. Z menu "Issues" wybrać "Search for Issues"
#. "Change View" [przycisk po prawej stronie] zmień na "List View"
#. "Columns" [przycisk po prawej stronie]: Odznaczyć: "Created", "Updated", "Development"
#. Columns: zaznaczyć: "Summary", "Issue Type", "Due Date", "Fix Version/s", "Epic Link"
#. Chwytając nagłówek kolumny, przenieś "Issue Type" (T) jako pierwsza kolumna
#. Ustawić kolumny w kolejności: "Issue Type", "Issue Key", "Epic Link", "Fix Version/s", "Due Date", "Status", "Summary"
#. Dodać kolumny: "Original Estimate", "Remaining Estimate", "Time Spent"
#. Z menu po prawej stronie u góry wybieramy "Export" -> "CSV (Current Fields)" -> "Delimiter" -> "Comma (,)"

JQL Search Basic
----------------
#. Z menu "Issues" wybrać "Search for Issues" w trybie Basic
#. "Project" -> swój projekt
#. Kliknij na nazwę kolumny "Due Date" dwukrotnie aby posortować rosnąco
#. "Status" -> "In Progress" oraz "Blocked"
#. More -> "Due Date" -> "Now Overdue"
#. Zmień zakres "Due Date" -> od "1/Oct/20" do "31/Oct/20"
#. Zmień zakres "Due Date" -> Due in next 8 hours or is overdue
#. Zmień zakres "Due Date" -> In range -7d to ... [pozostaw niewypełnione]

JQL Search Advanced
-------------------
#. Z menu "Issues" wybrać "Search for Issues" w trybie Advanced
#. Kliknij link Advanced z paska wyszukiwania
#. To co wpisujesz w tym polu, to tzw. JQL (Jira Query Language)
#. W polu wyszukiwania wpisz literę "p" i zobacz co Jira Ci podpowiedziała
#. Wybierz strzałką na klawiaturze pozycję "project" i kliknij enter
#. Z listy wybierz znak równa się ``=``
#. Z listy wybierz nazwę swojego projektu (można najechać i kliknąć myszką)
#. Klikamy enter aby wyszukać, powinno nam to wyświetlić wszystkie zadania z naszego projektu
#. Kliknij w pole wyszukiwania i po fragmencie, który wcześniej był wpisany dodaj spację i zobacz co Ci podpowiada
#. Wybierz ``AND`` i zacznij pisać status -> mamy dwie opcje do wyboru: status i statusCategory
#. Wybierz statusCategory -> następnie równa się ``=`` -> "In Progress" i klikamy enter aby wyszukać zadania
#. Edytuj zapytanie i dopisz na koniec: "Epic Link" -> równa się ``=`` -> wybrać Epic "Wyszukiwarka", ale z Twojego projektu
#. Wyczyść zapytanie
#. w poniższych zapytaniach MYPROJECT zamień na klucz swojego projektu
#. Wyszukaj: ``project = MYPROJECT AND fixVersion = earliestUnreleasedVersion()``
#. Wyszukaj: ``assignee = currentUser() and statusCategory != Done``

JQL Search Bulk Change
----------------------
#. Z menu "Issues" wybrać "Search for Issues" w trybie Advanced
#. Wyszukaj: ``project = MYPROJECT and due IS EMPTY`` (gdzie MYPROJECT to nazwa Twojego projektu)
#. Przycisk "Tools" (po prawej u góry) -> "Bulk Change" -> "all X issue(s)"
#. Zaznacz wszystkie (checkboxem do zaznaczania wszystkich na raz, nie rób tego pojedynczo)
#. Kliknij przycisk "Next" -> "Edit Issues" -> "Next"
#. Zmień "Change Due Date" i ustaw na "1/Nov/20"
#. Kliknij przycisk "Next" (na dole) -> "Confirm" -> "Ok, got it"
