*******
Jenkins
*******

- https://jenkins.io/
- https://jenkins.io/doc

.. figure:: /_img/cicd-loop.png
    :scale: 75%
    :align: center

    Continuous Integration -> Continuous Delivery -> Continuous Deployment

Jenkins in Devtools Ecosystem
-----------------------------
.. figure:: /_img/ecosystem-big-picture-01.png
    :scale: 50%
    :align: center

    Ecosystem Big Picture

.. figure:: /_img/ecosystem-jenkins-tooling.png
    :scale: 50%
    :align: center

    Jenkins in Devtools Ecosystem

Install
-------

Weekly version
^^^^^^^^^^^^^^
.. code-block:: console

    docker run -d --rm --name jenkins -p 8080:8080 -v /home/jenkins:/var/jenkins_home jenkins/jenkins
    cat /home/jenkins/secrets/initialAdminPassword

Install LTS
^^^^^^^^^^^
.. code-block:: console

    docker run -d  --rm --name jenkins -p 8080:8080 -v /home/jenkins:/var/jenkins_home jenkins/jenkins:lts
    cat /home/jenkins/secrets/initialAdminPassword

Docker Compose
^^^^^^^^^^^^^^
#. Create file ``docker-compose.yaml``

    .. code-block:: yaml

        version: '3'

        networks:
            devtools-ecosystem:
                driver: bridge

        services:
            jenkins:
                image: jenkins/jenkins
                container_name: jenkins
                restart: "no"
                ports:
                    - "8080:8080"
                networks:
                    - devtools-ecosystem
                volumes:
                    - /home/jenkins:/var/jenkins_home/
                    - /var/run/docker.sock:/var/run/docker.sock

#. Run Jenkins

    .. code-block:: console

        docker-compose up

#. Run Jenkins in background (daemon)

    .. code-block:: console

        docker-compose up -d


More information
^^^^^^^^^^^^^^^^
- https://github.com/jenkinsci/docker/blob/master/README.md

Architecture
------------
- Local executors (default: 2)
- Remote workers via SSH and labels
- Docker build
- New UI (Blue Ocean) currently accessible as a plugin, but soon to be default
- Jenkins uses Groovy scripts in ``Jenkinsfile`` in repository main directory

Administration
--------------
.. figure:: /_img/geek-and-poke-jenkins-down-and-up.jpg
    :scale: 50%
    :align: center

    Jenkins down... and up again.

User Management
^^^^^^^^^^^^^^^
- Always use *LDAP* (*OpenLDAP* or *Active Directory*)
- Each tool has separate *LDAP* read only account
- Connection only with *LDAPS* (secure)
- Internal and external users in one *LDAP* server
- Name groups as ``jenkins-users`` or ``jenkins-administrators``
- Local administrator ``jenkins-administrator`` only for fixing bugs with *LDAP*
- Use ``jenkins@example.com`` (for easy email filtering)
- Use ``jenkins.example.com`` as domain name with firewall blocking external access
- Wildcard *SSL* certificate (``*.example.com``)
- Only *HTTPS* access to tool!
- ``/etc/resolv.conf`` ``search example.com`` -> set by *DHCP*
- No nested groups
- All tool access groups in ``OU=ecosystem``
- Use LDAP groups for project roles from ``OU=projects``
- Do not use user accounts in project roles (only *LDAP* groups)
- Confluence page with all ``*-administrators`` + ``mailto:`` links
- Confluence page with *Jira* project leaders
- Confluence page with *Jenkins* job administrators
- Do not use technical accounts (use *SSH* keys)
- Use *SSH* keys with proper comment: ``user@example.com/computer-name``

Plugin installation
^^^^^^^^^^^^^^^^^^^
- Dependencies hell
- Plugin support (especially those free ones)
- Open Source plugins
- Plugin and upgrades
- Once given out, cannot be easily taken away

Build Triggers
^^^^^^^^^^^^^^
- Build after other projects are built
- Build periodically
- GitHub hook trigger for GITScm polling
- Poll SCM
- Trigger builds remotely (e.g., from scripts via REST API) - https://wiki.jenkins.io/display/JENKINS/Remote+access+API

.. literalinclude:: code/jenkins-api.sh
    :language: console
    :caption: build trigger via Jenkins API

Notifications
-------------
- Email
- Slack / HipChat
- IRC

