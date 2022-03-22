Jira Migracja
=============


Testy
-----
1. Weryfikacja działających kontenerów i ich ustawień:
	- `docker ps`
    - `docker inspect jiradb |grep -B1 '"Destination": "/var/lib/postgresql/data"'`
    - `docker inspect jiradb |grep -A13 "Env"`
    - `docker inspect jira |grep -B1 '"Destination": "/var/atlassian/application-data/jira"'`
    - `docker inspect jira |grep -A19 "Env"`
    - `docker inspect bitbucketdb |grep -B1 '"Destination": "/var/lib/postgresql/data"'`
    - `docker inspect bitbucketdb |grep -A13 "Env"`
    - `docker inspect bitbucket |grep -B1 '"Destination": "/var/atlassian/application-data/bitbucket"'`
    - `docker inspect bitbucket |grep -A20 "Env"`
    - `docker inspect nginx |grep -A5 "Env"`
    - `docker inspect nginx |grep -B1 '"Destination": "/etc/nginx/conf.d",'`
    - `docker inspect nginx |grep -B1 '"Destination": "/opt/nginx/keys",'`

1. Instalacja przeglądarki elinks
    - `apt install elinks`

1. Konfiguracja testowa
    - Dodano wpis w `/etc/hosts` w celach testowych: `127.0.0.1 jira.cloud.example.com`  # usunąć po testach

1. Testy
    - `elinks 'http://jira.cloud.example.com'`
    - `docker logs -f nginx`

1. Otwórz przeglądarkę na swoim komputerze `http://jira.cloud.example.com`


TODO
----
1. Poprawić uprawnienia do katalogów `/home/jira` oraz `/home/bitbucket` i ich bezpośrednich podfolderów
1. Uwaga!! Bitbucket nie korzysta z bazy danych Postgres, tylko z wbudowanej h2 z persystencją; konieczna jest migracja!!
