*************
Sonar Scanner
*************


Run
===
.. code-block:: sh

    export SONARQUBE_URL='http://...:9000'
    docker run --rm -e SONAR_HOST_URL="${SONARQUBE_URL}" -v /home/src-java:/usr/src sonarsource/sonar-scanner-cli


Sonar Properties
================
.. code-block:: properties
    :caption: ``sonar-project.properties`` for Java Project
    :emphasize-lines: 24-

    ## Sonar Server
    sonar.host.url=http://localhost:9000/
    sonar.login=admin
    sonar.password=admin

    ## About Project
    sonar.projectKey=mypythonproject
    sonar.projectName=My Python Project
    sonar.projectDescription=My Description
    sonar.links.homepage=https://www.example.com/
    sonar.links.scm=https://github.com/myuser/myproject/
    sonar.links.issue=https://github.com/myuser/myproject/issues
    sonar.links.ci=https://github.com/myuser/myproject/cicd

    ## Analysis
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true
    sonar.scm.provider=git
    sonar.verbose=false
    sonar.log.level=INFO
    sonar.showProfiling=false
    #sonar.scanner.dumpToFile=/tmp/sonar-python.properties

    ## Language
    sonar.language=java
    sonar.java.source=8

    ## Paths
    sonar.projectBaseDir=/usr/src/
    sonar.sources=src/main/java
    sonar.exclusions=**/migrations/**
    sonar.java.binaries=target/classes

.. code-block:: properties
    :caption: ``sonar-project.properties`` for Python Project
    :emphasize-lines: 24-

    ## Sonar Server
    sonar.host.url=http://localhost:9000/
    sonar.login=admin
    sonar.password=admin

    ## About Project
    sonar.projectKey=mypythonproject
    sonar.projectName=My Python Project
    sonar.projectDescription=My Description
    sonar.links.homepage=https://www.example.com/
    sonar.links.scm=https://github.com/myuser/myproject/
    sonar.links.issue=https://github.com/myuser/myproject/issues
    sonar.links.ci=https://github.com/myuser/myproject/cicd

    ## Analysis
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true
    sonar.scm.provider=git
    sonar.verbose=false
    sonar.log.level=INFO
    sonar.showProfiling=false
    #sonar.scanner.dumpToFile=/tmp/sonar-python.properties

    ## Language
    sonar.language=py

    ## Paths
    sonar.projectBaseDir=/usr/src/
    sonar.sources=.
    sonar.inclusions=**/*.py
    sonar.exclusions=**/migrations/**,**/*.pyc,**/__pycache__/**

    ## Python
    sonar.python.pylint=/usr/bin/pylint
    sonar.python.pylint_config=.pylintrc
    sonar.python.xunit.skipDetails=false
    sonar.python.xunit.reportPath=xunit.xml
    sonar.python.coverage.reportPath=coverage.xml
    sonar.core.codeCoveragePlugin=cobertura

    ## Turn off these rules
    ## python:s100: "Method names should comply with a naming convention"
    ## gives many false positives when overriding
    ## TestCase methods (such as setUp and tearDown) in test files
    sonar.issue.ignore.multicriteria=e1,e2
    sonar.issue.ignore.multicriteria.e1.ruleKey=python:S100
    sonar.issue.ignore.multicriteria.e1.resourceKey=**/tests.py
    sonar.issue.ignore.multicriteria.e2.ruleKey=python:S100
    sonar.issue.ignore.multicriteria.e2.resourceKey=**/tests.py


.. code-block:: properties
    :caption: ``sonar-project.properties`` for CSS Project
    :emphasize-lines: 24-

    ## Sonar Server
    sonar.host.url=http://localhost:9000/
    sonar.login=admin
    sonar.password=admin

    ## About Project
    sonar.projectKey=mypythonproject
    sonar.projectName=My Python Project
    sonar.projectDescription=My Description
    sonar.links.homepage=https://www.example.com/
    sonar.links.scm=https://github.com/myuser/myproject/
    sonar.links.issue=https://github.com/myuser/myproject/issues
    sonar.links.ci=https://github.com/myuser/myproject/cicd

    ## Analysis
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true
    sonar.scm.provider=git
    sonar.verbose=false
    sonar.log.level=INFO
    sonar.showProfiling=false
    #sonar.scanner.dumpToFile=/tmp/sonar-python.properties

    ## Language
    sonar.language=css

    ## Paths
    sonar.projectBaseDir=/usr/src/
    sonar.sources=.
    sonar.inclusions=**/*.css,**/*.less,**/*.scss
    sonar.exclusions=**/tinymce.**,**/jquery.*

    ## CSS
    sonar.css.node=/usr/bin/node
    sonar.css.file.suffixes=.css,.less,.scss


