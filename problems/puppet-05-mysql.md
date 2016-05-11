# Instalacja i konfiguracja MySQL
- manifest do tego zadania zapisz w katalogu `/etc/puppet/manifests/mysql.pp`
- zainstaluj moduł bazy MySQL wykorzystując Puppeta
- ustaw hasło roota na mypassword
- ustaw nasłuchiwanie serwera `mysqld` na `0.0.0.0`
- stwórz bazę danych `mydb` z `utf-8`
- stwórz usera `myusername` z hasłem `mypassword`
- nadaj wszystkie uprawnienia dla usera `myusername` dla bazy `mydb`
- ustaw backupowanie bazy danych do `/tmp/mysql-backup`
