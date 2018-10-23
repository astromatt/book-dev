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
