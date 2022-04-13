docker network create ecosystem
sudo mkdir /home/jenkins
sudo chown ubuntu:ubuntu /home/jenkins
sudo chmod o+rw /var/run/docker.sock
sudo ln -s /home/jenkins /var/jenkins_home

docker run \
    --name jenkins \
    --detach \
    --rm \
    --network ecosystem \
    --publish 8080:8080 \
    --volume /home/jenkins:/var/jenkins_home \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    jenkinsci/blueocean
