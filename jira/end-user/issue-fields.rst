Issue Fields
============


Main Fields
-----------
* `Status`
* `Sub-Tasks`
* `Issue Type`


Date Fields
-----------
* `Created Date`
* `Updated Date`
* `Due Date`
* `Start Date` (Jira Cloud)


User Picker
-----------
* `Assignee`
* `Reporter`
* `Watchers`


Text Field
----------
* `Summary`
* `Description`
* `Comments`

Description:

    * Acceptance criteria
    * Description: **INFO**
    * Description: **BEFORE**
    * Description: **TODO**
    * Description: **AFTER**
    * using (/) and (x)


Label Field
-----------
* `Labels`
* `Components`


Other Fields
------------
* `Attachment`
* `Linked Issues`
* `Votes`


Jira Software
-------------
* `Sprint`
* `Epic Link`


Priority
--------
* `Highest`, `High`, `Medium`, `Low`, `Lowest`
* `Blocker`, `Highest`, `High`, `Medium`, `Low`
* MoSCoW: `Must`, `Should`, `Could`, `Won't`
* `Must`, `Should`, `Could`
* `Important`, `Normal`
* `Expedite`, `Standard`
* `Urgent`, `Important`, `Standard`


Version
-------
* `Fix Version/s`
* `Affects Version/s`

Affects Version/s:

    * MyApp 1.0 (assume this is unsupported)
    * MyApp 2.0
    * MyApp 3.0

Fix Version/s:

    * MyApp 2.0.1
    * MyApp 3.0.5


Custom Fields
-------------
* kilka, maks kilkanaście
* Team Assigned
* Start Date
* Business Value
* Manday
* Severity
* Risk


Demonstration
-------------
* Edit issue and modify values
* Change inline issue field value
* Edit issue and create issue link
* Change priority
* Create custom fields


Assignments
-----------

Issue Fields Priority
^^^^^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog`
#. Edytuj zadanie `One`
#. Ustaw `Priority` na `Highest`

Issue Fields Issue Link
^^^^^^^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog` -> `Backlog` (w menu po lewej stronie)
#. Edytuj zadanie `Nine` (skrót klawiszowy ``e``)
#. Powiąż zadanie linkami:

    * `Linked Issues`: `blocks`
    * `Issue`: `Eight`

.. note:: Jeżeli po wpisaniu słowa `Eight` w pole `Linked Issue` Jira nie znajduje zadania, to spróbuj wpisać klucz zadania, np. ``MH-8``. Wtedy Jira powinna podpowiedzieć pełną nazwę zadania.
