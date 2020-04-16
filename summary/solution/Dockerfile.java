FROM alpine
RUN apk add --no-cache openjdk8 maven
WORKDIR /data

# docker build . -f Dockerfile.java -t testenv:java
# cd /home/src-java

## Run Unit tests:
# docker run --tty -v $(pwd):/data -v /home/maven:/root/.m2 testenv:java mvn test

## Run Integration tests:
# docker run --tty -v $(pwd):/data -v /home/maven:/root/.m2 testenv:java mvn verify


## Aliases:
# alias java-unittest='docker run --tty -v $(pwd):/data -v /home/maven:/root/.m2 testenv:java mvn test'
# alias java-integrationtest='docker run --tty -v $(pwd):/data -v /home/maven:/root/.m2 testenv:java mvn verify'
# java-unittest
# java-integrationtest
