JIRA
====

Documentation
-------------

- https://www.slideshare.net/mattharasymczuk/jira-and-jira-agile-training-course

Licencje
^^^^^^^^
- Cloud vs. Server
- Ilość użytkowników
- Długość trwania licencji
- Jira Core vs. Software vs. Service Desk

Instalacja
^^^^^^^^^^
- skąd pobrać
- jakie polecenia
- forwarding portów
- Jaka baza danych

Project Management
^^^^^^^^^^^^^^^^^^
- Prowadzenie projektów
- Kanban
- Scrum
- Portfolio
- Scrum + Kanban

Korzystanie z Jiry
------------------

Konfigurowanie profilu
^^^^^^^^^^^^^^^^^^^^^^
- Język
- Avatar
- Powiadamianie mailami
- Dobre praktyki filtrów na maila

Issues
^^^^^^
- Issue key:

    - krótki i zwięzły
    - łatwy do zapamiętania
    - 2-10 liter

- Issue Types:

    - Bug
    - Task
    - User Story
    - Epic
    - Sub-task

- Issue Fields:

    - Versions

        - Roadmap
        - Releases (with Bamboo)
        - Konwencja nazewnicza YYYY-MM (2017-01, 2017-02, 2017-03)

    - Components

        - Component Leaders

    - Custom Fields
    - Lables
    - Links
    - Assignee
    - Reporter
    - affectsVersion vs. fixVersion

- Epic

    - Brak worków (np. Poprawki błędów)
    - Doważalne (określone w czasie, mają datę początku i końca)
    - Dobre praktyki:

        - Due Date
        - Start Date
        - Assignee

- Kryteria akceptacyjne
- Dobre praktyki

    - INFO
    - BEFORE
    - TODO
    - AFTER

Issue Actions
^^^^^^^^^^^^^
- Workflow Actions (Open, In Progress, Done)
- Voting
- Watching
- Add Atachments
- Clone
- Move
- Create subtask
- Delete (kiedy?)
- Log Work
- Keyboard Shortcuts
- Comment

    - Mentions
    - Rich Text Editing
    - Tworzenie tabelek
    - Używanie formatowania

Time Reporting
^^^^^^^^^^^^^^
- Original Time Estimate
- Remaining Time
- Log Work
- Reports

Estimation
^^^^^^^^^^
- Time Estimate
- Manday
- Story Point
- Business Value

Workflow
^^^^^^^^
- Tworznie

    - Directed graph
    - Complete graph
    - Few vertices
    - Lots of Edges
    - Try simple and add statuses
    - Keep transitions from all statues

    - Simplified Workflow

- Dobre praktyki
- Triggery
- Post Functions
- Validators
- Closed vs Resolved vs Done

Priorities
^^^^^^^^^^
- Standard

    - Lowest
    - Low
    - Medium
    - High
    - Highest

- MoSCoW

    - Must
    - Schould
    - Could

Statusy
^^^^^^^
- To Do
- In Progress
- Done
- In Review
- Waiting / Blocked
- In Test

Resolutions
^^^^^^^^^^^
- Fixed
- Won't Fix
- Duplicate
- Cannot Reproduce
- Incomplete
- [Jira Agile] -> Done

Artifacts
^^^^^^^^^
- Backlog
- Sprintlog
- Task board
- Units
- Story Points
- Business Value

Metrics
^^^^^^^
- Velocity
- Capacity
- Maturity

Planning and Refinement
^^^^^^^^^^^^^^^^^^^^^^^
- Estimation
- How big your tasks should be?
- Estimation support systems
- Sprint goal
- Acceptance Criteria
- Definition of Done
- Time Tracking

JQL - JIRA Query Language
^^^^^^^^^^^^^^^^^^^^^^^^^
- List View, Detail View
- Konfiguracja Kolumn wyszukiwania
- Searching Issues
- Konfiguracja Boardów
- Bulk edit
- Import / Export CSV
- ``jira.issue.editable = true`` dla statusu Done (Workflow)

.. code-block:: sql

    project = DEMO

.. code-block:: sql

    project = DEMO
        AND status = "To Do"

.. code-block:: sql

    status = "To Do" OR status = "In Progress"

    status IN ("To Do", "In Progress")

    status NOT IN ("To Do", "In Progress")

