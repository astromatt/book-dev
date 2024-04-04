docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube

# By default, the image will use an embedded H2 database that is not suited for production.
docker run -d --name sonarqube \
    -p 9000:9000 -p 9092:9092 \
    -e SONARQUBE_JDBC_USERNAME=sonar \
    -e SONARQUBE_JDBC_PASSWORD=sonar \
    -e SONARQUBE_JDBC_URL=jdbc:postgresql://localhost/sonar \
    sonarqube
