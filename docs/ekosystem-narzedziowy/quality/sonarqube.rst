SonarQube
=========

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

.. toggle-code-block:: sh
    :label: Pokaż rozwiązanie dla instalacji za pomocą ``apt-get``

    echo "deb http://downloads.sourceforge.net/project/sonar-pkg/deb binary/" >> /etc/apt/sources.list
    apt-get update
    apt-get install --yes sonar
    service sonar stop
    sed -i 's(#sonar.jdbc.url=jdbc:postgresql(sonar.jdbc.url=jdbc:postgresql(g' /opt/sonar/conf/sonar.properties
    sed -i 's(sonar.jdbc.url=jdbc:h2(#sonar.jdbc.url=jdbc:h2(g' /opt/sonar/conf/sonar.properties
    sed -i 's(#sonar.jdbc.username=sonar(sonar.jdbc.username=sonar(g' /opt/sonar/conf/sonar.properties
    sed -i 's(#sonar.jdbc.password=sonar(sonar.jdbc.password=sonar(g' /opt/sonar/conf/sonar.properties
    service sonar start

.. toggle-code-block:: sh
    :label: Pokaż rozwiązanie dla instalacji za pomocą ``docker``

    docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube

    # By default, the image will use an embedded H2 database that is not suited for production.
    docker run -d --name sonarqube \
        -p 9000:9000 -p 9092:9092 \
        -e SONARQUBE_JDBC_USERNAME=sonar \
        -e SONARQUBE_JDBC_PASSWORD=sonar \
        -e SONARQUBE_JDBC_URL=jdbc:postgresql://localhost/sonar \
        sonarqube

.. tip:: User admin, Hasło admin

Wrzucanie wyników statycznej analizy kodu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Czy wcześniej zainstalowałeś `Bitbucket Server`?

    - Nie - Zaciągnij repozytorium https://github.com/SonarSource/sonar-examples.git i wrzuć wyniki odpalając ``mvn``
    - Tak - Zaciągnij repozytorium ``sonar-examples`` z twojej instancji `Bitbucket Server`

- Skonfiguruj aby statyczna analiza kodu uruchamiała z `Jenkins`
- Skonfiguruj tak, by w każdym `Pull Request` jako komentarz do linii kodu wyświetlały się uwagi z `SonarQube`
- Dostosuj poziom komentarzy, aby nie zalać programisty ich zbyt dużą ilością, np. wyświetlaj tylko ``Blocker`` i ``Critical``
