docker network create ecosystem
sudo mkdir -p /home/registry-ui
sudo chown ubuntu:ubuntu /home/registry-ui

docker run \
    --name=registry-ui \
    --detach \
    --rm \
    --network ecosystem \
    --publish 8888:8888 \
    --volume /home/registry-ui/config.yml:/opt/config.yml:ro \
    quiq/docker-registry-ui
