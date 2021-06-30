Search Advanced
===============


Rationale
---------
* JQL - JIRA Query Language


Where to find?
--------------
* `Issues` -> `Search for Issues`
* `Basic` -> `Advanced`
* `Detail View` -> `List View`
* Konfiguracja kolumn wyświetlania


Where is used?
--------------
* Searching Issues
* Board Configuration
* Filters for Dashboard
* Filters for Subscriptions
* Bulk edit (to change limit: ``echo 'jira.bulk.edit.limit.issue.count = 1000' >> $JIRA_HOME/jira-config.properties``)
* ``jira.issue.editable = true`` dla statusu Done (Workflow)


Operators
---------
* Operators capital letter

.. csv-table:: Operators
    :header: "Operator", "Description"
    :widths: 5, 95

    ``=``, "Equals"
    ``!=``, "Not equal (is different than)"
    ``>``, "Greater than"
    ``<``, "Less than"
    ``<=``, "Greater or equal"
    ``>=``, "Less or equal"
    ``~``, "Contains text"
    ``(...)``, "List"
    ``AND``, "Conjunction"
    ``OR``, "Disjunction"
    ``ORDER BY``, "Ordering"
    ``ASC``, "Ascending"
    ``DESC``, "Descending"


View
----
* Konfiguracja kolumn wyświetlania
* Import / Export CSV

    * All fields
    * current fields

* Limit wyświetlania wyników dla JQL (change: `General Configuration` -> `Advanced Settings` -> ``jira.search.views.default.max``)


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

    summary ~ "Hell*"

.. code-block:: sql

    summary ~ "*ell"

.. code-block:: sql

    summary ~ "*ell*"

.. code-block:: sql

    assignee != "myusername"

.. code-block:: sql

    statusCategory = "To Do"

.. code-block:: sql

    statusCategory != "Done"

.. code-block:: sql

    Flagged IS NOT EMPTY


Ordering
--------
.. code-block:: sql

    project = "MYPROJECT"
        ORDER BY priority DESC

.. code-block:: sql

    project = "MYPROJECT"
        ORDER BY priority DESC, key ASC


Complex queries
---------------
.. code-block:: sql

    project = "MYPROJECT"
        AND status = "In Progress"

.. code-block:: sql

    status = "To Do"
        OR status = "In Progress"

.. code-block:: sql

    status IN ("To Do", "In Progress")

.. code-block:: sql

    status NOT IN ("To Do", "In Progress")

.. code-block:: sql

    statusCategory NOT IN ("To Do", "Done")

.. code-block:: sql

    project = "MYPROJECT"
        AND resolution NOT IN ("Done", "Won't Do")

.. code-block:: sql

    project = "MYPROJECT" AND (
        priority = Highest
        OR Flagged IS NOT EMPTY
        OR statusCategory = "In Progress")


Demonstration
-------------
* Autocompletion
* Scalar and list operators
* Text Operators
* Bulk-change


Assignments
-----------

Search Advanced Bulk Change
^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Przejdź do wyszukiwania zadań:

    * Cloud: Z menu `Filters` wybrać `Advanced Issue Search`
    * Server: Z menu `Issues` wybrać `Search for Issues`

#. Upewnij się, że jesteś w trybie wyszukiwania: `Advanced`
#. Wyszukaj: ``project = MYPROJECT and due IS EMPTY`` (gdzie `MYPROJECT` to nazwa Twojego projektu)
#. Przycisk `Tools` (po prawej u góry) -> `Bulk Change` -> `all X issue(s)`
#. Zaznacz wszystkie (checkboxem do zaznaczania wszystkich na raz, nie rób tego pojedynczo)
#. Kliknij przycisk `Next` -> `Edit Issues` -> `Next`
#. Zmień `Change Due Date` i ustaw na `1/Nov/00`
#. Kliknij przycisk `Next` (na dole) -> `Confirm` -> `Ok, got it`
