***********
Assignments
***********


Logging
-------
#. Wejdź na stronę Jiry na adres podany przez prowadzącego
#. Zaloguj się wykorzystując swoje imię jako login i hasło (bez polskich znaków i z małej litery)


Create Project
--------------
#. Z menu u góry wybierz "Projects" -> "View Projects"
#. Kliknij przycisk "Create Projects" (prawy górny róg)
#. Kliknij przycisk "Scrum software development" -> Next
#. Ustaw:

    - Project name: wpisz swoje imię
    - Project key: wpisz swoje imię (dużymi literami)
    - Project Lead: ustaw siebie

#. Submit


Create Issues
-------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Dodaj zadania do backlog: "One", "Two", "Three", "Four", "Five", "Six"
#. Kliknij prawym klawiszem myszy na zadanie "Six" -> "Split Issue"

    - "Six" - Estimate: 1
    - "Seven" - Estimate: 2
    - "Eight" - Estimate: 3
    - "Nine" - Estimate: 4


Backlog
-------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Zaznacz wszystkie issues za pomocą klikania i trzymania klawisza Shift
#. Zaznacz trzy issues za pomocą klikania i trzymania klawisza Ctrl (klawisz Cmd na macOS)
#. Wybierz zadanie "One" -> Prawy klawisz myszy -> Send to "Bottom of the backlog"
#. Wybierz zadanie "One" -> Prawy klawisz myszy -> Send to "Top of the backlog" (gdzie się przeniosło?)
#. Wybierz zadanie "Two" -> Prawy klawisz myszy -> "Add Flag"
#. Wybierz zadanie "Two" -> Prawy klawisz myszy -> "Remove Flag"


Versions
--------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Dodaj wersje: "2020-10", "2020-11", "2020-12" z datami rozpoczęcia i zakończenia miesiąca
#. Przeciągnij zadanie "One", "Two", "Three", "Four" do wersji "2020-10"
#. Przeciągnij zadanie "Five", "Six", "Seven" do wersji "2020-11"
#. Przeciągnij zadanie "Eight", "Nine" do wersji "2020-12"


Epic
----
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Dodaj Epic -> Epic Name "Logowanie", "Summary" -> "Logowanie", Due Date: "1/Nov/20"
#. Dodaj Epic -> Epic Name "Wyszukiwarka", Summary "Wyszukiwarka", Due Date: "10/Nov/20"
#. Zmień "Logowanie" Epic Color na jasny niebieski
#. Zmień "Wyszukiwarka" Epic Color na jasny czerwony
#. Do Epic "Logowanie" dodaj zadania "One", "Two", "Three"
#. Do Epic "Wyszukiwarka" dodaj zadania "Four", "Five", "Seven"
#. Kliknij na "All Issues", później na "Issues without epics" i porównaj ilość zadań


Estimation
----------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. W detail view zadania "One" -> "Estimate" ustaw 3h, [menu kropeczki] -> Log Work -> Time Spent: 2h
#. W detail view zadania "Two" -> "Estimate" ustaw 8h
#. W detail view zadania "Three" -> "Estimate" ustaw 4h
#. Zobacz kolorowe kółka z estymacjami w nagłówku sprintu: "To Do", "In Progress", "Done"


Bulk Change
-----------
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


Add Sprints
-----------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Dodaj pierwszy sprint:

    - "Name": "2020-11 week 1"
    - "Duration": "1 week"
    - "Start Date": "1/Nov/20 09:00 AM"

#. Dodaj drugi sprint:

    - "Name": "2020-11 week 2"
    - "Duration": "1 week"
    - "Start Date": "7/Nov/20 09:00 AM"


Rozpoczęcie Sprintu
-------------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Backlog"
#. Do sprintu "2020-11 week 1" dodaj zadania: "One", "Two", "Three"
#. Przejedź suwakiem i dodaj "Four", "Five", "Six", zwróć uwagę na zmiany liczb w okienku "Issues" i "Estimate"
#. Wystartuj sprint ustawiając:

    - Goal: "Ukończenie szkolenia z Jiry"
    - Duration: "1 week"
    - Start Date: "26/Oct/20 09:30 AM"


