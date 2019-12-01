***************************
Lint (Static Code Analysis)
***************************


About SonarScanner
==================
* SonnarScanner requires Java 8
* https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner
* https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.0.3.778-linux.zip
* https://docs.sonarqube.org/display/PLUG/Java+Plugin+and+Bytecode
* https://docs.sonarqube.org/display/SONAR/Analysis+Parameters


sonar.properties
================
* ``sonar.properties`` in your repository main folder

.. code-block:: properties
    :caption: Minimal Sonar Project Properties

    sonar.projectKey=MyProject
    sonar.projectName=MyProject
    sonar.projectVersion=1.0

    sonar.sources=src/main/java
    sonar.java.binaries=target/classes
    sonar.java.source=9


Run SonarQube server
====================
.. code-block:: yaml

    version: '3'

    networks:
        ecosystem:
            driver: bridge

    services:
        sonar:
            image: sonarqube
            restart: always
            ports:
               - "8300:9000"
            networks:
                - ecosystem


Assignments
===========

Statyczna analiza kodu za pomocą SonarScanner i SonarQube
---------------------------------------------------------
#. Dla repozytorium https://github.com/AstroTech/ecosystem-example-java.git
#. Zacznij budować za pomocą ``mvn clean install``
#. Wyniki upublicznij w *SonarQube*
#. Build uzależnij od wyniku Quality Gates (plugin ``Sonar Quality Gates``)
#. Uruchom SonarQube za pomocą ``docker run -d --name sonarqube -p 9000:9000 sonarqube``
