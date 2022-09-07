docker network create ecosystem

docker run \
    --detach \
    --rm \
    --name registry \
    --network ecosystem \
    --publish 5000:5000 \
    --volume registry:/var/lib/registry \
    registry:2
