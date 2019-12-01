****
Java
****

* Java https://jenkins.io/solutions/java/

SonarScanner
============
* ``sonar.properties`` in your repository main folder

.. code-block:: properties
    :caption: Minimal Sonar Project Properties

    sonar.projectKey=MyProject
    sonar.projectName=MyProject
    sonar.projectVersion=1.0

    sonar.sources=src/main/java
    sonar.java.binaries=target/classes
    sonar.java.source=9


Maven
=====
.. code-block:: console

    $ docker container exec -u 0 -it jenkins sh

.. code-block:: console

    $ mkdir -p /opt
    $ cd /opt
    $ wget http://apache.claz.org/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.tar.gz
    $ tar -zxvf apache-maven-3.5.4-bin.tar.gz
    $ mv apache-maven-3.5.4 /opt/maven
    $ ln -s /opt/maven/bin/mvn /usr/local/bin/mvn

.. code-block:: console

    $ echo 'export M2_HOME=/opt/maven' > /etc/profile.d/maven.sh

Now load the environment variables in the current shell using the following command.

.. code-block:: console

    $ source /etc/profile.d/maven.sh


Assignments
===========

Build Maven Repo
----------------
#. Use Blue Ocean
#. Fork repository https://github.com/AstroTech/ecosystem-example-java.git
#. Use fork for building
#. Use Pipeline editor to build maven with steps:

    #. ``mvn compile``
    #. ``mvn test``
