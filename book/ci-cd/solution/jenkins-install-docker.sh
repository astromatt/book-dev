apt-get install docker.io
docker run --name jenkins -d -p 8080:8080 -v /tmp/jenkins:/var/jenkins_home jenkins/jenkins
docker container exec -u 0 -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
