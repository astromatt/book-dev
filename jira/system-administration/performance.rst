******************
Performance Tuning
******************


Rationale
=========
* JProfiler
* MAT (Memory Analyzer Tool) [heapdump and MAT from Eclipse]
* Performance SQL
* own database indexes
* *pgpool* and database cache
* *nginx* as a SSL terminator
* *Varnish* caching *REST* responses (JSON) and static files
* Java Melody
* New Relic


Cache
=====
.. literalinclude:: src/confluence-varnish.vcl
    :language: text


Optymalizacje
=============
* Wyłączyć Activity Stream
* Update gadżetów na Dashboardzie (update na bazie dla wszystkich gadgetów)
* Edukacja użytkowników aby nie mieli odpalonych miliona zakładek z JIRĄ
* Czy wszystkie monitory z Wallboardami są potrzebne?


Database
========
* ``/var/atlassian/application-data/jira/dbconfig.xml``

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
=================
* Jakub Kubryński on Garbage Collector https://www.youtube.com/watch?v=LCr3XyHdaZk
* G1 GC ``-XX:+UseG1GC``
* ``Xmx``
* ``/opt/atlassian/jira/bin/setenv.sh``

.. literalinclude:: src/jira-gc.sh
    :caption: Jira Garbage Collector
    :language: console


Monitorowanie
=============
* http://www.stagemonitor.org/
* New Relic
* JavaMelody
* JIRA embedded tools (in settings):

    * JMX monitoring
    * SQL profiling


Rozwiązywanie problemów
=======================
.. code-block:: console

    grep '/rest' /opt/atlassian/jira/logs/access_log.* |awk '{print $7}' |sort |uniq -c |sort -n

* Dużo zapytań API (varnish requestów, np. dashboardów)
* Inne usługi wysycające pamięć na maszynie, aż do limitów JAVY
* Przy port forwardnig ``ssh -L 5432:localhost:5432 root@adresIP`` w ``/var/lib/pgsql/data/pg_hba.conf`` musi być md5 przy IPv4 i IPv6
* Create issue by URL: http://localhost:8080/secure/CreateIssueDetails!init.jspa?pid=10000&issuetype=10002


Assignments
===========

Administracja - Garbage Collector
---------------------------------
#. Zmień Garbage Collector na G1
#. Zmień Xmx na 1GB
#. Wepnij Java Melody do monitorowania

Administracja - Zmiana Javy
---------------------------
#. Zainstaluj nową Javę na serwerze w katalogu ``/opt/java/$VERSION``
#. Utwórz symlink ``/opt/java/default/`` wskazujący na ``/opt/java/$VERSION`` (dlaczego to dobra praktyka?)
#. Zrestartuj Jirę by wykorzystywała nową Javę
