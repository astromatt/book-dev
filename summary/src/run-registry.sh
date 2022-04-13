docker network create ecosystem
sudo mkdir /home/registry
sudo chown ubuntu:ubuntu /home/registry

docker run \
    --detach \
    --rm \
    --name registry \
    --net ecosystem \
    --publish 5000:5000 \
    --volume /home/registry:/var/lib/registry \
    registry:2
