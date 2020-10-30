*****
Field
*****


Custom Fields
=============
- Dobre praktyki
- Ile?
- Konsekwencje
- CF w bazie danych
- Javascript w opisie (nie używać)


Field Configuration
===================


Field Configuration Schemes
===========================



Assignments
===========

Field Required Global
---------------------
#. Skrót klawiszowy "gg" -> "Field Configuration"
#. "Default Configuration" -> link "Configure" (po prawej)
#. Znajdź pole "Due Date" -> kliknij link "Required" (po prawej stronie)

Field Required per Project
--------------------------
#. Skrót klawiszowy "gg" -> "Field Configuration"
#. "Default Configuration" -> link "Copy" (po prawej)
#. "Name": "Imię Field Configuration" -> przycisk "Copy"
#. "Imię Field Configuration" -> link "Configure" (po prawej)
#. Znajdź pole "Due Date" -> kliknij link "Required" (po prawej stronie)

#. skrót klawiszowy "gg" -> "Field Configuration Scheme"
#. "Add field configuration scheme" (po prawej) -> "Imię Field Configuration Scheme" -> przycisk "Add"
#. "Imię Field Configuration Scheme" -> link "Configure" (po prawej)
#. Tu można mapować, jakie issue type ma mieć jakie "Field Configuration"
#. "Associate an issue type with a field configuration" (po prawej):

    - "Issue Type": "Epic"
    - "Field Configuration": "Imię Field Configuration"
    - Przycisk "Add"

Field Custom Numeric
--------------------
#. Stwórz Custom Field "Manhours":

    - Pole dodaj ekranu dla zadań w projekcie
    - Stwórz nowy board do projektu z estymacją w Manhours
    - Stwórz filtr, który wyciągnie wszystkie zadania z projektu
    - Na filtrze mają być kolumny: Key, Summary, Original Time Estimate, Manhours, Status
    - Podpowiedź: typ ``Number``

Field Custom User Picker
------------------------
#. Stwórz Custom Field "People Assigned":

    - W polu mamy mieć możliwość przypisywania wielu użytkowników do zadania
    - Pole dodaj ekranu dla zadań w projekcie
    - Stwórz filtr który wyszuka zadania w których jesteś wymieniony w tym Custom Field
    - Na podstawie filtru stwórz tablicę Kanban, z zadaniami które są do Ciebie przypisane w tym Custom Fieldzie
    - Pole ma wyświetlać się w widoku Backlog w kolumnie po prawej stronie
    - Podpowiedź: typ ``User Picker (Multiple Users)``

Field Custom Group Picker
-------------------------
#. Stwórz Custom Field "Team Assigned":

    - Dodaj 4 zespoły: Team A, Team B, Team C, Team D
    - Można wybrać więcej niż jeden zespół
    - Pole dodaj ekranu dla zadań w projekcie
    - Pole ma być wymagane przy tworzeniu nowego zadania
    - Podpowiedź: typ ``Checkbox``