.. code-block:: sql

    project = DEMO
        AND resolution NOT IN (Fixed, "Won't Fix")

.. code-block:: sql

    statusCategory = "To Do"
    statusCategory NOT IN ("To Do", "In Progress")
    statusCategory != "Done"

.. code-block:: sql

    statusCategory NOT IN (Done, "In Progress")
        AND assignee = currentUser()

.. code-block:: sql

    statusCategory NOT IN (Done, "In Progress")
        AND assignee IN membersOf("jira-administrators")

.. code-block:: sql

    statusCategory NOT IN (Done, "In Progress")
        AND assignee = currentUser()
        ORDER BY priority DESC, key ASC

.. code-block:: sql

    project = DEMO
        AND status WAS Done
        AND status != Done

.. code-block:: sql

    project = DEMO
        AND status WAS Done
        AND status != Done
        AND updated > -1d

.. code-block:: sql

    Sprint IN closedSprints()
    Sprint IN openSprints()
    Sprint IN futureSprints()

.. code-block:: sql

    project = DEMO
        AND sprint in openSprints()
        AND status != Done
        AND updated > -1d

.. code-block:: sql

    Flagged IS NOT EMPTY

.. code-block:: sql

    project = DEMO
        AND sprint IN openSprints()
        AND (statusCategory = "In Progress" OR Flagged is not EMPTY)

        -- opcjonalnie, ze względu na omawianie Waiting i in test itp.
        AND updated >= -1d

.. code-block:: sql

    project = DEMO
        AND sprint IN openSprints()
        AND assignee = currentUser()

.. code-block:: sql

    reporter = currentUser()
        AND statusCategory != Done
        AND assignee != currentUser()

.. code-block:: sql

    project = DEMO
        AND updated >= -7d
        AND assignee IN membersOf("jira-administrators")

.. code-block:: sql

    due >= 2017-03-01 AND due <= 2017-03-31

    due >= startOfMonth() AND due <= endOfMonth()

.. code-block:: sql

    due <= now()

Filtry
^^^^^^
- Tworzenie
- Subskrybcja
- Uprawnienia

    - Przydział do ról
    - Przydział do grup
    - Publiczny

- Współidzelenie

Dashboard
^^^^^^^^^
- Tworzenie
- Publikacja
- Dodawanie gadżetów

    - Filter Results
    - Issue Statistics
    - Average Age Chart
    - Resolution Time

- Wallboard plugin

    - Tables
    - Graphs
    - Piecharts

- Jira Agile Reports

    - Sprint Health Report
    - Burndown
    - Days Remaining

Project
^^^^^^^
- Project Lead
- Categories

    - Department
    - Team
    - Project / Product

- Project vs. Boards
- Issues
- Sub-Tasks
- Issue Collector

Board
^^^^^
- Scrum vs. Kanban

    - Scrum -> Rozwój (Story)
    - Kanban -> Utrzymanie (Task)
    - Praca w Scrum i Kanban jednocześnie
    - Konstytucja zespołu i dobre praktyki

- Board vs. Project

    - Board z wielu projektów
    - Board z części jednego projektu
    - Board dla Projektu
    - Wiele boardów do jednego projektu (różne estymaty)
    - Wiele projektów czy wiele boardów (np. po komponentach)?

- Sprinty:

    - Wielkość (ilość zadań, capacity chart)
    - Długość (tydzień)
    - Konwencja nazewnicza (YYYY-MM week W) (2017-03 week 2, 2017-03 week 3)

- Uprawnienia
- Konfiguracja
- Kolumny

    - Column Constraint (max, min)
    - Dodawanie i usuwanie kolumn
    - Wiele statusów w jednej kolumnie
    - Statusy ciągnące pracę

- Swimlines

    - wg. priorytetów
    - wg. wersji

- Quick Filters
- Card Colors
- Card Layout

    - Backlog
    - Active Sprint
    - Days in Column

- Estimation

    - Original Estimate + Remaining Estimate and Time Spent
    - Story Points
    - Business Value
    - Issue Count

- Working Days
- Issue Detail View
- Portfolio na bazie Kanbana
- Scope Changes
- Otwieranie i zamykanie sprintów
- Auto assign
- Flagowanie zadań
- Quick Filters dla Daily