Active Sprint
-------------
#. Z menu u góry wybierz "Boards" -> Twój Board
#. Przejdź na ekran Active Sprints
#. Przenieś zadania:

    - "One" do "In Progress"
    - "Two" do "In Progress"
    - "Three" do "Done"

#. Dodaj flagę do zadania "Four"
#. Z menu "Board" prawy górny róg:

    - Wybierz "Hide detail view
    - Wybierz "Print cards" i zmień "Card size" -> "small"


Board Configuration
-------------------
#. Z menu u góry wybierz "Boards" -> Twój Board
#. Z menu "Board" (prawy górny róg) -> "Configure"
#. Zakładka "General":

    - Usuń administratora "admin@example.com"
    - Zwróć uwagę na "Edit Filter Shares", "View Permissions"
    - Osoby które mają uprawnienia do "Filter" będą widziały i mogły otworzyć Board
    - To nie znaczy, że będę widziały zadania (to wymaga uprawnień w projekcie)

#. Zakładka "Columns":

    - Dodaj kolumnę "Blocked" w "Category" -> "In Progress"
    - Dodaj status "Rejected" w "Category" -> "Done" do kolumny "Done" i zaznacz "Set resolution"
    - Column Constraints "Issue Count, excluding sub-tasks
    - W kolumnie "Blocked" -> "Max" ustaw na: "2
    - W kolumnie "In Progress" -> "Min" ustaw na: "1"
    - Zaznacz "Days in column"

#. Zakładka "Swimlanes":

    - Wybierz "Base Swimlanes on" -> "Queries"
    - Dodaj Swimlane "Story" z JQL -> ``issuetype = Story``
    - Dodaj Swimlane "Task" z JQL -> ``issuetype = Task``

#. Zakładka "Quick Filters":

    - Zmień nazwę "Recently Updated" na "Daily"
    - Zmień JQL dla "Daily" na: ``updatedDate >= -1d OR Flagged IS NOT EMPTY``

#. Zakładka "Card colours":

    - Zmień "Colours based on" -> "Priorities"
    - Zmień kolor "Highest" oraz "High" na czerwony (FF0000)
    - Zmień kolor "Medium" na żółty (FFFF00)
    - Zmień kolor "Low" oraz "Lowest" na zielony (00FF00)

#. Zakładka "Card layout":

    - W sekcji "Backlog" -> wyświetl pole "Due Date"
    - W sekcji "Active sprints" -> wyświetl pole "Due Date"
    - Usuń wyświetlanie pola "Due Date" z sekcji Backlog (ale zostaw w "Active Sprint")

#. Zakładka "Estimation":

    - Zmień "Estimation Statistic" na "Original Time Estimate"
    - Zaznacz "Time Tracking" -> "Remaining Estimate and Time Spent"

#. Zakładka "Working days":

    - Wybierz "Region" -> "Europe"
    - "Time Zone" -> "(GMT+01:00) Warsaw"
    - Dodaj "Non-Working Days":

        * "1/Jan/20" (Nowy Rok)
        * "6/Jan/20" (Święto Trzech Króli)
        * "?/?/20" (pierwszy dzień Wielkiej Nocy)
        * "?/?/20" (drugi dzień Wielkiej Nocy)
        * "1/May/20" (Święto Państwowe)
        * "3/May/20" (Święto Narodowe Trzeciego Maja)
        * "?/?/20" (pierwszy dzień Zielonych Świątek) [pięćdziesiąt dni po wielkanocy]
        * "?/?/20" (dzień Bożego Ciała) [sześćdziesiąt dni po wielkanocy]
        * "15/Aug/20" (Wniebowzięcie Najświętszej Marii Panny / Święto Wojska Polskiego)
        * "1/Nov/20" (Wszystkich Świętych)
        * "11/Nov/20" (Narodowe Święto Niepodległości)
        * "25/Dec/20" (pierwszy dzień Bożego Narodzenia)
        * "26/Dec/20" (drugi dzień Bożego Narodzenia)


