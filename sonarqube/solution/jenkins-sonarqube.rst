Jaki jest główny język programowania z którym pracujesz?
Ile masz lat doświadczenia w programowaniu?
Ile masz lat doświadczenia w administracji systemami?
Z jakiego systemu operacyjnego korzystasz (nazwa + wersja)
Pobrać klucz .pem z Google Drive (link podany na chat)
Zainstalować klient SSH (np. w instalatorze GIT, lub apt-get albo brew)
Uruchomić Terminal (np. Git Bash)
ssh -V

# tylko dla Linux albo macOS, dla Windows nie trzeba
chmod 400 ~/Desktop/2020-09-gazsystem.pem
ssh -i ~/Desktop/2020-09-gazsystem.pem -l ubuntu <TWOJE_IP>
whoami   # sprawdzić czy wyskakuje ubuntu
curl https://get.docker.com |sudo sh
docker --version
sudo usermod -aG docker ubuntu
exit
zalogować się ponownie (użyć kawisz strzałka do góry)
docker network create ecosystem
docker volume create --name sonarqube_data
docker volume create --name sonarqube_extensions
docker volume create --name sonarqube_logs
docker run \
    --name sonarqube \
    --detach \
    --rm \
    --network ecosystem \
    --publish 9000:9000 \
    --volume sonarqube_data:/opt/sonarqube/data \
    --volume sonarqube_logs:/opt/sonarqube/logs \
    --volume sonarqube_extensions:/opt/sonarqube/extensions \
    sonarqube
docker ps
docker exec sonarqube cat /etc/os-release
docker images
"Otwórz zakładkę w przeglądarce:
- Strona: http://<TWOJE_IP>:9000/

Logowanie:
- username: admin
- hasło: admin"
"Otwórz zakładkę w przeglądarce:
- Strona: http://<GITLAB_IP>:8000/

Logowanie:
- username: root
- hasło: abcdefghi"
"GitLab:
- New Project (zielony przycisk u góry po prawej)
- Import project (trzecia zakładka od lewej)
- Repo by URL (drugi w dolnym rzędzie)
- Git repository URL: https://github.com/AstroTech/ecosystem-example-java.git
- Username i password zostawić puste
- Project name: JanT-java (tak jak Twoje imię i pierwsza litera nazwiska - jak w Twojej kolumnie; np. JanT)
- Project slug: jant-java (tak jak Twoje imię i pierwsza litera nazwiska - jak w Twojej kolumnie; np. JanT)
- Visibility Level: Public"
"# gdzie JanT to Twoje imię i pierwsza litera nazwiska
git clone http://<GITLAB_IP>:8000/root/JanT.git /home/ubuntu/src-java/"
cd /home/ubuntu/src-java/
sudo apt update
sudo apt install -y openjdk-8-jdk maven
"sudo update-alternatives --config java
# wybieramy numer 2
# czyli opcję z /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java"
mvn compile
mvn test
mvn verify
nano /home/ubuntu/src-java/sonar-project.properties
"sonar.projectKey=myjavaproject

## Language
sonar.language=java
sonar.java.source=8

