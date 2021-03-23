Issue Backlog
=============


Rationale
---------
* `Show Issue on Backlog`


Demonstration
-------------
* Select multiple issues in backlog (`ctrl` and `shift`)
* Send to top, send to bottom
* Add flag, remove flag
* Create version from backlog view
* Drag issues to versions
* Create `Epic`
* Drag issue to `Epic`
* Bulk change multiple issues in backlog


Assignments
-----------

Issue Backlog Manage
^^^^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog` (w menu po lewej stronie)
#. Zaznacz wszystkie issues za pomocą klikania i trzymania klawisza `shift`
#. Zaznacz trzy dowolne issues za pomocą klikania i trzymania klawisza `ctrl` (klawisz `cmd` na macOS)
#. Wybierz zadanie `One` -> prawy klawisz myszy -> `Send to Bottom of the backlog`
#. Wybierz zadanie `One` -> prawy klawisz myszy -> `Send to Top of the backlog` (gdzie się przeniosło?)
#. Wybierz zadanie `Two` -> prawy klawisz myszy -> `Add Flag`
#. Wybierz zadanie `Two` -> prawy klawisz myszy -> `Remove Flag`

Issue Backlog Versions
^^^^^^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog` -> `Backlog` (w menu po lewej stronie)
#. Otwórz menu z wersjami po lewej stronie od backlog
#. Dodaj wersje:

    * `2000-01` (z datą rozpoczęcia i zakończenia),
    * `2000-02` (z datą rozpoczęcia i zakończenia),
    * `2000-03` (bez ustawiania dat),

#. Przeciągnij zadanie `One`, `Two`, `Three`, `Four` do wersji `2000-01`
#. Przeciągnij zadanie `Five`, `Six`, `Seven` do wersji `2000-02`
#. Przeciągnij zadanie `Eight`, `Nine` do wersji `2000-03`

Issue Backlog Epic
^^^^^^^^^^^^^^^^^^
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
^^^^^^^^^^^^^^^^^
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
