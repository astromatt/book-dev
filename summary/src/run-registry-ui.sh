docker network create ecosystem

docker run \
    --name=registry-ui \
    --detach \
    --rm \
    --network ecosystem \
    --publish 8888:8888 \
    --volume registry_ui:/opt:ro \
    quiq/docker-registry-ui
