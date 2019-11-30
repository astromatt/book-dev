******
Backup
******


Procedure
=========
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


Script
======
.. literalinclude:: src/jira-backup.sh
    :caption: Jira backup
    :language: console


Assignments
===========

Administracja - backup
----------------------
#. Zrób backup ``$JIRA_HOME`` i ``$JIRA_INSTALL`` wykorzystując ``tar.gz`` (musi być data w nazwie pliku)
#. Wylistuj pliki w archiwum (możesz przeglądnąć za pomocą midnight commander)
#. Usuń katalogi ``$JIRA_HOME`` i ``$JIRA_INSTALL``
#. Przywróć oba katalogi do:

    - ``/opt/jira/home``
    - ``/opt/jira/install``

#. Podmienić skrypty startowe
#. Uruchom Jirę z nowej lokalizacji
#. Dodaj polecenie backupu ``$JIRA_HOME`` i ``$JIRA_INSTALL`` do *crontab* z ``@midnight``
