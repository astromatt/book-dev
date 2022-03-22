Migracja Bitbucket
==================


UWAGA
-----
* Bitbucket nie korzysta z bazy danych Postgres, tylko z wbudowanej h2 z persystencją; konieczna jest migracja do PostgreSQL!!
* Należy zwrócić uwagę, że bitbucket działa na tym samym serwerze co jira, dlatego adres jira.example.com wskazuje na tego samego hosta co bitbucket.example.com


Przed migracją
--------------
* Backup bazy dancyh
* Backup katalogu domowego aplikacji
* Backup konfiguracji proxypass w nginx


Struktura katalogów
-------------------
1. Stworzenie struktury katalogów na hoście docelowym:
   - `mkdir -p /home/bitbucket/`
   - `mkdir -p /home/bitbucket/home`
   - `mkdir -p /home/bitbucket/database`

2. Ustawienie uprawnień:
   - `chmod 755 -R /home/bitbucket/`


Przegląd konfiguracji zmiennych środowiskowych
----------------------------------------------
1. Wydobycie konfiguracji zmiennych środowiskowych bazy danych

    ```shell
    $ docker inspect bitbucketdb |grep -A13 "Env"
    "Env": [
        "POSTGRES_COLLATE_TYPE=C",
        "POSTGRES_USER=[hidden]",
        "POSTGRES_PASSWORD=[hidden]",
        "POSTGRES_DB=[hidden]",
        "POSTGRES_ENCODING=UNICODE",
        "POSTGRES_COLLATE=C",
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
    $ docker inspect bitbucket |grep -A20 "Env"
    "Env": [
        "SERVER_PROXY_NAME=bitbucket.example.com",
        "SERVER_PROXY_PORT=443",
        "SERVER_SCHEME=https",
        "SERVER_SECURE=true",
        "JVM_SUPPORT_RECOMMENDED_ARGS=-Dserver.additional-connector.1.port=7190",
        "PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "LANG=en_US.UTF-8",
        "LANGUAGE=en_US:en",
        "LC_ALL=en_US.UTF-8",
        "JAVA_VERSION=jdk8u262-b10",
        "JAVA_HOME=/opt/java/openjdk",
        "RUN_USER=bitbucket",
        "RUN_GROUP=bitbucket",
        "RUN_UID=2003",
        "RUN_GID=2003",
        "BITBUCKET_HOME=/var/atlassian/application-data/bitbucket",
        "BITBUCKET_INSTALL_DIR=/opt/atlassian/bitbucket",
        "ELASTICSEARCH_ENABLED=true",
        "APPLICATION_MODE=default"
    ],
    ```


Nazwy katalogów
---------------
1. Wydobycie nazwy katalogu bazy dancyh

    ```shell
    $ docker inspect bitbucketdb |grep -B1 '"Destination": "/var/lib/postgresql/data"'
    "Source": "/var/lib/docker/volumes/030037f565da8831005537407113d20a3f6893d73501d12a80065bfdc41d0066/_data",
    "Destination": "/var/lib/postgresql/data",
    ```

2. Wydobycie nazwy katalogu danych aplikacji

    ```shell
    $ docker inspect bitbucket |grep -B1 '"Destination": "/var/atlassian/application-data/bitbucket"'
    "Source": "/var/lib/docker/volumes/73c30cf27d011838fbfdb36992f4a3899b49918e2aa4201fd80719910286d957/_data",
    "Destination": "/var/atlassian/application-data/bitbucket",
    ```


Migracja Danych
---------------
1. Rsync bazy danych na serwer docelowy

    ```shell
    $ rsync -razv --delete /var/lib/docker/volumes/030037f565da8831005537407113d20a3f6893d73501d12a80065bfdc41d0066/_data/* jira.cloud.example.com:/home/bitbucket/database
    sent 5,305,864 bytes  received 23,811 bytes  969,031.82 bytes/sec
    total size is 48,020,887  speedup is 9.01
    ```

2. Rsync danych aplikacji na serwer docelowy

    ```shell
    $ rsync -razv --delete /var/lib/docker/volumes/73c30cf27d011838fbfdb36992f4a3899b49918e2aa4201fd80719910286d957/_data/* jira.cloud.example.com:/home/bitbucket/home
    sent 2,251,948,809 bytes  received 1,210,185 bytes  12,016,847.97 bytes/sec
    total size is 2,737,630,076  speedup is 1.22
    ```


