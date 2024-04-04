Migracja Jira
=============


Przed migracją
--------------
* Backup bazy dancyh
* Backup katalogu domowego aplikacji
* Backup konfiguracji proxypass w nginx


Struktura katalogów
-------------------
1. Stworzenie struktury katalogów na hoście docelowym:
   - `mkdir -p /home/jira/`
   - `mkdir -p /home/jira/home`
   - `mkdir -p /home/jira/database`

2. Ustawienie uprawnień:
   - `chmod 755 -R /home/jira/`


Przegląd konfiguracji zmiennych środowiskowych
----------------------------------------------
1. Wydobycie konfiguracji zmiennych środowiskowych bazy danych

    ```shell
    $ docker inspect jiradb |grep -A13 "Env"
    "Env": [
        "POSTGRES_USER=[hidden]",
        "POSTGRES_PASSWORD=[hidden]",
        "POSTGRES_DB=[hidden]",
        "POSTGRES_ENCODING=UNICODE",
        "POSTGRES_COLLATE=C",
        "POSTGRES_COLLATE_TYPE=C",
        "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/10/bin",
        "GOSU_VERSION=1.12",
        "LANG=en_US.utf8",
        "PG_MAJOR=10",
        "PG_VERSION=10.14-1.pgdg90+1",
        "PGDATA=/var/lib/postgresql/data"
    ],
    ```

1. Wydobycie konfiguracji zmiennych środowiskowych aplikacji

    ```shell
    $ docker inspect jira |grep -A19 "Env"
    "Env": [
        "ATL_PROXY_NAME=jira.example.com",
        "ATL_PROXY_PORT=443",
        "ATL_TOMCAT_SCHEME=https",
        "ATL_TOMCAT_SECURE=true",
        "JIRA_DATABASE_URL=postgresql://[hidden]@jira-database/[hidden]",
        "JIRA_DB_PASSWORD=[hidden]",
        "PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "LANG=en_US.UTF-8",
        "LANGUAGE=en_US:en",
        "LC_ALL=en_US.UTF-8",
        "JAVA_VERSION=jdk8u262-b10",
        "JAVA_HOME=/opt/java/openjdk",
        "RUN_USER=jira",
        "RUN_GROUP=jira",
        "RUN_UID=2001",
        "RUN_GID=2001",
        "JIRA_HOME=/var/atlassian/application-data/jira",
        "JIRA_INSTALL_DIR=/opt/atlassian/jira"
    ],
    ```

Nazwy katalogów
---------------
1. Wydobycie nazwy katalogu bazy dancyh

    ```shell
    $ docker inspect jiradb |grep -B1 '"Destination": "/var/lib/postgresql/data"'
    "Source": "/var/lib/docker/volumes/6c0c836d9d85d971b1fa4e14cc6ab60cd54eb51c58c4066a86da4483c0980ba8/_data",
    "Destination": "/var/lib/postgresql/data",
    ```