Charts
^^^^^^
- Burn-down Chart
- Burn-up Chart
- Control Chart
- Cumulative Flow Diagram
- Epic Burndown
- Epic Report
- Release Burndown
- Sprint Report
- Velocity Chart
- Version Report
- Version Burndown

- Refine Reports

Kanban
^^^^^^
- What’s Kanban?
- Pull system
- JIT
- Context switching
- Kanban Board
- Improvement:

    - Muda
    - Jidoka
    - Kaizen
    - Bottlenecks
    - Metrics
    - Lean

- Workflow:

    - Columns
    - Swimlanes
    - Expedite
    - Priority
    - SLA

Administracja
-------------
- Skrót klawiszowy ``gg``

Scheme
^^^^^^
- Issue Type Schemes
- Workflow Scheme
- Screen Scheme
- Field Configuration Scheme
- Permission Scheme
- Notification Scheme

Project Configuration
^^^^^^^^^^^^^^^^^^^^^
- Versions
- Components
- Roles and Permissions
- Application Links

Jira Administration
^^^^^^^^^^^^^^^^^^^
- Zmiana formatu daty
- Estymacja różnych issuetype
- Tworzenie Custom Field

    - Dobre praktyki
    - Ile?

- Re-index

Pluginy
^^^^^^^
- Kiedy instalować
- Różnice między pliginami w Cloud a Server

    - Atlassian Connect vs p2

- Stategia update'ów

    - pluginy darmowe
    - pluginy komercyjne

- Instalacja dodatkowych języków
- `Jira Agile Cards`

Documentacja
------------
- https://confluence.atlassian.com/display/JIRA/JIRA+Documentation

Instalacja
----------
- https://www.atlassian.com/software/jira/download?b=a#allDownloads

:Konfiguracja bazy danych:
    .. code-block:: sql

        CREATE USER jira WITH PASSWORD 'jira';
        CREATE DATABASE jira;
        GRANT ALL PRIVILEGES ON DATABASE jira TO jira;

:Instalacja Jiry:
    .. code-block:: sh

        wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-7.3.2-x64.bin
        chmod +x atlassian-jira-software-7.3.2-x64.bin
        ./atlassian-jira-software-7.3.2-x64.bin
        rm -fr atlassian-jira-software-7.3.2-x64.bin

:Wyłączanie Websudo (automatyczne wylogowywanie administratora):
    .. code-block:: sh

        service jira stop
        echo "jira.websudo.is.disabled = true" >> /var/atlassian/application-data/jira/jira-config.properties
        service jira start

Konfiguracja
------------
JIRA User Server
^^^^^^^^^^^^^^^^

- Go to Jira User Server (g+g and type JIRA User Server)
- Add application
- Set application name, password and IP Addresses (paste adresses from instances which you want connect with Jira User Server)

Programming
-----------
- REST API
- Atlassian CLI
- `Atlassian Python API <https://github.com/AstroTech/atlassian-python-api>`_

    - ``pip install atlassian-python-api``

API Documentation
^^^^^^^^^^^^^^^^^
- https://docs.atlassian.com/jira/REST/latest/
- https://jira.atlassian.com/plugins/servlet/restbrowser#/


Zadania praktyczne
------------------

Projekt
^^^^^^^
- Stwórz projekt
- Dodaj użytkownika ``admin`` do roli ``Developers``
- Dodaj użytkownika ``admin`` do roli ``Administrators``

Tworzenie issues
^^^^^^^^^^^^^^^^
- Pozostaw za pomocą Configure Fields  (ekran tworzenia zadania)

    - Issue Type
    - Summary
    - Priority
    - Attachment
    - Linked Issue

- Do jednego z zadań dodaj załącznik

    - obrazek PNG lub JEPG
    - archiwum .zip z przynajmniej dwoma plikami tekstowymi

- Zadania powinny mieć różne priorytety
- Zadania miały różne Issue Type
- Powiąż dwa zadania linkami jako "is blocked by"/"blocks"
- Sklonuj przynajmniej jedno zadanie
- Niech jedno zadanie ma trzy subtaski

    - status pierszego: To Do
    - status drugiego: In Progress
    - status trzeciego: Done

- Przenieś zadanie z projektu do innego projektu

Backlog i Estymacja
^^^^^^^^^^^^^^^^^^^
- Stwórz epiki

    - Logowanie
    - Panel administracyjny

