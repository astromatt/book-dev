docker network create ecosystem
# sudo chmod o+rw /run/user/1000/docker.sock
sudo ln -s /home/ubuntu/.local/share/docker/volumes/jenkins/_data /var/jenkins_home

docker run \
    --name jenkins \
    --detach \
    --rm \
    --network ecosystem \
    --publish 8080:8080 \
    --volume jenkins:/var/jenkins_home \
    --volume /run/user/1000/docker.sock:/var/run/docker.sock \
    jenkinsci/blueocean
