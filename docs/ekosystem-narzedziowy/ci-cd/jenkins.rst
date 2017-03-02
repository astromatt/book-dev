Jenkins
=======

.. todo:: zamienić na osobne pliki
.. todo:: obniżyć poziom nagłówków
.. todo:: Jenkins Multibranch (out-of the box)
.. todo:: Bitbucket Multibranch project (jako dodatkowy plugin)
.. todo:: Niespójność w nazewnictwie Job DSL i Pipeline DSL


`Job DSL`
---------

Podstawy składni `Groovy`
^^^^^^^^^^^^^^^^^^^^^^^^^

:Zmienne:
    .. code-block:: groovy

        String x
        def o

    .. code-block:: groovy

        x = 1
        println x

        x = new java.util.Date()
        println x

        x = -3.1499392
        println x

        x = false
        println x

        x = "Hi"
        println x

        def (a, b, c) = [10, 20, 'foo']

        def nums = [1, 3, 5]
        def a, b, c
        (a, b, c) = nums

:Control structures:

    .. code-block:: groovy

        def x = false
        def y = false

        if ( !x ) {
            x = true
        }

        assert x == true

        if ( x ) {
            x = false
        } else {
            y = true
        }

        assert x == y

    .. code-block:: groovy

        def x = 1.23
        def result = ""

        switch ( x ) {
            case "foo":
                result = "found foo"
                // lets fall through

            case "bar":
                result += "bar"

            case [4, 5, 6, 'inList']:
                result = "list"
                break

            case 12..30:
                result = "range"
                break

            case Integer:
                result = "integer"
                break

            case Number:
                result = "number"
                break

            case ~/fo*/: // toString() representation of x matches the pattern?
                result = "foo regex"
                break

            case { it < 0 }: // or { x < 0 }
                result = "negative"
                break

            default:
                result = "default"
        }

:Funkcje:
    - Optional ``return``

    .. code-block:: groovy

        def jobName = 'example'

        job(jobName) {

        }

:Klasy:

    .. code-block:: groovy

        class Person {
            String name
            int age
            def fetchAge = { age }
        }

        def p = new Person(name:'Jessica', age:42)

    .. code-block:: groovy

        class Person {
            String name
        }

        class Thing {
            String name
        }

        def p = new Person(name: 'Norman')
        def t = new Thing(name: 'Teapot')

    .. code-block:: groovy

        class Person {
            String name
            String toString() { name }
        }
        def sam = new Person(name:'Sam')

        // Create a GString with lazy evaluation of "sam"
        def gs = "Name: ${-> sam}"


:Pętle:
    .. code-block:: groovy

        String message = ''
        for (int i = 0; i < 5; i++) {
            message += 'Hi '
        }
        assert message == 'Hi Hi Hi Hi Hi '

:Zmienne ilości parametrów w finkcjach:
    .. code-block:: groovy

        def concat1 = { String... args -> args.join('') }
        assert concat1('abc','def') == 'abcdef'

        def concat2 = { String[] args -> args.join('') }
        assert concat2('abc', 'def') == 'abcdef'

        def multiConcat = { int n, String... args ->
            args.join('')*n
        }
        assert multiConcat(2, 'abc','def') == 'abcdefabcdef'

:Ciągi zanków:
    .. code-block:: groovy

        def viewspec = '''
        //depot/Tools/build/... //jryan_car/Tools/build/...
        //depot/commonlibraries/utils/... //jryan_car/commonlibraries/utils/...
        //depot/helloworld/... //jryan_car/helloworld/...
        '''

        job('PerforceJob') {
            scm {
                p4(viewspec)
            }
        }

:Zapytania API REST:
    .. code-block:: groovy

        def project = 'Netflix/asgard'
        def branchApi = new URL("https://api.github.com/repos/${project}/branches")
        def branches = new groovy.json.JsonSlurper().parse(branchApi.newReader())

        branches.each {
            def branchName = it.name
            def jobName = "${project}-${branchName}".replaceAll('/','-')

            job(jobName) {
                scm {
                    git("https://github.com/${project}.git", branchName)
                }
            }
        }