Installing MVN
--------------
.. code-block:: console

    docker container exec -u 0 -it jenkins bash

.. code-block:: console

    mkdir -p /opt
    cd /opt
    wget http://apache.claz.org/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.tar.gz
    tar -zxvf apache-maven-3.5.4-bin.tar.gz
    mv apache-maven-3.5.4 /opt/maven
    ln -s /opt/maven/bin/mvn /usr/local/bin/mvn

.. code-block:: console

    echo 'export M2_HOME=/opt/maven' > /etc/profile.d/maven.sh

Now load the environment variables in the current shell using the following command.

.. code-block:: console

    source /etc/profile.d/maven.sh


SonarScanner
------------
- https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner
- https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.0.3.778-linux.zip
- SonnarScanner requires Java 8
- https://docs.sonarqube.org/display/PLUG/Java+Plugin+and+Bytecode
- https://docs.sonarqube.org/display/SONAR/Analysis+Parameters

If your code is in other version:

.. literalinclude:: code/sonar-minimal.properties
    :language: properties
    :caption: Minimal Sonar Project Properties

.. literalinclude:: code/sonar-extra.properties
    :language: properties
    :caption: Extra Sonar Project Properties

.. figure:: /_img/geek-and-poke-development-driven-tests.jpg
    :scale: 15%
    :align: center

    Development Driven Tests


.. code-block:: yaml

    version: '3'

    networks:
      prodnetwork:
        driver: bridge

    volumes:
      jenkins-data:

    services:
      jenkins:
        image: jenkins/jenkins
        restart: always
        ports:
          - "18080:8080"
        networks:
          - prodnetwork
        volumes:
          - /tmp/jenkins:/var/lib/jenkins/
        depends_on:
          - sonar
        environment:
          - SONAR_PORT=9000
      sonar:
        image: sonarqube
        restart: always
        ports:
         - "19000:9000"
         - "19092:9092"
        networks:
          - prodnetwork

Large repos
-----------
- is a sign of git missuse, and should be tackled with GIT LFS
- Use command line git rather than jGit
- command line git handles memory better
- Use reference repository (bare)
- Shallow clone (GIT from 1.9+ can push from shallow clones)
- Don't fetch tags
- Narrow refspec - only clone specific branches (honor refspec on initial clone)
- Pipeline stash / unstash (sparse checkout on master node, and then stash checkout, and unstash on remotes)
- Sparse checkout (Subset of working tree - single directory [exclude or include on per file basis])

Blue Ocean
----------
- Multibranch projects are the first class citizens
- New UI
- Interoperable with old UI
- Accessible at ``/blue/`` in the URL after "Blue Ocean" plugin installation.
- Pipeline editor


.. figure:: /_img/cicd-pipeline.png
    :scale: 50%
    :align: center

    Blue Ocean pipeline

.. figure:: /_img/cicd-blueocean-success.png
    :scale: 75%
    :align: center

    Blue Ocean pipeline Success

.. figure:: /_img/cicd-blueocean-failing.png
    :scale: 50%
    :align: center

    Blue Ocean pipeline Failing

Environment Variables
---------------------
.. csv-table:: Jenkins Environment Variables
    :header: "Variable", "Description"
    :file: data/jenkins-environmental-variables.csv

Groovy syntax
-------------
.. literalinclude:: code/groovy-variable.groovy
    :language: groovy
    :caption: Variable

.. literalinclude:: code/groovy-contitional.groovy
    :language: groovy
    :caption: Conditional

.. literalinclude:: code/groovy-control-structure.groovy
    :language: groovy
    :caption: Control structure

.. literalinclude:: code/groovy-function.groovy
    :language: groovy
    :caption: Function

.. literalinclude:: code/groovy-class.groovy
    :language: groovy
    :caption: Class

.. literalinclude:: code/groovy-loop.groovy
    :language: groovy
    :caption: Loop

.. literalinclude:: code/groovy-import.groovy
    :language: groovy
    :caption: Import

.. literalinclude:: code/groovy-exception.groovy
    :language: groovy
    :caption: Exception

.. literalinclude:: code/groovy-http.groovy
    :language: groovy
    :caption: Rest API HTTP queries


