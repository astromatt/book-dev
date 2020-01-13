FROM alpine

RUN apk add git maven openjdk8
RUN git clone https://github.com/AstroTech/ecosystem-example-java /tmp

WORKDIR /tmp
CMD mvn test
