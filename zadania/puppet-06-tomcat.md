# Instalacja Java i Tomcat
- manifest do tego zadania zapisz w katalogu `/etc/puppet/manifests/tomcat.pp`
- zainstaluj Javę za pomocą Puppeta
- zainstaluj Tomcat8 za pomocą Puppeta do `/opt/tomcat8`
- Skonfiguruj dwie instancje Tomcata działające jednocześnie
    - Jedna uruchamiana na domyślnych portach
    - Druga uruchamiana na 8006 a connector z portu 8081 przekierowywał na 8443
    - Na pierwszej uruchom WAR z lokacji `/opt/tomcat8/webapps/docs/appdev/sample/sample.war`