:Importy:
    .. code-block:: groovy

        package utilities

        class MyUtilities {
            static void addMyFeature(def job) {
                job.with {
                    description('Arbitrary feature')
                }
            }
        }

    .. code-block:: groovy

        import utilities.MyUtilities

        def myJob = job('example')
        MyUtilities.addMyFeature(myJob)

:Exception:
    .. code-block:: groovy

        try {
            'moo'.toLong()   // this will generate an exception
            assert false     // asserting that this point should never be reached
        } catch ( e ) {
            assert e in NumberFormatException
        }


Podstawy składni `Job DSL`
^^^^^^^^^^^^^^^^^^^^^^^^^^

Jedyne wymagane to nazwa `Job`:

:DSL Methods:
    .. code-block:: groovy

        job('my-job')

:Job:
    .. code-block:: groovy

        job(String name, Closure closure = null)
        freeStyleJob(String name, Closure closure = null)
        buildFlowJob(String name, Closure closure = null)
        ivyJob(String name, Closure closure = null)
        matrixJob(String name, Closure closure = null)
        mavenJob(String name, Closure closure = null)
        multiJob(String name, Closure closure = null)
        workflowJob(String name, Closure closure = null)
        multibranchWorkflowJob(String name, Closure closure = null)

    .. code-block:: groovy

        def myJob = freeStyleJob('SimpleJob')
        myJob.with {
            description 'A Simple Job'
        }

:View:
    .. code-block:: groovy

        listView(String name, Closure closure = null)
        sectionedView(String name, Closure closure = null)
        nestedView(String name, Closure closure = null)
        deliveryPipelineView(String name, Closure closure = null)
        buildPipelineView(String name, Closure closure = null)
        buildMonitorView(String name, Closure closure = null)
        categorizedJobsView(String name, Closure closure = null)

:Folder:
    .. code-block:: groovy

        folder(String name, Closure closure = null)

    .. code-block:: groovy

        folder('project-a')
        freeStyleJob('project-a/compile')
        listView('project-a/pipeline')
        folder('project-a/testing')

:Config:
    .. code-block:: groovy

        configFiles(Closure configFilesClosure = null)

:Queue:
    .. code-block:: groovy

        queue(String jobName)
        queue(Job job)

:Reading from workspace:
    .. code-block:: groovy

        InputStream streamFileFromWorkspace(String filePath)
        String readFileFromWorkspace(String filePath)
        String readFileFromWorkspace(String jobName, String filePath)

    .. code-block:: groovy

        job('example') {
            steps {
                shell(readFileFromWorkspace('build.sh'))
            }
        }

        job('acme-tests') {
            description(readFileFromWorkspace('acme-tests', 'README.txt'))
        }

:Logging:
    .. code-block:: groovy

        out.println('Hello from a Job DSL script!')
        println('Hello from a Job DSL script!')

    .. code-block:: groovy

        import java.util.logging.Logger

        Logger logger = Logger.getLogger('org.example.jobdsl')
        logger.info('Hello from a Job DSL script!')

:Confiugure:
    .. code-block:: groovy

        job('example') {
            ...
            configure { project ->
                project / buildWrappers / EnvInjectPasswordWrapper {
                    injectGlobalPasswords(true)
                }
            }
        }

Przykłady `Job DSL`
^^^^^^^^^^^^^^^^^^^

.. code-block:: groovy

    job('DSL-Tutorial-1-Test') {
        scm {
            git('git://github.com/quidryan/aws-sdk-test.git')
        }
        triggers {
            scm('H/15 * * * *')
        }
        steps {
            maven('-e clean test')
        }
    }

