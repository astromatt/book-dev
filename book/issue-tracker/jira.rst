JIRA
====
- https://confluence.atlassian.com/display/JIRA/JIRA+Documentation


Wymagania przed szkoleniem
--------------------------
#. System operacyjny wspierany przez Atlassian (zalecany Linux)
#. Ściągnięta odpowiednia binarka dla wybranego systemu operacyjnego https://www.atlassian.com/software/jira/download

Licencje
^^^^^^^^
- Cloud vs. Server
- Ilość użytkowników
- Długość trwania licencji
- Jira Core vs. Software vs. Service Desk
- Evaluation license

Konferencje
^^^^^^^^^^^
- Atlassian Camp (development)
- Atlassian Summit (business)

- https://www.atlassian.com/company/events/summit-europe
- https://www.atlassian.com/company/events/summit-europe/programs/atlascamp?tab=build-add-ons
- http://www.intenso.pl/jira-day/

Instalacja
^^^^^^^^^^
- skąd pobrać (https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-X.X.X-x64.bin)
- jakie polecenia
- forwarding portów
- Jaka baza danych
- SSL proxy

Project Management
^^^^^^^^^^^^^^^^^^
- Prowadzenie projektów
- Kanban
- Scrum
- Portfolio
- Scrum + Kanban

Korzystanie z Jiry
------------------
- ``gg`` oraz ``.``

Konfigurowanie profilu
^^^^^^^^^^^^^^^^^^^^^^
- Język
- Avatar (gravatar)
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

    * Doważalne
    * optymalna długość
    * kategoryzowanie
    * timeline i roadmapa
    * planowanie kwartalne
    * przypisywanie epikow do wersji
    * board epików
    * Business Value epików


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
- Bulk change limit
- Limit wyświetlania wyników dla JQL
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

    updated >= startOfWeek(-7d) AND updated <= endOfWeek(-7d)

.. code-block:: sql

    due <= now()
        AND statusCategory != Done

.. code-block:: sql

    status WAS NOT "In Progress" BEFORE "2011/02/02"
    status WAS NOT IN ("Resolved","In Progress") BEFORE "2011/02/02"
    status WAS IN ("Resolved","In Progress")
    status WAS "Resolved" BY jsmith DURING ("2010/01/01","2011/01/01")
    status WAS "Resolved" BY jsmith BEFORE "2011/02/02"


.. code-block:: sql

    AFTER "date"
    BEFORE "date"
    BY "username"
    DURING ("date1","date2")
    ON "date"
    FROM "oldvalue"
    TO "newvalue"

.. code-block:: sql

    assignee CHANGED

    priority CHANGED BY freddo BEFORE endOfWeek() AFTER startOfWeek()

    status CHANGED FROM "In Progress" TO "Open"

.. code-block:: sql

    currentLogin()
    lastLogin()
    now()
    startOfDay()
    startOfWeek()
    startOfMonth()
    startOfYear()
    endOfDay()
    endOfWeek()
    endOfMonth()
    endOfYear()

More info: https://confluence.atlassian.com/jira064/advanced-searching-720416661.html

Filtry
^^^^^^
- Tworzenie
- Subskrybcja
- Uprawnienia

    - Przydział do ról
    - Przydział do grup
    - Publiczny

- Współdzielenie

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
- Priority Scheme

Project Configuration
^^^^^^^^^^^^^^^^^^^^^
- Versions
- Components
- Roles and Permissions
- Application Links

Konfiguracja Jiry
^^^^^^^^^^^^^^^^^
- Time Tracking
- Priorytetyzacja i dobre praktyki
- Estymacja różnych issuetype (nie tylko Story)
- Re-index
- Application Links
- Zaawansowane opcje konfiguracyjne
- Zmiana formatu daty

.. figure:: img/jira-date-format.png
    :scale: 100%
    :align: center

    Zmiana formatu daty w zaawansowanych opcjach konfiguracyjnych

