Jenkins
=======

Installation and configuration
------------------------------

Install Using DEB on Ubuntu

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

.. code-block:: sh

    docker pull jenkins
    docker run -p 8080:8080 -p 50000:50000 -v /tmp/jenkins_home_on_host:/var/jenkins_home jenkins


Ćwiczenia
---------

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

.. toggle-code-block:: rst
    :label: Pokaż rozwiązanie dla Bitbucket Server

    Connect Jenkins with Bitbucket Server:

    - Install Stash Notifier Plugin in Jenkins
    - In Configure System - Global Jenkins System Configuration set as follows

    =============== ======================
    Key             Value
    =============== ======================
    Stash Root URL  http://localhost:7990/
    Stash User      ``jenkins``
    Stash Password  ``jenkins``
    =============== ======================


.. toggle-code-block:: rst
    :label: Pokaż rozwiązanie dla Pull Requestów

    Dashboard -> New Item -> "Freestyle project"

    ======================== ======================== =======================================================
    Section                   Key                      Value
    ======================== ======================== =======================================================
                             Project name             `Pull Request`
    Source Code Management   Source Code Management   `GIT`
    Source Code Management   Repository URL           ``ssh://git@localhost:7999/eco/workshop.git``
    Source Code Management   Credentials              ``jenkins``
    Source Code Management   [Advanced] -> Refspec    ``+refs/pull-requests/*/from:refs/remotes/origin/pr/*``
    Source Code Management   Branch Specifier         ``**/pr/*``
    Build Triggers           Schedule                 ``* * * * *``
    Post-build Actions       Notify Stash Instance
    ======================== ======================== =======================================================


.. toggle-code-block:: rst
    :label: Pokaż rozwiązanie dla brancha ``master``

    Dashboard -> New Item -> "Freestyle project"

    ======================== ======================== =============================================
    Section                  Key                      Value
    ======================== ======================== =============================================
                             Project name             `Master`
    Source Code Management   Source Code Management   `GIT`
    Source Code Management   Repository URL           ``ssh://git@localhost:7999/eco/workshop.git``
    Source Code Management   Credentials              ``jenkins``
    Source Code Management   Branch Specifier         ``**/master``
    Build Triggers           Schedule                 ``* * * * *``
    Post-build Actions       Notify Stash Instance
    ======================== ======================== =============================================


.. toggle-code-block:: rst
    :label: Pokaż rozwiązanie dla brancha ``feature``

    Dashboard -> New Item -> "Freestyle project"

    ======================== ======================== =============================================
    Section                  Key                      Value
    ======================== ======================== =============================================
                             Project name             `Feature`
    Source Code Management   Source Code Management   `GIT`
    Source Code Management   Repository URL           ``ssh://git@localhost:7999/eco/workshop.git``
    Source Code Management   Credentials              ``jenkins``
    Source Code Management   Branch Specifier         ``*/feature/*``
    Build Triggers           Schedule                 ``* * * * *``
    Post-build Actions       Notify Stash Instance
    ======================== ======================== =============================================


.. toggle-code-block:: rst
    :label: Pokaż rozwiązanie dla brancha ``bugfix``

    Dashboard -> New Item -> "Freestyle project"

    ======================== ======================== =============================================
    Section                  Key                      Value
    ======================== ======================== =============================================
                             Project name             `Feature`
    Source Code Management   Source Code Management   `GIT`
    Source Code Management   Repository URL           ``ssh://git@localhost:7999/eco/workshop.git``
    Source Code Management   Credentials              ``jenkins``
    Source Code Management   Branch Specifier         ``*/bugfix/*``
    Build Triggers           Schedule                 ``* * * * *``
    Post-build Actions       Notify Stash Instance
    ======================== ======================== =============================================


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

.. toggle-code-block:: xml
    :label: Pokaż rozwiązanie 2

    <?xml version="1.0" encoding="UTF-8"?>
    <jmeterTestPlan version="1.2" properties="2.8" jmeter="2.13 r1665067">
      <hashTree>
        <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="Test Plan" enabled="true">
          <stringProp name="TestPlan.comments"></stringProp>
          <boolProp name="TestPlan.functional_mode">false</boolProp>
          <boolProp name="TestPlan.serialize_threadgroups">false</boolProp>
          <elementProp name="TestPlan.user_defined_variables" elementType="Arguments" guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
            <collectionProp name="Arguments.arguments"/>
          </elementProp>
          <stringProp name="TestPlan.user_define_classpath"></stringProp>
        </TestPlan>
        <hashTree>
          <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Thread Group" enabled="true">
            <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>
            <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">
              <boolProp name="LoopController.continue_forever">false</boolProp>
              <stringProp name="LoopController.loops">1</stringProp>
            </elementProp>
            <stringProp name="ThreadGroup.num_threads">1</stringProp>
            <stringProp name="ThreadGroup.ramp_time">1</stringProp>
            <longProp name="ThreadGroup.start_time">1462974797000</longProp>
            <longProp name="ThreadGroup.end_time">1462974797000</longProp>
            <boolProp name="ThreadGroup.scheduler">false</boolProp>
            <stringProp name="ThreadGroup.duration"></stringProp>
            <stringProp name="ThreadGroup.delay"></stringProp>
          </ThreadGroup>
          <hashTree>
            <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP Request" enabled="true">
              <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
                <collectionProp name="Arguments.arguments"/>
              </elementProp>
              <stringProp name="HTTPSampler.domain">localhost</stringProp>
              <stringProp name="HTTPSampler.port">8080</stringProp>
              <stringProp name="HTTPSampler.connect_timeout"></stringProp>
              <stringProp name="HTTPSampler.response_timeout"></stringProp>
              <stringProp name="HTTPSampler.protocol"></stringProp>
              <stringProp name="HTTPSampler.contentEncoding"></stringProp>
              <stringProp name="HTTPSampler.path">/</stringProp>
              <stringProp name="HTTPSampler.method">GET</stringProp>
              <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
              <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
              <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
              <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
              <boolProp name="HTTPSampler.monitor">false</boolProp>
              <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
            </HTTPSamplerProxy>
            <hashTree/>
          </hashTree>
        </hashTree>
      </hashTree>
    </jmeterTestPlan>
