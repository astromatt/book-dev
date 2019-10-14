*********************
Jira Software (Agile)
*********************

* :cite:`AgileManifesto2001`


More information
----------------
.. warning:: There's much more information at my slides https://www.slideshare.net/astrotech/scrum-master-training-course and https://www.slideshare.net/astrotech/scrum-training-course Those slides will be converted to the book format with time.



Project Management
------------------
- Prowadzenie projektów
- Kanban
- Scrum
- Portfolio
- Scrum + Kanban

Artifacts
---------
- Backlog
- Sprintlog
- Task board
- Units:

    - Story Points
    - Business Value

Epic
----
- Brak worków (np. Poprawki błędów)
- Doważalne (określone w czasie, mają datę początku i końca)
- Dobre praktyki:

    - Due Date
    - Start Date
    - Assignee

- Doważalne
- optymalna długość
- kategoryzowanie
- timeline i roadmapa
- planowanie kwartalne
- przypisywanie epikow do wersji
- board epików
- Business Value epików

Estimation
----------
- Time Estimate
- Manday
- Story Point
- Business Value
- #NoEstimates and Monte Carlo simulation (https://www.infoq.com/presentations/monte-carlo)

Metrics
-------
- Velocity
- Capacity
- Maturity

Planning and Refinement
-----------------------
- Estimation
- How big your tasks should be?
- Estimation support systems
- Sprint goal
- Acceptance Criteria
- Definition of Done
- Time Tracking

Dobre praktyki
--------------
- Kryteria akceptacyjne
- INFO
- BEFORE
- TODO
- AFTER
- używanie (/) i (x)

Board
-----
- Scrum vs. Kanban

    - Scrum -> Rozwój (Story)
    - Kanban -> Utrzymanie (Task)
    - Praca w Scrum i Kanban jednocześnie
    - Konstytucja zespołu i dobre praktyki

- Board vs. Project

    - Board z wielu projektów
    - Board z części jednego projektu
    - Board dla Projektu
    - Wiele boardów do jednego projektu (różne estymaty)
    - Wiele projektów czy wiele boardów (np. po komponentach)?

- Sprinty:

    - Wielkość (ilość zadań, capacity chart)
    - Długość (tydzień)
    - Konwencja nazewnicza (YYYY-MM week W) (2017-03 week 2, 2017-03 week 3)

- Uprawnienia
- Konfiguracja
- Kolumny

    - Column Constraint (max, min)
    - Dodawanie i usuwanie kolumn
    - Wiele statusów w jednej kolumnie
    - Statusy ciągnące pracę

- Swimlines

    - wg. priorytetów
    - wg. wersji

- Quick Filters
- Card Colors
- Card Layout

    - Backlog
    - Active Sprint
    - Days in Column

- Estimation

    - Original Estimate + Remaining Estimate and Time Spent
    - Story Points
    - Business Value
    - Issue Count

- Working Days
- Issue Detail View
- Portfolio na bazie Kanbana
- Scope Changes
- Otwieranie i zamykanie sprintów
- Auto assign
- Flagowanie zadań
- Quick Filters dla Daily

Charts
------
- Burn-down Chart
- Burn-up Chart
- Control Chart
- Cumulative Flow Diagram
- Epic Burndown
- Epic Report
- Release Burndown
- Sprint Report
- Velocity Chart
- Version Report
- Version Burndown

- Refine Reports

Kanban
------
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

Assignments
-----------

Board
^^^^^
#. Stwórz Board dla zadań rozwojowych (Story, Bug):

    - Dodaj kolumnę ``In Test`` oraz ``In Review`` wraz z odpowiadającymi im statusami
    - Dodaj status ``Won't Do``, który będzie w kolumnie ``Done`` jednocześnie ze statusem ``Done``
    - Stwórz Quick Filter ``Daily``:

        - zadania są w trakcie wykonywania
        - zaktualizowane w ciągu ostatniego dnia
        - lub mają flagę

    - Stwórz wersję board z Estymacją Time Estimate
    - Stwórz wersję board z Estymacją w Story Points

#. Stwórz Board dla zadań utrzymaniowych (Task)

    - Kolumny: ``To Do``, ``In Progress`` ``Blocked``, ``Done``
    - Dodaj status ``Won't Do``, który będzie w kolumnie ``Done`` jednocześnie ze statusem ``Done``

#. Stwórz board Kanban z Epikami:

    - Stwórz swimline dla kwartałów
    - Określ aby w kolumnie "In Progress" mogły być maksymalnie 3 Epiku

#. Stwórz board zadań przypisanych do Ciebie:

    - zadania mogą być w dowolnym projekcie
    - board ma być publiczny

Backlog i Estymacja
^^^^^^^^^^^^^^^^^^^
- Stwórz epiki

    - Logowanie
    - Panel administracyjny

- oszacuj zadania używając Story Points i skali S,M,L (Small: 1, Medium: 2, Large: 3)
- Zadanie wyestymuj na 4h
- Zaloguj 1h 30m do zadania i ustaw remaining na 3h

Wersje
^^^^^^
- Stwórz wersje

    - 2019-01 (rozpoczęcie: 1 styczeń 2019; zakończenie: 31 styczeń 2019)
    - 2019-02 (rozpoczęcie: 1 luty 2019; zakończenie: 28 luty 2019)
    - 2019-03 (rozpoczęcie: 1 marzec 2019; zakończenie: 31 marzec 2019)

- Zadania przydziel do wersji

Sprinty
^^^^^^^
- Stwórz Sprinty

    - 2019-01 week 1 (ma 4 Story Points)
    - 2019-01 week 2 (ma 10 Story Points)
    - 2019-01 week 3 (ma 8 Story Points)
    - 2019-01 week 4 (ma 10 Story Points)
    - 2019-02 week 5 (ma 8 Story Points)

- Wystartuj sprint ``2019-01 week 1``

    - Data rozpoczęcia 1 styczeń 2019, 9:00
    - Data zakończenia 7 styczeń 2017, 9:00

- Przenieś dwa zadania do "In progress"
- Przenieś jedno zadanie do "Done"
- Zamknij sprint
- Zadania które nie zostały zakończone w sprincie niech spadną do następnego tygodnia

    - Co się dzieje z otwartymi zadaniami?
    - Co się dzieje z zamkniętymi zadaniami?
    - Co się dzieje z zamkniętymi subtaskami, ale otwartym zadaniem?
    - Co się dzieje z otwartymi subtaskami ale zamkniętym zadaniem?

- Zobacz raporty

More information
----------------
.. warning:: There's much more information at my slides https://www.slideshare.net/astrotech/scrum-master-training-course and https://www.slideshare.net/astrotech/scrum-training-course Those slides will be converted to the book format with time.

