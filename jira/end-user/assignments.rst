***********
Assignments
***********

"Wejdź na stronę Jiry
- Zaloguj się wykorzystując swoje imię jako login i hasło (bez polskich znaków i z małej litery)"

"Z menu u góry wybierz ""Projects"" -> View Projects:
- Kliknij przycisk ""Create Projects"" (prawy górny róg)
- Scrum software development i klikamy Next później Select
- Ustaw: Project name: wpisz swoje imię; Project key: wpisz swoje imię (dużymi literami); Project Lead: ustaw siebie -> Submit"

"Z menu u góry wybierz ""Boards"" -> Twój Board:
- Dodaj wersje ""2020-10"", ""2020-11"", ""2020-12"" z datami rozpoczęcia i zakończenia miesiąca
- Dodaj zadania do backlog: ""One"", ""Two"", ""Three"",  ""Four"", ""Five"", ""Six""
- Przeciągnij zadanie ""One"" do wersji ""2020-10""
- Przeciągnij zadanie ""Two"" i ""Three"" do wersji ""2020-11"""

"Przejdź do ""Project Settings"" (przycisk w menu na dole po lewej)
- Zakładka Components -> dodaj: ""Frontend"", ""Backend"", ""Database""
- Zakładka Versions -> dodaj: ""2021-Q1"", ""2021-Q2"", ""2021-Q3"", ""2021-Q4""
- Zakładka Users and roles -> dodaj siebie do roli ""Administrators"", dodaj użytkownika ""admin"" do roli ""Developers""
- Zakładka Issue Types -> Task -> dodaj pole ""Due Date"", usuń pole ""Labels""
- Zakładka Issue Types -> dodaj nową zakładkę ""Daty"", dodaj na tej zakładce pole typu ""Due Date""
- Zakładka General -> zmień awatar swojego projektu na rakietę
- Zakładka General -> zmień nazwę swojego projektu na ""Imię N.""

gdzie:
- ""Imię"" to Twoje imię,
- ""N."" to pierwsza litera Twojego nazwiska
- Przykłady: ""Jan T."", ""Mark W."", ""Melissa L."", ""Matt K."""

"Z menu u góry wybierz ""Boards"" -> Twój Board:
- Zaznacz wszystkie issues za pomocą klikania i trzymania klawisza Shift
- Zaznacz trzy issues za pomocą klikania i trzymania klawisza Ctrl (klawisz Cmd na macOS)
- Wybierz zadanie ""Two"" -> Prawy klawisz myszy -> ""Two"" i Send to... -> ""Bottom of the backlog""
- Wybierz zadanie ""Four"" -> Prawy klawisz myszy -> ""Add Flag""
- Wybierz zadanie ""Four"" -> Prawy klawisz myszy -> ""Remove Flag"""

"- Wybierz zadanie ""Five"" -> Prawy klawisz myszy -> ""Split Issue"":
- ""Five"" - Estimate: 1
- ""Seven"" - Estimate: 2
- ""Eight"" - Estimate: 3
- ""Nine"" - Estimate: 4"

"Zaznacz zadania:
- ""Four"", ""Five"", ""Six"", ""Seven""
- Prawym klawiszem -> ""Bulk Change""
- ""Edit Issues"" -> Next
- Zmień issue type na ""Task""
- Fix Version ""Add to existing"" -> ""2021-Q1""
- Rozwiń na dole ""Unavailable Actions"" i zobacz co tam jest
- Kliknij ""Next"" (na dole)
- Potwierdzamy ""Confirm""
- Po chwili klikamy ""Refresh""
- Po ukończeniu klikamy ""Ok, got it""
- Zwróć uwagę, że po zmianie część zadań w backlog nie ma story pointów"

"Z menu u góry wybierz ""Boards"" -> Twój Board:
- Stwórz sprint o nazwie ""2020-10 week 4"" i dodaj do niego zadania ""One"", ""Two"", ""Three""
- Przejedź suwakiem i dodaj ""Four"", ""Five"", ""Seven"", zwróć uwagę na okienko ""Issues"" i ""Estimate""
- Wystartuj sprint ustawiając -> Goal: ""Ukończenie szkolenia z Jiry"", Duration: ""1 week"", Start Date: ""26/Oct/20 09:30 AM"""
"Na zakładce Active Sprints:

