*******************
Board Configuration
*******************


Project Management
==================
- Kanban
- Scrum
- Scrum + Kanban
- Portfolio


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



Assignments
===========

Board Configuration General
---------------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Z menu "Board" (prawy górny róg) -> "Configure"
#. Zakładka "General":

    - Usuń administratora "admin@example.com"
    - Zwróć uwagę na "Edit Filter Shares", "View Permissions"
    - Osoby które mają uprawnienia do "Filter" będą widziały i mogły otworzyć Board
    - To nie znaczy, że będę widziały zadania (to wymaga uprawnień w projekcie)

Board Configuration Columns
---------------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Z menu "Board" (prawy górny róg) -> "Configure"
#. Zakładka "Columns":

    - Dodaj kolumnę "Blocked" w "Category" -> "In Progress"
    - Dodaj status "Rejected" w "Category" -> "Done" do kolumny "Done" i zaznacz "Set resolution"
    - Column Constraints "Issue Count, excluding sub-tasks
    - W kolumnie "Blocked" -> "Max" ustaw na: "2
    - W kolumnie "In Progress" -> "Min" ustaw na: "1"
    - Zaznacz "Days in column"

Board Configuration Swimlanes
-----------------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Z menu "Board" (prawy górny róg) -> "Configure"
#. Zakładka "Swimlanes":

    - Wybierz "Base Swimlanes on" -> "Queries"
    - Dodaj Swimlane "Story" z JQL -> ``issuetype = Story``
    - Dodaj Swimlane "Task" z JQL -> ``issuetype = Task``

Board Configuration Quick Filters
---------------------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Z menu "Board" (prawy górny róg) -> "Configure"
#. Zakładka "Quick Filters":

    - Zmień nazwę "Recently Updated" na "Daily"
    - Zmień JQL dla "Daily" na: ``updatedDate >= -1d OR Flagged IS NOT EMPTY``

Board Configuration Card Colors
-------------------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Z menu "Board" (prawy górny róg) -> "Configure"
#. Zakładka "Card colours":

    - Zmień "Colours based on" -> "Priorities"
    - Zmień kolor "Highest" oraz "High" na czerwony (FF0000)
    - Zmień kolor "Medium" na żółty (FFFF00)
    - Zmień kolor "Low" oraz "Lowest" na zielony (00FF00)

Board Configuration Card Layout
-------------------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Z menu "Board" (prawy górny róg) -> "Configure"
#. Zakładka "Card layout":

    - W sekcji "Backlog" -> wyświetl pole "Due Date"
    - W sekcji "Active sprints" -> wyświetl pole "Due Date"
    - Usuń wyświetlanie pola "Due Date" z sekcji Backlog (ale zostaw w "Active Sprint")

Board Configuration Estimation
------------------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Z menu "Board" (prawy górny róg) -> "Configure"
#. Zakładka "Estimation":

    - Zmień "Estimation Statistic" na "Original Time Estimate"
    - Zaznacz "Time Tracking" -> "Remaining Estimate and Time Spent"

Board Configuration Working Days
--------------------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Z menu "Board" (prawy górny róg) -> "Configure"
#. Zakładka "Working days":

    - Wybierz "Region" -> "Europe"
    - "Time Zone" -> "(GMT+01:00) Warsaw"
    - Dodaj "Non-Working Days" (wybierz trzy dowolne święta):

        * "1/Jan/00" (Nowy Rok)
        * "6/Jan/00" (Święto Trzech Króli)
        * "?/?/00" (pierwszy dzień Wielkiej Nocy)
        * "?/?/00" (drugi dzień Wielkiej Nocy)
        * "1/May/00" (Święto Państwowe)
        * "3/May/00" (Święto Narodowe Trzeciego Maja)
        * "?/?/00" (pierwszy dzień Zielonych Świątek) [pięćdziesiąt dni po wielkanocy]
        * "?/?/00" (dzień Bożego Ciała) [sześćdziesiąt dni po wielkanocy]
        * "15/Aug/00" (Wniebowzięcie Najświętszej Marii Panny / Święto Wojska Polskiego)
        * "1/Nov/00" (Wszystkich Świętych)
        * "11/Nov/00" (Narodowe Święto Niepodległości)
        * "25/Dec/00" (pierwszy dzień Bożego Narodzenia)
        * "26/Dec/00" (drugi dzień Bożego Narodzenia)

Board Configuration Issue Detail View
-------------------------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Z menu "Board" (prawy górny róg) -> "Configure"
#. Zakładka "Issue Detail View":

    - Sekcja "General Fields" -> usuń: Status, Priority, Labels, Affects Version/s
    - Sekcja "Date Fields" -> dodaj "Due Date", usuń: "Created" i "Updated
    - Sekcja "People" -> usuń "Reporter" i "Assignee
    - Sekcja "Links" -> usuń "Linked Issue"

Board Configuration Active Sprint
---------------------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Z menu "Board" (prawy górny róg) -> "Configure"
#. Wróć na "Boards" -> Twój Board -> "Active Sprint":

    - Usuń wszystkie zadania z kolumny "In Progress" (powinna podświetlić się na żółto)
    - Dodaj trzy zadania do kolumny "Blocked" (powinna podświetlić się na czerwono)
