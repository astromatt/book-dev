*****
Issue
*****


Rationale
=========
* `Create Issue`
* `View Issue`
* `Edit Issue`
* `Show Issue on Backlog`


Issue Types
===========
* `Bug`
* `Task`
* `Story`
* `Epic`
* `Sub-task`


Priority
========
* `Highest`, `High`, `Medium`, `Low`, `Lowest`
* `Blocker`, `Highest`, `High`, `Medium`, `Low`
* MoSCoW: `Must`, `Should`, `Could`, `Won't`
* `Must`, `Should`, `Could`
* `Important`, `Normal`
* `Expedite`, `Standard`
* `Urgent`, `Important`, `Standard`


Description
===========
- Acceptance criteria
- Description: **INFO**
- Description: **BEFORE**
- Description: **TODO**
- Description: **AFTER**
- using (/) and (x)


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


Demonstration
=============
* Edit issue and modify values
* Change inline issue field value
* Select multiple issues in backlog (`ctrl` and `shift`)
* Send to top, send to bottom
* Add flag, remove flag
* Create version from backlog view
* Drag issues to versions
* Create `Epic`
* Drag issue to `Epic`
* Bulk change multiple issues in backlog
* Edit issue and create issue link
* Create issue subtask and change priority


Assignments
===========

Issue Priority
--------------
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog`
#. Edytuj zadanie `One`
#. Ustaw `Priority` na `Highest`

Issue Backlog
-------------
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog` (w menu po lewej stronie)
#. Zaznacz wszystkie issues za pomocą klikania i trzymania klawisza `shift`
#. Zaznacz trzy dowolne issues za pomocą klikania i trzymania klawisza `ctrl` (klawisz `cmd` na macOS)
#. Wybierz zadanie `One` -> prawy klawisz myszy -> `Send to Bottom of the backlog`
#. Wybierz zadanie `One` -> prawy klawisz myszy -> `Send to Top of the backlog` (gdzie się przeniosło?)
#. Wybierz zadanie `Two` -> prawy klawisz myszy -> `Add Flag`
#. Wybierz zadanie `Two` -> prawy klawisz myszy -> `Remove Flag`

Issue Versions
--------------
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog` -> `Backlog` (w menu po lewej stronie)
#. Otwórz menu z wersjami po lewej stronie od backlog
#. Dodaj wersje:

    * `2000-01` (z datą rozpoczęcia i zakończenia),
    * `2000-02` (z datą rozpoczęcia i zakończenia),
    * `2000-03` (bez ustawiania dat),

#. Przeciągnij zadanie `One`, `Two`, `Three`, `Four` do wersji `2000-01`
#. Przeciągnij zadanie `Five`, `Six`, `Seven` do wersji `2000-02`
#. Przeciągnij zadanie `Eight`, `Nine` do wersji `2000-03`

Issue Epic
----------
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog` -> `Backlog` (w menu po lewej stronie)
#. Dodaj `Epic` z polami:

    * `Epic Name`: `Logowanie`
    * `Summary`: `Logowanie`
    * `Due Date`: `1/Jan/00`

#. Dodaj `Epic` z polami:

    * `Epic Name`: `Wyszukiwarka`
    * `Summary`: `Wyszukiwarka`
    * `Due Date`: `31/Jan/00`

#. Jeżeli przy tworzeniu `Epic` nie widzisz pola `Due Date` to:

    * sprawdź czy w `Configure fields` (przycisk na górze po prawej okienka popup) jest zaznaczone pole `Due Date` (aby się wyświetlało)
    * sprawdź czy w `Project settings` (trybik w menu po lewej na dole) -> zakładka `Issue types` -> `Epic` -> na liście jest pole `Due Date`

#. Do `Logowanie` dodaj zadania: `One`, `Two`, `Three`
#. Do `Wyszukiwarka` dodaj zadania: `Four`, `Five`, `Seven`
#. Zmień kolor `Logowanie` na jasny niebieski
#. Zmień kolor `Wyszukiwarka` na jasny czerwony
#. Kliknij opcję `All Issues` i zobacz ilość zadań
#. Kliknij opcję `Issues without epics` i zobacz ilość zadań

Issue Bulk Change
-----------------
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

Issue Links
-----------
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog` -> `Backlog` (w menu po lewej stronie)
#. Edytuj zadanie `Nine` (skrót klawiszowy ``e``)
#. Powiąż zadanie linkami:

    * `Linked Issues`: `blocks`
    * `Issue`: `Eight`

Issue Sub-Tasks
---------------
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog` -> `Backlog` (w menu po lewej stronie)
#. Edytuj zadanie `Nine` (skrót klawiszowy ``e``)
#. Dodaj trzy sub-taski:

    * Summary: `A`, Priority: `Highest`
    * summary: `B`, Priority: `Low`
    * summary: `C`, Priority: `Medium`
