*****
Issue
*****


Rationale
=========
* Create Issue
* View Issue
* Edit Issue
* Show Issue on Backlog


Issue Types
===========
* Bug
* Task
* Story
* Epic
* Sub-task


Fields
======
* Summary
* Issue Type
* Reporter
* Components
* Description
* Fix Version/s
* Priority
* Labels
* Attachment
* Linked Issues
* Assignee
* Epic Link
* Sprint
* Comment
* Status
* Affects Version/s
* Created Date
* Updated Date
* Due Date
* Comments
* Sub-Tasks
* Votes
* Watchers


Custom Fields
=============
* kilka, maks kilkanaście
* Team Assigned
* Start Date
* Business Value
* Manday
* Severity
* Risk


Priority
========
* Highest, High, Medium, Low, Lowest
* [MoSCoW] Must, Should, Could, Won't
* Must, Should, Could
* Blocker, Highest, High, Medium, Low
* Urgent, Important, Standard
* Important, Normal
* Important, Normal, Someday/Maybe
* Expedite, Standard
* DEFCON-1, DEFCON-2, DEFCON-3


Description
===========
- Kryteria akceptacyjne
- Sekcja w description: INFO
- Sekcja w description: BEFORE
- Sekcja w description: TODO
- Sekcja w description: AFTER
- używanie (/) i (x)


Assignments
===========

Issue Priority
--------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Edytuj zadanie "One"
#. Ustaw "Priority" na "Highest"

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
#. Dodaj wersje: "2000-01", "2000-02", "2000-03", "2000-04", "2000-05", "2000-06" z datami rozpoczęcia i zakończenia miesiąca
#. Przeciągnij zadanie "One", "Two", "Three", "Four" do wersji "2000-01"
#. Przeciągnij zadanie "Five", "Six", "Seven" do wersji "2000-02"
#. Przeciągnij zadanie "Eight", "Nine" do wersji "2000-03"

Issue Epic
----------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Dodaj Epic -> Epic Name "Logowanie", "Summary" -> "Logowanie", Due Date: "1/Jan/21"
#. Dodaj Epic -> Epic Name "Wyszukiwarka", Summary "Wyszukiwarka", Due Date: "31/Jan/21"
#. Zmień "Logowanie" Epic Color na jasny niebieski
#. Zmień "Wyszukiwarka" Epic Color na jasny czerwony
#. Do Epic "Logowanie" dodaj zadania "One", "Two", "Three"
#. Do Epic "Wyszukiwarka" dodaj zadania "Four", "Five", "Seven"
#. Kliknij na "All Issues", później na "Issues without epics" i porównaj ilość zadań

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

    - Summary: "A", Priority: "Highest", Status: "To Do",
    - summary: "B", Priority: "Low", Status: "In Progress"
    - summary: "C", Priority: "Medium", Status: "Done"

#. Estymuj zadania, tylko jeżeli widzisz pole
