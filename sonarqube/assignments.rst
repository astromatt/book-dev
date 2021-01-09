***********
Assignments
***********



Jenkins
=======
#. Repository ``https://github.com/AstroTech/ecosystem-example-java``
#. Run SonarScanner analysis in Jenkins
#. Use official Docker images:

    * Jenkins ``jenkins/jenkins:alpine``
    * SonarQube: ``sonarqube:latest``
    * SonarScanner: ``sonarsource/sonar-scanner-cli:latest``

:Solution:
    * Dockerfile :download:`_solution/Dockerfile`
    * Sonar-Project.properties :download:`_solution/sonar-project.properties`
    * Jenkinsfile (inline) :download:`_solution/Jenkinsfile.inline`
    * Jenkinsfile (env) :download:`_solution/Dockerfile`


Pitest
======
#. Repository ``https://github.com/AstroTech/ecosystem-example-java``
#. Install ``openjdk-8-jdk`` and ``maven``
#. Set Java 8 as default ``update-alternatives --config java``
#. Add ``jUnit`` as a project dependency in ``pom.xml``
#. Install Pitest as a plugin in ``pom.xml``

.. code-block:: xml

    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.13</version>
        <scope>test</scope>
    </dependency>

.. code-block:: xml

    <plugin>
        <groupId>org.pitest</groupId>
        <artifactId>pitest-maven</artifactId>
        <version>1.5.2</version>
     </plugin>

.. code-block:: sh

    mvn compile

    # Unit Tests
    mvn test

    # Integration tests
    mvn verify

    # Mutation Tests
    mvn org.pitest:pitest-maven:mutationCoverage
