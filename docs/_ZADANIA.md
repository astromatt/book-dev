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
- Zrób by maszyna była stawiana z manifestu Puppeta
- Podnieś maszynę i rozpocznij pobieranie obrazu


# Puppet

## Zarządzanie użytkownikami i grupami
- Stwórz plik `/etc/puppet/manifests/www-data.pp`:
- Upewnij się że instnieje grupa www-data i ma gid=33
- Upewnij się, że istnieje user www-data i należy do grupy www-data i ma uid=33

## Podstawowa konfiguracja maszyny
- Zainstaluj Puppeta
- Zrób by Puppet wykonał polecenie `apt-get update`
- Upewnij się, że następujące paczki są zainstalowane:
    - `nmap`
    - `htop`
    - `git`

## Zmiana hostname
- Za pomocą manifestu Puppeta zmień hostname maszyny na `ecosystem.local`
- Upewnij się, że po wpisaniu polecenia `hostname` będzie ustawiona na odpowiednią wartość.

## Konfiguracja Apache2
- Za pomocą Puppet upewnij się by był użytkownik `www-data` i miał `uid=33`
- Za pomocą Puppet upewnij się by była grupa `www-data` i miała `gid=33`
- Upewnij się że katalog `/var/www` istnieje i właścicielem jego są user `www-data` i grupa `www-data` i że ma uprawnienia `rwxr-xr-x`
- Zainstaluj i skonfiguruj Apache2 wykorzystując moduł Puppet
- Z terminala wygeneruj certyfikaty self signed OpenSSL (`.cert` i `.key`) (za pomocą i umieść je w `/etc/ssl/`)
- Za pomocą Puppet Stwórz dwa vhosty
    - `insecure.example.com` na porcie 80 i z katalogiem domowym `/var/www/insecure.example.com`
    - `ssl.example.com` na porcie 443 i z katalogiem domowym `/var/www/ssl.example.com` + używanie certyfikatów SSL wcześniej wygenerowanych

## Instalacja i konfiguracja MySQL
- zainstaluj moduł bazy MySQL wykorzystując Puppeta
- ustaw hasło roota na mypassword
- ustaw nasłuchiwanie serwera `mysqld` na `0.0.0.0`
- stwórz bazę danych `mydb` z `utf-8`
- stwórz usera `myusername` z hasłem `mypassword`
- nadaj wszystkie uprawnienia dla usera `myusername` dla bazy `mydb`
- ustaw backupowanie bazy danych do `/tmp/mysql-backup`

## Instalacja Java i Tomcat
- zainstaluj Javę za pomocą Puppeta
- zainstaluj Tomcat8 za pomocą Puppeta do `/opt/tomcat8`
- Skonfiguruj dwie instancje Tomcata działające jednocześnie
    - Jedna uruchamiana na domyślnych portach
    - Druga uruchamiana na 8006 a connector z portu 8081 przekierowywał na 8443
    - Na pierwszej uruchom WAR z lokacji `/opt/tomcat8/webapps/docs/appdev/sample/sample.war`


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