Jira Administration
^^^^^^^^^^^^^^^^^^^
- Zarządzanie licencjami
- Backup systemu
- Tworzenie instancji testowych
- Instalacja i upgrade + dobre praktyki
- Tunning JVM pod Jirę
- Dobre praktyki z Custom

Tworzenie Custom Field
^^^^^^^^^^^^^^^^^^^^^^
- Dobre praktyki
- Ile?
- Konsekwencje
- CF w bazie dancyh
- Javascript w opisie (nie używać)

Dirty hacks
^^^^^^^^^^^
- Manipulacje na bazie
- Django Inspect DB + Jira = Django ORM
- Skryptowanie
- Time tracking

Pluginy
^^^^^^^
- Kiedy instalować
- Licencje pluginów
- Różnice między pliginami w Cloud a Server

    - Atlassian Connect vs p2

- Stategia update'ów

    - pluginy darmowe
    - pluginy komercyjne

- Instalacja dodatkowych języków
- Pluginy a wykorzystywane zasoby:

    - Pamięć RAM
    - Baza danych
    - System operacyjny
    - Zasoby sieciowe

- ``Jira Agile Cards``
- Dane pluginów w bazie danych Jiry

Install
-------
- Terminal z połączeniem SSH do produkcji Background color RED
- https://www.atlassian.com/software/jira/download?b=a#allDownloads

Database
^^^^^^^^
.. code-block:: console

    # CentOS
    $ yum install posgresql-server
    $ postgresql-setup initdb
    $ systemctl start posgresql

.. code-block:: console

    # Ubuntu / Debian
    $ apt-get install postgresql

Konfiguracja bazy danych:

.. code-block:: console

    # Musimy być na roocie
    su posgres
    psql

.. code-block:: sql

    CREATE USER jira WITH PASSWORD 'jira';
    CREATE DATABASE jira;
    GRANT ALL PRIVILEGES ON DATABASE jira TO jira;

W ubunutu ścieżka do *pg_hba* to: ``/etc/postgresql/9.5/main/pg_hba.conf``.
Dla CentOS trzeba zmienić plik ``/var/lib/pgsql/data/pg_hba.conf``, tak aby można było łączyć się z localhost (po IPv4 i IPv6) za pomocą hasła (md5):

.. code-block:: text

    # "local" is for Unix domain socket connections only
    local   all             all                                     peer
    # IPv4 local connections:
    host    all             all             127.0.0.1/32            md5
    # IPv6 local connections:
    host    all             all             ::1/128                 md5

.. code-block:: console

    $ systemctl restart postgresql

Jira install
^^^^^^^^^^^^
.. literalinclude:: code/jira-install.sh
    :caption: Jira install
    :language: console

Firewall
^^^^^^^^
.. code-block:: console

    # CentOS
    $ firewall-cmd --zone=public --add-port=8080/tcp --permanet
    $ firewall-cmd --zone=public --add-port=5432/tcp --permanet
    $ firewall-cmd --reload

    # Other Linux
    $ iptables -I INPUT 1 -i eth0 -p tcp --dport 8080 -j ACCEPT
    $ iptables -I INPUT 1 -i eth0 -p tcp --dport 5432 -j ACCEPT

Websudo
^^^^^^^
- automatic admin logout
- admin rights notification

.. code-block:: sh

    service jira stop
    echo "jira.websudo.is.disabled = true" >> /var/atlassian/application-data/jira/jira-config.properties
    service jira start

