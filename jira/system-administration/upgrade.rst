*******
Upgrade
*******


Instalacja nowej wersji
=======================
#. Wejdź na stronę https://www.atlassian.com/software/jira/download
#. Kliknij prawym na przycisk `Download` obok wydania Jira `TAR.GZ` i `Copy Link Location`
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
=======================
#. Poniższych edycji dokonujemy w pliku ``atlassian-jira-XXX/bin/setenv.sh`` gdzie XXX to numer wersji (nowej)

.. code-block:: console

    JIRA_HOME="/opt/jira/home"
    JVM_SUPPORT_RECOMMENDED_ARGS="-server -XX:MaxPermSize=512m -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:+PrintGC -XX:+PrintGCDateStamps -XX:+OptimizeStringConcat -XX:+PrintGCDetails -XX:+DisableExplicitGC -Xloggc:/opt/jira/logs/gc-jira-$(hostname)-$(date +%Y.%m.%d).log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=10M"
    JVM_MINIMUM_MEMORY="512m"
    JVM_MAXIMUM_MEMORY="2048m"


Zmiana portu działania Jiry
===========================
#. Edytuj linijkę ``/opt/jira/install/conf/server.xml`` i znajdź

    .. code-block:: xml

        Connector port="8080"

#. Zamień na:

    .. code-block:: xml

        Connector port="8000"


Sprawdzenie wersji Javy dla Jiry
================================
#. Odpal poniższe polecenie

    .. code-block:: console

        /opt/java/default/bin/java -version

#. Zobacz aktualną wersję na http://www.oracle.com/technetwork/java/javase/downloads/1880261
#. Jeżeli wersja się różni ściągnij za pomocą ``wget`` nową Javę do ``/opt/java/``
#. rozpakuj i usuń symlink ``/opt/java/default``
#. stwórz symlink ``/opt/java/default`` wskazujący na nową Javę


Backup bazy oraz home'a
=======================
#. Odpal skrypt ``/opt/jira/backup-jira.sh``


Upgrade Jiry
============
.. code-block:: console

    $ service jira stop
    $ rm -fr /opt/jira/install
    $ ln -s /opt/jira/atlassian-jira-XXX
    $ /opt/jira/install
    $ service jira start


Sprzątanie
==========
#. Możesz usunąć stary katalog instalacyjny Jiry.
#. Proponuję jednak zostawić jedną, poprzednią wersję tak na wszelki wypadek, gdyby jakieś zmiany nie zostały przeniesione.
