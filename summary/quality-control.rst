Quality Control
===============


.. contents::


Sonar Qube
----------
* https://docs.sonarqube.org/latest/setup/environment-variables/

.. code-block:: sh

    docker network create ecosystem

.. literalinclude:: src/run-sonarqube.sh
    :language: sh

.. note:: For SonarQube 8.2+ make sure you're using volumes as shown with
          the above commands, and not bind mounts. Using bind mounts
          prevents plugins and languages from populating correctly.
          https://docs.sonarqube.org/latest/setup/install-server/#header-3

.. code-block:: sh

    --env SONAR_JDBC_URL=... \
    --env SONAR_JDBC_USERNAME=... \
    --env SONAR_JDBC_PASSWORD=...

    # SONAR_JDBC_URL=jdbc:postgresql://localhost:5432/sonarqube?currentSchema=my_schema


Sonar Scanner
-------------
* ``sonar-project.properties``
* Further Reading: https://dev.astrotech.io/sonarqube/sonarscanner.html
* Further Reading: https://python.astrotech.io/devsecops/ci-cd/static-analysis.html

.. code-block:: sh

    docker run --rm --network ecosystem -v $(pwd):/usr/src sonarsource/sonar-scanner-cli


Configuration for Java
----------------------
.. code-block:: properties
    :caption: Java

    ## Sonar Server
    sonar.host.url=http://sonarqube:9000/
    sonar.login=admin
    sonar.password=abcdefghi

    ## About Project
    sonar.projectKey=myjavaproject
    sonar.projectName=myjavaproject
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


Configuration for Python
------------------------
.. code-block:: properties
    :caption: Python

    ## Sonar Server
    sonar.host.url=http://sonarqube:9000/
    sonar.login=admin
    sonar.password=abcdefghi

    ## About Project
    sonar.projectKey=mypythonproject
    sonar.projectName=mypythonproject
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


Automation
----------
.. code-block:: sh
    :caption: ``test-functional.sh``

    #!/bin/sh

    cd example-py-doctest/
    python3 -m doctest -v doctests/*

.. code-block:: sh
    :caption: ``test-integration.sh``

    #!/bin/sh

    pip install -r requirements.txt
    cd example-py-pytest/
    python3 -m pytest

.. code-block:: sh
    :caption: ``test-static.sh``

    #!/bin/sh

    docker run --rm --network ecosystem -v $(pwd):/usr/src sonarsource/sonar-scanner-cli

.. code-block:: sh
    :caption: ``test-unit.sh``

    #!/bin/sh

    cd example-py-unittest
    python3 -m unittest


Alternatives
------------
Server side quality monitoring:

    * SonarLint https://www.sonarlint.org
    * SonarQube https://www.sonarqube.org
    * SonarScanner https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/
    * Findbugs http://findbugs.sourceforge.net
    * PMD https://pmd.github.io
    * Checkstyle https://checkstyle.sourceforge.io

UI Testing:

    * https://www.selenium.dev/

Cloud based quality monitoring:

    * SonarCloud https://sonarcloud.io
    * Coveralls https://coveralls.io

Code Coverage:

    * JaCoCo https://www.jacoco.org/jacoco/
    * Cobertura http://cobertura.github.io/cobertura/

Mutation Testing:

    * PiTest http://pitest.org

Load Testing:

    * Locust https://locust.io
    * Gatling https://gatling.io
    * JMeter https://jmeter.apache.org

BDD Testing:

    * Lettuce http://lettuce.it
    * Cucumber https://cucumber.io
    * JBehave https://jbehave.org
    * https://lettuce.readthedocs.io/en/latest/recipes/django-lxml.html
    * https://behave.readthedocs.io/en/stable/
