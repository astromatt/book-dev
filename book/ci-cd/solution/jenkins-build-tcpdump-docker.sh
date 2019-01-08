## Connect to AWS
ssh ubuntu@<IP_ADDRESS> -i private-key.pem


## Run Gerrit
docker run --rm --name gerrit -d -p 8001:8080 gerritcodereview/gerrit


## Clone repository from github
git clone https://github.com/AstroTech/tcpdump /tmp/tcpdump


## Build Docker Image
cd /tmp/tcpdump
echo 'FROM ubuntu' > Dockerfile
echo 'RUN apt update && apt install -y gcc libpcap-dev make' >> Dockerfile
git commit -am "Dockerfile"
docker build . -t tcpdump:latest


## Replace repository remote URL for uploading to Gerrit
git remote set-url origin http://localhost:8001/tcpdump
git push --set-upstream origin master


## Run artifactory
docker run --rm --name artifactory -d -p 8002:8081 docker.bintray.io/jfrog/artifactory-oss:latest


## Run Jenkins
mkdir /home/jenkins
chown ubuntu:ubuntu /home/jenkins
docker run --rm --name jenkins -d -p 8000:8080 -v /home/jenkins:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins
chmod 666 /var/run/docker.sock


## Connect to Jenkins container
docker exec -u0 -it jenkins bash

    ## Execute following lines inside the container to install docker for Jenkins
    apt update
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
    echo "deb https://download.docker.com/linux/debian stretch stable" > /etc/apt/sources.list.d/docker.list
    apt install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
    apt update
    apt install -y docker-ce


## Add Gerrit repository to Jenkins and configure builds to run on containers
./configure
make
make check
# create artefact

## Publish artefact to Artifactory
USERNAME='admin'
PASSWORD='admin'
FILE='/var/jenkins_home/jobs/tcpdump/branches/master/builds/$BUILD_NUMBER/archive/*'
URL='http://artifactory:8081/artifactory/generic-local/'

curl -u $USERNAME:$PASSWORD -T $FILE $URL