- oszacuj zadania używając Story Points i skali S,M,L (Small: 1, Medium: 2, Large: 3)
- Zadanie wyestymuj na 4h
- Zaloguj 1h 30m do zadania i ustaw remaining na 3h


Wersje
^^^^^^
- Stwórz werjse

    - 2017-03 (rozpoczęcie: 1 marzec 2017; zakończenie: 31 marzec 2017)
    - 2017-04 (rozpoczęcie: 1 kwiecień 2017; zakończenie: 31 kwiecień 2017)
    - 2017-05 (rozpoczęcie: 1 maj 2017; zakończenie: 31 maj 2017)

- Zadania przydziel do wersji

Sprinty
^^^^^^^
- Stwórz Sprinty

    - 2017-03 week 3 (ma 10 Story Points)
    - 2017-03 week 4 (ma 8 Story Points)
    - 2017-04 week 1 (ma 12 Story Points)

- Wystartuj sprint ``2017-03 week 3``

    - Data rozpoczęcia 13 marzec 2017, 9:00
    - Data zakończenia 20 marzec 2017, 9:00

- Przenieś dwa zadania do "In progress"
- Przenieś jedno zadanie do "Done"
- Zamknij sprint
- Zadania które nie zostały zakończone w sprincie niech spadną do następnego tygodnia

    - Co się dzieje z otwartymi zadaniami?
    - Co się dzieje z zamkniętymi zadaniami?
    - Co się dzieje z zamkniętymi subtaskami, ale otwartym zadaniem?
    - Co się dzieje z otwartymi subtaskami ale zamkniętym zadaniem?

- Zobacz raporty

JQL i Wyszukiwanie zadań
^^^^^^^^^^^^^^^^^^^^^^^^
- wyszukaj wszystkie zadania, które są w statusie "In Progress"
- wyszukaj zadania, które zostały zaktualizowan od wczoraj
- wyszukaj zadania, które należą do obecnie otwartego sprintu
- wyszukaj zadania oflagowane
- wyszukaj zadania, które należą do osób z grupy jira-administrators
- wyszukaj zadania, które były przypisane do Ciebie, ale już nie są
- Wyszukaj wszystkie zadania zaktualizowane przez Ciebie w okresie ostatniego tygodnia

- Pokaż mandaye, story points, fixVersion

Filtry
^^^^^^
- Stwórz filtr "Daily"
- Stwórz filtr "Przekroczony Deadline", ustaw uprawnienia by był widoczny dla administratorów w projekcie
- Stwórz filtr "Praca mojego zespołu z ostatniego tygodnia", ustaw by przychodził mail z zadaniami w poniedziałki o 6 rano

Custom Field
^^^^^^^^^^^^
- Dodaj `Custom Field` typu `Number` o nazwie `Manday`, ustaw board do szacowania w `Mandayach`, dodaj do Screen
- Dodaj `Custom Field` typu listy dwupoziomowej - Słownik
- Sprawdź czy pola wyświetlają się przy zakładaniu zadań (czy nie są ukryte w `Configure Fields`)

Administracja
^^^^^^^^^^^^^
- Zmień priorytety na MoSCoW, zmień ikony i kolory (czerwony, zielony, szary)
- Dodaj Screen aby przy zamykaniu zadań wyświetlało się użytkownikowi okienko z logowaniem czasu

Board
^^^^^
- Stwórz Board dla zadań rozwojowych (Story, Bug):

    - Dodaj kolumnę `In Test` oraz `In Review` wraz z odpowiadającymi im statusami
    - Dodaj status `Won't Do`, który będzie w kolumnie `Done` jednocześnie ze statusem `Done`
    - Stwórz Quick Filter `Daily`:

        - zadania są w trakcie wykonywania
        - zaktualizowane w ciągu ostatniego dnia
        - lub mają flagę

    - Stwórz wersję board z Estymacją Time Estimate
    - Stwórz wersję board z Estymacją w Story Points

- Stwórz Board dla zadań utrzymaniowych (Task)
- Stwórz board Kanban z Epikami:

    - Stwórz swimline dla kwartałów
    - Określ aby w kolumnie "In Progress" mogły być maksymalnie 3 Epiku

- Stwórz board zadań przypisanych do Ciebie:

    - zadania mogą być w dowolnym projekcie
    - board ma być publiczny

