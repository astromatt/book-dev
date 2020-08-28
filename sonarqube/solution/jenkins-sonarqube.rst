Uruchomić Git Bash
chmod 400 ~/Desktop/2020-08-gazsystem.pem
ssh ubuntu@<TWOJE_IP> -i ~/Desktop/2020-08-gazsystem.pem
curl https://get.docker.com |sudo sh
docker --version
sudo usermod -aG docker ubuntu
exit
zalogować się ponownie (użyć kawisz strzałka do góry)
docker network create ecosystem
docker volume create --name sonarqube_data
docker volume create --name sonarqube_extensions
docker volume create --name sonarqube_logs
"docker run \
    --name sonarqube \
    --detach \
    --rm \
    --network ecosystem \
    --publish 9000:9000 \
    --volume sonarqube_data:/opt/sonarqube/data \
    --volume sonarqube_logs:/opt/sonarqube/logs \
    --volume sonarqube_extensions:/opt/sonarqube/extensions \
    sonarqube"
GitLab import projektu https://github.com/AstroTech/ecosystem-example-java.git
git clone http://52.208.211.196:8000/root/ImieN.git /home/ubuntu/src-java/
cd /home/ubuntu/src-java/
sudo apt update
sudo apt install -y openjdk-8-jdk maven
sudo update-alternatives --config java  # wybieramy opcję 2
mvn compile
mvn test
mvn verify
vim /home/ubuntu/src-java/sonar-project.properties
"sonar.projectKey=myjavaproject

## Language
sonar.language=java
sonar.java.source=8