## Paths
sonar.projectBaseDir=/usr/src/
sonar.sources=src/main/java
sonar.exclusions=**/migrations/**
sonar.java.binaries=target/classes"
cat /home/ubuntu/src-java/sonar-project.properties
docker run --rm -e SONAR_HOST_URL="http://<TWOJE_IP>:9000/" -v /home/ubuntu/src-java:/usr/src sonarsource/sonar-scanner-cli
otwórz przeglądarkę na http://<TWOJE_IP>:9000/ i odśwież stronę
Mam "myjavaproject" w SonarQube
cd /home/ubuntu/src-java/
git config --global user.name "Jan Twardowski"
git config --global user.email "jan.twardowski@polsa.gov.pl"
git add sonar-project.properties
git commit -m "Sonar Properties"
"git push
# username: root
# hasło: abcdefghi"
"Otwórz w przeglądarce
- Gitlab: http://18.184.103.67:8000/dashboard/projects
- wybierz swój projekt"
Powinien być plik "sonar-project.properties" z odpowiednią zawartością
ssh -i ~/Desktop/2020-09-gazsystem.pem -l ubuntu <TWOJE_IP>
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
-> Dostępne [Available]

(albo przejdź na stronę http://<TWOJE_IP>:8080/pluginManager/available)"
na zakładce dostępne szukamy "Blue Ocean", na końcu listy wyników wyszukiwania (drugi od końca)
zaznaczamy "Blue Ocean" i klikamy przycisk "Download now and install after restart"
zaznaczamy opcję "Restart Jenkins when installation is complete and no jobs are running"
po dwóch minutach odświeżamy stronę (jeżeli sama się nie przeładowała) i logujemy się do Jenkinsa
[lewe menu] -> Open Blue Ocean (lub wchodzimy na stronę http://<TWOJE_IP>:8080/blue/)
Na popupie "Welcome to Jenkins" -> klikamy "Create a new Pipeline" -> i wybieramy GIT
"# gdzie JanT to Twoje imię i pierwsza litera nazwiska
# ważne jest dodanie .git na końcu!!
http://<GITLAB_IP>:8000/root/JanT.git"
Create credential: login "root", haslo "abcdefghi" i kliknąć Create Credential, później Create Pipeline
Na popupie "You don't have any branches that contain a Jenkinsfile" -> klikamy "Create Pipeline"
"klikamy na plus (na środku ekranu jako ""dodaj stage""),
[po prawej] nazywamy krok ""Build""
Add Step -> ""shell script"" -> wpisujemy: echo ""building...""
[na górze] klikamy ""Save""
[na środku]  ""Save & run"""
Build powinien się udać
Wchodzimy na ekran z podsumowaniem wyniku budowania -> [prawy górny róg] kliknąć Ołówek [edit]
"Klikamy na plus (na środku ekranu jako ""dodaj stage"")
Nazywamy Stage: ""Test"""
"W ramach stage ""Test""
Dodajemy krok i nazywamy go ""Unit Test""

Add Step -> ""shell script"" -> wpisujemy: echo ""unit testing..."""
"W ramach stage ""Test""
Dodajemy krok drugi (równoległy do ""Unit Test"") i nazywamy go ""Integration Test""

Add Step -> ""shell script"" -> wpisujemy: echo ""integration testing..."""
"Dodaj nowy stage i nazwij go ""Static Code Analysis""
Add Step -> ""shell script"" -> wpisujemy: echo ""static code analysis..."""
"Dodaj nowy stage i nazwij go ""Publish Artifact""
Add Step -> ""shell script"" -> wpisujemy: echo ""publishing artifact..."""
"[na górze] klikamy ""Save""
[na środku]  ""Save & run"""
Build powinien się udać
"Wchodzimy na ekran z podsumowaniem wyniku budowania -> [prawy górny róg] kliknąć Ołówek [edit]
W kroku ""Build"" zmienić treść kroku ""shell script"" na -> mvn compile
[na górze] klikamy ""Save""
[na środku]  ""Save & run"""
Build powinien się nieudać (będzie na czerwono - błąd budowania - "mvn not found")
docker exec -u root jenkins apk add --no-cache openjdk8 maven docker git
Uruchom nieudany build jeszcze raz
Build powinien się udać
"Wchodzimy na ekran z podsumowaniem wyniku budowania -> [prawy górny róg] kliknąć Ołówek [edit]
W kroku ""Test"" -> ""Unit Test"" zmienić treść kroku ""shell script"" na -> mvn test
[na górze] klikamy ""Save""
[na środku]  ""Save & run"""
"Wchodzimy na ekran z podsumowaniem wyniku budowania -> [prawy górny róg] kliknąć Ołówek [edit]
W kroku ""Test"" -> ""Integration Test"" zmienić treść kroku ""shell script"" na -> mvn verify
[na górze] klikamy ""Save""
[na środku]  ""Save & run"""
Restart build i powinno być zielone (build zakończył się powodzeniem)
"Dodajemy stage sekwencyjnie [plusik] o nazwie ""Static Code Analysis""
Dodaj krok ""shell script"" -> o zawartości:

docker run --rm -e SONAR_HOST_URL=""http://<TWOJE_IP>:9000/"" -v $(pwd):/usr/src sonarsource/sonar-scanner-cli
"
Build powinien się nieudać ('Unknown': sonar.projectKey)
"docker exec -it -u root jenkins sh

# na dokerowym kontenerze uruchomić
docker run --rm -e SONAR_HOST_URL=""http://<TWOJE_IP>:9000/"" -v $(pwd):/usr/src sonarsource/sonar-scanner-cli

# zobacz przyczynę niepowodzenia
# wylistuj katalogi w /var/jenkins_home/workspace/"
"Edytujemy stage o nazwie ""Static Code Analysis""
Edytuj krok ""shell script"" -> zmień zawartość

docker run --rm -e SONAR_HOST_URL=""http://<TWOJE_IP>:9000/"" -v /home/jenkins/workspace/XXX:/usr/src sonarsource/sonar-scanner-cli"
"Poprawić w stage ""Static Code Analysis""
zmienić parametr ""-v"" przy uruchamianiu docker
podmienic $(pwd) na ""/home/jenkins/workspace/XXX_master""
gdzie XXX to Twoje imie i pierwsza litera nazwiska

czyli pełne polecenie wygląda tak:

docker run --rm -e SONAR_HOST_URL=""http://<TWOJE_IP>:9000/"" -v /home/jenkins/workspace/XXX_master:/usr/src sonarsource/sonar-scanner-cli"
Build powinien się udać
"Otwórz swojego sonara i zobacz datę ostatniej analizy w projekcie ""myjavaproject""
data powinna być z przed chwili"
Uruchom ponownie build
Tym razem powinien się nie udać (powód błąd wykonania: git clean -fdx)
cd /home/jenkins/workspace/XXX-java_master && sudo git clean -fdx
Otworzyć swoje repozytorium na http://<GITLAB_IP>:8000/dashboard/projects
"W pliku ""sonar-project.properties"" dodaj linię na końcu:

sonar.working.directory=/tmp/"
Następnie "commit changes"
Wejdź na sonarqube http://<TWOJE_IP>:9000/
W Administration -> Marketplace -> Wyszukaj pluginu "Build Breaker" -> Install
"Na górze w pasku ""SonarQube needs to be restarted in order to
install 1 plugins"" -> kliknij restart server -> następnie zaczekaj około minuty i odśwież stronę"
"W Administration -> Configuration -> General Settings -> z menu po lewej wybierz Build Breaker
Upewnij się, że wszystko jest ok"
Quality Gates -> Stwórz nowy Quality Gate o nazwie "My way"
"Usuń wszystkie reguły ""My Way"" (jeżeli jakieś są)
Add Condition -> On Overall Code -> Technical Debt -> is greater than -> wpisz cyfrę: 1
W ""My Way"" ma być tylko jedna reguła: Technical Debt is greater than 1 min"
"W sekcji ""Projects"" (poniżej sekcji Conditions, którą właśnie edytowałeś/aś)
na zakładce ""All"" zaznacz ""myjavaproject"" aby aktywować Quality Gate w projekcie
Upewnij się, że ""myjavaproject"" ma zaznaczony checkbox"
"Uruchom Build ponownie, który powinien sfailować
(powód: niespełnienie Quality Gate - Project does not pass the quality gate.)"
Zmień w Quality Gate "Technical Debt" na 50
Uruchom Build ponownie, tym razem powinen przejść
sudo mkdir -p /home/registry
sudo chmod 777 /home/registry
"docker run \
    --detach \
    --rm \
    --name registry \
    --net ecosystem \
    --publish 5000:5000 \
    --volume /home/registry:/var/lib/registry \
    registry:2"
Edytuj pipeline w Jenkinsie
"Edytuj stage o nazwie ""Publish Artifact"" z krokiem ""shell script"" o treści:

echo 'publishing artifact'

Następnie Save -> ""Save & Run"""
cd /home/ubuntu/src-java/
git pull
docker ps -a
docker images
"nano Dockerfile
# Wpisz w pliku:

FROM alpine
COPY . /usr/src/

# wychodzimy przez ctrl-x -> y -> enter"
docker build . -t myimg
"docker images
# upewnij się, że jest myimg"
docker build . -t myimg:1.0
docker images
git log -1 --format='%h'
docker build . -t myimg:$(git log -1 --format='%h')
docker images
docker build . -t localhost:5000/myimg
docker build . -t localhost:5000/myimg:$(git log -1 --format='%h')
docker push localhost:5000/myimg
docker push localhost:5000/myimg:$(git log -1 --format='%h')
docker images
docker rmi localhost:5000/myimg
docker rmi localhost:5000/myimg:$(git log -1 --format='%h')
docker images
curl -s http://localhost:5000/v2/myimg/tags/list |python3 -m json.tool
Otworzyć swoje repozytorium na http://<GITLAB_IP>:8000/dashboard/projects
"Zmodyfikuj zawartość pliku ""Dockerfile"" i wpisz:

FROM alpine
COPY . /usr/src/"
"Edytuj pipeline w Jenkinsie i w stage ""Publish Artifact"" usuń obecny krok, i dodaj trzy nowe kroki (""shell script)"":

docker build . -t localhost:5000/myapp:$(git log -1 --format=""%h"")
docker push localhost:5000/myapp:$(git log -1 --format=""%h"")
docker rmi localhost:5000/myapp:$(git log -1 --format=""%h"")"
Następnie Save -> "Save & Run" i build powinien się zbudować na zielono (tzn. wszysko ok)
Otworzyć swoje repozytorium na http://<GITLAB_IP>:8000/dashboard/projects
Nasz build powinien być zielony (tzn. Wszystko działa)
Aby zobaczyć czy image został umieszczony w registry
curl -s http://localhost:5000/v2/myimg/tags/list |python3 -m json.tool
Zobacz zawartość pliku "Jenkinsfile"
Do pliku sonar-project.properties dodajemy sonar.host.url z URL ze zmiennej środowiskowej
"Edytuj pipeline i usuń z kroku ""Static code analysis"" fragment:
 -e SONAR_HOST_URL=""http://<TWOJE_IP>:9000/""

Tak, aby zostawić:
docker run --rm -v /home/jenkins/workspace/matth-java_master:/usr/src sonarsource/sonar-scanner-cli"
sudo ln -s /home/jenkins /var/jenkins_home
"Edytuj pipeline i krok ""Static code analysis"":
Zmodyfikuj parametr -v

Tak, aby zostawić:
docker run --rm -v $(pwd):/usr/src sonarsource/sonar-scanner-cli"
ANKIETA