Zmiana uprawnień
----------------
* wykonujemy na serwerze docelowym (w cloud)
* Ten krok jest ważny, inaczej kontener dockerowy będzie miał problem
  z zapisem i odczytem informacji w katalogach bazy danych i aplikacji
* `chown -R 999:999 /home/bitbucket/database`
* `chown -R 2003:2003 /home/bitbucket/home`


Przygotowanie skryptów startowych
---------------------------------
1. Do pliku `/home/jira/run-jiradb.sh` wpisz:

    ```shell
    docker run \
        --name bitbucketdb \
        --detach \
        --restart always \
        --network atlassian \
        --env POSTGRES_USER=... \
        --env POSTGRES_PASSWORD=... \
        --env POSTGRES_DB=... \
        --volume /home/bitbucket/database:/var/lib/postgresql \
        postgres:10
    ```

    Uwaga: w miejsce kropek (wartości zmiennych środowiskowych
    `--env POSTGRES_` wpisać dane zgodnie z ustawieniami wyciągniętymi
    w kroku: `Wydobycie konfiguracji zmiennych środowiskowych bazy danych`

2. Do pliku `/home/jira/run-jira.sh` wpisz:

    ```shell
    docker run \
        --name bitbucket \
        --detach \
        --restart always \
        --network atlassian \
        --env SERVER_PROXY_NAME=bitbucket.cloud.example.com \
        --env SERVER_PROXY_PORT=443 \
        --env SERVER_SCHEME=https \
        --env SERVER_SECURE=true \
        --env JVM_SUPPORT_RECOMMENDED_ARGS=-Dserver.additional-connector.1.port=7190 \
        --volume /home/bitbucket/home/:/var/atlassian/application-data/bitbucket \
        --publish 7999:7999 \
        --publish 7990:7990 \
        atlassian/bitbucket:7.6.0
    ```

3. Nadaj uprawnienia skryptom startowym:
    - `chmod +x /home/bitbucket/run-*.sh`


Uruchomienie kontenerów
-----------------------
1. Uruchomienie bazy danych na serwerze docelowym:
   - `/home/bitbucket/run-bitbucketdb.sh`

2. Uruchomienie aplikacji na serwerze docelowym:
   - `/home/bitbucket/run-bitbucket.sh`


Uruchomienie kontenerów
-----------------------
* W poniższych poleceniach docker konieczne jest wpisanie ustawień zmiennych
  środowiskowych wyciągniętych z kroku: `Przegląd konfiguracji zmiennych
  środowiskowych`

1. Uruchomienie bazy danych na serwerze docelowym


2. Uruchomienie aplikacji na serwerze docelowym

3. Uwaga:
   * na bitbucket.example.com jest uruchomiona wersja 7.6
   * przy migracji unikać pokusy upgrade do wersji latest (na chwilę obecną
     latest to 7.14.0)
   * UWAGA: Obecna licencja na Bitbucket skończyła się 10 grudnia 2020. Upgrade
     do nowej wersji spowoduje zablokowanie możliwości pushowania kodu bez
     bez wykupienia nowej licencji. Nie upgrade'ować do czasu jej kupienia!
   * Jeżeli zostnie uruchomiony `atlassian/bitbucket:latest` to proces
     upgrade zablokuje pushowanie kodu!


Weryfikacja
-----------
* `docker logs -f bitbucketdb`
* `docker logs -f bitbucket`


Konfiguracja Nginx
------------------
1. wprowadzić config do pliku `/home/nginx/conf/bitbucket.conf`

    ```lua
    server {
      listen 443 ssl;
      server_name         bitbucket.cloud.example.com;
      ssl_certificate     /opt/nginx/keys/bitbucket.crt;
      ssl_certificate_key /opt/nginx/keys/bitbucket.key;

      location / {
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Server $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass  http://bitbucket:7990;
        client_max_body_size 100M;
      }
    }

    server {
        listen 80;
        server_name bitbucket.cloud.example.com www.bitbucket.cloud.example.com;
        return 301 https://bitbucket.cloud.example.com$request_uri;
    }
    ```

2. Sprawdzamy czy działa:
   - `docker logs nginx -f`
   - otwieramy przeglądarkę na `https://bitbucket.cloud.example.com`


Konfiguracja po uruchomieniu
----------------------------
1. Base URL. Przy pierwszym zalogowaniu na Bitbucket dla kont, które mają
   uprawnienia administracyjen powinno wyskoczyć żółte powiadomienie w
   prawym górnym rogu:

   ```text
   Base URL mismatch You are accessing Bitbucket from a URL that does not
   match the configured base URL.
   Change it in Server Settings
   ```

   Aby wprowadzić zmianę należy:
   * Kliknąć opcję: `Change it in Server Settings` lub wejść na
     https://bitbucket.cloud.example.com/admin/server-settings
   * Zmienić opcję konfiguracyjną `Base URL` z `https://bitbucket.example.com`
    na `https://bitbucket.cloud.example.com`

2. Application Links. Aby wprowadzić zmianę należy:
   * W opcjach konfiguracyjncyh wejść na `Application Links`, lub wejść na:
     https://bitbucket.cloud.example.com/plugins/servlet/applinks/listApplicationLinks
   * Zalogować się na swoje konto
   * Wybrać `JIRA` a następnie kliknąć ikonę ołówka po prawej
   * Ustawić: `Application URL`: `https://jira.cloud.example.com`
   * Ustawić: `Display URL`: `https://jira.cloud.example.com`

3. Migracja Bazy Danych z H2 do Postgres
    * Wejść na https://bitbucket.cloud.example.com/admin/db
    * Kliknąć przycisk `Migrate database`
    * Dane zgodnie z ustawieniami wyciągniętymi w kroku:
      `Wydobycie konfiguracji zmiennych środowiskowych bazy danych`
    * Database Type: `PostgreSQL`
    * Hostname: `bitbucketdb`
    * Port: `5432`
    * Database name: `[hidden]`
    * Database username: `[hidden]`
    * Database passowrd: `[hidden]`
    * Kliknąć przycisk `Test` i powinno pojawić się: "Successfully established
      database connection"
    * Kliknąć przycisk `Start migration`
    * Proces migraji powinien trwać kilka minut
    * Po migracji wszystkie opcje konfiguracyjne powinny być poprawnie
      ustawione i zapisane na stałe


Upgrade
-------
* UWAGA: Obecna licencja na Bitbucket skończyła się 10 grudnia 2020. Upgrade
  do nowej wersji spowoduje zablokowanie możliwości pushowania kodu bez
  bez wykupienia nowej licencji. Nie upgrade'ować do czasu jej kupienia!

* UWAGA: Support and updates for Atlassian Bitbucket ended on 10 Dec 2020.
  Updates released after this date are not valid with this license.

1. Można wykonać upgrade aplikacji, bez konieczności podnoszenia Postgres do
   najnowszej wersji, np. `postgres:13.3`

2. Aby zaktualizować bazę danych:
    * zatrzymać aplikację oraz bazę danych i usunąć kontener
    * zrobić backup za pomocą polecenia `pg_dumpall` do pliku
    * następnie usunąć katalog bazy danych `/home/bitbucket/database`
    * uruchomić nowy image, np. `postgres:13.3`
    * zaimportować dane za pomocą polecenia `psql` z pliku z backupem danych

3. Upgrade aplikacji:
   * Aktualną wersję można sprawdzić na:
      https://hub.docker.com/r/atlassian/bitbucket/tags?page=1&ordering=last_updated

   * Wykonanie upgrade:

    ```shell
    $ docker stop bitbucket
    $ docker rm bitbucket
    $ docker run \
        --name bitbucket \
        --detach \
        --restart always \
        --network atlassian \
        --env SERVER_PROXY_NAME=bitbucket.cloud.example.com \
        --env SERVER_PROXY_PORT=443 \
        --env SERVER_SCHEME=https \
        --env SERVER_SECURE=true \
        --env JVM_SUPPORT_RECOMMENDED_ARGS=-Dserver.additional-connector.1.port=7190 \
        --volume /home/bitbucket/home/:/var/atlassian/application-data/bitbucket \
        --publish 7999:7999 \
        --publish 7990:7990 \
        atlassian/bitbucket:7.14.0
    ```

4. Upgrade aplikacji i uruchomienie powinno trwać kilka minut
   - można podejrzeć logi `docker logs -f bitbucket`
