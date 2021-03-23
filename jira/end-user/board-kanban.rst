Board Kanban
============


Rationale
---------
- What’s Kanban?
- Pull system
- JIT
- Context switching
- Kanban Board


Improvement
-----------

    - Muda
    - Jidoka
    - Kaizen
    - Bottlenecks
    - Metrics
    - Lean


Kanban Board
------------
- Workflow
- Columns
- Swimlanes
- Expedite
- Priority
- SLA

.. figure:: ../_img/jira-board-backlog-kanban.png


Backlog
-------
* Kanban backlog
* Sub-Task view (expand)


Demonstration
-------------
* Estimate issue
* Add sprint: set name, set duration, set start date
* Add issues to sprint
* Start sprint: set goal
* Active sprint: move issues, add flag, print cards (on paper)
* Close sprint: drop issues to next sprint


Assignments
-----------

Board Usage Estimation
^^^^^^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` (w menu po lewej)
#. W detail view zadania `One` -> okienko `Estimate` ustaw 3 (lub pole `Story Point` przy edycji zadania)
#. W detail view zadania `Three` -> okienko `Estimate` ustaw 4 (lub pole `Story Point` przy edycji zadania)
#. W detail view zadania `Five` -> okienko `Estimate` ustaw 8 (lub pole `Story Point` przy edycji zadania)
#. Zwróć uwagę, że estymować można tylko zadania typu `Story`

.. note:: `Story Points` (jak sama nazwa wskazuje) domyślnie mogą być przyznawane tylko zadaniom typu `Story`. Można to zmienić w konfiguracji (wymaga uprawnień administratora) `Custom Field` -> `Story Points` -> Ikona trybiku (po prawej) -> `Configure` -> `Applicable contexts for scheme` -> `Edit Configuration`.

Board Usage Sprint Create
^^^^^^^^^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` (w menu po lewej)
#. Dodaj pierwszy sprint:

    - `Name`: `2000-01 week 1`
    - `Duration`: `1 week`
    - `Start Date`: `1/Jan/00 09:00 AM`

#. Dodaj drugi sprint:

    - `Name`: `2000-01 week 2`
    - `Duration`: `1 week`
    - `Start Date`: `7/Jan/00 09:00 AM`

Board Usage Sprint Start
^^^^^^^^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` (w menu po lewej)
#. Do sprintu `2000-01 week 1` dodaj zadania: `One`, `Two`, `Three`
#. Przejedź suwakiem i dodaj `Four`, `Five`, `Six`, zwróć uwagę na zmiany liczb w okienku `Issues` i `Estimate`
#. Wystartuj sprint ustawiając:

    - `Goal`: `Ukończenie szkolenia z Jiry`
    - `Duration`: `1 week`
    - `Start Date`: `1/Jan/00 09:00 AM`

#. Co oznaczają wartości z estymacjami w nagłówku sprintu: `To Do`, `In Progress`, `Done` (w rozpoczętym sprincie, na ekranie `Backlog` w prawym górnym rogu - trzy kolorowe owale).

Board Usage Sprint Work
^^^^^^^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Active Sprints` (w menu po lewej)
#. Przenieś zadania:

    - `One` do `In Progress`
    - `Two` do `In Progress`
    - `Three` do `Done`

#. Dodaj flagę do zadania `Four`
#. Z menu `Board` prawy górny róg:

    - Wybierz `Hide detail view`
    - Wybierz `Print cards` i zmień `Card size` -> `small`

#. Zobacz jak zmieniły się wartości z estymacjami w nagłówku sprintu: `To Do`, `In Progress`, `Done` (w rozpoczętym sprincie, na ekranie `Backlog` w prawym górnym rogu - trzy kolorowe owale).

Board Usage Sprint Close
^^^^^^^^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Active Sprint` (w menu po lewej)
#. Zakończ aktualny sprint -> Prawy górny róg `Complete Sprint`
#. Zadania niezakończone mają `spaść` do sprintu następnego, tj. `2000-01 week 2`

    - Co się dzieje z otwartymi zadaniami?
    - Co się dzieje z zamkniętymi zadaniami?
    - Co się dzieje z zamkniętymi subtaskami, ale otwartym zadaniem?
    - Co się dzieje z otwartymi subtaskami ale zamkniętym zadaniem?

