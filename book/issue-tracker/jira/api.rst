JIRA API
========

REST API
--------
- https://docs.atlassian.com/software/jira/docs/api/REST/server/
- https://developer.atlassian.com/jiradev/jira-apis/about-the-jira-rest-apis/jira-rest-api-tutorials
- https://docs.atlassian.com/jira/REST/latest/
- https://jira.atlassian.com/plugins/servlet/restbrowser#/

Atlassian CLI
-------------
- https://marketplace.atlassian.com/plugins/org.swift.atlassian.cli/cloud/overview
- https://bobswift.atlassian.net/wiki/spaces/ACLI/overview

Atlassian Python API
--------------------
- https://github.com/AstroTech/atlassian-python-api>
- ``pip install atlassian-python-api``

Assignments
-----------

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

.. toggle-code-block:: console
    :label: Pokaż jak uruchomić skrypt project administrators

    from atlassian import Confluence
    from atlassian import Jira


    jira = Jira(
        url='http://localhost:8080',
        username='admin',
        password='admin')

    confluence = Confluence(
        url='http://localhost:8090',
        username='admin',
        password='admin')


    html = ['<table><tr><th>Project Key</th><th>Project Name</th><th>Leader</th><th>Email</th></tr>']

    for data in jira.project_leaders():
        row = '<tr><td>{project_key}</td><td>{project_name}<td></td>{lead_name}<td></td><a href="mailto:{lead_email}">{lead_email}</a></td></tr>'
        html.append(row.format(**data))

    html.append('</table><p></p><p></p>')

    status = confluence.create_page(
        space='DEMO',
        parent_id=confluence.get_page_id('DEMO', 'demo'),
        title='JIRA Administrators',
        body='\r\n'.join(html))

    pprint(status)

Atlassian Python API - Changelog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Napisz skrypt ``jira-changelog.py``
#. Wygeneruj Changelog, tj. listę zadań które zmieniły się pomiędzy dwoma wersjami (wykorzystaj JQL)

    - Wynik zapisz w Confluence na osobnej stronie dla każdej wersji
    - Jeżeli nie masz zainstalowanego Confluence to zrzuć do pliku ``/var/www/changelog-XXX.html`` i skonfiguruj nginx aby wyświetlał tą stronę, XXX to nazwa wersji