Przenieś zadania:
- ""One"" do ""In Progress""
- ""Two"" do ""In Progress""
- ""Three"" do ""Done""

Dodaj flagę do zadania ""Five""

Z menu ""Board"" prawy górny róg:
- Wybierz ""Hide detail view""
- Wybierz ""Print cards"" i zmień ""Card size"" -> ""small""
- Wybierz ""Configure"""

"W konfiguracji board na zakładce ""General"":
- Usuń administratora ""admin@example.com""
- Zwróć uwagę na ""Edit Filter Shares"", ""View Permissions""
- Osoby które mają uprawnienia do ""Filter"" będą widziały i mogły otworzyć Board
- To nie znaczy, że będę widziały zadania (to wymaga uprawnień w projekcie)"

"W konfiguracji board na zakładce ""Columns"":
- Dodaj kolumnę ""Blocked"" w ""Category"" -> ""In Progress""
- Dodaj status ""Rejected"" w ""Category"" -> ""Done"" do kolumny ""Done"" i zaznacz ""Set resolution""
- Column Constraints ""Issue Count, excluding sub-tasks""
- W kolumnie ""Blocked"" -> ""Max"" ustaw na: ""2""
- W kolumnie ""In Progress"" -> ""Min"" ustaw na: ""1""
- Zaznacz ""Days in column"""

"W konfiguracji board na zakładce ""Swimlines"":
- wybierz ""Base Swimlanes on"" -> ""Queries""
- Dodaj Swimline ""Story"" z JQL -> ""issuetype = Story""
- Dodaj Swimline ""Task"" z JQL -> ""issuetype = Task"""

"W konfiguracji board na zakładce ""Quick Filters"":
- Zmień nazwę ""Recently Updated"" na ""Daily""
- Zmień JQL dla ""Daily"" na: Flagged is not EMPTY or (updatedDate >= -1d and statusCategory = ""In Progress"")"

"W konfiguracji board na zakładce ""Card colours"":
- Zmień ""Colours based on"" -> ""Priorities""
- Zmień kolor ""Highest"" oraz ""High"" na czerwony (FF0000)
- Zmień kolor ""Medium"" na zółty (FFFF00)
- Zmień kolor ""Low"" oraz ""Lowest"" na zielony (00FF00)"

"W konfiguracji board na zakładce ""Card layout"":
- W sekcji Backlog -> wyświetl pole Due Date
- W sekcji Active sprints -> wyświetl pole Due Date
- Usuń wyświetlanie pola ""Due Date"" z sekcji Backlog (ale zostaw w Active Sprint)"

"W konfiguracji board na zakładce ""Estimation"":
- Zmień ""Estimation Statistic"" na ""Original Time Estimate""
- Zaznacz ""Time Tracking"" -> ""Remaining Estimate and Time Spent"""

"W konfiguracji board na zakładce ""Working days"":
- Wybierz Region -> ""Europe""
- Time Zone -> (GMT+01:00) Warsaw
- Dodaj ""Non-Working Days"" -> ""1/Nov/20"", ""11/Nov/20"", ""25/Dec/20"", ""26/Dec/20"""

"W konfiguracji board na zakładce ""Issue Detail View"":
- Sekcja ""General Fields"" -> usuń: Status, Priority, Labels, Affects Version/s
- Sekcja ""Date Fields"" -> dodaj ""Due Date"", usuń: ""Created"" i ""Updated""
- Sekcja ""People"" -> usuń ""Reporter"" i ""Assignee""
- Sekcja ""Links"" -> usuń ""Linked Issue"""

"Na Active Sprint Board:
- Usuń wszystkie zadania z kolumny ""In Progress"" (powinna podświetlić się na żółto)
- Dodaj trzy zadania do kolumny ""Blocked"" (powinna podświetlić się na czerwono)"

