docker run \
    --name sonarqube \
    --detach \
    --rm \
    --network ecosystem \
    --publish 9000:9000 \
    --volume sonarqube_data:/opt/sonarqube/data \
    --volume sonarqube_logs:/opt/sonarqube/logs \
    --volume sonarqube_extensions:/opt/sonarqube/extensions \
    sonarqube
