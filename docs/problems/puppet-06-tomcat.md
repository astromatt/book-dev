# Puppet Tomcat installation and configuration

## English

- Create manifest in `/etc/puppet/manifests/mysql.pp`
- Install `Java` using `Puppet` module
- Install `Tomcat 8` using `Puppet` module in `/opt/tomcat8`
- Configure to `Tomcat` instances running simultanously on your hostname
    - One instance is running on default ports
    - Another instance is using `8006` port for connector and `8081` to redirect to `8443`
    - On the first instance deploy `WAR` from `/opt/tomcat8/webapps/docs/appdev/sample/sample.war`

## Polish

- Manifest do tego zadania zapisz w pliku `/etc/puppet/manifests/tomcat.pp`
- Zainstaluj język `Java` za pomocą modułu `Puppet`
- Zainstaluj `Tomcat 8` za pomocą `Puppet` w katalogu `/opt/tomcat8`
- Skonfiguruj dwie instancje `Tomcat` działające jednocześnie
    - Jedna uruchamiana na domyślnych portach
    - Druga uruchamiana na `8006` a connector z portu `8081` przekierowywał na `8443`
    - Na pierwszej uruchom `WAR` z lokacji `/opt/tomcat8/webapps/docs/appdev/sample/sample.war`