"W Backlog:
- W detail view zadania ""One"" -> ""Estimate"" ustaw 3h, [menu kropeczki] -> Log Work -> Time Spent: 2h
- Dodaj Epic -> Epic Name ""Logowanie"", ""Summary"" -> ""Logowanie"", Due Date: ""1/Nov/20""
- Dodaj Epic -> Epic Name ""Wyszukiwarka"", Summary ""Wyszukiwarka"", Due Date: ""10/Nov/20""
- Zmień ""Logowanie"" Epic Color na jasny niebieski
- Zmień ""Wyszukiwarka"" Epic Color na jasny czerwony
- W detail view zadania ""Two"" -> ""Estimate"" ustaw 8h
- W detail view zadania ""Three"" -> ""Estimate"" ustaw 4h
- Do Epic ""Logowanie"" dodaj zadania ""One"", ""Two"", ""Three""
- Do Epic ""Wyszukiwarka"" dodaj zadania ""Four"", ""Five"", ""Seven""
- Kliknij na ""All Issues"", później na ""Issues without epics"" i porównaj ilość zadań
- Zobacz kolorowe kółka z estymacjami w nagłówku sprintu: To Do, In Progress, Done"
Dodaj sprint: "2020-11 week 1", Duration "1 week", "Start Date": "1/Nov/20 09:00 AM"

"Wejdź na Active Sprint:
- zakończ aktualny sprint -> Prawy górny róg ""Complete Sprint""
- zadania niezakończone mają ""spaść"" do sprintu następnego, tj. ""2020-11 week 1"""

"Z menu ""Issues"" wybrać ""Search for Issues"":
- Change View [przycisk po prawej stronie] zmień na List View
- Columns [przycisk po prawej stronie]: Odznaczyć: Created, Updated, Development
- Columns: zaznaczyć: Summary, Issue Type, Due Date, Fix Version/s, Epic Link
- Chwytając nagłówek kolumny, przenieś Issue Type (T) jako pierwsza kolumna
- Ustawić kolumny w kolejnośći: Issue Type, Issue Key, Epic Link, Fix Version/s, Due Date, Status, Summary
- Dodać kolumny: Original Estimate, Remaining Estimate, Time Spent
- Z menu po prawej stronie u góry wybieramy Export -> CSV (Current Fields) -> Delimiter -> Comma (,)"

"Z menu ""Issues"" wybrać ""Search for Issues"" w trybie Basic:
- Project -> swój projekt
- Kliknij na nazwę kolumny Due Date dwukrotnie aby posortować rosnąco
- Status -> In Progress oraz Blocked
- More -> Due Date -> Now Overdue
- Zmień zakres Due Date -> od 1/Oct/20 do 31/Oct/20
- Zmień zakres Due Date -> Due in next 8 hours or is overdue
- Zmień zakres Due Date -> In range -7d to ... [pozostaw niewypełnione]"

"Z menu ""Issues"" wybrać ""Search for Issues"" w trybie Advanced:
- Klikniij link Advanced z paska wyszukiwania
- To co wpiisujesz w tym polu, to tzw. JQL (Jira Query Language)
- W polu wyszukiwania wpisz literę ""p"" i zobacz co Jira Ci podpowiedziała
- Wybierz strałką na klawiaturze pozucję ""project"" i kliknij enter
- Z listy wybierz znak równa się ""=""
- Z listy wybierz nazwę swojego projektu (można najechać i klikąć myszką)
- Klikamy enter aby wyszukać, powinno nam to wyświetlić wszysktie zadania z naszego projektu
- Kliknij w pole wyszukiwania i po fragmencie, który wsześniej był wpisany dodaj spację i zobacz co Ci podpowiada
- Wybieirz AND i zacznij pisać status -> mamy dwie opcje do wyboru: status i statusCategory
- Wybierz statusCategory -> następnie równa się ""="" -> ""In Progress"" i klikamy enter aby wyszukać zadania
- Edytuj zapytanie i dopisz na koniec: ""Epic Link"" -> równa się ""="" -> wybrać Epic ""Wyszukiwarka"", ale z Twojego projektu
- Wyczyść zapytanie
- w poniższych zapytaniach MYPROJECT zamień na klucz swojego projektu
- Wyszukaj: ""project = MYPROJECT AND fixVersion = earliestUnreleasedVersion()""
- Wyszukaj: ""assignee = currentUser() and statusCategory != Done"""

