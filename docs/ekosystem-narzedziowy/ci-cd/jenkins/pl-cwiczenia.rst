Ćwiczenia
=========

Instalacja Jenkinsa i konfuguracja buildów
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Zainstaluj `Jenkins` za pomocą paczek `DEB` przez ``apt-get``
- Alternatywnie możesz użyć `Docker` albo manifestów `Puppeta`
- Zaciągnij repozytorium https://github.com/SonarSource/sonar-examples.git
- Zacznij budować różne projekty ``sonar-examples/projects/languages/java``
    - `ut` - unit tests
    - `it` - integration tests

Budowanie Pull Requestów
^^^^^^^^^^^^^^^^^^^^^^^^
- Skonfiguruj plan by budował gałęzie `GIT Flow`
    - `Pull Requests`
    - ``feature``
    - ``bugfix``
    - ``master``

Budowanie Checkstyle, PMD, JaCoCo, Findbugs i PITest
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Zaciągnij repozytorium https://github.com/SonarSource/sonar-examples.git
- Zacznij budować różne projekty ``sonar-examples/projects/languages/java``
- Wyniki upublicznij w `SonarQube`
    - Do instalacji możesz wykorzystać ``puppet module install maestrodev/sonarqube``
- Dodaj w ``pom.xml`` zależność ``pitest`` i przetestuj projekt wykorzystując domyślne mutatory

Pipeline DSL
^^^^^^^^^^^^
- Przepisz całą konfigurację wykorzustując plik ``Jenkinsfile`` i `Pipeline DSL`

Jenkins Docker Plugin
^^^^^^^^^^^^^^^^^^^^^
- Zainstaluj `Docker Plugin` w `Jenkins`
- Skonfiguruj zadanie aby uruchamiało kontener
- Zadanie ma provisionować konfigurację wewnątrz kontenera
- Zadanie ma uruchamiać build wewnątrz kontenera
- Zadanie ma niszczyć kontener po buildze

Jenkins i testy wydajnościowe JMeter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Przeprowadź test wydajnościowy głównej strony aplikacji uruchomionej na Twoim komputerze (np. `SonarQube` jeżeli wykonałeś poprzednie ćwiczenie)
- Test wydajnościowy powinien zapisany w ``xml`` oraz uruchamiany bez wykorzystania GUI
