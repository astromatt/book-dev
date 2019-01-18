SonarQube
=========


Sonar Family
------------
* SonarQube
* SonarCloud
* SonarLint
* SonarScanner


Install
-------
.. code-block:: console

    docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube

SonarScanner
------------

Set-up
^^^^^^
.. code-block:: console

    cd PROJECT_DIRECTORY
    docker run --rm -d --name sonarqube -p 9000:9000 -v $(pwd):/src sonarqube
    docker exec -u 0 -it sonarqube bash

        curl -sL https://deb.nodesource.com/setup_8.x -o /opt/node.sh
        bash /opt/node.sh
        apt install -y nodejs pylint python-coverage python-nose
        wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492.zip -O /opt/sonar-scanner.zip
        unzip -d /opt/ /opt/sonar-scanner.zip
        ln -s /opt/sonar-scanner-*/bin/sonar-scanner /usr/bin/sonar-scanner

Running
^^^^^^^
.. code-block:: console

    sonar-scanner -Dproject.settings=/src/sonar-multilanguage.properties

Python
^^^^^^
.. literalinclude:: src/sonar-python.properties
    :language: properties

JavaScript
^^^^^^^^^^
.. literalinclude:: src/sonar-javascript.properties
    :language: properties

CSS
^^^
.. literalinclude:: src/sonar-css.properties
    :language: properties

HTML
^^^^
.. literalinclude:: src/sonar-html.properties
    :language: properties

Multi-language
^^^^^^^^^^^^^^
.. literalinclude:: src/sonar-multilanguage.properties
    :language: properties


Budowanie Pull Request
----------------------
.. code-block:: properties

    sonar.pullrequest.base=master
    sonar.pullrequest.branch=feature/my-new-feature
    sonar.pullrequest.key=5
    sonar.pullrequest.provider=GitHub
    sonar.pullrequest.github.repository=my-company/my-repo https://blog.sonarsource.com/sonarcloud-loves-your-build-pipeline

Analiza kodu za pomocą ``mvn``
------------------------------

pom.xml
^^^^^^^
.. code-block:: xml

    <settings>
        <pluginGroups>
            <pluginGroup>org.sonarsource.scanner.maven</pluginGroup>
        </pluginGroups>
        <profiles>
            <profile>
                <id>sonar</id>
                <activation>
                    <activeByDefault>true</activeByDefault>
                </activation>
                <properties>
                    <!-- Optional URL to server. Default value is http://localhost:9000 -->
                    <sonar.host.url>
                      http://myserver:9000
                    </sonar.host.url>
                </properties>
            </profile>
         </profiles>
    </settings>

Używnianie
^^^^^^^^^^
.. code-block:: sh

    mvn sonar:sonar

Dokumentacja
------------
* https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner+for+Maven


Zadania
-------

Instalacja
^^^^^^^^^^
- Zainstaluj `SonarQube`

.. tip:: User admin, Hasło admin

Wrzucanie wyników statycznej analizy kodu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Czy wcześniej zainstalowałeś `Bitbucket Server`?

    - Nie - Zaciągnij repozytorium https://github.com/SonarSource/sonar-training-examples.git i wrzuć wyniki odpalając ``mvn``
    - Tak - Zaciągnij repozytorium ``sonar-training-examples`` z twojej instancji `Bitbucket Server`

- Skonfiguruj aby statyczna analiza kodu uruchamiała z `Jenkins`
- Skonfiguruj tak, by w każdym `Pull Request` jako komentarz do linii kodu wyświetlały się uwagi z `SonarQube`
- Dostosuj poziom komentarzy, aby nie zalać programisty ich zbyt dużą ilością, np. wyświetlaj tylko ``Blocker`` i ``Critical``
