*****
Board
*****


Project Management
==================
- Prowadzenie projektów
- Kanban
- Scrum
- Portfolio
- Scrum + Kanban


Artifacts
=========
- Backlog
- Sprintlog
- Task board
- Units:

    - Story Points
    - Business Value

Epic
====
- Brak worków (np. Poprawki błędów)
- Doważalne (określone w czasie, mają datę początku i końca)
- Dobre praktyki:

    - Due Date
    - Start Date
    - Assignee

- optymalna długość
- kategoryzowanie
- timeline i roadmapa
- planowanie kwartalne
- przypisywanie Epiców do wersji
- board epików
- Business Value epików


Estimation
==========
- Time Estimate
- Manday
- Story Point
- Business Value
- #NoEstimates and Monte Carlo simulation (https://www.infoq.com/presentations/monte-carlo)


Metrics
=======
- Velocity
- Capacity
- Maturity


Planning and Refinement
=======================
- Estimation
- How big your tasks should be?
- Estimation support systems
- Sprint goal
- Acceptance Criteria
- Definition of Done
- Time Tracking


Dobre praktyki
==============
- Kryteria akceptacyjne
- Sekcja w description: INFO
- Sekcja w description: BEFORE
- Sekcja w description: TODO
- Sekcja w description: AFTER
- używanie (/) i (x)


Board
=====
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

- Swimlanes

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
- Portfolio na bazie Kanban Board
- Scope Changes
- Otwieranie i zamykanie sprintów
- Auto assign
- Flagowanie zadań
- Quick Filters dla Daily


Charts
======
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


Assignments
===========

Board Sprint Add
----------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Dodaj pierwszy sprint:

    - "Name": "2020-11 week 1"
    - "Duration": "1 week"
    - "Start Date": "1/Nov/20 09:00 AM"

#. Dodaj drugi sprint:

    - "Name": "2020-11 week 2"
    - "Duration": "1 week"
    - "Start Date": "7/Nov/20 09:00 AM"

Board Sprint Start
------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Do sprintu "2020-11 week 1" dodaj zadania: "One", "Two", "Three"
#. Przejedź suwakiem i dodaj "Four", "Five", "Six", zwróć uwagę na zmiany liczb w okienku "Issues" i "Estimate"
#. Wystartuj sprint ustawiając:

    - Goal: "Ukończenie szkolenia z Jiry"
    - Duration: "1 week"
    - Start Date: "26/Oct/20 09:30 AM"

Board Sprint Work
-----------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Przenieś zadania:

    - "One" do "In Progress"
    - "Two" do "In Progress"
    - "Three" do "Done"

#. Dodaj flagę do zadania "Four"
#. Z menu "Board" prawy górny róg:

    - Wybierz "Hide detail view
    - Wybierz "Print cards" i zmień "Card size" -> "small"

Board Configure
---------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Z menu "Board" (prawy górny róg) -> "Configure"
#. Zakładka "General":

    - Usuń administratora "admin@example.com"
    - Zwróć uwagę na "Edit Filter Shares", "View Permissions"
    - Osoby które mają uprawnienia do "Filter" będą widziały i mogły otworzyć Board
    - To nie znaczy, że będę widziały zadania (to wymaga uprawnień w projekcie)

#. Zakładka "Columns":

    - Dodaj kolumnę "Blocked" w "Category" -> "In Progress"
    - Dodaj status "Rejected" w "Category" -> "Done" do kolumny "Done" i zaznacz "Set resolution"
    - Column Constraints "Issue Count, excluding sub-tasks
    - W kolumnie "Blocked" -> "Max" ustaw na: "2
    - W kolumnie "In Progress" -> "Min" ustaw na: "1"
    - Zaznacz "Days in column"

#. Zakładka "Swimlanes":

    - Wybierz "Base Swimlanes on" -> "Queries"
    - Dodaj Swimlane "Story" z JQL -> ``issuetype = Story``
    - Dodaj Swimlane "Task" z JQL -> ``issuetype = Task``