.. code-block:: groovy

    def project = 'quidryan/aws-sdk-test'
    def branchApi = new URL("https://api.github.com/repos/${project}/branches")
    def branches = new groovy.json.JsonSlurper().parse(branchApi.newReader())

    branches.each {
        def branchName = it.name
        def jobName = "${project}-${branchName}".replaceAll('/','-')

        job(jobName) {
            scm {
                git("git://github.com/${project}.git", branchName)
            }
            steps {
                maven("test -Dproject.name=${project}/${branchName}")
            }
        }
    }

.. code-block:: groovy

        def giturl = 'https://github.com/quidryan/aws-sdk-test.git'

        for(i in 0..10) {
            job("DSL-Tutorial-1-Test-${i}") {
                scm {
                    git(giturl)
                }
                steps {
                    maven("test -Dtest.suite=${i}")
                }
            }
        }

``Jenkinsfile``
---------------
- https://jenkins.io/doc/book/pipeline/jenkinsfile/

Example
^^^^^^^
.. code-block:: groovy

    pipeline {
        agent any

        stages {
            stage('Build') {
                steps {
                    echo 'Building..'
                }
            }
            stage('Test') {
                steps {
                    echo 'Testing..'
                }
            }
            stage('Deploy') {
                steps {
                    echo 'Deploying....'
                }
            }
        }
    }

Build
^^^^^
.. code-block:: groovy

    pipeline {
        agent any

        stages {
            stage('Build') {
                steps {
                    sh 'make'
                    archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
                }
            }
        }
    }

Test
^^^^
.. code-block:: groovy

    pipeline {
        agent any

        stages {
            stage('Test') {
                steps {
                    /* `make check` returns non-zero on test failures,
                    * using `true` to allow the Pipeline to continue nonetheless
                    */
                    sh 'make check || true'
                    junit '**/target/*.xml'
                }
            }
        }
    }

Deploy
^^^^^^
.. code-block:: groovy

    pipeline {
        agent any

        stages {
            stage('Deploy') {
                when { currentBuild.result == 'SUCCESS' }
                steps {
                    sh 'make publish'
                }
            }
        }
    }


Advanced syntax
^^^^^^^^^^^^^^^
.. code-block:: groovy

    def username = 'Jenkins'
    echo 'Hello Mr. ${username}'
    echo "I said, Hello Mr. ${username}"

Environment
^^^^^^^^^^^

===========  ============================================
Variable
===========  ============================================
BUILD_ID     The current build ID, identical to BUILD_NUMBER for builds created in Jenkins versions 1.597+
JOB_NAME     Name of the project of this build, such as "foo" or "foo/bar".
JENKINS_URL  Full URL of Jenkins, such as example.com:port/jenkins/ (NOTE: only available if Jenkins URL set in "System Configuration")
===========  ============================================


.. code-block:: groovy

    pipeline {
        agent any
        stages {
            stage('Example') {
                steps {
                    echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                }
            }
        }
    }

.. code-block:: groovy

    pipeline {
        agent any
        environment {
            CC = 'clang'
        }
        stages {
            stage('Example') {
                environment {
                    DEBUG_FLAGS = '-g'
                }
                steps {
                    sh 'printenv'
                }
            }
        }
    }

Parameters
^^^^^^^^^^
.. code-block:: groovy

    pipeline {
        agent any
        parameters {
            string(name: 'Greeting', defaultValue: 'Hello', description: 'How should I greet the world?')
        }
        stages {
            stage('Example') {
                steps {
                    echo "${Greeting} World!"
                }
            }
        }
    }

Handling failures
^^^^^^^^^^^^^^^^^
.. code-block:: groovy

    pipeline {
        agent any
        stages {
            stage('Test') {
                steps {
                    sh 'make check'
                }
            }
        }
        post {
            always {
                junit '**/target/*.xml'
            }
            failure {
                mail to: team@example.com, subject: 'The Pipeline failed :('
            }
        }
    }