#. Zakładka "Issue Detail View":

    - Sekcja "General Fields" -> usuń: Status, Priority, Labels, Affects Version/s
    - Sekcja "Date Fields" -> dodaj "Due Date", usuń: "Created" i "Updated
    - Sekcja "People" -> usuń "Reporter" i "Assignee
    - Sekcja "Links" -> usuń "Linked Issue"

#. Wróć na "Active Sprint Board":

    - Usuń wszystkie zadania z kolumny "In Progress" (powinna podświetlić się na żółto)
    - Dodaj trzy zadania do kolumny "Blocked" (powinna podświetlić się na czerwono)


Zamykanie sprintu
-----------------
#. Z menu u góry wybierz "Boards" -> Twój Board -> "Active Sprint"
#. zakończ aktualny sprint -> Prawy górny róg "Complete Sprint
#. zadania niezakończone mają "spaść" do sprintu następnego, tj. "2020-11 week 1"


Project Settings
----------------
#. Przejdź do "Project Settings" (przycisk w menu na dole po lewej)
#. Zakładka "Components" -> dodaj: "Frontend", "Backend", "Database"
#. Zakładka "Versions" -> dodaj: "2021-Q1", "2021-Q2", "2021-Q3", "2021-Q4"
#. Zakładka "Users and roles" -> dodaj siebie do roli "Administrators", dodaj użytkownika "admin" do roli "Developers"
#. Zakładka "Issue Types" -> Task -> dodaj pole "Due Date", usuń pole "Labels"
#. Zakładka "Issue Types" -> dodaj nową zakładkę "Dates", dodaj na niej pole "Due Date"
#. Zakładka "General" -> zmień awatar swojego projektu na rakietę
#. Zakładka "General" -> zmień nazwę swojego projektu na "Imię N."

gdzie:

- "Imię" to Twoje imię
- "N." to pierwsza litera Twojego nazwiska
- Przykłady: "Jan T.", "Mark W.", "Melissa L.", "Matt K."

Search View
-----------
#. Z menu "Issues" wybrać "Search for Issues"
#. "Change View" [przycisk po prawej stronie] zmień na "List View"
#. "Columns" [przycisk po prawej stronie]: Odznaczyć: "Created", "Updated", "Development"
#. Columns: zaznaczyć: "Summary", "Issue Type", "Due Date", "Fix Version/s", "Epic Link"
#. Chwytając nagłówek kolumny, przenieś "Issue Type" (T) jako pierwsza kolumna
#. Ustawić kolumny w kolejności: "Issue Type", "Issue Key", "Epic Link", "Fix Version/s", "Due Date", "Status", "Summary"
#. Dodać kolumny: "Original Estimate", "Remaining Estimate", "Time Spent"
#. Z menu po prawej stronie u góry wybieramy "Export" -> "CSV (Current Fields)" -> "Delimiter" -> "Comma (,)"

Search Basic
------------
#. Z menu "Issues" wybrać "Search for Issues" w trybie Basic
#. "Project" -> swój projekt
#. Kliknij na nazwę kolumny "Due Date" dwukrotnie aby posortować rosnąco
#. "Status" -> "In Progress" oraz "Blocked"
#. More -> "Due Date" -> "Now Overdue"
#. Zmień zakres "Due Date" -> od "1/Oct/20" do "31/Oct/20"
#. Zmień zakres "Due Date" -> Due in next 8 hours or is overdue
#. Zmień zakres "Due Date" -> In range -7d to ... [pozostaw niewypełnione]

