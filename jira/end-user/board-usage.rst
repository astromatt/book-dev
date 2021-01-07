***********
Board Usage
***********


Project Management
==================
- Kanban
- Scrum
- Scrum + Kanban
- Portfolio
- Scrum vs. Kanban

    - Scrum -> Rozwój (Story)
    - Kanban -> Utrzymanie (Task)
    - Praca w Scrum i Kanban jednocześnie
    - Konstytucja zespołu i dobre praktyki

.. figure:: img/jira-board-select.jpg
.. figure:: img/agile-wheel-1.png
.. figure:: img/agile-wheel-2.png
.. figure:: img/scrum-sprint-week-continuous.png
.. figure:: img/scrum-daily-timer.png
.. figure:: img/scrum-userstory.png


Scrum
=====
- Backlog
- Sprintlog
- Task board

.. figure:: img/jira-board-backlog-scrum.png
.. figure:: img/jira-board-sprint.png


Epic
====
- Brak worków (np. Poprawki błędów)
- Doważalne (określone w czasie, mają datę początku i końca)
- Wymagalność:

    - `Due Date`
    - `Start Date`
    - `Assignee`

- Optymalna długość
- Kategoryzowanie
- Timeline i roadmapa
- Planowanie kwartalne
- Przypisywanie Epiców do wersji
- Board epików
- Business Value epików


Planning and Refinement
=======================
.. figure:: img/agile-epic-decomposition-01-mindmapping.jpg
.. figure:: img/agile-epic-decomposition-02-epics.jpg
.. figure:: img/agile-epic-decomposition-03-epic.jpg
.. figure:: img/agile-epic-decomposition-04-epics.jpg
.. figure:: img/agile-epic-decomposition-05-ordering.jpg
.. figure:: img/agile-epic-decomposition-06-ordered.jpg
.. figure:: img/agile-epic-decomposition-07-todecompose.jpg
.. figure:: img/agile-epic-decomposition-08-decomposition.jpg
.. figure:: img/agile-epic-decomposition-09-ordering.jpg
.. figure:: img/agile-epic-decomposition-10-ordered.jpg
.. figure:: img/agile-epic-decomposition-11-estimation.jpg
.. figure:: img/agile-epic-decomposition-12-priorities.jpg
.. figure:: img/agile-epic-decomposition-13-sprints.jpg
.. figure:: img/agile-epic-decomposition-14-issues.jpg
.. figure:: img/agile-epic-decomposition-15-jira.jpg
.. figure:: img/agile-epic-decomposition-16-epicmaping.jpg
.. figure:: img/agile-epic-decomposition-17-board.jpg
.. figure:: img/agile-epic-decomposition-18-risk.jpg
.. figure:: img/agile-epic-decomposition-19-portfolio.jpg


Estimation
==========
- Time Estimate
- Manday
- Story Point
- Business Value
- ``#NoEstimates`` and Monte Carlo simulation:

    * https://www.infoq.com/presentations/monte-carlo
    * https://docs.google.com/spreadsheets/d/1BmSuj1jA2ZfhUBzPtqDBqDjMjSXMqj3QoHZGR-TesOA/edit#gid=542217325


Metrics
=======
- Velocity
- Capacity
- Maturity

.. figure:: img/scrum-capacity-sprint.png
.. figure:: img/scrum-capacity-backlog.png


Planning and Refinement
=======================
- Estimation
- How big your tasks should be?
- Estimation support systems
- Sprint goal
- Acceptance Criteria
- Definition of Done
- Time Tracking


Roadmap
=======
.. figure:: img/jira-board-roadmap.png


Kanban
======
- What’s Kanban?
- Pull system
- JIT
- Context switching
- Kanban Board
- Improvement:

    - Muda
    - Jidoka
    - Kaizen
    - Bottlenecks
    - Metrics
    - Lean

- Workflow:

    - Columns
    - Swimlanes
    - Expedite
    - Priority
    - SLA

.. figure:: img/jira-board-backlog-kanban.png


Demonstration
=============
* Estimate issue
* Add sprint: set name, set duration, set start date
* Add issues to sprint
* Start sprint: set goal
* Active sprint: move issues, add flag, print cards (on paper)
* Close sprint: drop issues to next sprint


Assignments
===========

Board Usage Estimation
----------------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` (w menu po lewej)
#. W detail view zadania `One` -> okienko `Estimate` ustaw 3 (lub pole `Story Point` przy edycji zadania)
#. W detail view zadania `Three` -> okienko `Estimate` ustaw 4 (lub pole `Story Point` przy edycji zadania)
#. W detail view zadania `Five` -> okienko `Estimate` ustaw 8 (lub pole `Story Point` przy edycji zadania)
#. Zwróć uwagę, że estymować można tylko zadania typu `Story`

.. note:: `Story Points` (jak sama nazwa wskazuje) domyślnie mogą być przyznawane tylko zadaniom typu `Story`. Można to zmienić w konfiguracji (wymaga uprawnień administratora) `Custom Field` -> `Story Points` -> Ikona trybiku (po prawej) -> `Configure` -> `Applicable contexts for scheme` -> `Edit Configuration`.

Board Usage Sprint Create
-------------------------
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
------------------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` (w menu po lewej)
#. Do sprintu `2000-01 week 1` dodaj zadania: `One`, `Two`, `Three`
#. Przejedź suwakiem i dodaj `Four`, `Five`, `Six`, zwróć uwagę na zmiany liczb w okienku `Issues` i `Estimate`
#. Wystartuj sprint ustawiając:

    - `Goal`: `Ukończenie szkolenia z Jiry`
    - `Duration`: `1 week`
    - `Start Date`: `1/Jan/00 09:00 AM`

#. Co oznaczają wartości z estymacjami w nagłówku sprintu: `To Do`, `In Progress`, `Done` (w rozpoczętym sprincie, na ekranie `Backlog` w prawym górnym rogu - trzy kolorowe owale).

Board Usage Sprint Work
-----------------------
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
------------------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Active Sprint` (w menu po lewej)
#. Zakończ aktualny sprint -> Prawy górny róg `Complete Sprint`
#. Zadania niezakończone mają `spaść` do sprintu następnego, tj. `2000-01 week 2`

    - Co się dzieje z otwartymi zadaniami?
    - Co się dzieje z zamkniętymi zadaniami?
    - Co się dzieje z zamkniętymi subtaskami, ale otwartym zadaniem?
    - Co się dzieje z otwartymi subtaskami ale zamkniętym zadaniem?
