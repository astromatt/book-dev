# Vagrant

## Tworzenie i konfigurowanie maszyny
- Poniższe polecenia wykonaj w pliku Vagrantfile
- Stwórz maszynę z oficjalnego obrazu 32 bitowej wersji Ubuntu LTS (Long Time Support)
- Ustaw hostname na `ubuntu.local`
- Jeżeli masz słabszą maszynę (2 CPU core, 4 GB RAM):
	- 1 CPU core
	- 1024 MB Ram
- Jeżeli masz lepszy komputer:
	- 2 CPU core
	- 4096 MB RAM
- Ustaw forwarding portu 80 na 8080 hosta oraz 443 na 8443
- Ustaw aby ten katalog był synchronizowany na maszynie gościa w `/var/www/host`
- Podnieś maszynę i rozpocznij pobieranie obrazu


# Puppet

## Podstawowa konfiguracja maszyny
- manifest do tego zadania zapisz w katalogu `/etc/puppet/manifests/packages.pp`
- Zrób by Puppet wykonał polecenie `apt-get update`
- Upewnij się, że następujące paczki są zainstalowane:
    - `nmap`
    - `htop`
    - `git`

## Zmiana hostname
- manifest do tego zadania zapisz w katalogu `/etc/puppet/manifests/hostname.pp`
- Za pomocą manifestu Puppeta zmień hostname maszyny na `ecosystem.local`
- Upewnij się, że po wpisaniu polecenia `hostname` będzie ustawiona na odpowiednią wartość.

## Zarządzanie użytkownikami i grupami
- manifest do tego zadania zapisz w katalogu `/etc/puppet/manifests/www-data.pp`
- Za pomocą Puppet upewnij się by był użytkownik `www-data` i miał `uid=33`
- Za pomocą Puppet upewnij się by była grupa `www-data` i miała `gid=33`
- Upewnij się że katalog `/var/www` istnieje i właścicielem jego są user `www-data` i grupa `www-data` i że ma uprawnienia `rwxr-xr-x`

## Konfiguracja Apache2
- manifest do tego zadania zapisz w katalogu `/etc/puppet/manifests/apache.pp`
- Zainstaluj i skonfiguruj Apache2 wykorzystując moduł Puppet
- Z terminala wygeneruj certyfikaty self signed OpenSSL (`.cert` i `.key`) (za pomocą i umieść je w `/etc/ssl/`)
- Za pomocą Puppet Stwórz dwa vhosty
    - `insecure.example.com` na porcie 80 i z katalogiem domowym `/var/www/insecure.example.com`
    - `ssl.example.com` na porcie 443 i z katalogiem domowym `/var/www/ssl.example.com` + używanie certyfikatów SSL wcześniej wygenerowanych
- Stwórz pliki z treścią:
    - `/var/www/insecure.example.com/index.html` z treścią `Ehlo World!`
    - `/var/www/ssl.example.com/index.html` z treścią `Ehlo SSL!`
- W przeglądarce na laptopie wejdź na stronę:
    - http://127.0.0.1:8080
    - https://127.0.0.1:8443

## Instalacja i konfiguracja MySQL
- manifest do tego zadania zapisz w katalogu `/etc/puppet/manifests/mysql.pp`
- zainstaluj moduł bazy MySQL wykorzystując Puppeta
- ustaw hasło roota na mypassword
- ustaw nasłuchiwanie serwera `mysqld` na `0.0.0.0`
- stwórz bazę danych `mydb` z `utf-8`
- stwórz usera `myusername` z hasłem `mypassword`
- nadaj wszystkie uprawnienia dla usera `myusername` dla bazy `mydb`
- ustaw backupowanie bazy danych do `/tmp/mysql-backup`

## Instalacja Java i Tomcat
- manifest do tego zadania zapisz w katalogu `/etc/puppet/manifests/tomcat.pp`
- zainstaluj Javę za pomocą Puppeta
- zainstaluj Tomcat8 za pomocą Puppeta do `/opt/tomcat8`
- Skonfiguruj dwie instancje Tomcata działające jednocześnie
    - Jedna uruchamiana na domyślnych portach
    - Druga uruchamiana na 8006 a connector z portu 8081 przekierowywał na 8443
    - Na pierwszej uruchom WAR z lokacji `/opt/tomcat8/webapps/docs/appdev/sample/sample.war`

## Automatyzacja stawiania Vagrant + Puppet
- Skopiuj dotychczasowe manifesty puppeta na swój komputer do katalogu `puppet/manifests/`
- Skopiuj certyfikaty SSL, które wygenerowałeś na swój komputer do katalogu `conf/ssl/`
- Wyłącz maszynę z Vagrantem `vagrant halt` a następnie ją usuń `vagrant destroy`
- Edytuj plik `Vagrantfile` i dopisz, by maszyna była stawiana z manifestów Puppeta
- W pliku `Vagrantfile` trzymaj jak najmniej logiki i wszystko rób za pomocą Puppeta
- Zrób by certyfikaty były przenoszone z Twojego laptopa na maszynę gościa (nie generuj nowych, tylko wykorzystaj stare!) oczywiście za pomocą Puppeta
- Każdy z manifestów powinien być w osobnych plikach a jeden `default.pp` powinien includować pozostałe

# Jenkins

## Instalacja i konfiguracja Jenkinsa
- Postaw Jenkins za pomocą paczek DEB
- Zaciągnij repo git https://github.com/SonarSource/sonar-examples.git
- Zacznij budować różne projekty `sonar-examples/projects/languages/java`

## Budowanie Pull Requestów
- Skonfiguruj plan by budował pull requesty

## Budowanie Checkstyle, PMD, Findbugs i Jacoco
- Zaciągnij repo git https://github.com/SonarSource/sonar-examples.git
- Zacznij budować różne projekty `sonar-examples/projects/languages/java`
- Wyniki upublicznij w SonarQube

## Jenkins DSL
- Przepisz całą konfigurację wykorzustując plik Jenkins DSL