Search Advanced
---------------
#. Z menu "Issues" wybrać "Search for Issues" w trybie Advanced
#. Kliknij link Advanced z paska wyszukiwania
#. To co wpisujesz w tym polu, to tzw. JQL (Jira Query Language)
#. W polu wyszukiwania wpisz literę "p" i zobacz co Jira Ci podpowiedziała
#. Wybierz strzałką na klawiaturze pozycję "project" i kliknij enter
#. Z listy wybierz znak równa się ``=``
#. Z listy wybierz nazwę swojego projektu (można najechać i kliknąć myszką)
#. Klikamy enter aby wyszukać, powinno nam to wyświetlić wszystkie zadania z naszego projektu
#. Kliknij w pole wyszukiwania i po fragmencie, który wcześniej był wpisany dodaj spację i zobacz co Ci podpowiada
#. Wybierz ``AND`` i zacznij pisać status -> mamy dwie opcje do wyboru: status i statusCategory
#. Wybierz statusCategory -> następnie równa się ``=`` -> "In Progress" i klikamy enter aby wyszukać zadania
#. Edytuj zapytanie i dopisz na koniec: "Epic Link" -> równa się ``=`` -> wybrać Epic "Wyszukiwarka", ale z Twojego projektu
#. Wyczyść zapytanie
#. w poniższych zapytaniach MYPROJECT zamień na klucz swojego projektu
#. Wyszukaj: ``project = MYPROJECT AND fixVersion = earliestUnreleasedVersion()``
#. Wyszukaj: ``assignee = currentUser() and statusCategory != Done``

Search Advanced
---------------
Z menu "Issues" wybrać "Search for Issues" w trybie Advanced:
#. Wyszukaj

    project = MYPROJECT
        AND sprint IN openSprints()
        AND (Flagged IS NOT EMPTY
             OR updated >= -1d
             OR statusCategory = "In Progress")

#. Wynik zapisz jako "Save As" (przycisk u góry nad polem wyszukiwania)
#. Nazwij "Daily"

Search Advanced
---------------
Z menu "Issues" wybrać "Search for Issues" w trybie Advanced:
#. Wyszukaj "assignee = currentUser() and statusCategory != Done
#. Przycisk trzy kropki "..." obok "Save" -> wybieramy Save as "My To Do
#. kliknij link details koło przycisku "Save as
#. Wybierz "Edit permissions" -> zmień nazwę filtru -> na "Imię Todo" (gdzie Imię, to Twoje imię)
#. Ustaw "add Viewers" -> "Any logged-in user" -> kliknij "+Add" (ważne, inaczej nie zadziała)
#. Upewnij się, że w polu Viewers dodane zostało "Shared with logged-in users (VIEW)
#. Kliknij przycisk "Save
#. Znów klikamy "Details" i wybieramy "New Subscription
#. Wybieramy Schedule: Days per Week; Interval: "Once per day at 5:00 am" Monday
#. Upewnij się, że jest odznaczone "Email this filter, even if there are no issues found
#. Kliknij Subscribe
#. Zmodyfikuj wyszukiwanie na: assignee = currentUser() AND statusCategory != "Done" AND due <= 7d
#. Kliknij przycisk "Save"



Z menu u góry wybierz "Boards" -> "View all boards" -> Create board (przycisk u góry po prawej)
#. Wybierz "Create a Kanban board
#. Board from an existing Saved Filter
#. Kliknij przycisk "Next
#. Board name: "Imię Todo" (gdzie Imię, to Twoje imię)
#. Saved filter: wybrać filtr, który został stworzony wcześniej, tj. "Imię Todo" (gdzie Imię, to Twoje imię)
#. Kliknij przycisk "Create board
#. Przycisk Board (górny prawy róg) -> Configure
#. Na zakładce Swimlanes
#. Zmodyfikuj nazwę Expedite i zamień na Must
#. Dodaj nowe: Should z JQL: priority in (High, Medium, Low)
#. Zmodyfikuj nazwę "Everything Else" na "Could
#. Zmień kolejność aby była: Must, Should, Could, tzn. Must ma być na górze, poniżej Should, na dole Could

Z menu "Issues" wybrać "Search for Issues" w trybie Advanced:
#. Z "FAVOURITE FILTERS" (menu po lewej) wybrać "Imię Todo"  (gdzie Imię, to Twoje imię)
#. Zmodyfikuj zapytanie: assignee = currentUser() AND (statusCategory != Done AND due <= 7d OR Flagged is not EMPTY)
#. kliknij "Search" a następnie "Save"

