docker run --rm --name jenkins -d -p 8000:8080 -v /tmp/jenkins:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins
docker exec -u0 -it jenkins bash
    chmod 666 /var/run/docker.sock
    apt update
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
    echo "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" > /etc/apt/sources.list.d/docker.list
    apt install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
    apt update
    apt install -y docker-ce

cd /tmp/tcpdump/
echo 'FROM ubuntu' > Dockerfile
echo 'RUN apt update && apt install -y gcc libpcap-dev make' >> Dockerfile
git commit -am "Dockerfile"
git push
docker build . -t tcpdump:latest

