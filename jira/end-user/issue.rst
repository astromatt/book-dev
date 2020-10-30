*****
Issue
*****


Issue Types
===========
* Bug
* Task
* User Story
* Epic
* Sub-task


Issue Fields
============
* Components

    - Component Leaders

* Labels
* Links
* Assignee
* Reporter


Custom Fields
=============
* kilka, maks kilkanaście
* Team Assigned
* Start Date (and Due Date)


Versions
========
* Roadmap
* Releases (with Bamboo)
* Semantic Versioning: major.minor.bugfix - (1.2.3, 3.9.1)
* Konwencja nazewnicza YYYY-MM (2000-01, 2000-02, 2000-03)
* Konwencja nazewnicza YYYY-QX - (2000-Q1, 2000-Q2, 2000-Q3, 2000-Q4)
* Konwencja nazewnicza YYYY - (2000, 2001, 2002, 2003)
* Time Tracking Report by Version
* affectsVersion vs. fixVersion


Priorities
==========
* Lower, Low, Medium, High, Highest
* MoSCoW: Must, Should, Could
* Low, Medium, High, Highest, Blocker
* Urgent, Important, Standard
* Important, Normal
* Expedite, Standard
* Top, Normal, Bottom
* Important, Normal, Someday/Maybe
* DEFCON-1, DEFCON-2, DEFCON-3


Statusy
=======
* To Do
* In Progress
* Done
* In Review
* Waiting / Blocked
* In Test


Resolutions
===========
* Fixed
* Won't Fix
* Duplicate
* Cannot Reproduce
* Incomplete
* [Jira Agile] -> Done


Issue Actions
=============
* Workflow Actions (Open, In Progress, Done)
* Voting
* Watching
* Add Attachments
* Clone
* Move
* Create subtask
* Delete (kiedy?)
* Log Work
* Keyboard Shortcuts
* Comment

    - Mentions
    - Rich Text Editing
    - Tworzenie tabelek
    - Używanie formatowania


Time Reporting
==============
* Original Time Estimate
* Remaining Time
* Log Work
* Reports
* Monte Carlo Estimation:

    * https://www.infoq.com/presentations/monte-carlo/
    * https://docs.google.com/spreadsheets/d/1BmSuj1jA2ZfhUBzPtqDBqDjMjSXMqj3QoHZGR-TesOA/edit#gid=542217325
    * Roadmaps: Start Date, Due Date


Assignments
===========

Issues Create
-------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Dodaj zadania do backlog: "One", "Two", "Three", "Four", "Five", "Six"
#. Kliknij prawym klawiszem myszy na zadanie "Six" -> "Split Issue"

    - "Six" - Estimate: 1
    - "Seven" - Estimate: 2
    - "Eight" - Estimate: 3
    - "Nine" - Estimate: 4

Issue Edit
----------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Edytuj zadanie "One"
#. Ustaw "Priority" na "Highest"

Issue Log Work
--------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprints"
#. Wybierz dowolne zadanie i otwórz szczegóły zadania na nowej zakładce w przeglądarce
#. Wybierz z menu trzech kropek "..." (u góry) -> Log Work
#. Alternatywnie po wybraniu zadania klikasz skrót klawiszowy kropka "." -> Log Work

Issue Attachment
----------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Edytuj zadanie "One"
#. Do zadania dodaj załącznik

    - obrazek ".png" lub ".jpg"
    - archiwum ".zip" z przynajmniej dwoma plikami tekstowymi

Issue Clone
-----------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Sklonuj zadanie "One"

    - z załącznikami
    - ze zachowaniem sprintu

Issue Backlog
-------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Zaznacz wszystkie issues za pomocą klikania i trzymania klawisza Shift
#. Zaznacz trzy issues za pomocą klikania i trzymania klawisza Ctrl (klawisz Cmd na macOS)
#. Wybierz zadanie "One" -> Prawy klawisz myszy -> Send to "Bottom of the backlog"
#. Wybierz zadanie "One" -> Prawy klawisz myszy -> Send to "Top of the backlog" (gdzie się przeniosło?)
#. Wybierz zadanie "Two" -> Prawy klawisz myszy -> "Add Flag"
#. Wybierz zadanie "Two" -> Prawy klawisz myszy -> "Remove Flag"

Issue Versions
--------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Dodaj wersje: "2020-10", "2020-11", "2020-12" z datami rozpoczęcia i zakończenia miesiąca
#. Przeciągnij zadanie "One", "Two", "Three", "Four" do wersji "2020-10"
#. Przeciągnij zadanie "Five", "Six", "Seven" do wersji "2020-11"
#. Przeciągnij zadanie "Eight", "Nine" do wersji "2020-12"

Issue Epic
----------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Dodaj Epic -> Epic Name "Logowanie", "Summary" -> "Logowanie", Due Date: "1/Nov/20"
#. Dodaj Epic -> Epic Name "Wyszukiwarka", Summary "Wyszukiwarka", Due Date: "10/Nov/20"
#. Zmień "Logowanie" Epic Color na jasny niebieski
#. Zmień "Wyszukiwarka" Epic Color na jasny czerwony
#. Do Epic "Logowanie" dodaj zadania "One", "Two", "Three"
#. Do Epic "Wyszukiwarka" dodaj zadania "Four", "Five", "Seven"
#. Kliknij na "All Issues", później na "Issues without epics" i porównaj ilość zadań

Issue Estimation
----------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. W detail view zadania "One" -> "Estimate" ustaw 3h, [menu kropeczki] -> Log Work -> Time Spent: 2h
#. W detail view zadania "Two" -> "Estimate" ustaw 8h
#. W detail view zadania "Three" -> "Estimate" ustaw 4h
#. Zobacz kolorowe kółka z estymacjami w nagłówku sprintu: "To Do", "In Progress", "Done"

Issue Bulk Change
-----------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Zaznacz zadania (trzymając Ctrl lub Cmd): "Two", "Four", "Six", "Eight"
#. Kliknij prawym klawiszem myszy -> "Bulk Change" -> "Edit Issues" -> Next
#. Zmień issue type na "Task"
#. Rozwiń na dole "Unavailable Actions" i zobacz co tam jest
#. Kliknij "Next" (na dole)
#. Potwierdzamy "Confirm"
#. Po chwili klikamy "Refresh"
#. Po ukończeniu klikamy "Ok, got it"
#. Zwróć uwagę, że po zmianie część zadań w backlog nie ma story pointów (Story Pointy domyślnie mogą być przyznawane tylko zadaniom typu "Story")

Issue Links
-----------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Edytuj zadanie "Nine"
#. Powiąż zadanie linkami jako "is blocked by"/"blocks" z "Eight"

Issue Sub-Tasks
---------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Edytuj zadanie "Nine"
#. Dodaj trzy sub-taski:

    - status pierwszego: "To Do"
    - status drugiego: "In Progress"
    - status trzeciego: "Done"
    - wyceń każde z zadań na 2h

Issue Move
----------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Przenieś zadanie z projektu do innego projektu

    - nie wysyłaj informacji mailem o zmianach