Z menu "Issues" wybrać "Search for Issues" w trybie Advanced:
#. Wyszukaj: project = MYPROJECT and due IS EMPTY  (gdzie MYPROJECT to nazwa Twojego projektu)
#. Przycisk Tools (po prawej u góry) -> Bulk Change -> all issue(s)
#. Zaznacz wszystkie (checkboxem do zaznaczania wszystkich na raz, nie rób tego pojedynczo)
#. Kliknij przycisk Next -> Edit Issues -> Next
#. Zmień "Change Due Date" i ustaw na "1/Nov/20
#. Kliknij przycisk "Next" (na dole) -> "Confirm" -> "Ok, got it
#. Przejdź na Board "Imię Todo" (gdzie Imię, to Twoje imię)
#. Zmień w zadaniach "Four" oraz "Seven" priorytet na "Highest" (zadania powinno pojawić się w Swimlane "Must")
#. Zmień w zadaniach "Nine" oraz "Eight" priorytet na "Lowest" (zadania powinno pojawić się w Swimlane "Could")
#. Zwiń zadania które są w Swimlane "Could", przez kliknięcie strzałeczki obok nazwy "Could
#. Board (u góry po prawej) -> Configure -> Na zakładce General -> "Edit Filter Query
#. Popraw zapytanie: assignee = currentUser() AND issuetype != Epic AND (statusCategory != Done AND due <= 7d OR Flagged is not EMPTY)
#. Przycisk "Search" -> "Save
#. Przejdź na Board "Imię Todo" (gdzie Imię, to Twoje imię)
#. Zobacz czy nie ma Epiców

Z menu u góry wybierz "Boards" -> View all Boards:
#. Poszukaj swojego Board "Imię Todo" (gdzie Imię, to Twoje imię)
#. kliknij trzy kropeczki "..." po prawej stronie
#. Delete i potwierdzasz przyciskiem "Delete"

Z menu u góry "Issues" wybrać "Manage filters" (na dole):
#. wbierz filtr z aktywną subskrybcją
#. klikniij na link "1 Subscription
#. Wybierz Actions "Delete" (po prawej)

Z menu u góry wybierz "Dashboards":
#. Manage Dashboars
#. Create new dashboard (przycisk u góry po prawej)
#. Name "Imię Dashboard" (gdzie Imię, to Twoje imię)
#. Start from "Blank Dashboard
#. Add Viewers -> Project -> Twój Projekt -> Developers -> "+ Add
#. Add Viewers -> Project -> Twój Projekt -> Administrators -> "+ Add
#. Kliknij przycisk Add

Z menu u góry wybierz "Dashboards" wybieirz swój Dashboard:
#. kiknij na Add gadget
#. Load all gadgets
#. Wybierz z listy Filter Results i kliknij przycisk "Add gadget" (po prawej)
#. Wybierz z listy Issue Statistics i kliknij przycisk "Add gadget" (po prawej)
#. Wybierz z listy Sprint Burndown Gadget i kliknij przycisk "Add gadget" (po prawej)
#. Wybierz z listy Sprint Health Gadget i kliknij przycisk "Add gadget" (po prawej)
#. Wybierz z listy Version Report i kliknij przycisk "Add gadget" (po prawej)
#. Wybierz z listy Days Remaning in Sprint Gadget i kliknij przycisk "Add gadget" (po prawej)
#. Zamknij okenko X (górny prawy róg)

#. Dla gadgetu Issue Statistics ustawiamy filtr Twojego projektu, Statistic: Type Status, Sort Total, Sort Direction Descending
#. Upewnij się, że nie jest zaznaczone "Update every 15 minutes" -> Save
#. Edytowanie gadgetu jest w jego prawym górnym rogu po kliknięciu trzech kropek "...

#. Filter Results wybiierz swój Filtr "Imię Todo", Number of Results: 20, Dodaj kolumne Due Date
#. Posortuj po Due Date przez kliknięcie kolumny

Version Report
#. Wyberz Board: Imię Board
#. Zaznacz Show board name
#. Wybierz Version: 2020-10
#. Zaznacz Show version name

Days Remaining in Sprint Gadget:
#. Wybierz Board: Imię Board
#. Zaznacz Show board name
#. Zaznacz Show sprint name
#. Wybierz Sprint: Next Sprint Due (auto)

