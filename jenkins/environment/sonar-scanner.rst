************
SonarScanner
************


- https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner
- https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.0.3.778-linux.zip
- SonnarScanner requires Java 8
- https://docs.sonarqube.org/display/PLUG/Java+Plugin+and+Bytecode
- https://docs.sonarqube.org/display/SONAR/Analysis+Parameters

If your code is in other version:

.. code-block:: properties
    :caption: Minimal Sonar Project Properties

    sonar.projectKey=MyProject
    sonar.projectName=MyProject
    sonar.projectVersion=1.0

    sonar.sources=src/main/java
    sonar.java.binaries=target/classes
    sonar.java.source=9

.. code-block:: properties
    :caption: Extra Sonar Project Properties

    sonar.host.url=https://sonarcloud.io
    sonar.organization=Your Organization
    sonar.login=...

    sonar.language=py
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true

    sonar.projectKey=MyProject
    sonar.projectName=MyProject
    sonar.projectDescription=Your Project Description
    sonar.links.homepage=https://github.com/AstroTech/ecosystem-example-python
    sonar.links.scm=https://github.com/AstroTech/ecosystem-example-python
    sonar.links.issue=hhttps://github.com/AstroTech/ecosystem-example-python/issues
    sonar.links.ci=https://www.travis-ci.org/AstroTech/ecosystem-example-python

    sonar.projectBaseDir=src
    sonar.sources=.
    sonar.exclusions=**/migrations/**

    # Pylint
    sonar.python.pylint=/usr/local/bin/pylint
    sonar.python.pylint_config=.pylintrc
    sonar.python.pylint.reportPath=pylint-report.txt

    # Unit tests
    sonar.python.xunit.reportPath=test-reports/*.xml
    sonar.python.coverage.reportPath=coverage.xml

    # Integration tests
    sonar.python.coverage.itReportPath=it-coverage.xml

    # Turn off these rules
    sonar.issue.ignore.multicriteria=e1,e2
    # python:s100: "Method names should comply with a naming convention" gives many false positives when overriding
    # TestCase methods (such as setUp and tearDown) in test files.
    sonar.issue.ignore.multicriteria.e1.ruleKey=python:S100
    sonar.issue.ignore.multicriteria.e1.resourceKey=**/tests.py
    sonar.issue.ignore.multicriteria.e2.ruleKey=python:S100
    sonar.issue.ignore.multicriteria.e2.resourceKey=**/tests.py



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
