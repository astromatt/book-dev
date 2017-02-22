# Puppet MySQL installation and configuration

## English

- Create manifest in `/etc/puppet/manifests/mysql.pp`
- Install `MySQL` database using `Puppet` module
- Set `root` password to `mypassword`
- Set `mysqld` to listen on all interfaces (`0.0.0.0`)
- Create database `mydb` with `utf-8`
- Create user `myusername` with password `mypassword`
- Grant all privileges to `myusername` for `mydb`
- Setup database backup to `/tmp/mysql-backup`

## Polish

- Manifest do tego zadania zapisz w pliku `/etc/puppet/manifests/mysql.pp`
- Zainstaluj bazę danych `MySQL` wykorzystując moduł `Puppet`
- Ustaw hasło dla użytkownika `root` na `mypassword`
- Ustaw nasłuchiwanie serwera `mysqld` na wszystkich interfejsach (`0.0.0.0`)
- Stwórz bazę danych `mydb` z `utf-8`
- Stwórz usera `myusername` z hasłem `mypassword`
- Nadaj wszystkie uprawnienia dla usera `myusername` dla bazy `mydb`
- Ustaw backupowanie bazy danych do `/tmp/mysql-backup`
