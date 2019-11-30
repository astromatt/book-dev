*******
Jenkins
*******







Maven
^^^^^
- Pipeline Maven Integration Plugin
- https://wiki.jenkins.io/display/JENKINS/Pipeline+Maven+Plugin

.. literalinclude:: code/jenkinsfile-maven.groovy
    :language: groovy
    :caption: Maven

Dobre praktyki
--------------
- Skrypt releasowy trzymany w konfiguracji narzędzia
- Instalacja nadmiarowych pluginów
- Korzystanie z pluginów zamiast z linii poleceń
- Przygotowanie środowiska + provisioning
- Spawnowanie agentów w cloud i czas setupu nowego środowiska
- Długość buildów
- Ignorowanie testów ?!
- Skipowanie testów (verbose)
- Budowanie Pull Requestów
- Jak długo trzymać branche?
- Jak automatycznie czyścić branche?
- Budowanie na różnych środowiskach
- Colorful deployments (version names from colors of the first six hexes in Git ref)
- Technology radar: https://www.thoughtworks.com/radar

- Spockframework: https://www.youtube.com/watch?v=64jZVsScbU8

.. code-block:: groovy
    :caption: Spock Framework

    // source: http://thejavatar.com/testing-with-spock/

    def "should return false if user does not have role required for viewing page"() {
       given:
          // context
          pageRequiresRole Role.ADMIN
          userHasRole Role.USER
       when:
          // some action is performed
          boolean authorized = authorizationService.isUserAuthorizedForPage(user, page)
       then:
          // expect specific result
          authorized == false
    }


Extra
^^^^^
- https://jenkins.io/solutions/pipeline/
- Python https://jenkins.io/solutions/python/
- Java https://jenkins.io/solutions/java/

.. literalinclude:: code/jenkinsfile-color.groovy
    :language: groovy
    :caption: Color

.. literalinclude:: code/jenkinsfile-artifactory.groovy
    :language: groovy
    :caption: Artifactory

.. literalinclude:: code/jenkinsfile-commit-message.groovy
    :language: groovy
    :caption: Commit Hash from git shell

- Jenkins odpalający ``git bisect`` i testy dla każdego commita z próby, tak długo aż nie znajdzie problemu

Build Strategy
--------------
.. figure:: img/geek-and-almost-green.jpg
    :scale: 25%
    :align: center

    Almost green... just some broken tests

.. figure:: img/cicd-strategy-color.png
    :scale: 25%
    :align: center

    Build Strategy

.. figure:: img/gitflow-all.png
    :scale: 25%
    :align: center

    Git Flow


Ćwiczenia
---------

Instalacja Jenkinsa i konfiguracją buildów
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Zainstaluj *Jenkins* za pomocą *Docker*
#. Zaciągnij repozytorium https://github.com/AstroTech/ecosystem-example-java.git
#. Ustaw Job aby budował aplikację za pomocą ``mvn clean install``

Building c/c++ projects inside ``docker``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Zainstaluj *Jenkins* za pomocą *Docker*
#. Zaciągnij repozytorium https://github.com/AstroTech/ecosystem-example-c
#. Budowanie ma odbywać się w kontenerze ``docker`` uruchamianym jako sibling
#. Dodaj job za pomocą Blue Ocean

    - apt update && apt install -y gcc libpcap-dev make
    - ./configure
    - make
    - make check
    - make install

Budowanie Pull Requestów
^^^^^^^^^^^^^^^^^^^^^^^^
- Skonfiguruj ręcznie plan by budował gałęzie wg. schematu *Git Flow*

    - Pull Requests
    - ``feature``
    - ``bugfix``
    - ``master``

.. figure:: img/gitflow-pull-request.png
    :scale: 50%
    :align: center

    Pull Requests

- Spróbuj wykorzystać któryś z dostępnych pluginów:

    - https://plugins.jenkins.io/bitbucket-build-status-notifier
    - https://plugins.jenkins.io/stashNotifier
    - https://plugins.jenkins.io/stash-pullrequest-builder

Trigger przez API
^^^^^^^^^^^^^^^^^
- Napisz skrypt ``sh`` wykorzystujący ``curl``
- Skrypt po odpaleniu ma triggerować build
- Dodaj skrypt do ``crontab``
- Skrypt ma się uruchamiać ``@daily``
- Zwróć uwagę, że ``cron`` ma mniejszą ilość zmiennych środowiskowych (skrypt, który u Ciebie działa, może nie być odpalany przez ``cron``)

Statyczna analiza kodu za pomocą *SonarScanner* i *SonarQube*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Dla repozytorium https://github.com/AstroTech/ecosystem-example-java.git
- Zacznij budować za pomocą ``mvn clean install``
- Wyniki upublicznij w *SonarQube*
- Build uzależnij od wyniku Quality Gates (plugin ``Sonar Quality Gates``)
- Uruchom SonarQube za pomocą ``docker run -d --name sonarqube -p 9000:9000 sonarqube``

Budowanie *PITest*
^^^^^^^^^^^^^^^^^^
- Dla repozytorium https://github.com/AstroTech/ecosystem-example-java.git
- Zacznij budować różne projekty ``coverage-metrics``
- Wyniki upublicznij w *SonarQube*
- Dodaj w ``pom.xml`` zależność ``pitest`` i przetestuj projekt wykorzystując domyślne mutatory

Jenkinsfile i Pipeline DSL
^^^^^^^^^^^^^^^^^^^^^^^^^^
- Przepisz całą konfigurację wykorzystując *Pipeline DSL* zapisany w *Jenkinsfile*

Jenkins Docker Plugin
^^^^^^^^^^^^^^^^^^^^^
- Skonfiguruj zadanie aby uruchamiało kontener
- Zadanie ma provisionować konfigurację wewnątrz kontenera
- Zadanie ma uruchamiać build wewnątrz kontenera
- Zadanie ma niszczyć kontener po buildze

Jenkins i testy wydajnościowe JMeter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Przeprowadź test wydajnościowy głównej strony aplikacji uruchomionej na Twoim komputerze (np. SonarQube jeżeli wykonałeś poprzednie ćwiczenie)
- Test wydajnościowy powinien zapisany w ``xml`` oraz uruchamiany bez wykorzystania GUI

Selenium
^^^^^^^^
#. Nagraj test w selenium
#. Uruchom test przy każdym commicie do brancha ``feature`` i ``bugfix``
