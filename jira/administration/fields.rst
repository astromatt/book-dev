******
Fields
******


Custom Fields
=============
- Dobre praktyki
- Ile?
- Konsekwencje
- CF w bazie dancyh
- Javascript w opisie (nie używać)


Field Configuration
===================


Field Configuration Schemes
===========================



Assignments
===========

Custom Field
------------
#. Stwórz Custom Field "People Assigned":

    - W polu mamy mieć możliwość przypisywania wielu użytkowników do zadania
    - Pole dodaj ekranu dla zadań w projekcie
    - Stwórz filtr który wyszuka zadania w których jesteś wymieniony w tym Custom Field
    - Na podstawie filtru stwórz tablicę Kanban, z zadaniami które są do Ciebie przypisane w tym Custom Fieldzie
    - Pole ma wyświetlać się w widoku Backlog w kolumnie po prawej stronie
    - Podpowiedź: typ ``User Picker (Multiple Users)``

#. Stwórz Custom Field "Team Assigned":

    - Dodaj 4 zespoły: Team A, Team B, Team C, Team D
    - Można wybrać więcej niż jeden zespół
    - Pole dodaj ekranu dla zadań w projekcie
    - Pole ma być wymagane przy tworzeniu nowego zadania
    - Podpowiedź: typ ``Checkbox``

#. Stwórz Custom Field "Manhours":

    - Pole dodaj ekranu dla zadań w projekcie
    - Stwórz nowy board do projektu z estymacją w Manhours
    - Stwórz filtr, który wyciągnie wszystkie zadania z projektu
    - Na filtrze mają być kolumny: Key, Summary, Original Time Estimate, Manhours, Status
    - Podpowiedź: typ ``Number``

