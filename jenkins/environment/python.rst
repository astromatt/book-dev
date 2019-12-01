******
Python
******


* Python https://jenkins.io/solutions/python/


SonarScanner
============
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