User Management
^^^^^^^^^^^^^^^
- Always use LDAP (OpenLDAP or Active Directory)
- name groups as ``jira-users`` or ``jira-administrators``
- local administrator ``jira-administrator`` only for fixing bugs with LDAP
- use ``jira@example.com`` (for easy email fiterling)
- use ``jira.example.com`` as domain name with Firewall blocking external access
- ``/etc/resolv.conf`` ``search example.com`` -> ustawianie przez DHCP
- Internal and external users in one LDAP server
- Read only access via LDAPs
- avoid nested groups
- all tools in ``OU=ecosystem``
- use LDAP groups for project roles from ``OU=projects``
- do not use user accounts in project roles (only LDAP groups)
- Confluence page with all ``*-administrators`` + ``mailto:`` links
- Confluence page with JIRA project administrators
- Do not use technical accounts (use SSH keys)
- Use SSH keys with proper comment


Upgrade
-------
Instalacja nowej wersji
^^^^^^^^^^^^^^^^^^^^^^^
#. Wejdź na stronę https://www.atlassian.com/software/jira/download
#. Kliknij prawym na przycisk Download obok wydania Jira TAR.GZ i "Copy Link Location"
#. Uruchom polecenia poniżej:

    .. code-block:: console

        # Tu wklej zawartość linku
        $ URL=""

        $ ssh root@localhost
        $ cd /opt/jira
        $ wget "$URL" -O jira.tgz
        $ tar zxf jira.tgz
        $ rm -fr jira.tgz

Ustawienia środowiskowe
^^^^^^^^^^^^^^^^^^^^^^^
#. Poniższych edycji dokonujemy w pliku ``atlassian-jira-XXX/bin/setenv.sh`` gdzie XXX to numer wersji (nowej)

.. code-block:: console

    JIRA_HOME="/opt/jira/home"
    JVM_SUPPORT_RECOMMENDED_ARGS="-server -XX:MaxPermSize=512m -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:+PrintGC -XX:+PrintGCDateStamps -XX:+OptimizeStringConcat -XX:+PrintGCDetails -XX:+DisableExplicitGC -Xloggc:/opt/jira/logs/gc-jira-$(hostname)-$(date +%Y.%m.%d).log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=10M"
    JVM_MINIMUM_MEMORY="512m"
    JVM_MAXIMUM_MEMORY="2048m"

Zmiana portu działania Jiry
^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Edytuj linijkę ``/opt/jira/install/conf/server.xml`` i znajdź

    .. code-block:: xml

        Connector port="8080"

#. Zamień na:

    .. code-block:: xml

        Connector port="8000"

Sprawdzenie wersji Javy dla Jiry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Odpal poniższe polecenie

    .. code-block:: console

        /opt/java/default/bin/java -version

#. Zobacz aktualną werjsę na http://www.oracle.com/technetwork/java/javase/downloads/1880261
#. Jeżeli wersja się różni ściągnij za pomocą ``wget`` nową Javę do ``/opt/java/``
#. rozpakuj i usuń symlink ``/opt/java/default``
#. stwórz symlink ``/opt/java/default`` wskazujący na nową Javę

Backup bazy oraz home'a
^^^^^^^^^^^^^^^^^^^^^^^
Odpal skrypt ``/opt/jira/backup-jira.sh``

Upgrade Jiry
^^^^^^^^^^^^
.. code-block:: console

    $ service jira stop
    $ rm -fr /opt/jira/install
    $ ln -s /opt/jira/atlassian-jira-XXX
    $ /opt/jira/install
    $ service jira start

Sprzątanie
^^^^^^^^^^
#. Możesz usunąć stary katalog instalacyjny Jiry.
#. Proponuję jednak zostawić jedną, poprzednią wersję tak na wszelki wypadek, gdyby jakieś zmiany nie zostały przeniesione.

Utils
-----

Reindex
^^^^^^^
.. literalinclude:: code/jira-reindex.py
    :caption: Jira reindex
    :language: python

Project Administrators
^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: code/jira-project-administrators.py
    :caption: Jira Project Administrators
    :language: python

Migracja danych
---------------
.. literalinclude:: code/jira-migrate.py
    :caption: Jira Migrate
    :language: python