"Z menu ""Issues"" wybrać ""Search for Issues"" w trybie Advanced:
- Wyszukaj

    project = MYPROJECT
        AND sprint IN openSprints()
        AND (Flagged IS NOT EMPTY
             OR updated >= -1d
             OR statusCategory = ""In Progress"")

- Wynik zapisz jako ""Save As"" (przycisk u góry nad polem wyszukiwania)
- Nazwij ""Daily"""

"Z menu ""Issues"" wybrać ""Search for Issues"" w trybie Advanced:
- Wyszukaj ""assignee = currentUser() and statusCategory != Done""
- Przycisk trzy kropki ""..."" obok ""Save"" -> wybieramy Save as ""My To Do""
- kliknij link details koło przycisku ""Save as""
- Wybierz ""Edit permissions"" -> zmień nazwę filtru -> na ""Imię Todo"" (gdzie Imię, to Twoje imię)
- Ustaw ""add Viewers"" -> ""Any logged-in user"" -> kliknij ""+Add"" (ważne, inaczej nie zadziała)
- Upewnij się, że w polu Viewers dodane zostało ""Shared with logged-in users (VIEW)""
- Kliknij przycisk ""Save""
- Znów klikamy ""Details"" i wybieramy ""New Subscription""
- Wybieramy Schedule: Days per Week; Interval: ""Once per day at 5:00 am"" Monday
- Upewnij się, że jest odznaczone ""Email this filter, even if there are no issues found""
- Kliknij Subscribe
- Zmodyfiikuj wyszukiwanie na: assignee = currentUser() AND statusCategory != ""Done"" AND due <= 7d
- Kliknij przycisk ""Save"""

"Z menu u góry wbierz ""Boards"" -> ""View all boards"" -> Create board (przycisk u góry po prawej)
- Wybierz ""Create a Kanban board""
- Board from an existing Saved Filter
- Kliknij przycisk ""Next""
- Board name: ""Imię Todo"" (gdzie Imię, to Twoje imię)
- Saved filter: wybrać filtr, który został stworzony wcześniej, tj. ""Imię Todo"" (gdzie Imię, to Twoje imię)
- Kliknij przycisk ""Create board""
- Prycisk Board (górny prawy róg) -> Configure
- Na zakładce Swimlines
- Zmodyfikuj nazwę Expedite i zamień na Must
- Dodaj nowe: Should z JQL: priority in (High, Medium, Low)
- Zmodyfikuj nazwę ""Everything Else"" na ""Could""
- Zmień kolejność aby była: Must, Should, Could, tzn. Must ma być na górze, poniżej Should, na dole Could"

"Z menu ""Issues"" wybrać ""Search for Issues"" w trybie Advanced:
- Z ""FAVOURITE FILTERS"" (menu po lewej) wybrać ""Imię Todo""  (gdzie Imię, to Twoje imię)
- Zmodyfikuj zapytanie: assignee = currentUser() AND (statusCategory != Done AND due <= 7d OR Flagged is not EMPTY)
- kliknij ""Search"" a następnie ""Save"""

"Z menu ""Issues"" wybrać ""Search for Issues"" w trybie Advanced:
- Wyszukaj: project = MYPROJECT and due IS EMPTY  (gdzie MYPROJECT to nazwa Twojego projektu)
- Przycisk Tools (po prawej u góry) -> Bulk Change -> all issue(s)
- Zaznacz wszystkie (checkboxem do zaznaczania wszystkich na raz, nie rób tego pojedynczo)
- Kliknij przycisk Next -> Edit Issues -> Next
- Zmień ""Change Due Date"" i ustaw na ""1/Nov/20""
- Kliknij przycisk ""Next"" (na dole) -> ""Confirm"" -> ""Ok, got it""
- Przejdź na Board ""Imię Todo"" (gdzie Imię, to Twoje imię)
- Zmień w zadaniach ""Four"" oraz ""Seven"" priorytet na ""Highest"" (zadania powinno pojawić się w Swimline ""Must"")
- Zmień w zadaniach ""Nine"" oraz ""Eight"" priorytet na ""Lowest"" (zadania powinno pojawić się w Swimline ""Could"")
- Zwiń zadania które są w Swimline Could, przez kliknięcie stałeczki obok nazwy ""Could""
- Board (u góry po prawej) -> Confiigure -> Na zakładce General -> ""Edit Filter Query""
- Popraw zapytanie: assignee = currentUser() AND issuetype != Epic AND (statusCategory != Done AND due <= 7d OR Flagged is not EMPTY)
- Przycisk ""Search"" -> ""Save""
- Przejdź na Board ""Imię Todo"" (gdzie Imię, to Twoje imię)
- Zobacz czy nie ma Epiców"

"Z menu u góry wybierz ""Boards"" -> View all Boards:
- Poszukaj swojego Boarda  ""Imię Todo"" (gdzie Imię, to Twoje imię)
- kliknij trzy kropeczki ""..."" po prawej stronie
- Delete i potwierdzasz przyciskiem ""Delete"""

