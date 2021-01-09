FROM alpine

RUN apk add git maven openjdk8
RUN git clone https://github.com/AstroTech/ecosystem-example-java /tmp

WORKDIR /tmp

# To run the unit tests, call mvn test
# To run the integration tests as well, call mvn verify
CMD mvn test && mvn verify
