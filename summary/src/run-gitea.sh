sudo mkdir -p /home/gitea
sudo chown ubuntu:ubuntu /home/gitea

docker run \
    --name gitea \
    --detach \
    --rm \
    --env USER_UID=1000 \
    --env USER_GID=1000 \
    --network ecosystem \
    --publish 3000:3000 \
    --publish 2222:22 \
    --volume /home/gitea:/data \
    --volume /etc/timezone:/etc/timezone:ro \
    --volume /etc/localtime:/etc/localtime:ro \
    gitea/gitea
