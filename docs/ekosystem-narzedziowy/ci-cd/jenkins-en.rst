Jenkins
=======

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