``Jenkinsfile`` - Pipeline model definition
-------------------------------------------
- https://jenkins.io/doc/book/pipeline/jenkinsfile/
- https://jenkins.io/doc/pipeline/steps/
- https://jenkins.io/doc/tutorials/building-a-multibranch-pipeline-project/
- http://localhost:8080/pipeline-syntax/
- http://localhost:8080/pipeline-syntax/globals#currentBuild
- http://localhost:8080/pipeline-syntax/globals#env
- ``Jenkinsfile``
- Bundled with Blue Ocean
- ``declarative-linter`` validate before running job
- The first line of a Jenkinsfile should be #!/usr/bin/env groovy
- Automatically create Pipelines for all Branches and Pull Requests
- Code review/iteration on the Pipeline
- Audit trail for the Pipeline
- Single source of truth for the Pipeline, which can be viewed and edited by multiple members of the project.

.. figure:: /_img/ecosystem-jenkins-pipeline.png
    :scale: 50%
    :align: center

    Pipeline model definition plugin

Sample ``Jenkinsfile``:

.. literalinclude:: code/jenkinsfile-simple.groovy
    :language: groovy
    :caption: Simple

.. literalinclude:: code/jenkinsfile-example.groovy
    :language: groovy
    :caption: Example

.. literalinclude:: code/jenkinsfile-test.groovy
    :language: groovy
    :caption: Test

.. literalinclude:: code/jenkinsfile-build.groovy
    :language: groovy
    :caption: Build

.. literalinclude:: code/jenkinsfile-deploy.groovy
    :language: groovy
    :caption: Deploy

.. literalinclude:: code/jenkinsfile-environment.groovy
    :language: groovy
    :caption: Environment

.. literalinclude:: code/jenkinsfile-parameter.groovy
    :language: groovy
    :caption: Parameters

.. literalinclude:: code/jenkinsfile-agent.groovy
    :language: groovy
    :caption: Agent

.. literalinclude:: code/jenkinsfile-parallel.groovy
    :language: groovy
    :caption: Parallel

.. literalinclude:: code/jenkinsfile-option.groovy
    :language: groovy
    :caption: Option

.. literalinclude:: code/jenkinsfile-tool.groovy
    :language: groovy
    :caption: Tool

.. literalinclude:: code/jenkinsfile-timeout.groovy
    :language: groovy
    :caption: Timeout

.. literalinclude:: code/jenkinsfile-input.groovy
    :language: groovy
    :caption: Input

.. literalinclude:: code/jenkinsfile-artifact.groovy
    :language: groovy
    :caption: Artifact

Post Actions
^^^^^^^^^^^^
At the end of pipeline directive:

:``always``: Run the steps in the post section regardless of the completion status of the Pipeline’s or stage’s run.

:``changed``: Only run the steps in post if the current Pipeline’s or stage’s run has a different completion status from its previous run.

:``failure``: Only run the steps in post if the current Pipeline’s or stage’s run has a "failed" status, typically denoted by red in the web UI.

:``success``: Only run the steps in post if the current Pipeline’s or stage’s run has a "success" status, typically denoted by blue or green in the web UI.

:``unstable``: Only run the steps in post if the current Pipeline’s or stage’s run has an "unstable" status, usually caused by test failures, code violations, etc. This is typically denoted by yellow in the web UI.

:``aborted``: Only run the steps in post if the current Pipeline’s or stage’s run has an "aborted" status, usually due to the Pipeline being manually aborted. This is typically denoted by gray in the web UI

.. literalinclude:: code/jenkinsfile-post.groovy
    :language: groovy
    :caption: Post

Triggers
^^^^^^^^

:``cron``: Accepts a cron-style string to define a regular interval at which the Pipeline should be re-triggered, for example: ``triggers { cron('H */4 * * 1-5') }``

:``pollSCM``: Accepts a cron-style string to define a regular interval at which Jenkins should check for new source changes. If new changes exist, the Pipeline will be re-triggered. For example: ``triggers { pollSCM('H */4 * * 1-5') }`` Available since Jenkins 2.22

:``upstream``: Accepts a comma separated string of jobs and a threshold. When any job in the string finishes with the minimum threshold, the Pipeline will be re-triggered. For example: ``triggers { upstream(upstreamProjects: 'job1,job2', threshold: hudson.model.Result.SUCCESS) }``

.. literalinclude:: code/jenkinsfile-trigger.groovy
    :language: groovy
    :caption: Trigger

When
^^^^
:``branch``: Execute the stage when the branch being built matches the branch pattern given, for example: ``when { branch 'master' }``. Note that this only works on a multibranch Pipeline.

