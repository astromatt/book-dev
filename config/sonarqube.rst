SonarQube
=========

* ``sonar-project.properties``
* Further Reading: https://dev.astrotech.io/sonarqube/sonarscanner.html
* Further Reading: https://python.astrotech.io/devsecops/ci-cd/static-analysis.html

.. code-block:: properties
    :caption: Java

    ## Sonar Server
    sonar.host.url=http://sonarqube:9000/
    sonar.login=admin
    sonar.password=admin

    ## About Project
    sonar.projectKey=myproject
    sonar.projectName=myproject
    sonar.sourceEncoding=UTF-8

    ## SonarScanner Config
    sonar.verbose=false
    sonar.log.level=INFO
    sonar.showProfiling=false
    sonar.projectBaseDir=/usr/src/
    sonar.working.directory=/tmp/

    ## Build Breaker
    sonar.buildbreaker.skip=false
    sonar.buildbreaker.queryInterval=10000
    sonar.buildbreaker.queryMaxAttempts=1000

    ## Debugging
    # sonar.verbose=true
    # sonar.log.level=DEBUG
    # sonar.showProfiling=true
    # sonar.scanner.dumpToFile=/tmp/sonar-project.properties

    ## Java
    sonar.language=java
    sonar.java.source=8
    sonar.java.binaries=target/classes
    sonar.sources=src/main/java
    sonar.exclusions=**/migrations/**

.. code-block:: properties
    :caption: Python

    ## Sonar Server
    sonar.host.url=http://sonarqube:9000/
    sonar.login=admin
    sonar.password=admin

    ## About Project
    sonar.projectKey=myproject
    sonar.projectName=myproject
    sonar.sourceEncoding=UTF-8

    ## SonarScanner Config
    sonar.verbose=false
    sonar.log.level=INFO
    sonar.showProfiling=false
    sonar.projectBaseDir=/usr/src/
    sonar.working.directory=/tmp/

    ## Build Breaker
    sonar.buildbreaker.skip=false
    sonar.buildbreaker.queryInterval=10000
    sonar.buildbreaker.queryMaxAttempts=1000

    ## Debugging
    # sonar.verbose=true
    # sonar.log.level=DEBUG
    # sonar.showProfiling=true
    # sonar.scanner.dumpToFile=/tmp/sonar-project.properties

    ## Python
    sonar.language=py
    sonar.sources=.
    sonar.inclusions=**/*.py
    sonar.exclusions=**/migrations/**,**/*.pyc,**/__pycache__/**
