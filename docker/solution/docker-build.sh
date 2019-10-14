apk add git
apk add openjdk8-jdk
apk add maven

cd /tmp
git clone https://github.com/AstroTech/ecosystem-example-java
cd ecosystem-example-java

mvn test
