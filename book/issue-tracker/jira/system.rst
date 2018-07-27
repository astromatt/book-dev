Jira System Administration
==========================

Dobre praktyki
--------------
- Terminal z połączeniem SSH do produkcji Background color RED
- https://www.atlassian.com/software/jira/download?b=a#allDownloads

Installing Jira
---------------

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
.. literalinclude:: src/jira-install.sh
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

User Management (JIRA User Server)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Go to Jira User Server (g+g and type JIRA User Server)
#. Add application
#. Set application name, password and IP Addresses (paste adresses from instances which you want connect with Jira User Server)

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


Upgrading JIRA
--------------

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
---------------------------
#. Edytuj linijkę ``/opt/jira/install/conf/server.xml`` i znajdź

    .. code-block:: xml

        Connector port="8080"

#. Zamień na:

    .. code-block:: xml

        Connector port="8000"

Sprawdzenie wersji Javy dla Jiry
--------------------------------
#. Odpal poniższe polecenie

    .. code-block:: console

        /opt/java/default/bin/java -version

#. Zobacz aktualną wersję na http://www.oracle.com/technetwork/java/javase/downloads/1880261
#. Jeżeli wersja się różni ściągnij za pomocą ``wget`` nową Javę do ``/opt/java/``
#. rozpakuj i usuń symlink ``/opt/java/default``
#. stwórz symlink ``/opt/java/default`` wskazujący na nową Javę

Backup bazy oraz home'a
-----------------------
Odpal skrypt ``/opt/jira/backup-jira.sh``

Upgrade Jiry
------------
.. code-block:: console

    $ service jira stop
    $ rm -fr /opt/jira/install
    $ ln -s /opt/jira/atlassian-jira-XXX
    $ /opt/jira/install
    $ service jira start

Sprzątanie
----------
#. Możesz usunąć stary katalog instalacyjny Jiry.
#. Proponuję jednak zostawić jedną, poprzednią wersję tak na wszelki wypadek, gdyby jakieś zmiany nie zostały przeniesione.

Utils
=====

Reindex
-------
.. literalinclude:: src/jira-reindex.py
    :caption: Jira reindex
    :language: python

Project Administrators
----------------------
.. literalinclude:: src/jira-project-administrators.py
    :caption: Jira Project Administrators
    :language: python

Migracja danych
===============
.. literalinclude:: src/jira-migrate.py
    :caption: Jira Migrate
    :language: python

Backup
======
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

.. literalinclude:: src/jira-backup.sh
    :caption: Jira backup
    :language: console

Test Environment
================
.. literalinclude:: src/jira-fabric.py
    :caption: Jira test environment
    :language: python

.. literalinclude:: src/jira-delete-projects.py
    :caption: Jira delete projects
    :language: python

Jira Performance
================
- JProfiler
- MAT (Memory Analyzer Tool) [heapdump and MAT from Eclipse]
- Performance SQL
- own database indexes
- *pgpool* and database cache
- *nginx* as a SSL terminator
- *Varnish* caching *REST* responses (JSON) and static files
- Java Melody

Optymalizacje
-------------
- Wyłączyć Activity Stream
- Update gadżetów na Dashboardzie (update na bazie dla wszystkich gadgetów)
- Edukacja użytkowników aby nie mieli odpalonych miliona zakładek z JIRĄ
- Czy wszystkie monitory z Wallboardami są potrzebne?

Database
--------
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
-----------------
- Jakub Kubryński on Garbage Collector https://www.youtube.com/watch?v=LCr3XyHdaZk
- G1 GC ``-XX:+UseG1GC``
- ``Xmx``
- ``/opt/atlassian/jira/bin/setenv.sh``

.. literalinclude:: src/jira-gc.sh
    :caption: Jira Garbage Collector
    :language: console

Monitorowanie
-------------
- http://www.stagemonitor.org/
- New Relic
- JavaMelody
- JIRA embedded tools (in settings):

    - JMX monitoring
    - SQL profiling


Rozwiązywanie problemów
-----------------------
.. code-block:: console

    grep '/rest' /opt/atlassian/jira/logs/access_log.* |awk '{print $7}' |sort |uniq -c |sort -n

- Dużo zapytań API (varnish requestów, np. dashboardów)
- Inne usługi wysycające pamięć na maszynie, aż do limitów JAVY
- Przy port forwardnig ``ssh -L 5432:localhost:5432 root@adresIP`` w ``/var/lib/pgsql/data/pg_hba.conf`` musi być md5 przy IPv4 i IPv6

- Create issue by URL: http://localhost:8080/secure/CreateIssueDetails!init.jspa?pid=10000&issuetype=10002

Baza danych
===========
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
----------------------------
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
--------------------------------
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
---------------------------------------------
.. code-block:: console

    $ psql -h localhost -p 5432 -U jira -d jira < "/tmp/$(date +%F)_jira.pgdump"

Change JIRA DB config
---------------------
- Change ``/var/atlassian/application-data/jira/dbconfig.xml``

.. code-block:: console

    $ service jira start

Zadanie - Administracja - bazą danych
-------------------------------------
#. Zrób backup bazy danych (musi być data w nazwie pliku)
#. Zrób drop bazy
#. Zmień DB Pool connection
#. Przywróć backup do bazy jira_new
#. Dodaj polecenie backupu bazy danych do *crontab* z ``@midnight``

Zadanie - Administracja - backup
--------------------------------
#. Zrób backup ``$JIRA_HOME`` i ``$JIRA_INSTALL`` wykorzystując ``tar.gz`` (musi być data w nazwie pliku)
#. Wylistuj pliki w archiwum (możesz przeglądnąć za pomocą midnight commander)
#. Usuń katalogi ``$JIRA_HOME`` i ``$JIRA_INSTALL``
#. Przywróć oba katalogi do:

    - ``/opt/jira/home``
    - ``/opt/jira/install``

#. Podmienić skrypty startowe
#. Uruchom Jirę z nowej lokalizacji
#. Dodaj polecenie backupu ``$JIRA_HOME`` i ``$JIRA_INSTALL`` do *crontab* z ``@midnight``

Zadanie - Administracja - Garbage Collector
-------------------------------------------
#. Zmień Garbage Collector na G1
#. Zmień Xmx na 1GB
#. Wepnij Java Melody do monitorowania

Zadanie - Administracja - Zmiana Javy
-------------------------------------
#. Zainstaluj nową Javę na serwerze w katalogu ``/opt/java/$VERSION``
#. Utwórz symlink ``/opt/java/default/`` wskazujący na ``/opt/java/$VERSION`` (dlaczego to dobra praktyka?)
#. Zrestartuj Jirę by wykorzystywała nową Javę