Backup
------
- XML (http://localhost:8080/secure/admin/XmlBackup!default.jspa)
- ``rsync``:

    - ``JIRA_HOME="/var/atlassian/application-data/jira"``
    - ``JIRA_INSTALL="/opt/atlassian/jira/"``
    - database replication
    - ``pg_dump`` i ``pg_restore``

- database replication consistency and ``rsync`` while upgrading
- ``/var/atlassian/application-data/jira/.jira-home.lock``
- Cold standby in alternative datacenter
- database replication between datacenter
- cold standby and licensing (same SEN number)

.. literalinclude:: code/jira-backup.sh
    :caption: Jira backup
    :language: console

Test Environment
----------------
.. literalinclude:: code/jira-fabric.py
    :caption: Jira test environment
    :language: python

.. literalinclude:: code/jira-delete-projects.py
    :caption: Jira delete projects
    :language: python

Jira Performance
----------------
- JProfiler
- MAT (Memory Analyzer Tool) [heapdump and MAT from Eclipse]
- Performance SQL
- own database indexes
- *pgpool* and database cache
- *nginx* as a SSL terminator
- *Varnish* caching *REST* responses (JSON) and static files
- Java Melody

Optymalizacje
^^^^^^^^^^^^^
- Wyłączyć Activity Stream
- Update gadżetów na Dashboardzie (update na bazie dla wszystkich gadgetów)
- Edukacja użytkowników aby nie mieli odpalonych miliona zakładek z JIRĄ
- Czy wszystkie monitory z Wallboardami są potrzebne?

Database
^^^^^^^^
- ``/var/atlassian/application-data/jira/dbconfig.xml``

.. code-block:: xml

    <pool-min-size>20</pool-min-size>
    <pool-max-size>20</pool-max-size>
    <pool-max-wait>30000</pool-max-wait>
    <validation-query>select 1</validation-query>
    <min-evictable-idle-time-millis>60000</min-evictable-idle-time-millis>
    <time-between-eviction-runs-millis>300000</time-between-eviction-runs-millis>
    <pool-max-idle>20</pool-max-idle>
    <pool-remove-abandoned>true</pool-remove-abandoned>
    <pool-remove-abandoned-timeout>300</pool-remove-abandoned-timeout>
    <pool-test-on-borrow>false</pool-test-on-borrow>
    <pool-test-while-idle>true</pool-test-while-idle>


Garbage Collector
^^^^^^^^^^^^^^^^^
- Jakub Kubryński on Garbage Collector https://www.youtube.com/watch?v=LCr3XyHdaZk
- G1 GC ``-XX:+UseG1GC``
- ``Xmx``
- ``/opt/atlassian/jira/bin/setenv.sh``

.. literalinclude:: code/jira-gc.sh
    :caption: Jira Garbage Collector
    :language: console

Monitorowanie
^^^^^^^^^^^^^
- http://www.stagemonitor.org/
- New Relic
- JavaMelody
- JIRA embedded tools (in settings):

    - JMX monitoring
    - SQL profiling


Rozwiązywanie problemów
^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    grep '/rest' /opt/atlassian/jira/logs/access_log.* |awk '{print $7}' |sort |uniq -c |sort -n

- Dużo zapytań API (varnish requestów, np. dashboardów)
- Inne usługi wysycające pamięć na maszynie, aż do limitów JAVY
- Przy port forwardnig ``ssh -L 5432:localhost:5432 root@adresIP`` w ``/var/lib/pgsql/data/pg_hba.conf`` musi być md5 przy IPv4 i IPv6

- Create issue by URL: http://localhost:8080/secure/CreateIssueDetails!init.jspa?pid=10000&issuetype=10002

Baza danych
-----------
- AO = Add-On (plugins)
- cwd_user i cwd_directories
- jiraissue
- mailserver
- filtersubscription
- worklog
- customfieldvalue i customfield
- project i project_key
- fileattachment

.. code-block:: console

    ssh -L 5432:localhost:5432 root@adresIP

Backup data with ``pg_dump``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    $ service jira stop
    $ pg_dump -i -h localhost -p 5432 -U jira -F c -b -v -f "/tmp/$(date +%F)_jira.pgdump" jira

.. code-block:: console

    $ pg_dump -?
    -p, –port=PORT database server port number
    -i, –ignore-version proceed even when server version mismatches
    -h, –host=HOSTNAME database server host or socket directory
    -U, –username=NAME connect as specified database user
    -W, –password force password prompt (should happen automatically)
    -d, –dbname=NAME connect to database name
    -v, –verbose verbose mode
    -F, –format=c|t|p output file format (custom, tar, plain text)
    -c, –clean clean (drop) schema prior to create
    -b, –blobs include large objects in dump
    -v, –verbose verbose mode
    -f, –file=FILENAME output file name

Restore data with ``pg_restore``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: sql

    DROP DATABSE jira;
    CREATE DATABASE jira_new;
    GRANT ALL PRIVILEGES ON DATABASE jira_new TO jira;

.. code-block:: console

    $ pg_restore -i -h localhost -p 5432 -U jira -v "/tmp/$(date +%F)_jira.pgdump" -d jira_new

.. code-block:: console

    $ pg_restore -?
    -p, –port=PORT database server port number
    -i, –ignore-version proceed even when server version mismatches
    -h, –host=HOSTNAME database server host or socket directory
    -U, –username=NAME connect as specified database user
    -W, –password force password prompt (should happen automatically)
    -d, –dbname=NAME connect to database name
    -v, –verbose verbose mode

Restore data with ``psql`` from plaintext SQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    $ psql -h localhost -p 5432 -U jira -d jira < "/tmp/$(date +%F)_jira.pgdump"

Change JIRA DB config
^^^^^^^^^^^^^^^^^^^^^
- Change ``/var/atlassian/application-data/jira/dbconfig.xml``

.. code-block:: console

    $ service jira start


Konfiguracja
------------

JIRA User Server
^^^^^^^^^^^^^^^^
- Go to Jira User Server (g+g and type JIRA User Server)
- Add application
- Set application name, password and IP Addresses (paste adresses from instances which you want connect with Jira User Server)

Programming
-----------
- REST API:

    - https://docs.atlassian.com/software/jira/docs/api/REST/server/
    - https://developer.atlassian.com/jiradev/jira-apis/about-the-jira-rest-apis/jira-rest-api-tutorials
    - https://docs.atlassian.com/jira/REST/latest/
    - https://jira.atlassian.com/plugins/servlet/restbrowser#/

- Atlassian CLI:

    - https://marketplace.atlassian.com/plugins/org.swift.atlassian.cli/cloud/overview
    - https://bobswift.atlassian.net/wiki/spaces/ACLI/overview

- Atlassian Python API:

    - https://github.com/AstroTech/atlassian-python-api>
    - ``pip install atlassian-python-api``

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

Custom Field
^^^^^^^^^^^^
- Stwórz Custom Field (Multiple User) dla osób, które są przypisane do zadania
- Dodaj tego custom field do Screena dla Projektu
- Stwórz filtr który wyszuka zadania w których jesteś wymieniony w naszym Custom Field
- Na podstawie filtru stwórz tablicę Kanban, z zadaniami które są do Ciebie przypisane w naszym Custom Fieldzie
- Zrób by wyświetlało się w kolumnie po prawej

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

Administracja - Instalacja Jiry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Zainstaluj jirę z licencją evaluation
#. Utwórz przykładowy projekt

Administracja - bazą danych
^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Zrób backup bazy danych (musi być data w nazwie pliku)
#. Zrób drop bazy
#. Zmień DB Pool connection
#. Przywróć backup do bazy jira_new
#. Dodaj polecenie backupu bazy danych do *crontab* z ``@midnight``

Administracja - backup
^^^^^^^^^^^^^^^^^^^^^^
#. Zrób backup ``$JIRA_HOME`` i ``$JIRA_INSTALL`` wykorzystując ``tar.gz`` (musi być data w nazwie pliku)
#. Wylistuj pliki w archiwum (możesz przeglądnąć za pomocą midnight commander)
#. Usuń katalogi ``$JIRA_HOME`` i ``$JIRA_INSTALL``
#. Przywróć oba katalogi do:

    - ``/opt/jira/home``
    - ``/opt/jira/install``

#. Podmienić skrypty startowe
#. Uruchom Jirę z nowej lokalizacji
#. Dodaj polecenie backupu ``$JIRA_HOME`` i ``$JIRA_INSTALL`` do *crontab* z ``@midnight``

Administracja - Garbage Collector
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Zmień Garbage Collector na G1
#. Zmień Xmx na 1GB
#. Wepnij Java Melody do monitorowania

Administracja - Zmiana Javy
^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Zainstaluj nową Javę na serwerze w katalogu ``/opt/java/$VERSION``
#. Utwórz symlink ``/opt/java/default/`` wskazujący na ``/opt/java/$VERSION`` (dlaczego to dobra praktyka?)
#. Zrestartuj Jirę by wykorzystywała nową Javę

Atlassian Python API - Instalacja
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Zainstaluj bibliotekę Atlassian Python API ``atlassian-python-api``

.. note:: Kod biblioteki dostępny jest na GitHub https://github.com/AstroMatt/atlassian-python-api

.. warning:: Wymagany Python 3.4 lub nowszy

.. toggle-code-block:: console
    :label: Pokaż rozwiązanie instalacji Pythona i ``atlassian-python-api``

    $ apt-get update
    $ apt-get install python3-pip
    $ python3 -m pip install atlassian-python-api

Atlassian Python API - Reindeksacja
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Stwórz skrypt ``jira-reindex.py``
#. Skrypt wykorzystując bibliotekę ``atlassian-python-api`` ma reindeksować JIRĘ
#. Skrypt ``jira-reindex.py`` dodaj Crontab by był uruchamiany o 4 w nocy (zwróć uwagę na zmienne środowiskowe)

.. toggle-code-block:: python
    :label: Pokaż kod skryptu do reindeksacji

    from atlassian import Jira


    jira = Jira(
        url="http://localhost:8080/",
        username="jira-administrator",
        password="admin")

    jira.reindex()

.. toggle-code-block:: console
    :label: Pokaż jak uruchomić skrypt do reindeksacji

    $ python3 jira-reindex.py

Atlassian Python API - Project Administrators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Stwórz skrypt ``jira-administrators.py``
#. Skrypt ma wyliistować wszystkich administratorów projektów w JIRA w tabelce, wraz z ich emailem jako link "mailto"

    - Wynik zapisz w Confluence i dodaj się do watchers strony, by być powiadamianym o zmianach
    - Jeżeli nie masz zainstalowanego Confluence to zrzuć do pliku ``/var/www/jira-admins.html`` i skonfiguruj nginx aby wyświetlał tą stronę

:Podpowiedź: Aby uruchomić Confluence możesz wykorzystać Docker

    .. code-block:: console

        $ apt-get update
        $ apt-get install docker.io
        $ docker run -v /var/atlassian/application-data/confluence:/var/atlassian/application-data/confluence -d -p 8090:8090 atlassian/confluence-server

Atlassian Python API - Changelog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Napisz skrypt ``jira-changelog.py``
#. Wygeneruj Changelog, tj. listę zadań które zmieniły się pomiędzy dwoma wersjami (wykorzystaj JQL)

    - Wynik zapisz w Confluence na osobnej stronie dla każdej wersji
    - Jeżeli nie masz zainstalowanego Confluence to zrzuć do pliku ``/var/www/changelog-XXX.html`` i skonfiguruj nginx aby wyświetlał tą stronę, XXX to nazwa wersji