## Paths
sonar.projectBaseDir=/usr/src/
sonar.sources=src/main/java
sonar.exclusions=**/migrations/**
sonar.java.binaries=target/classes"
export IP='<TWOJE_IP>'
echo $IP
docker run --rm -e SONAR_HOST_URL="http://${IP}:9000/" -v /home/ubuntu/src-java:/usr/src sonarsource/sonar-scanner-cli
otwórz przeglądarkę na http://<TWOJE_IP>:9000/
ssh ubuntu@<TWOJE_IP> -i ~/Desktop/2020-08-gazsystem.pem
export IP='<TWOJE_IP>'
echo $IP
sudo mkdir -p /home/jenkins
sudo chmod 777 /home/jenkins
sudo chmod 777 /var/run/docker.sock
"docker run \
    --name jenkins \
    --detach \
    --rm \
    --network ecosystem \
    --publish 8080:8080 \
    --volume /home/jenkins:/var/jenkins_home \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    jenkins/jenkins:alpine"
docker ps
cat /home/jenkins/secrets/initialAdminPassword
otwórz przeglądarkę na http://<TWOJE_IP>:8080/
install suggested plugins
user "admin", haslo "abcdefghi", email "admin@example.com"
"[lewe menu]
-> Konfiguracja [Manage Jenkins]
-> Zarządzaj Wtyczkami [Manage Plugins]
-> Dosępne [Available]

(albo przejdź na stronę http://<TWOJE_IP>:8080/pluginManager/available)"
na zakładce dostępne szukamy "Blue Ocean", na końcu listy wyników wyszukiwania
zaznaczamy "Blue Ocean" i klikamy przycisk "Download now and install after restart"
zaznaczamy opcję "Restart Jenkins when installation is complete and no jobs are running"
po dwóch minutach odświeżamy stronę (jeżeli sama się nie przeładowała) i logujemy się do Jenkinsa
[lewe menu] -> Blue Ocean (lub wchodzimy na stronę http://<TWOJE_IP>:8080/blue/)
Create a new Pipeline -> GIT
"http://52.208.211.196:8000/root/<TWOJE IMIE i pierwsza litera nazwiska>.git
(ważne jest dodanie .git na końcu!!!)"
Create credential: login "root", haslo "abcdefghi" i kliknąć Create Credential, później Create Pipeline
You don't have any branches that contain a Jenkinsfile -> Create Pipeline
"klikamy na plus (na środku ekranu jako ""dodaj stage""),
[po prawej] nazywamy krok ""Build""
Add Step -> ""shell script"" -> wpisujemy ""echo 'building...'""
[na górze] klikamy ""Save""
[na środku]  ""Save & run"""
Build powinien się udać
Wchodzimy na ekran z podsumowaniem wyniku budowania -> [prawy górny róg] kliknąć Ołówek [edit]
W kroku build zmienić treść "shell script" na -> "mvn compile"
Dodajemy stage sekwencyjnie [plusik] o nazwie "Test" z krokiem "shell script" -> mvn test
Dodajemy stage równolegle [plusik] o nazwie "Test integration" z krokiem "shell script" -> mvn verify
"[na górze] klikamy ""Save""
[na środku]  ""Save & run""
Automatycznie się zbuduje i będzie na czerwono (błąd budowania - ""mvn not found"")"
docker exec -u root jenkins apk add --no-cache openjdk8 maven docker git
Restart build i powinno być zielone (build zakończył się powodzeniem)
"Dodajemy stage sekwencyjnie [plusik] o nazwie ""Static Code Analysis""
Dodaj krok ""shell script"" -> o zawartości:

docker run --rm -e SONAR_HOST_URL=""http://<TWOJE_IP>:9000/"" -v $(pwd):/usr/src sonarsource/sonar-scanner-cli
"
Otworzyć swoje repozytorium na http://52.208.211.196:8000/dashboard/projects
Kliknąć plus [lekko w lewo i do góry od środka ekranu] obok wyboru branch -> New file
"Plik nazwij: ""sonar-project.properties"" i w zawartości wpisz:

sonar.projectKey=myproject
sonar.sources=src/main/java
sonar.language=java
sonar.java.source=8
sonar.java.binaries=target/classes
sonar.working.directory=/tmp/"
Następnie "commit changes"
sudo mkdir -p /home/registry
sudo chmod 777 /home/registry
"docker run \
    --detach \
    --name registry \
    --restart always \
    --net ecosystem \
    --publish 5000:5000 \
    --volume /home/registry:/var/lib/registry \
    registry:2"
Edytuj pipeline w Jenkinsie
"Dodajemy stage równolegle [plusik] o nazwie ""Publish"" z krokiem ""shell script"" o treści:

echo 'pushing to docker registry...'

Następnie Save -> ""Save & Run"""
"Poprawić w stage ""Static Code Analysis""
zmienić parametr ""-v"" przy uruchamianiu docker
podmienic $(pwd) na ""/home/jenkins/workspace/XXX_master""
gdzie XXX to Twoje imie i pierwsza litera nazwiska

czyli pełne polecenie wygląda tak:

docker run --rm -e SONAR_HOST_URL=""http://<TWOJE_IP>:9000/"" -v /home/jenkins/workspace/XXX_master:/usr/src sonarsource/sonar-scanner-cli"
Otworzyć swojego SonarQube na http://<TWOJE_IP>:9000/
Projekt o nazwie "myproject" został dodany przez budowanie w Jenkins
Wejdź do swojego projektu na http://52.208.211.196:8000/dashboard/projects
"Zmodyfikuj zawartość pliku ""Dockerfile"" i wpisz:

FROM alpine
COPY . /usr/src/"
"Edytuj pipeline w Jenkinsie i w stage ""Publish"" usuń obecny krok, i dodaj trzy nowe (""shell script)"":

docker build . -t localhost:5000/myapp:$(git log -1 --format=""%h"")
docker push localhost:5000/myapp:$(git log -1 --format=""%h"")
docker rmi localhost:5000/myapp:$(git log -1 --format=""%h"")"
Następnie Save -> "Save & Run" i build powinien się zbudować na zielono (tzn. wszysko ok)
cd /home/jenkins/workspace/*_master/ && sudo git clean -fdx
Wejdź do swojego projektu na http://52.208.211.196:8000/dashboard/projects
W GitLab na końcu pliku "sonar-project.properties" dodać linię "sonar.working.directory=/tmp/"
Nasz build powinien być zielony (tzn. Wszystko działa)
Aby zobaczyć czy image został umieszczony w registry
curl -s http://localhost:5000/v2/myapp/tags/list |python3 -m json.tool
Zobacz zawartość pliku "Jenkinsfile"
