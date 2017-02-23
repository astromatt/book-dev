Zadania do rozwiązania
======================

Instalacja pakietów za pomocą `Puppet`
--------------------------------------
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/packages.pp``
- Zainstaluj następujące pakiety za pomocą `Puppet`:

    - ``nmap``
    - ``htop``
    - ``git``

- Upewnij się by `Puppet` wykonał polecenie ``apt-get update`` na początku

Zmiana hostname
---------------
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/hostname.pp``
- Za pomocą manifestu zmień hostname maszyny na ``ecosystem.local``
- Upewnij się, że po wpisaniu polecenia ``hostname`` będzie ustawiona na odpowiednią wartość
- Upewnij się, że hostname nie przywróci się do domyślnej wartości po ponownym uruchomieniu

Zarządzanie użytkownikami, grupami i katalogami
-----------------------------------------------
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/users.pp``
- Upewnij się, że użytkownik ``myuser`` istnieje, ma ``uid=1337`` i należy do grupy ``mygroup``
- Upewnij się, że grupa ``mygroup`` istnieje i ma ``gid=99``
- Upewnij się, że:

    - Katalog ``/var/www`` istnieje
    - Właścicielem jego jest user ``myuser``
    - Właścicielem jego jest grupa ``mygroup``
    - Ma uprawnienia ``rwxr-xr-x``

Instalacja i konfiguracja Apache2
---------------------------------
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/apache.pp``
- Zainstaluj i skonfiguruj `Apache 2` wykorzystując moduł `Puppet`
- Z terminala wygeneruj certyfikaty self signed OpenSSL i umieść je w ``/etc/ssl/``:

    - ``/etc/ssl/ssl.example.com.cert``
    - ``/etc/ssl/ssl.example.com.key``

- Za pomocą `Puppet` stwórz dwa vhosty:

    - ``insecure.example.com`` na porcie ``80`` i z katalogiem domowym ``/var/www/insecure.example.com``
    - ``ssl.example.com`` na porcie ``443`` i z katalogiem domowym ``/var/www/ssl.example.com`` + używanie certyfikatów SSL wcześniej wygenerowanych

- Stwórz pliki z treścią:

    - ``/var/www/insecure.example.com/index.html`` z treścią ``Ehlo World! - Insecure``
    - ``/var/www/ssl.example.com/index.html`` z treścią ``Ehlo World! - SSL!``

- W przeglądarce na komputerze lokalnym wejdź na stronę:

    - http://127.0.0.1:8080
    - https://127.0.0.1:8443

Instalacja i konfiguracja MySQL
-------------------------------
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/mysql.pp``
- Zainstaluj bazę danych `MySQL` wykorzystując moduł `Puppet`
- Ustaw hasło dla użytkownika ``root`` na ``mypassword``
- Ustaw nasłuchiwanie serwera ``mysqld`` na wszystkich interfejsach (``0.0.0.0``)
- Stwórz bazę danych ``mydb`` z ``utf-8``
- Stwórz usera ``myusername`` z hasłem ``mypassword``
- Nadaj wszystkie uprawnienia dla usera ``myusername`` dla bazy ``mydb``
- Ustaw backupowanie bazy danych do ``/tmp/mysql-backup``

Instalacja i konfiguracja Tomcat
--------------------------------
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/tomcat.pp``
- Zainstaluj język `Java` za pomocą modułu `Puppet`
- Zainstaluj `Tomcat 8` za pomocą `Puppet` w katalogu ``/opt/tomcat8``
- Skonfiguruj dwie instancje `Tomcat` działające jednocześnie:

    - Jedna uruchamiana na domyślnych portach
    - Druga uruchamiana na ``8006`` a connector z portu ``8081`` przekierowywał na ``8443``
    - Na pierwszej uruchom ``war`` z lokacji ``/opt/tomcat8/webapps/docs/appdev/sample/sample.war``