Multiple agents
^^^^^^^^^^^^^^^
.. code-block:: groovy

    pipeline {
        agent none
        stages {
            stage('Build') {
                agent any
                steps {
                    checkout scm
                    sh 'make'
                    stash includes: '**/target/*.jar', name: 'app'
                }
            }
            stage('Test on Linux') {
                agent {
                    label 'linux'
                }
                steps {
                    unstash 'app'
                    sh 'make check'
                }
                post {
                    always {
                        junit '**/target/*.xml'
                    }
                }
            }
            stage('Test on Windows') {
                agent {
                    label 'windows'
                }
                steps {
                    unstash 'app'
                    bat 'make check'
                }
                post {
                    always {
                        junit '**/target/*.xml'
                    }
                }
            }
        }
    }

Optional parameters
^^^^^^^^^^^^^^^^^^^

.. code-block:: groovy

    git url: 'git://example.com/amazing-project.git', branch: 'master'
    git([url: 'git://example.com/amazing-project.git', branch: 'master'])

.. code-block:: groovy

    sh 'echo hello' /* short form  */
    sh([script: 'echo hello'])  /* long form */

Advanced usage
^^^^^^^^^^^^^^
.. code-block:: groovy

    stage('Build') {
        /* .. snip .. */
    }

    stage('Test') {
        parallel linux: {
            node('linux') {
                checkout scm
                try {
                    unstash 'app'
                    sh 'make check'
                }
                finally {
                    junit '**/target/*.xml'
                }
            }
        },
        windows: {
            node('windows') {
                /* .. snip .. */
            }
        }
    }

Ćwiczenia
---------

Instalacja Jenkinsa i konfuguracja buildów
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Zainstaluj `Jenkins` za pomocą paczek `DEB` przez ``apt-get``
- Alternatywnie możesz użyć `Docker` albo manifestów `Puppeta`
- Czy wcześniej zainstalowałeś `Bitbucket Server`?

    - Nie - Zaciągnij repozytorium https://github.com/SonarSource/sonar-examples.git
    - Tak - Zaciągnij repozytorium ``sonar-examples`` z twojej instancji `Bitbucket Server`

- Zacznij budować różne projekty ``sonar-examples/projects/languages/java``:

    - `ut` - unit tests
    - `it` - integration tests

- Ustaw joby przez `Jenkinsa`

.. tip:: Bitubcket plugin do Jenkinsa

.. toggle-code-block:: sh
    :label: Pokaż rozwiązanie za pomocą ``apt-get`` na `Ubuntu`

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

.. toggle-code-block:: sh
    :label: Pokaż rozwiązanie za pomocą ``docker`` na `Ubuntu`

.. code-block:: sh

    docker pull jenkins
    docker run -p 8080:8080 -p 50000:50000 -v /tmp/jenkins_home_on_host:/var/jenkins_home jenkins

.. warning:: Sprawdź, czy w swoim pliku ``Vagrantfile`` masz skonfigurowany forwardnig portów dla guest:``8080`` -> host:``80``


Budowanie Pull Requestów
^^^^^^^^^^^^^^^^^^^^^^^^
- Skonfiguruj ręcznie plan by budował gałęzie `GIT Flow`:

    - `Pull Requests`
    - ``feature``
    - ``bugfix``
    - ``master``

- Spróbuj wykorzystać któryś z dostępnych pluginów:

    - https://plugins.jenkins.io/bitbucket-build-status-notifier
    - https://plugins.jenkins.io/stashNotifier

.. toggle-code-block:: rst
    :label: Pokaż konfigurację dla Bitbucket Server

    =============== ======================
    Key             Value
    =============== ======================
    Stash Root URL  http://localhost:7990/
    Stash User      jenkins
    Stash Password  jenkins
    =============== ======================