2. Wydobycie nazwy katalogu danych aplikacji

    ```shell
    $ docker inspect jira |grep -B1 '"Destination": "/var/atlassian/application-data/jira"'`
    "Source": "/var/lib/docker/volumes/e322d619e228ffb90792974b2bc33288126acf1ec4154f9d57c5cb54620a71e5/_data",
    "Destination": "/var/atlassian/application-data/jira",
    ```


Migracja Danych
---------------
1. Rsync bazy danych na serwer docelowy

    ```shell
    $ rsync -razv --delete /var/lib/docker/volumes/6c0c836d9d85d971b1fa4e14cc6ab60cd54eb51c58c4066a86da4483c0980ba8/_data/* jira.cloud.example.com:/home/jira/database
    sent 58,006,863 bytes  received 101,377 bytes  2,834,548.29 bytes/sec
    total size is 393,669,602  speedup is 6.77
    ```

2. Rsync danych aplikacji na serwer docelowy

    ```shell
    $ rsync -razv  --delete /var/lib/docker/volumes/e322d619e228ffb90792974b2bc33288126acf1ec4154f9d57c5cb54620a71e5/_data/* jira.cloud.example.com:/home/jira/home
    sent 1,835,402,087 bytes  received 152,803 bytes  17,235,257.18 bytes/sec
    total size is 2,665,654,176  speedup is 1.45
    ```


Zmiana uprawnień
----------------
* wykonujemy na serwerze docelowym (w cloud)
* Ten krok jest ważny, inaczej kontener dockerowy będzie miał problem
  z zapisem i odczytem informacji w katalogach bazy danych i aplikacji
* `chown -R 999:999 /home/jira/database`
* `chown -R 2001:2001 /home/jira/home`


Przygotowanie skryptów startowych
---------------------------------
1. Do pliku `/home/jira/run-jiradb.sh` wpisz:

    ```shell
    docker run \
        --name jiradb \
        --detach \
        --restart always \
        --network atlassian \
        --env POSTGRES_USER=... \
        --env POSTGRES_PASSWORD=... \
        --env POSTGRES_DB=... \
        --volume /home/jira/database:/var/lib/postgresql/data \
        postgres:10
    ```

    Uwaga: w miejsce kropek (wartości zmiennych środowiskowych
    `--env POSTGRES_` wpisać dane zgodnie z ustawieniami wyciągniętymi
    w kroku: `Wydobycie konfiguracji zmiennych środowiskowych bazy danych`

2. Do pliku `/home/jira/run-jira.sh` wpisz:

    ```shell
    docker run \
        --name jira \
        --detach \
        --restart always \
        --network atlassian \
        --env ATL_PROXY_NAME=jira.cloud.example.com \
        --env ATL_PROXY_PORT=443 \
        --env ATL_TOMCAT_SCHEME=https \
        --env ATL_TOMCAT_SECURE=true \
        --volume /home/jira/home/:/var/atlassian/application-data/jira \
        atlassian/jira-software:8.12.2
    ```

3. Nadaj uprawnienia skryptom startowym:
    - `chmod +x /home/jira/run-*.sh`


Uruchomienie kontenerów
-----------------------
1. Uruchomienie bazy danych na serwerze docelowym:
   - `/home/jira/run-jiradb.sh`

2. Uruchomienie aplikacji na serwerze docelowym:
   - `/home/jira/run-jira.sh`

3. Jira po migracji uruchamia się kilka do kilkunastu minut i to jest
   "normalne" zachowanie. Czasami przeprowadzany jest proces reindeksacji i to
   on tyle trwa. W tym czasie w logach `docker logs -f jira` można zobaczyć:

    ```log
    2021-06-28 21:31:28,976+0000 Caesium-1-1 INFO      [c.a.jira.upgrade.UpgradeScheduler] JIRA upgrades completed successfully
    2021-06-28 21:31:28,984+0000 Caesium-1-1 INFO      [c.a.jira.upgrade.UpgradeScheduler] Plugins upgrades completed successfully
    2021-06-28 21:31:28,985+0000 Caesium-1-1 INFO      [c.a.jira.upgrade.UpgradeIndexManager] Reindexing is not allowed after this upgrade and there is no immediate reindex requests
    ```

5. Późniejsze restarty będą trwały znacznie krócej (około 2-3 minuty)

6. Uwaga:
   * na jira.example.com jest uruchomiona wersja 8.12.2
   * przy migracji unikać pokusy upgrade do wersji latest (na chwilę obecną
     latest to 8.17.1)
   * jeżeli zostnie uruchomiony `atlassian/jira-software:latest`  to proces
     upgrade może trwać nawet godzinę!
   * Nie należy wtedy przerywać procesu!

7. Aby wykonać upgrade Jiry należy uruchomić to samo polecenie `docker run`,
   z nowszą wersją obrazu
    * dobrą praktyką jest unikanie wpisywania `latest`


Konfiguracja Nginx
------------------
* wprowadzić config do pliku `/home/nginx/conf/jira.conf`

    ```lua
    server {
      listen 443 ssl;
      server_name          jira.cloud.example.com;
      ssl_certificate      /opt/nginx/keys/jira.crt;
      ssl_certificate_key  /opt/nginx/keys/jira.key;

      location / {
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Server $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass  http://jira:8080;
        client_max_body_size 10M;
      }
    }

    server {
        listen 80;
        server_name jira.cloud.example.com www.jira.cloud.example.com;
        return 301 https://jira.cloud.example.com$request_uri;
    }
    ```

Konfiguracja po uruchomieniu
----------------------------
1. Base URL. Przy pierwszym zalogowaniu na Jirę dla kont, które mają
   uprawnienia administracyjen powinno wyskoczyć zapytanie:

   ```text
   Jira's base URL is set to https://jira.example.com but you are accessing Jira
   from https://jira.cloud.example.com.
   ```

   Aby wprowadzić zmianę należy:
   * Skrót klawiszowy `gg`
   * Wpisać: `Global configuration`
   * Zalogować się na swoje konto
   * Edit Settings (przycisk po prawej u góry)
   * Zmienić opcję konfiguracyjną `Base URL` z `https://jira.example.com`
    na `https://jira.cloud.example.com`

2. Application Links. Aby wprowadzić zmianę należy:
   * Skrót klawiszowy `gg`
   * Wpisać: `Application Links`
   * Zalogować się na swoje konto
   * Wybrać `Bitbucket` a następnie kliknąć ikonę ołówka po prawej
   * Ustawić: `Application URL`: `http://bitbucket:7990`
   * Ustawić: `Display URL`: `https://bitbucket.cloud.example.com`

3. Reindeksacja:
   * Po migracji dobrze jest wykonać reindeksację pełną
   * Skrót klawiszowy `gg`
   * Wpisać: `Indexing`
   * Zalogować się na swoje konto
   * W sekcji `Re-indexing` Wybieramy opcję `Full re-index`
   * Klikamy przycisk `Re-index`
   * Reindeksacja może potrwać kilka minut


Upgrade
-------
1. Można wykonać upgrade aplikacji, bez konieczności podnoszenia Postgres do
   najnowszej wersji, np. `postgres:13.3`

2. Aby zaktualizować bazę danych:
    * zatrzymać aplikację oraz bazę danych i usunąć kontener
    * zrobić backup za pomocą polecenia `pg_dumpall` do pliku
    * następnie usunąć katalog bazy danych `/home/jira/database`
    * uruchomić nowy image, np. `postgres:13.3`
    * zaimportować dane za pomocą polecenia `psql` z pliku z backupem danych

3. Upgrade aplikacji:
   * Aktualną wersję można sprawdzić na:
      https://hub.docker.com/r/atlassian/jira-software/tags?page=1&ordering=last_updated

   * Wykonanie upgrade:

     ```shell
     $ docker stop jira
     $ docker rm jira
     $ docker run \
         --name jira \
         --detach \
         --restart always \
         --network atlassian \
         --env ATL_PROXY_NAME=jira.cloud.example.com \
         --env ATL_PROXY_PORT=443 \
         --env ATL_TOMCAT_SCHEME=https \
         --env ATL_TOMCAT_SECURE=true \
         --volume /home/jira/home/:/var/atlassian/application-data/jira \
         atlassian/jira-software:8.17.1
     ```

4. Upgrade aplikacji i uruchomienie powinno trwać kilka minut
   - można podejrzeć logi `docker logs -f jira`
