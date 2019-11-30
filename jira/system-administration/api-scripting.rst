*****************
API and Scripting
*****************

Accessing Jira
==============

REST API
--------
* https://docs.atlassian.com/software/jira/docs/api/REST/server/
* https://developer.atlassian.com/jiradev/jira-apis/about-the-jira-rest-apis/jira-rest-api-tutorials
* https://docs.atlassian.com/jira/REST/latest/
* https://jira.atlassian.com/plugins/servlet/restbrowser#/

Atlassian CLI
-------------
* https://marketplace.atlassian.com/plugins/org.swift.atlassian.cli/cloud/overview
* https://bobswift.atlassian.net/wiki/spaces/ACLI/overview

Atlassian Python API
--------------------
* https://github.com/atlassian-api/atlassian-python-api
* ``pip install atlassian-python-api``


Sctipting
=========

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


Assignments
===========

Atlassian Python API - Instalacja
---------------------------------
#. Zainstaluj bibliotekę Atlassian Python API ``atlassian-python-api``

.. note:: Kod biblioteki dostępny jest na GitHub https://github.com/atlassian-api/atlassian-python-api

.. warning:: Wymagany Python 3.4 lub nowszy

Atlassian Python API - Reindeksacja
-----------------------------------
#. Stwórz skrypt ``jira-reindex.py``
#. Skrypt wykorzystując bibliotekę ``atlassian-python-api`` ma reindeksować JIRĘ
#. Skrypt ``jira-reindex.py`` dodaj Crontab by był uruchamiany o 4 w nocy
#. Pamiętaj, że cron ma inne zmienne środowiskowe

Atlassian Python API - Project Administrators
---------------------------------------------
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
--------------------------------
#. Napisz skrypt ``jira-changelog.py``
#. Wygeneruj Changelog, tj. listę zadań które zmieniły się pomiędzy dwoma wersjami (wykorzystaj JQL)

    - Wynik zapisz w Confluence na osobnej stronie dla każdej wersji
    - Jeżeli nie masz zainstalowanego Confluence to zrzuć do pliku ``/var/www/changelog-XXX.html`` i skonfiguruj nginx aby wyświetlał tą stronę, XXX to nazwa wersji
