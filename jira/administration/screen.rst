******
Screen
******


Screens
=======
* Definiowanie
* Podłączanie do workflow
* Przypisywanie custom fields
* Jak dodać screen do statusu w workflow?


Screen Schemes
==============
* Screen dla edycji
* Screen dla view
* Rozróżnienie screenów jest deprecated


Issue Type Screen Scheme
========================


Assignments
===========

Screen Configuration
--------------------
#. Skrót klawiszowy ``gg`` -> `Screens`

    * Przycisk `Add screen` (po prawej u góry) -> `Name`: `Imię Log Work` -> Przycisk `Add`
    * Dodaj pole `Log Work` do `Screen`

#. Skrót klawiszowy ``gg`` -> `Screens`

    * Przycisk `Add screen` (po prawej u góry) -> `Name`: `Imię Comment` -> `Add`
    * Nie dodawaj żadnego pola

Screen Workflow Mapping
-----------------------
#. Skrót klawiszowy ``gg`` -> `Workflows`

    * Wybierz Twój workflow -> link `Edit` (po prawej)
    * Wybierz tranzycję `To Done` (z `In Review` do `Done`) -> link `Edit` (z menu po prawej) -> `Screen`: `Imię Log Work` -> Przycisk `Save`
    * Wybierz tranzycję `All` (do statusu `Blocked`) -> link `Edit` (z menu po prawej) -> `Screen`: `Imię Comment` -> -> Przycisk `Save`
    * Kliknij przycisk `Publish` (po prawej u góry) -> `Save a backup copy?`: `No` -> Przycisk `Publish`

#. Wróć na swój `Board` i odśwież stronę w przeglądarce (zawsze dobrze to zrobić po zmianach konfiguracji)
#. Przenieś zadanie do statusu `Blocked` -> powinno wyskoczyć okno z prośbą o komentarz
#. Przenieś zadanie do `In Test`, następnie do `In Review` a następnie do `Done` -> powinno wyskoczyć okno z prośbą o zalogowanie czasu pracy
