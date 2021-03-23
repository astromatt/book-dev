Issue
=====


Rationale
---------
* `Create Issue`
* `View Issue`
* `Edit Issue`
* `Show Issue on Backlog`


Issue Types
-----------
* `Bug`
* `Task`
* `Story`
* `Epic`
* `Sub-task`


Demonstration
-------------
* Create issue: select project, issuetype, set summary
* Create issue in backlog
* Split issue in backlog
* Edit issue and modify values
* Select multiple issues in backlog (`ctrl` and `shift`)
* Send to top, send to bottom
* Add flag, remove flag
* Create version from backlog view
* Drag issues to versions
* Create `Epic`
* Drag issue to `Epic`


Assignments
-----------

Basics Issue Create
^^^^^^^^^^^^^^^^^^^
#. Z menu u góry kliknij przycisk `Create`
#. Dodaj zadanie:

    - Project: Twój project
    - Issue Type: `Task`
    - Summary: `One`

Basics Issue Create in Backlog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog`
#. Na dole w backlog jest napis `Create Issue`
#. Klikając na ikonkę, wybierz `Task` (niebieska ikona)
#. Dodaj zadania do backlog:

    - `Two`,
    - `Three`,
    - `Four`,
    - `Five`,
    - `Six`.

Basics Issue Split
^^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog`
#. Kliknij prawym klawiszem myszy na zadanie `Six` -> `Split Issue`

    - `Six`
    - `Seven`
    - `Eight`
    - `Nine`

#. Zwróć uwagę, że trzeba kliknąć prawym klawiszem myszy na zadaniu w backlog (na jego treści, a nie kluczu)

Issue Backlog
^^^^^^^^^^^^^
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog` (w menu po lewej stronie)
#. Zaznacz wszystkie issues za pomocą klikania i trzymania klawisza `shift`
#. Zaznacz trzy dowolne issues za pomocą klikania i trzymania klawisza `ctrl` (klawisz `cmd` na macOS)
#. Wybierz zadanie `One` -> prawy klawisz myszy -> `Send to Bottom of the backlog`
#. Wybierz zadanie `One` -> prawy klawisz myszy -> `Send to Top of the backlog` (gdzie się przeniosło?)
#. Wybierz zadanie `Two` -> prawy klawisz myszy -> `Add Flag`
#. Wybierz zadanie `Two` -> prawy klawisz myszy -> `Remove Flag`

Issue Versions
^^^^^^^^^^^^^^
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
^^^^^^^^^^
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
