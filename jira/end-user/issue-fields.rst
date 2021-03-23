Issue
=====


Priority
--------
* `Highest`, `High`, `Medium`, `Low`, `Lowest`
* `Blocker`, `Highest`, `High`, `Medium`, `Low`
* MoSCoW: `Must`, `Should`, `Could`, `Won't`
* `Must`, `Should`, `Could`
* `Important`, `Normal`
* `Expedite`, `Standard`
* `Urgent`, `Important`, `Standard`


Description
-----------
- Acceptance criteria
- Description: **INFO**
- Description: **BEFORE**
- Description: **TODO**
- Description: **AFTER**
- using (/) and (x)


Date Fields
-----------
* `Created Date`
* `Updated Date`
* `Due Date`
* `Start Date` (Jira Cloud)


Other Fields
------------
* `Summary`
* `Comments`
* `Reporter`
* `Assignee`
* `Labels`
* `Components`
* `Attachment`
* `Linked Issues`
* `Epic Link`
* `Sprint`
* `Status`
* `Sub-Tasks`
* `Votes`
* `Watchers`

* `Created Date`
* `Updated Date`
* `Due Date`
* `Issue Type`
* `Description`
* `Fix Version/s`
* `Affects Version/s`
* `Priority`


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
* Bulk change multiple issues in backlog
* Edit issue and create issue link
* Create issue subtask and change priority
* Bulk change multiple issues in backlog


Assignments
-----------

Issue Priority
^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog`
#. Edytuj zadanie `One`
#. Ustaw `Priority` na `Highest`

Issue Links
^^^^^^^^^^^
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog` -> `Backlog` (w menu po lewej stronie)
#. Edytuj zadanie `Nine` (skrót klawiszowy ``e``)
#. Powiąż zadanie linkami:

    * `Linked Issues`: `blocks`
    * `Issue`: `Eight`

.. note:: Jeżeli po wpisaniu słowa `Eight` w pole `Linked Issue` Jira nie znajduje zadania, to spróbuj wpisać klucz zadania, np. ``MH-8``. Wtedy Jira powinna podpowiedzieć pełną nazwę zadania.

Issue Sub-Tasks
^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog` -> `Backlog` (w menu po lewej stronie)
#. Edytuj zadanie `Nine` (skrót klawiszowy ``e``)
#. Dodaj trzy sub-taski:

    * Summary: `A`, Priority: `Highest`
    * summary: `B`, Priority: `Low`
    * summary: `C`, Priority: `Medium`

Issue Bulk Change
^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog` -> `Backlog` (w menu po lewej stronie)
#. Zaznacz zadania (trzymając `ctrl` lub `cmd`): `Two`, `Four`, `Six`, `Eight`
#. Kliknij prawym klawiszem myszy -> `Bulk Change` -> `Edit Issues` -> `Next`
#. Zmień issue type na `Task`
#. Rozwiń na dole `Unavailable Actions` i zobacz co tam jest
#. Kliknij `Next` (na dole)
#. Potwierdzamy `Confirm`
#. Po chwili klikamy `Refresh`
#. Po ukończeniu klikamy `Ok, got it`

.. note:: Zwróć uwagę, że po zmianie część zadań w backlog nie ma estymacji w `Story Point`. Te wartości nie zniknęły i są nadal przypisane do zadania, ale na obecnym widoku są ukryte. `Story Points` (jak sama nazwa wskazuje) domyślnie mogą być przyznawane tylko zadaniom typu `Story`. Można to zmienić w konfiguracji (wymaga uprawnień administratora) `Custom Field` -> `Story Points` -> Ikona trybiku (po prawej) -> `Configure` -> `Applicable contexts for scheme` -> `Edit Configuration`.