"Z menu u góry ""Issues"" wybrać ""Manage filters"" (na dole):
- wbierz filtr z aktywną subskrybcją
- klikniij na link ""1 Subscription""
- Wybierz Actions ""Delete"" (po prawej)"

"Z menu u góry wybierz ""Dashboards"":
- Manage Dashboars
- Create new dashboard (przycisk u góry po prawej)
- Name ""Imię Dashboard"" (gdzie Imię, to Twoje imię)
- Start from ""Blank Dashboard""
- Add Viewers -> Project -> Twój Projekt -> Developers -> ""+ Add""
- Add Viewers -> Project -> Twój Projekt -> Administrators -> ""+ Add""
- Kliknij przycisk Add"

"Z menu u góry wybierz ""Dashboards"" wybieirz swój Dashboard:
- kiknij na Add gadget
- Load all gadgets
- Wybierz z listy Filter Results i kliknij przycisk ""Add gadget"" (po prawej)
- Wybierz z listy Issue Statistics i kliknij przycisk ""Add gadget"" (po prawej)
- Wybierz z listy Sprint Burndown Gadget i kliknij przycisk ""Add gadget"" (po prawej)
- Wybierz z listy Sprint Health Gadget i kliknij przycisk ""Add gadget"" (po prawej)
- Wybierz z listy Version Report i kliknij przycisk ""Add gadget"" (po prawej)
- Wybierz z listy Days Remaning in Sprint Gadget i kliknij przycisk ""Add gadget"" (po prawej)
- Zamknij okenko X (górny prawy róg)

- Dla gadgetu Issue Statistics ustawiamy filtr Twojego projektu, Statistic: Type Status, Sort Total, Sort Direction Descending
- Upewnij się, że nie jest zaznaczone ""Update every 15 minutes"" -> Save
- Edytowanie gadgetu jest w jego prawym górnym rogu po kliknięciu trzech kropek ""..."""

"Konfiguracja Workflow:
- skrót klawiszowy ""gg"" -> workflows
- Konfiguracja workflow (warunki, walidatory, wyzwalacze i post-funkcje)"

Konfiguracja pól w zgłoszeniu (dodawanie, modyfikacja i wymagalność)
Custom Field
Issue Type i Issue Type Scheme
Screen i Screen Scheme
Permission Scheme
Role i uprawnienia
Raporty na tablicach Agile
Rejestracja czasu pracy przy zgłoszeniu
Pluginy (w instancjach Cloud i Behind the Firewall) i zarządzanie dodatkami, performance, bada danych
"Automatyzacja zadań administracyjnych, REST API, python-atlassian-api, Zakładanie zadań z URL
- http://18.195.183.213:8080/secure/CreateIssueDetails!init.jspa?pid=10000&issuetype=10002
- https://github.com/atlassian-api/atlassian-python-api
- https://developer.atlassian.com/server/jira/platform/rest-apis/
- https://docs.atlassian.com/jira-software/REST/latest/
- https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/"