#. Zakładka "Quick Filters":

    - Zmień nazwę "Recently Updated" na "Daily"
    - Zmień JQL dla "Daily" na: ``updatedDate >= -1d OR Flagged IS NOT EMPTY``

#. Zakładka "Card colours":

    - Zmień "Colours based on" -> "Priorities"
    - Zmień kolor "Highest" oraz "High" na czerwony (FF0000)
    - Zmień kolor "Medium" na żółty (FFFF00)
    - Zmień kolor "Low" oraz "Lowest" na zielony (00FF00)

#. Zakładka "Card layout":

    - W sekcji "Backlog" -> wyświetl pole "Due Date"
    - W sekcji "Active sprints" -> wyświetl pole "Due Date"
    - Usuń wyświetlanie pola "Due Date" z sekcji Backlog (ale zostaw w "Active Sprint")

#. Zakładka "Estimation":

    - Zmień "Estimation Statistic" na "Original Time Estimate"
    - Zaznacz "Time Tracking" -> "Remaining Estimate and Time Spent"

#. Zakładka "Working days":

    - Wybierz "Region" -> "Europe"
    - "Time Zone" -> "(GMT+01:00) Warsaw"
    - Dodaj "Non-Working Days":

        * "1/Jan/20" (Nowy Rok)
        * "6/Jan/20" (Święto Trzech Króli)
        * "?/?/20" (pierwszy dzień Wielkiej Nocy)
        * "?/?/20" (drugi dzień Wielkiej Nocy)
        * "1/May/20" (Święto Państwowe)
        * "3/May/20" (Święto Narodowe Trzeciego Maja)
        * "?/?/20" (pierwszy dzień Zielonych Świątek) [pięćdziesiąt dni po wielkanocy]
        * "?/?/20" (dzień Bożego Ciała) [sześćdziesiąt dni po wielkanocy]
        * "15/Aug/20" (Wniebowzięcie Najświętszej Marii Panny / Święto Wojska Polskiego)
        * "1/Nov/20" (Wszystkich Świętych)
        * "11/Nov/20" (Narodowe Święto Niepodległości)
        * "25/Dec/20" (pierwszy dzień Bożego Narodzenia)
        * "26/Dec/20" (drugi dzień Bożego Narodzenia)

#. Zakładka "Issue Detail View":

    - Sekcja "General Fields" -> usuń: Status, Priority, Labels, Affects Version/s
    - Sekcja "Date Fields" -> dodaj "Due Date", usuń: "Created" i "Updated
    - Sekcja "People" -> usuń "Reporter" i "Assignee
    - Sekcja "Links" -> usuń "Linked Issue"

#. Wróć na "Boards" -> Twój Board -> "Active Sprint":

    - Usuń wszystkie zadania z kolumny "In Progress" (powinna podświetlić się na żółto)
    - Dodaj trzy zadania do kolumny "Blocked" (powinna podświetlić się na czerwono)

Board Sprint Close
------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprint"
#. Zakończ aktualny sprint -> Prawy górny róg "Complete Sprint
#. Zadania niezakończone mają "spaść" do sprintu następnego, tj. "2020-11 week 1"

    - Co się dzieje z otwartymi zadaniami?
    - Co się dzieje z zamkniętymi zadaniami?
    - Co się dzieje z zamkniętymi subtaskami, ale otwartym zadaniem?
    - Co się dzieje z otwartymi subtaskami ale zamkniętym zadaniem?

Board Reports
-------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Reports"
#. Przedyskutuj "Burndown Chart"
#. Przedyskutuj "Burnup Chart"
#. Przedyskutuj "Sprint Report"
#. Przedyskutuj "Velocity Chart"
#. Przedyskutuj "Cumulative Flow Diagram"
#. Przedyskutuj "Version Report"
#. Przedyskutuj "Epic Report"
#. Przedyskutuj "Control Chart"
#. Przedyskutuj "Epic Burndown"
#. Przedyskutuj "Release Burndown"
#. Przedyskutuj "Time Tracking Report"








