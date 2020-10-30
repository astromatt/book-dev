***********
Dirty Hacks
***********

Manipulacje na bazie
====================


Django ORM
==========
Django Inspect DB + Jira = Django ORM


Skryptowanie
============


Time tracking
=============


Atlassian Python API
====================
* https://github.com/atlassian-api/atlassian-python-api
* https://github.com/atlassian-api/atlassian-python-api/tree/master/examples/jira
* ``pip install atlassian-python-api``

.. literalinclude:: src/jira-reindex.py
    :caption: Jira reindex
    :language: python

.. literalinclude:: src/jira-project-administrators.py
    :caption: Jira Project Administrators
    :language: python


Atlassian CLI
=============
* https://marketplace.atlassian.com/plugins/org.swift.atlassian.cli/cloud/overview
* https://bobswift.atlassian.net/wiki/spaces/ACLI/overview


DevTools Ecosystem Integration
==============================
* https://dev.astrotech.io/git/internals/hooks.html#branch-hook
* https://dev.astrotech.io/git/tools/git-flow.html#konwencje-nazewnicze
* https://dev.astrotech.io/summary/pictures.html#ecosystem
* https://dev.astrotech.io/summary/pictures.html#jira
* https://dev.astrotech.io/summary/pictures.html#ci-cd
* ``git log --oneline --format='"%h", "%an", "%ae", "%ad", "%s"' --date=iso > ~/Desktop/git-log.csv``


REST API
========
* https://developer.atlassian.com/server/jira/platform/rest-apis/
* https://docs.atlassian.com/jira-software/REST/latest/
* https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/
* https://developer.atlassian.com/jiradev/jira-apis/about-the-jira-rest-apis/jira-rest-api-tutorials
* https://jira.atlassian.com/plugins/servlet/restbrowser#/


Create Issue From URL
=====================
* Z menu u góry wybierz "Projects" -> "View All projects" -> "Inspect Element" (źródło strony) -> znajdź: "data-project-id" (to będzie "pid")
* http://18.195.183.213:8080/secure/CreateIssueDetails!init.jspa?pid=10000&issuetype=10002

.. code-block:: javascript

    javascript:window.location='http://18.195.183.213:8080/secure/CreateIssueDetails!init.jspa?pid=10006&issuetype=10003&fixVersions=10015&components=10002&summary=' + document.getElementById('search_form_input').value


Assignments
===========

Atlassian Python API - Instalacja
---------------------------------
#. Zainstaluj bibliotekę Atlassian Python API ``atlassian-python-api``

.. note:: Kod biblioteki dostępny jest na GitHub https://github.com/atlassian-api/atlassian-python-api

.. warning:: Wymagany Python 3.6 lub nowszy

Atlassian Python API - Reindeksacja
-----------------------------------
#. Stwórz skrypt ``jira-reindex.py``
#. Skrypt wykorzystując bibliotekę ``atlassian-python-api`` ma reindeksować JIRĘ
#. Skrypt ``jira-reindex.py`` dodaj Crontab by był uruchamiany o 4 w nocy
#. Pamiętaj, że cron ma inne zmienne środowiskowe