.. code-block:: properties
    :caption: ``sonar-project.properties`` for JavaScript Project
    :emphasize-lines: 24-

    ## Sonar Server
    sonar.host.url=http://localhost:9000/
    sonar.login=admin
    sonar.password=admin

    ## About Project
    sonar.projectKey=mypythonproject
    sonar.projectName=My Python Project
    sonar.projectDescription=My Description
    sonar.links.homepage=https://www.example.com/
    sonar.links.scm=https://github.com/myuser/myproject/
    sonar.links.issue=https://github.com/myuser/myproject/issues
    sonar.links.ci=https://github.com/myuser/myproject/cicd

    ## Analysis
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true
    sonar.scm.provider=git
    sonar.verbose=false
    sonar.log.level=INFO
    sonar.showProfiling=false
    #sonar.scanner.dumpToFile=/tmp/sonar-python.properties

    ## Language
    sonar.language=js

    ## Paths
    sonar.projectBaseDir=/usr/src/
    sonar.sources=.
    sonar.inclusions=**/*.js,**/*.jsx,**/*.vue
    sonar.exclusions=**/tinymce.**,**/jquery.*

    ## JavaScript
    sonar.javascript.jQueryObjectAliases=$,jQuery
    sonar.javascript.environments=amd,applescript,atomtest,browser,commonjs,couch,embertest,greasemonkey,jasmine,jest,jquery,meteor,mocha,mongo,nashorn,node,phantomjs,prototypejs,protractor,qunit,rhino,serviceworker,shared-node-browser,shelljs,webextensions,worker,wsh,yui
    sonar.javascript.globals=angular,goog,google,OpenLayers,d3,dojo,dojox,dijit,Backbone,moment,casper
    sonar.javascript.exclusions=**/node_modules/**,**/bower_components/**
    sonar.nodejs.executable=/usr/bin/node

.. code-block:: properties
    :caption: ``sonar-project.properties`` for Multi-language Project
    :emphasize-lines: 24-

    ## Sonar Server
    sonar.host.url=http://localhost:9000/
    sonar.login=admin
    sonar.password=admin

    ## About Project
    sonar.projectKey=mypythonproject
    sonar.projectName=My Python Project
    sonar.projectDescription=My Description
    sonar.links.homepage=https://www.example.com/
    sonar.links.scm=https://github.com/myuser/myproject/
    sonar.links.issue=https://github.com/myuser/myproject/issues
    sonar.links.ci=https://github.com/myuser/myproject/cicd

    ## Analysis
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true
    sonar.scm.provider=git
    sonar.verbose=false
    sonar.log.level=INFO
    sonar.showProfiling=false
    #sonar.scanner.dumpToFile=/tmp/sonar-python.properties

    ## Paths
    sonar.projectBaseDir=/usr/src/
    sonar.sources=.
    sonar.inclusions=**/*.css,**/*.less,**/*.scss,**/*.html,**/*.xhtml,**/*.jspf,**/*.jspx,**/*.cshtml,**/*.vbhtml,**/*.aspx,**/*.ascx,**/*.rhtml,**/*.erb,**/*.shtm,**/*.shtml,**/*.js,**/*.jsx,**/*.vue,**/*.py
    sonar.exclusions=**/tinymce.**,**/jquery.*,**/sitemap.xml,**/migrations/**,**/*.pyc,**/__pycache__/**

    ## CSS
    sonar.css.node=/usr/bin/node
    sonar.css.file.suffixes=.css,.less,.scss

    ## JavaScript
    sonar.javascript.jQueryObjectAliases=$,jQuery
    sonar.javascript.environments=amd,applescript,atomtest,browser,commonjs,couch,embertest,greasemonkey,jasmine,jest,jquery,meteor,mocha,mongo,nashorn,node,phantomjs,prototypejs,protractor,qunit,rhino,serviceworker,shared-node-browser,shelljs,webextensions,worker,wsh,yui
    sonar.javascript.globals=angular,goog,google,OpenLayers,d3,dojo,dojox,dijit,Backbone,moment,casper
    sonar.javascript.exclusions=**/node_modules/**,**/bower_components/**
    sonar.nodejs.executable=/usr/bin/node

    ## Python
    sonar.python.pylint=/usr/bin/pylint
    sonar.python.pylint_config=.pylintrc
    sonar.python.xunit.skipDetails=false
    sonar.python.xunit.reportPath=xunit.xml
    sonar.python.coverage.reportPath=coverage.xml
    sonar.core.codeCoveragePlugin=cobertura
    sonar.issue.ignore.multicriteria=e1,e2
    sonar.issue.ignore.multicriteria.e1.ruleKey=python:S100
    sonar.issue.ignore.multicriteria.e1.resourceKey=**/tests.py
    sonar.issue.ignore.multicriteria.e2.ruleKey=python:S100
    sonar.issue.ignore.multicriteria.e2.resourceKey=**/tests.py


Create Own Image
================
.. code-block:: console

    $ cd PROJECT_DIRECTORY
    $ docker run --rm -d --name sonarqube -p 9000:9000 -v $(pwd):/src sonarqube
    $ docker exec -u 0 -it sonarqube bash

        curl -sL https://deb.nodesource.com/setup_8.x -o /opt/node.sh
        bash /opt/node.sh
        apt install -y nodejs
        wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492.zip -O /opt/sonar-scanner.zip
        unzip -d /opt/ /opt/sonar-scanner.zip
        ln -s /opt/sonar-scanner-*/bin/sonar-scanner /usr/bin/sonar-scanner
        VERSION=$(cd /src/ && hg log -l 1 --template '{node}\n')

        apt install -y python-pip pylint python-coverage python-nose
        pip install -r /src/requirements.txt


Configuration
=============
#. Quality Profile -> Python
#. Skopiuj profil "Sonar way" i nazwij nowy jako "PyLint"
#. Trybik (prawy górny róg) -> Activate more rules
#. Przefiltruj listę (lewy dolny róg) po "Repository" równym "PyLint"
#. Bulk Change (góra ekrany) -> Activate in "PyLint" -> zaakceptuj
#. Ustaw "PyLint jako domyślny"
#. Uruchom analizę

.. warning:: Po uruchomieniu ``SonarQube`` z obrazu ``Docker`` instalacja pluginów, a następnie restart ``SonarQube`` niszczy możliwość przeprowadzania analizy


Further Reading
===============
* https://sonarqube.com
* http://docs.sonarqube.org/display/SONAR/Documentation
* https://sonarqube.com/dashboard/index?did=143
* https://sonarqube.com/governance?id=662857
* https://python.astrotech.io/quality/ci-cd/tools.html
* https://python.astrotech.io/quality/ci-cd/pipelines.html
* https://python.astrotech.io/quality/ci-cd/static-analysis.html
