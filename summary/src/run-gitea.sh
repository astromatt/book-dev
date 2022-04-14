docker network create ecosystem

docker run \
    --name gitea \
    --detach \
    --rm \
    --env USER_UID=1000 \
    --env USER_GID=1000 \
    --network ecosystem \
    --publish 3000:3000 \
    --publish 2222:2222 \
    --volume gitea_data:/var/lib/gitea \
    --volume gitea_config:/etc/gitea \
    --volume /etc/timezone:/etc/timezone:ro \
    --volume /etc/localtime:/etc/localtime:ro \
    gitea/gitea:latest-rootless
