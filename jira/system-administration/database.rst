**************
DB Performance
**************


Dobre praktyki
==============
- Terminal z połączeniem SSH do produkcji Background color RED


About
=====
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
============================
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
================================
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
=============================================
.. code-block:: console

    $ psql -h localhost -p 5432 -U jira -d jira < "/tmp/$(date +%F)_jira.pgdump"


Change JIRA DB config
=====================
- Change ``/var/atlassian/application-data/jira/dbconfig.xml``

.. code-block:: console

    $ service jira start


Assignments
===========

Administracja - bazą danych
---------------------------
#. Zrób backup bazy danych (musi być data w nazwie pliku)
#. Zrób drop bazy
#. Zmień DB Pool connection
#. Przywróć backup do bazy jira_new
#. Dodaj polecenie backupu bazy danych do *crontab* z ``@midnight``
