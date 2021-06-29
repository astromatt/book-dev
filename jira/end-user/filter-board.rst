Filter Board
============


Demonstration
-------------
* Create board `My TODO` from filter
* Edit filter for board `My TODO`
* Create board portfolio with `Epic` issues
* Delete board `My TODO`


Assignments
-----------

Filter Board Create
^^^^^^^^^^^^^^^^^^^
#. Przejdź do swojego projektu:

    * Server: Z menu u góry wybierz `Boards` -> `View all boards`
    * Cloud: Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog`
    * Cloud: Rozwiń listę rozwijaną w menu u po lewej z napisem `Board`

#. Kliknij przycisk `Create board`:

    * Server: przycisk u góry po prawej
    * Cloud: na dole listy rozwijanej

#. Wybierz `Create a Kanban board` -> `Board from an existing Saved Filter` -> `Next`
#. Board name: `Imię Todo` (gdzie Imię, to Twoje imię)
#. Saved filter: wybrać filtr: `Imię Todo` (gdzie Imię, to Twoje imię)
#. Kliknij przycisk `Create board`

Filter Board Edit
^^^^^^^^^^^^^^^^^
#. Przejdź do swojego projektu:

    * Server: Z menu u góry wybierz `Boards` -> `View all boards` -> `Imię Todo` (gdzie Imię, to Twoje imię)
    * Cloud: Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog`
    * Cloud: Rozwiń listę rozwijaną w menu u po lewej z napisem `Board`

#. Przycisk `Board` (u góry po prawej) -> `Configure` -> Na zakładce `General` -> `Edit Filter Query`
#. Popraw zapytanie:

    .. code-block:: sql

        assignee = currentUser()
            AND issuetype != "Epic"
            AND (statusCategory != "Done"
                 AND due <= 7d
                 OR Flagged is not EMPTY)
            ORDER BY duedate DESC, priority DESC

#. Przycisk `Search` -> `Save`
#. Przejdź na Board `Imię Todo` (gdzie Imię, to Twoje imię)
#. Zobacz czy nie ma zadań typu `Epic`

Filter Board Portfolio
^^^^^^^^^^^^^^^^^^^^^^
#. Przejdź do wyszukiwania zadań:

    * Cloud: Z menu `Filters` wybrać `Advanced Issue Search` w trybie `Switch to JQL`
    * Server: Z menu `Issues` wybrać `Search for Issues` w trybie `Advanced`

#. Stwórz filtr, który wyszukuje w Twoim projekcie zadań typu `Epic`
#. Nazwij filtr: `Imię Portfolio` (gdzie Imię, to Twoje imię)
#. Z menu u góry wybierz `Boards` -> `View all boards`
#. Kliknij przycisk `Create board` (przycisk u góry po prawej)
#. Wybierz `Create a Kanban board` -> `Board from an existing Saved Filter` -> `Next` -> `Imię Portfolio` (gdzie Imię, to Twoje imię)
#. Stwórz dwa `Swimlane`: `2000-Q1` i `2000-Q1`, zapytania:

    * Określ aby w kolumnie `In Progress` mogły być maksymalnie 3 zadania

#. Stwórz board zadań przypisanych do Ciebie:

    * zadania mogą być w dowolnym projekcie
    * board ma być publiczny

.. note:: Board nie może korzystać z Kanban Backlog, a dokładnie z opcji `Epics panel`. Jeżeli ta opcja w konfiguracji board jest włączona, to Epiki zostaną wykorzystane jako panel w widoku backlog (a tego nie chcemy).

Filter Board Delete
^^^^^^^^^^^^^^^^^^^
#. Przejdź do swojego projektu:

    * Server: Z menu u góry wybierz `Boards` -> `View all boards`
    * Cloud: Z menu u góry wybierz `Projects` -> Twój Projekt -> `Backlog`

#. Wybierz swój board:

    * Server: Poszukaj swojego Board `Imię Todo` (gdzie Imię, to Twoje imię)
    * Cloud: Rozwiń listę rozwijaną w menu u po lewej z napisem `Board`

#. Kliknij trzy kropeczki `...` po prawej stronie
#. Delete i potwierdzasz przyciskiem `Delete`