Sprint Burndown Gadget:
#. Wybierz Board: Imię Board
#. Zaznacz Show board name
#. Zaznacz Show sprint name
#. Wybierz Sprint: Next Sprint Due (auto)

Sprint Health Gadget:
#. Wybierz Board: Imię Board
#. Zaznacz Show board name
#. Zaznacz Show sprint name
#. Wybierz Sprint: Next Sprint Due (auto)

Przenieś wszystkie gadżedy sprintowe po prawej stronie, a pozostałe po lewej
Zmień "Edit Layout" (prawy górny róg) na trzykolumnowy i przenieś wykresy wersji i burndown do nowej kolumny
Zadanie do domu: Zrobić board z zadaniami dla siebie personalnie, drugi dla całego zespołu


#. Edytuj filtr "Imię Todo" dodając sortowanie po duedate i priority
#. assignee = currentUser() AND issuetype != Epic AND (statusCategory != Done AND due <= 7d OR Flagged is not EMPTY) ORDER BY duedate DESC, priority DESC
#. Search -> Save
#. Przejdź na dashboard i zobacz co się zmieniło w Filter Result

Konfiguracja Workflow:
#. skrót klawiszowy "gg" -> workflows
#. Konfiguracja workflow (warunki, walidatory, wyzwalacze i post-funkcje)
#. Wybieramy własny workflow i Edit
#. Przycisk Edit po prawej stronie
#. Przycisk Diagram
#. Przycisk Dwie stałki do góry "^" (orworzy edytor workflow na full screen)
#. Add Status "In Test", nie zaznaczamy "Allow all statuses to transition to this one" -> Add -> status category: In Progress -> Create
#. Chwyć jedną kropkę z "In Progress" i polącz z jedną kropką z "In Test" (tzw. tranzycja) -> Name: To Test -> Add
#. Dodaj tranzycję do In Progress o nazwie To In Progress
#. Dodaj tranzycję do Done o nazwie To Done
#. Delete Transition All do statusu Done, tak aby móc kończyć zadania tylko przetestowane
#. Kliknij na tranzycję To Test (z In Progress do In Test) i klikamy na Conditions -> Add Condition -> Only Assignee Condition -> Add
#. Kliknij na nazwę workflow
#. Dodaj status In Review -> Category: In Progress -> Create
#. Edytuj tranzycję z In Test do Done, zmień by prowadziła z In Test do In Review oraz zmień nazwę na To Review
#. Dodaj tranzycję z In Review do Done o nazwie "To Done
#. Edytuj tranzycję "To Review" i edytuj Post Function (menu z prawej strony) -> Add post function -> Assign to Reporter -> Add
#. Kliknij przycisk Publish (przycisk po prawej u góry) -> Save a backup copy?: No -> Publish

Na Twoim board:
#. Board (prawy górny)
#. Zakładka Columns
#. Zwróć uwagę na Unmapped Statuses
#. Dodaj kolumnę In Test i przenieś do niej status In Test
#. Dodaj kolumnę In Review i przednieiś do niej status In Review
#. Wróć na Board i zobacz nowe kolumny
#. Przenieś zadanie "Four" do "In Test" (zwróć uwagę, że nie można było go przenieść do "In Review", a kolumna Done, była tylko Rejected)
#. Przenieś zadanie "Four" do "In Review
#. Tylko z Review można przenieść do Done

Konfiguracja Screens:

#. skrót klawiszowy "gg" -> screens
#. Add screen (po prawej u góry) -> Imię Log Work -> Add
#. Dodaj pole Log Work

#. skrót klawiszowy "gg" -> screens
#. Add screen (po prawej u góry) -> Imię Comment -> Add
#. Nie dodawaj żadnego pola

#. skrót klawiszowy "gg" -> workflows
#. Wybierz swój workflow i Edit (po prawej)
#. Wybierz tranzycję "To Done" (z In Review do Done) -> Edit (z menu po prawej) -> Screen: Imię Log Work -> Save
#. Wybierz tranzycję "All" (do statusu Blocked) -> Edit (z menu po prawej) -> Screen: Imię Comment -> Save
#. Kliknij przycisk Publish (przycisk po prawej u góry) -> Save a backup copy?: No -> Publish

