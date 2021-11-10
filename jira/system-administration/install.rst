**********
Instalacja
**********


Instalacja
==========
* skąd pobrać

    * https://product-downloads.atlassian.com/software/jira/downloads/atlassian-jira-software-X.X.X-x64.bin

* jakie polecenia
* forwarding portów
* SSL proxy


Database
========

Jaka baza danych?
-----------------
* Wspierane: PostgreSQL, MySQL, Oracle, MSSQL
* Preferowana: PostgreSQL

Instalacja PostgreSQL na CentOS
-------------------------------
.. code-block:: console

    yum install posgresql-server
    postgresql-setup initdb
    systemctl start posgresql

Instalacja PostgreSQL na Ubuntu
-------------------------------
.. code-block:: console

    # Ubuntu / Debian
    $ apt-get install postgresql

Tworzenie bazy danych
---------------------
* Będąc zalogowanym jako ``root`` wykonaj:

.. code-block:: console

    su posgres
    psql

.. code-block:: sql

    CREATE USER jira WITH PASSWORD 'jira';
    CREATE DATABASE jira;
    GRANT ALL PRIVILEGES ON DATABASE jira TO jira;

Konfiguracja połączenia z bazą danych
-------------------------------------
* Konieczna jest modyfikacja pliku ``pg_hba.conf`` aby można było łączyć się z localhost (po IPv4 i IPv6) za pomocą hasła (md5)
* Ubuntu: ``/etc/postgresql/9.5/main/pg_hba.conf``.
* CentOS: ``/var/lib/pgsql/data/pg_hba.conf``

.. code-block:: text

    # "local" is for Unix domain socket connections only
    local   all             all                                     peer
    # IPv4 local connections:
    host    all             all             127.0.0.1/32            md5
    # IPv6 local connections:
    host    all             all             ::1/128                 md5

Restart bazy danych
-------------------
.. code-block:: console

    $ systemctl restart postgresql


Jira install
============
.. code-block:: console
    :caption: Jira install

    VERSION='7.13.1'
    wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-${VERSION}-x64.bin
    chmod +x atlassian-jira-software-${VERSION}-x64.bin
    ./atlassian-jira-software-${VERSION}-x64.bin
    rm -fr atlassian-jira-software-${VERSION}-x64.bin

Environment
-----------
#. Poniższych edycji dokonujemy w pliku ``atlassian-jira-XXX/bin/setenv.sh`` gdzie XXX to numer wersji (nowej)

.. code-block:: console

    JIRA_HOME="/opt/jira/home"
    JVM_SUPPORT_RECOMMENDED_ARGS="-server -XX:MaxPermSize=512m -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:+PrintGC -XX:+PrintGCDateStamps -XX:+OptimizeStringConcat -XX:+PrintGCDetails -XX:+DisableExplicitGC -Xloggc:/opt/jira/logs/gc-jira-$(hostname)-$(date +%Y.%m.%d).log -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=10M"
    JVM_MINIMUM_MEMORY="512m"
    JVM_MAXIMUM_MEMORY="2048m"

Firewall
--------
.. code-block:: console

    # CentOS
    $ firewall-cmd --zone=public --add-port=8080/tcp --permanet
    $ firewall-cmd --zone=public --add-port=5432/tcp --permanet
    $ firewall-cmd --reload

    # Other Linux
    $ iptables -I INPUT 1 -i eth0 -p tcp --dport 8080 -j ACCEPT
    $ iptables -I INPUT 1 -i eth0 -p tcp --dport 5432 -j ACCEPT


Configuration
=============

Websudo
-------
* automatic admin logout
* admin rights notification

.. code-block:: sh

    service jira stop
    echo "jira.websudo.is.disabled = true" >> /var/atlassian/application-data/jira/jira-config.properties
    service jira start


Assignments
===========

Install Jira
------------
#. Zainstaluj Jirę z licencją evaluation (wykorzystaj 10 minute email * drugi wynik w Google)
#. Utwórz projekt Moon Village (klucz: MOON) z przykładowymi danymi