.. toggle-code-block:: rst
    :label: Pokaż rozwiązanie dla Pull Requestów

    Dashboard -> New Item -> "Freestyle project"

    ======================== ======================== =======================================================
    Section                   Key                      Value
    ======================== ======================== =======================================================
                             Project name             Pull Request
    Source Code Management   Source Code Management   GIT
    Source Code Management   Repository URL           ssh://git@localhost:7999/eco/workshop.git
    Source Code Management   Credentials              jenkins
    Source Code Management   [Advanced] -> Refspec    +refs/pull-requests/*/from:refs/remotes/origin/pr/*
    Source Code Management   Branch Specifier         **/pr/*
    Build Triggers           Schedule                 * * * * *
    Post-build Actions       Notify Stash Instance
    ======================== ======================== =======================================================


.. toggle-code-block:: rst
    :label: Pokaż rozwiązanie dla brancha ``master``

    Dashboard -> New Item -> "Freestyle project"

    ======================== ======================== =============================================
    Section                  Key                      Value
    ======================== ======================== =============================================
                             Project name             Master
    Source Code Management   Source Code Management   GIT
    Source Code Management   Repository URL           ssh://git@localhost:7999/eco/workshop.git
    Source Code Management   Credentials              jenkins
    Source Code Management   Branch Specifier         **/master
    Build Triggers           Schedule                 * * * * *
    Post-build Actions       Notify Stash Instance
    ======================== ======================== =============================================


.. toggle-code-block:: rst
    :label: Pokaż rozwiązanie dla brancha ``feature``

    Dashboard -> New Item -> "Freestyle project"

    ======================== ======================== =============================================
    Section                  Key                      Value
    ======================== ======================== =============================================
                             Project name             Feature
    Source Code Management   Source Code Management   GIT
    Source Code Management   Repository URL           ssh://git@localhost:7999/eco/workshop.git
    Source Code Management   Credentials              jenkins
    Source Code Management   Branch Specifier         */feature/*
    Build Triggers           Schedule                 * * * * *
    Post-build Actions       Notify Stash Instance
    ======================== ======================== =============================================


.. toggle-code-block:: rst
    :label: Pokaż rozwiązanie dla brancha ``bugfix``

    Dashboard -> New Item -> "Freestyle project"

    ======================== ======================== =============================================
    Section                  Key                      Value
    ======================== ======================== =============================================
                             Project name             Feature
    Source Code Management   Source Code Management   GIT
    Source Code Management   Repository URL           ssh://git@localhost:7999/eco/workshop.git
    Source Code Management   Credentials              jenkins
    Source Code Management   Branch Specifier         */bugfix/*
    Build Triggers           Schedule                 * * * * *
    Post-build Actions       Notify Stash Instance
    ======================== ======================== =============================================

.. toggle-code-block:: rst
    :label: Pokaż plugin, który to zrobi za Ciebie

    - https://plugins.jenkins.io/stash-pullrequest-builder

Budowanie `Checkstyle`, `PMD`, `JaCoCo`, `Findbugs` i `PITest`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Dla repozytorium ``sonar-examples``
- Zacznij budować różne projekty ``sonar-examples/projects/languages/java``
- Wyniki upublicznij w `SonarQube`
- Do instalacji możesz wykorzystać ``puppet module install maestrodev/sonarqube``
- Dodaj w ``pom.xml`` zależność ``pitest`` i przetestuj projekt wykorzystując domyślne mutatory

`Job DSL`
^^^^^^^^^
- Przepisz całą konfigurację wykorzustując plik ``Job DSL`

`Jenkins Docker Plugin`
^^^^^^^^^^^^^^^^^^^^^^^
- Zainstaluj `Docker Plugin` w `Jenkins`
- Skonfiguruj zadanie aby uruchamiało kontener
- Zadanie ma provisionować konfigurację wewnątrz kontenera
- Zadanie ma uruchamiać build wewnątrz kontenera
- Zadanie ma niszczyć kontener po buildze

`Jenkins` i testy wydajnościowe `JMeter`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
