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

Date Fields
===========
* `Created Date`
* `Updated Date`
* `Due Date`
* `Start Date` (Jira Cloud)

Other Fields
============
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
=============
* kilka, maks kilkanaście
* Team Assigned
* Start Date
* Business Value
* Manday
* Severity
* Risk



Assignments
===========

Issue Priority
--------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog`
#. Edytuj zadanie `One`
#. Ustaw `Priority` na `Highest`

Issue Backlog
-------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog`
#. Zaznacz wszystkie issues za pomocą klikania i trzymania klawisza `shift`
#. Zaznacz trzy dowolne issues za pomocą klikania i trzymania klawisza `ctrl` (klawisz `cmd` na macOS)
#. Wybierz zadanie `One` -> prawy klawisz myszy -> `Send to Bottom of the backlog`
#. Wybierz zadanie `One` -> prawy klawisz myszy -> `Send to Top of the backlog` (gdzie się przeniosło?)
#. Wybierz zadanie `Two` -> prawy klawisz myszy -> `Add Flag`
#. Wybierz zadanie `Two` -> prawy klawisz myszy -> `Remove Flag`

Issue Versions
--------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog`
#. Otwórz menu z wersjami po lewej stronie od backlog
#. Dodaj wersje:

    * `2000-01` (z datą rozpoczęcia i zakończenia),
    * `2000-02` (z datą rozpoczęcia i zakończenia),
    * `2000-03` (bez ustawiania dat),
    * `2000-04` (bez ustawiania dat),
    * `2000-05` (bez ustawiania dat),
    * `2000-06` (bez ustawiania dat),

#. Przeciągnij zadanie `One`, `Two`, `Three`, `Four` do wersji `2000-01`
#. Przeciągnij zadanie `Five`, `Six`, `Seven` do wersji `2000-02`
#. Przeciągnij zadanie `Eight`, `Nine` do wersji `2000-03`

Issue Epic
----------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog`
#. Dodaj `Epic` z polami:

    * `Epic Name`: `Logowanie`
    * `Summary`: `Logowanie`
    * `Due Date`: `1/Jan/00`

#. Dodaj `Epic` z polami:

    * `Epic Name`: `Wyszukiwarka`
    * `Summary`: `Wyszukiwarka`
    * `Due Date`: `31/Jan/00`

#. Do `Logowanie` dodaj zadania: `One`, `Two`, `Three`
#. Do `Wyszukiwarka` dodaj zadania: `Four`, `Five`, `Seven`
#. Zmień kolor `Logowanie` na jasny niebieski
#. Zmień kolor `Wyszukiwarka` na jasny czerwony
#. Rozwiń opcję `All Issues` i zobacz ilość zadań
#. Rozwiń opcję `Issues without epics` i zobacz ilość zadań

Issue Bulk Change
-----------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog`
#. Zaznacz zadania (trzymając `ctrl` lub `cmd`): `Two`, `Four`, `Six`, `Eight`
#. Kliknij prawym klawiszem myszy -> `Bulk Change` -> `Edit Issues` -> `Next`
#. Zmień issue type na `Task`
#. Rozwiń na dole `Unavailable Actions` i zobacz co tam jest
#. Kliknij `Next` (na dole)
#. Potwierdzamy `Confirm`
#. Po chwili klikamy `Refresh`
#. Po ukończeniu klikamy `Ok, got it`

.. note:: Zwróć uwagę, że po zmianie część zadań w backlog nie ma estymacji w Story Pointach. Te wartości nie zniknęły i są nadal przypisane do zadania, ale na obecnym widoku są ukryte. Story Points (jak sama nazwa wskazuje) domyślnie mogą być przyznawane tylko zadaniom typu `Story`. Można to zmienić w konfiguracji (wymaga uprawnień administratora) `Custom Field` -> `Story Points` -> Ikona trybiku (po prawej) -> `Configure` -> `Applicable contexts for scheme` -> `Edit Configuration`.

Issue Links
-----------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog`
#. Edytuj zadanie `Nine`
#. Powiąż zadanie linkami jako `is blocked by`/`blocks` z `Eight`

Issue Sub-Tasks
---------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog`
#. Edytuj zadanie `Nine`
#. Dodaj trzy sub-taski:

    - Summary: `A`, Priority: `Highest`, Status: `To Do`,
    - summary: `B`, Priority: `Low`, Status: `In Progress`
    - summary: `C`, Priority: `Medium`, Status: `Done`

#. Aby zmienić status trzeba najpierw stworzyć zadanie, a później w jego edycji kliknąć jeden z przycisków na górze ekranu

