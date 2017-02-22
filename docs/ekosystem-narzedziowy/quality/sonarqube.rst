*********
SonarQube
*********

Installation
============

Install using DEB on Ubuntu
---------------------------

.. code-block:: sh

    echo "deb http://downloads.sourceforge.net/project/sonar-pkg/deb binary/" >> /etc/apt/sources.list
    apt-get update
    apt-get install --yes sonar
    service sonar stop
    sed -i 's(#sonar.jdbc.url=jdbc:postgresql(sonar.jdbc.url=jdbc:postgresql(g' /opt/sonar/conf/sonar.properties
    sed -i 's(sonar.jdbc.url=jdbc:h2(#sonar.jdbc.url=jdbc:h2(g' /opt/sonar/conf/sonar.properties
    sed -i 's(#sonar.jdbc.username=sonar(sonar.jdbc.username=sonar(g' /opt/sonar/conf/sonar.properties
    sed -i 's(#sonar.jdbc.password=sonar(sonar.jdbc.password=sonar(g' /opt/sonar/conf/sonar.properties
    service sonar start

Install using Docker
--------------------

    $ docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube
