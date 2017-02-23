*******
Jenkins
*******

Installation and configuration
==============================

Install Using DEB on Ubuntu
---------------------------

.. code-block:: sh

    wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
    echo "deb http://pkg.jenkins-ci.org/debian binary/" >> /etc/apt/sources.list
    apt-get update
    apt-get install --yes jenkins
    sudo su - jenkins
    ssh-keygen
    cat ~/.ssh/id_rsa.pub
    exit
    service jenkins stop
    # sed -i 's/HTTP_PORT=8080/HTTP_PORT=8081/g' /etc/default/jenkins
    service jenkins start

Install Using Docker
--------------------

.. code-block:: sh

    docker pull jenkins
    docker run -p 8080:8080 -p 50000:50000 -v /tmp/jenkins_home_on_host:/var/jenkins_home jenkins

Real-Life Examples
==================


Practical Exercises
===================

Jenkins Installation and Build Configuration
--------------------------------------------
- Install `Jenkins` using `DEB` packages by ``apt-get``
- Alternatively you might want to use `Docker` or `Puppet` manifests
- Download repository https://github.com/SonarSource/sonar-examples.git
- Start building projects in ``sonar-examples/projects/languages/java``
    - `ut` - unit tests
    - `it` - integration tests

Building Pull Requests
----------------------
- Configure plan to build `GIT Flow` branches
    - `Pull Requests`
    - ``feature``
    - ``bugfix``
    - ``master``

Building Checkstyle, PMD, JaCoCo, Findbugs and PITest
-----------------------------------------------------
- Download repository https://github.com/SonarSource/sonar-examples.git
- Start building projects in ``sonar-examples/projects/languages/java``
- Push static code analysis results to `SonarQube`
    - You might want to install `SonarQube` using ``puppet module install maestrodev/sonarqube``
- Add ``pitest`` dependency to ``pom.xml`` and test project using default mutators

Pipeline DSL
------------
- Rewrite configuration using ``Jenkinsfile`` and `Pipeline DSL`

Jenkins Docker Plugin
---------------------
- Install `Docker Plugin` in `Jenkins`
- Configure job to run inside container
- Job has to provision the environment
- Job has to build the project inside container
- Job has to destroy container after build

Jenkins and load testing with JMeter
------------------------------------
- Run load test for main page of application run on you computer (ie. `SonarQube` if you have solved the previous problems)
- Load test should be in ``xml`` file and run without GUI


Zadania praktyczne
==================

Instalacja Jenkinsa i konfuguracja buildów
------------------------------------------
- Zainstaluj `Jenkins` za pomocą paczek `DEB` przez ``apt-get``
- Alternatywnie możesz użyć `Docker` albo manifestów `Puppeta`
- Zaciągnij repozytorium https://github.com/SonarSource/sonar-examples.git
- Zacznij budować różne projekty ``sonar-examples/projects/languages/java``
    - `ut` - unit tests
    - `it` - integration tests

Budowanie Pull Requestów
------------------------
- Skonfiguruj plan by budował gałęzie `GIT Flow`
    - `Pull Requests`
    - ``feature``
    - ``bugfix``
    - ``master``

Budowanie Checkstyle, PMD, JaCoCo, Findbugs i PITest
------------------------------------------------------
- Zaciągnij repozytorium https://github.com/SonarSource/sonar-examples.git
- Zacznij budować różne projekty ``sonar-examples/projects/languages/java``
- Wyniki upublicznij w `SonarQube`
    - Do instalacji możesz wykorzystać ``puppet module install maestrodev/sonarqube``
- Dodaj w ``pom.xml`` zależność ``pitest`` i przetestuj projekt wykorzystując domyślne mutatory

Pipeline DSL
------------
- Przepisz całą konfigurację wykorzustując plik ``Jenkinsfile`` i `Pipeline DSL`

Jenkins Docker Plugin
---------------------
- Zainstaluj `Docker Plugin` w `Jenkins`
- Skonfiguruj zadanie aby uruchamiało kontener
- Zadanie ma provisionować konfigurację wewnątrz kontenera
- Zadanie ma uruchamiać build wewnątrz kontenera
- Zadanie ma niszczyć kontener po buildze

Jenkins i testy wydajnościowe JMeter
------------------------------------
- Przeprowadź test wydajnościowy głównej strony aplikacji uruchomionej na Twoim komputerze (np. `SonarQube` jeżeli wykonałeś poprzednie ćwiczenie)
- Test wydajnościowy powinien zapisany w ``xml`` oraz uruchamiany bez wykorzystania GUI