:``environment``: Execute the stage when the specified environment variable is set to the given value, for example: ``when { environment name: 'DEPLOY_TO', value: 'production' }``

:``expression``: Execute the stage when the specified Groovy expression evaluates to true, for example: ``when { expression { return params.DEBUG_BUILD } }``

:``not``: Execute the stage when the nested condition is false. Must contain one condition. For example: ``when { not { branch 'master' } }``

:``allOf``: Execute the stage when all of the nested conditions are true. Must contain at least one condition. For example: ``when { allOf { branch 'master'; environment name: 'DEPLOY_TO', value: 'production' } }``

:``anyOf``: Execute the stage when at least one of the nested conditions is true. Must contain at least one condition. For example: ``when { anyOf { branch 'master'; branch 'staging' } }``

.. literalinclude:: code/jenkinsfile-when.groovy
    :language: groovy
    :caption: When

Docker
^^^^^^
- https://youtu.be/TsWkZLLU-s4?t=3653
- Install Docker on Jenkins container

    .. code-block:: console

        docker exec -itu 0 jenkins bash
        curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
        echo "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable" > /etc/apt/sources.list.d/docker.list
        apt install -y apt-transport-https
        apt update
        apt install -y docker-ce

- Spawning sibling containers instead of container inside the container

    .. code-block:: console

        $ docker run -v /var/run/docker.sock:/var/run/docker.sock ...

- Using docker

    .. code-block:: console

        $ docker pull openjdk:8-jdk
        $ docker pull maven:3-jdk-7
        $ docker pull maven:3-jdk-8
        $ docker pull golang:1.7
        $ docker pull ruby:2.3
        $ docker pull python:2
        $ docker pull python:3

.. literalinclude:: code/jenkinsfile-docker.groovy
    :language: groovy
    :caption: Docker

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
- Colorful deployments (version names from colors of the first six hexes in GIT ref)
- Technology radar: https://www.thoughtworks.com/radar

- Spockframework: https://www.youtube.com/watch?v=64jZVsScbU8

.. literalinclude:: code/spockframework.groovy
    :language: groovy
    :caption: Spock Framework

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
.. figure:: /_img/geek-and-almost-green.jpg
    :scale: 25%
    :align: center

    Almost green... just some broken tests

.. figure:: /_img/build-strategy.png
    :scale: 25%
    :align: center

    Build Strategy

.. figure:: /_img/git-flow-whiteboard.jpg
    :scale: 25%
    :align: center

    GIT Flow


Ćwiczenia
---------

Instalacja Jenkinsa i konfiguracją buildów
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Zainstaluj *Jenkins* za pomocą *Docker*
#. Zaciągnij repozytorium https://github.com/AstroTech/sonarqube-example-java-maven-junit.git
#. Ustaw Job aby budował aplikację za pomocą ``mvn clean install``

Building c/c++ projects inside ``docker``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Zainstaluj *Jenkins* za pomocą *Docker*
#. Zaciągnij repozytorium https://github.com/AstroTech/tcpdump
#. Budowanie ma odbywać się w kontenerze ``docker`` uruchamianym jako sibling
#. Dodaj job za pomocą Blue Ocean

    - apt update && apt install -y gcc libpcap-dev make
    - ./configure
    - make
    - make check
    - make install

Budowanie Pull Requestów
^^^^^^^^^^^^^^^^^^^^^^^^
- Skonfiguruj ręcznie plan by budował gałęzie wg. schematu *GIT Flow*

    - Pull Requests
    - ``feature``
    - ``bugfix``
    - ``master``

.. figure:: /_img/git-pull-request-09.jpg
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
- Dla repozytorium ``sonar-training-examples`` (https://github.com/AstroTech/sonarqube-example-java-maven-junit.git)
- Zacznij budować za pomocą ``mvn clean install``
- Wyniki upublicznij w *SonarQube*
- Build uzależnij od wyniku Quality Gates (plugin ``Sonar Quality Gates``)
- Uruchom SonarQube za pomocą ``docker run -d --name sonarqube -p 9000:9000 sonarqube``

Budowanie *PITest*
^^^^^^^^^^^^^^^^^^
- Dla repozytorium ``sonar-training-examples`` (https://github.com/AstroTech/sonarqube-example-java-maven-junit.git)
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
