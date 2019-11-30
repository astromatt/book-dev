**************
Installing MVN
**************

.. code-block:: console

    $ docker container exec -u 0 -it jenkins bash

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
