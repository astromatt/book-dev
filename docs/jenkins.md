# Jenkins

## Install using DEB on Ubuntu

```sh
wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
echo "deb http://pkg.jenkins-ci.org/debian binary/" >> /etc/apt/sources.list
apt-get update
apt-get install --yes jenkins
sudo su - jenkins
ssh-keygen
cat ~/.ssh/id_rsa.pub
exit
service jenkins stop
sed -i 's/HTTP_PORT=8080/HTTP_PORT=8081/g' /etc/default/jenkins
service jenkins start
```

## Install using Docker

    $ docker pull jenkins
	$ docker run -p 8080:8080 -p 50000:50000 -v /tmp/jenkins_home_on_host:/var/jenkins_home jenkins

## Instalacja i konfiguracja Jenkinsa

### Zadanie

- Postaw Jenkins za pomocą paczek DEB
- Zaciągnij repo git https://github.com/SonarSource/sonar-examples.git
- Zacznij budować różne projekty sonar-examples/projects/languages/java
- Wyniki upublicznij w SonarQube