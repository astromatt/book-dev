***********
Dirty hacks
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
* ``pip install atlassian-python-api``

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

.. warning:: Wymagany Python 3.6 lub nowszy

Atlassian Python API - Reindeksacja
-----------------------------------
#. Stwórz skrypt ``jira-reindex.py``
#. Skrypt wykorzystując bibliotekę ``atlassian-python-api`` ma reindeksować JIRĘ
#. Skrypt ``jira-reindex.py`` dodaj Crontab by był uruchamiany o 4 w nocy
#. Pamiętaj, że cron ma inne zmienne środowiskowe
