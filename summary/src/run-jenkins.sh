docker network create ecosystem
sudo chmod 666 /var/run/docker.sock
sudo ln -s /var/lib/docker/volumes/jenkins/_data/ /var/jenkins_home

docker run \
    --name jenkins \
    --detach \
    --rm \
    --network ecosystem \
    --publish 8080:8080 \
    --volume jenkins:/var/jenkins_home \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    jenkinsci/blueocean
