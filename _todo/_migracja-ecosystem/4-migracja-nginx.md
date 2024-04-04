Migracja Nginx
==============


Struktura katalogów
-------------------
1. Stworzenie struktury katalogów na hoście docelowym:
    - `mkdir /home/nginx`
    - `mkdir /home/nginx/config`
    - `mkdir /home/nginx/keys`

2. Zmiana uprawnień na czas rsync, dla ułatwienia przenoszenia danych:
   - `chmod 777 -R /home/nginx/`


Przegląd konfiguracji zmiennych środowiskowych
----------------------------------------------
1. Wydobycie konfiguracji zmiennych środowiskowych aplikacji

    ```shell
    $ docker inspect nginx |grep -A5 "Env"
    "Env": [
        "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "NGINX_VERSION=1.19.2",
        "NJS_VERSION=0.4.3",
        "PKG_RELEASE=1~buster"
    ],
    ```


Migracja Konfiguracji
---------------------
1. Wydobycie nazwy katalogu named volume Nginx

    ```shell
    $ docker inspect nginx |grep -B1 '"Destination": "/etc/nginx/conf.d",'
    "Source": "/home/altlasian/nginx",
    "Destination": "/etc/nginx/conf.d",
    ```

2. Rsync z jira.example.com do jira.cloud.example.com

    ```shell
    $ rsync -razv --delete altlasian/nginx/nginx.conf jira.cloud.example.com:/home/nginx/config/
    sent 615 bytes  received 35 bytes  433.33 bytes/sec
    total size is 2,349  speedup is 3.61
    ```


Migracja Certyfikatów
---------------------
1. Wydobycie nazwy katalogu named volume Nginx

    ```shell
    $ docker inspect nginx |grep -B1 '"Destination": "/opt/nginx/keys",'
    "Source": "/opt/nginx/keys",
    "Destination": "/opt/nginx/keys",
    ```

2. Rsync z jira.example.com do jira.cloud.example.com

    ```shell
    $ rsync -razv --delete /opt/nginx/keys/* jira.cloud.example.com:/home/nginx/keys
    sent 14,088 bytes  received 168 bytes  9,504.00 bytes/sec
    total size is 19,562  speedup is 1.37a
    ```


Konfiguracja
------------
1. Upewnić się, że skopiowano konfigurację `jira.conf` oraz `bitbucket.conf`


Uruchomienie Kontenera
----------------------
1. Uruchomienie aplikacji na serwerze docelowym

    ```shell
    $ docker run \
         --name nginx \
         --detach \
         --restart always \
         --network atlassian \
         --volume /home/nginx/config:/etc/nginx/conf.d \
         --volume /home/nginx/keys:/opt/nginx/keys/ \
         --publish 80:80 \
         --publish 443:443 \
         nginx:1.21.0
    ```