#. Wróc na swój Board i odśwież stronę w przeglądarce (dobra praktyka po większych zmianach)
#. Przenieś zadanie do statusu Blocked, powinno wyskoczyś okno z prośbą o komnetarz
#. Przenieś zadanie do In Test, następnie do In Review a następnie do Done i powinno wyskoczyć okno z prośbą o zalogowanie czasu pracy

Rejestracja czasu pracy przy zgłoszeniu:
#. Na Twoim boardzie
#. Wybierz dowolne zadanie
#. Na szczegółach zadania wybierz menu trzech kropek "..." -> Log Work
#. Alternatywnie po wybraniu zadania klikasz skrót klawiszowy kropka "." -> Log Work

Wymagalność pola globalnie we wszystkich projektach:
#. skrót klawiszowy "gg" -> Field Configuration
#. Default Configuration -> Configure (po prawej)
#. Znajdź pole Due Date -> kliknij link Required (po prawej stronie)

Wymagalność pola globalnie w określonym projekcie/projektach:

#. skrót klawiszowy "gg" -> Field Configuration
#. Default Configuration -> Copy (po prawej)
#. Name: Imię Field Configuration -> Copy
#. Imię Field Configuration -> Configure (po prawej)
#. Znajdź pole Due Date -> kliknij link Required (po prawej stronie)

#. skrót klawiszowy "gg" -> Field Configuration Scheme
#. Add field configuration scheme (po prawej) -> Imię Field Configuration Scheme -> Add
#. Imię Field Configuration Scheme -> Confugure
#. Tu można mapować, jakie issue type ma mieć jakie Field Configuration
#. Associate an issue type with a field configuration (po prawej) -> Issue Type: Epic; Field Configuration: Imię Field Configuration -> Add

Pluginy (w instancjach Cloud i Behind the Firewall):
#. Skrót klawiszowy "gg" -> Find apps
#. Zarządzanie dodatkami
#. Wpływ pluginów na wydajność Jiry
#. Wpływ pluginów na bazę danych Jiry
#. Wpływ pluginów na możliwość aktualizacji Jiry

Analiza raportów na Boardzie
#. Z menu u góry wybierz "Boards" -> Twój Board

#. Burndown Chart
#. Burnup Chart
#. Sprint Report
#. Velocity Chart
#. Cumulative Flow Diagram
#. Version Report
#. Epic Report
#. Control Chart
#. Epic Burndown
#. Release Burndown
#. Time Tracking Report

Automatyzacja zadań administracyjnych

Python-atlassian-api:
#. https://github.com/atlassian-api/atlassian-python-api
#. https://github.com/atlassian-api/atlassian-python-api/tree/master/examples/jira

Integracja z systemami Ekosystemu narzędziowego:
#. https://dev.astrotech.io/git/internals/hooks.html#branch-hook
#. https://dev.astrotech.io/git/tools/git-flow.html#konwencje-nazewnicze
#. https://dev.astrotech.io/summary/pictures.html#ecosystem
#. https://dev.astrotech.io/summary/pictures.html#jira
#. https://dev.astrotech.io/summary/pictures.html#ci-cd

REST API:
#. https://developer.atlassian.com/server/jira/platform/rest-apis/
#. https://docs.atlassian.com/jira-software/REST/latest/
#. https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/

Zakładanie zadań z URL:
#. http://18.195.183.213:8080/secure/CreateIssueDetails!init.jspa?pid=10000&issuetype=10002
#. Projects -> View All projects -> Inspect Element (źródło strony) -> znajdź: "data-project-id
#. javascript:window.location='http://18.195.183.213:8080/secure/CreateIssueDetails!init.jspa?pid=10006&issuetype=10003&fixVersions=10015&components=10002&summary=' + document.getElementById('search_form_input').value
Custom Field
Issue Type i Issue Type Scheme
Screen i Screen Scheme
Permission Scheme
Role i uprawnienia
