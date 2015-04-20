How to setup a new box
======================

At the workshop you'll receive an Developer Tools Ecosystem already set-up and configured!
Then to run this you have to simply type:

.. code-block:: bash

    vagrant up

If you want to setup your own ecosystem from scratch, read and execute the following instructions.


Create and Setup the Environment
--------------------------------

.. code-block:: bash

    sudo su -
    apt-get update
    apt-get install --yes git vim nmap htop wget curl unzip maven openjdk-7-jdk

    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale
    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    locale-gen en_US.UTF-8
    dpkg-reconfigure locales


Install VirtualBox Guest Additions
----------------------------------

.. code-block:: bash

    apt-get install linux-headers-generic build-essential dkms
    wget http://dlc-cdn.sun.com/virtualbox/4.3.26/VBoxGuestAdditions_4.3.26.iso
    mkdir /media/VBoxGuestAdditions
    mount -o loop,ro VBoxGuestAdditions_4.3.26.iso /media/VBoxGuestAdditions
    sh /media/VBoxGuestAdditions/VBoxLinuxAdditions.run
    rm VBoxGuestAdditions_4.3.26.iso
    umount /media/VBoxGuestAdditions
    rmdir /media/VBoxGuestAdditions


Install and Setup Database
--------------------------

.. code-block:: bash

    apt-get install --yes postgresql-9.3
    su postgres -
    psql

.. code-block:: sql

    CREATE USER confluence WITH PASSWORD 'confluence';
    CREATE DATABASE confluence;
    GRANT ALL PRIVILEGES ON DATABASE confluence TO confluence;
    CREATE USER jira WITH PASSWORD 'jira';
    CREATE DATABASE jira;
    GRANT ALL PRIVILEGES ON DATABASE jira TO jira;
    CREATE USER sonar WITH PASSWORD 'sonar';
    CREATE DATABASE sonar;
    GRANT ALL PRIVILEGES ON DATABASE stash TO sonar;
    CREATE USER stash WITH PASSWORD 'stash';
    CREATE DATABASE stash;
    GRANT ALL PRIVILEGES ON DATABASE stash TO stash;


Install Jira
-------------

.. code-block:: bash

    wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-6.4.2-x64.bin
    chmod +x atlassian-jira-6.4.2-x64.bin
    ./atlassian-jira-6.4.2-x64.bin
    rm -fr atlassian-jira-6.4.2-x64.bin


Install Confluence
------------------

.. code-block:: bash

    wget https://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-5.7.3-x64.bin
    chmod +x atlassian-confluence-5.7.3-x64.bin
    ./atlassian-confluence-5.7.3-x64.bin
    rm -fr atlassian-confluence-5.7.3-x64.bin


Install Stash
-------------

.. code-block:: bash

    wget https://www.atlassian.com/software/stash/downloads/binary/atlassian-stash-3.8.0-x64.bin
    chmod +x atlassian-stash-3.8.0-x64.bin
    ./atlassian-stash-3.8.0-x64.bin
    rm -fr atlassian-stash-3.8.0-x64.bin


Install Jenkins
---------------

.. code-block:: bash

    wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
    echo "deb http://pkg.jenkins-ci.org/debian binary/" >> /etc/apt/sources.list
    apt-get update
    apt-get install --yes jenkins
    sudo su - jenkins
    ssh-keygen
    cat ~/.ssh/id_rsa.pub
    exit
    service jenkins stop
    sed -i 's/HTTP_PORT=8080/HTTP_PORT=8081/g' /etc/default/jenkins
    service jenkins start


Install SonarQube
-----------------

.. code-block:: bash

    echo "deb http://downloads.sourceforge.net/project/sonar-pkg/deb binary/" >> /etc/apt/sources.list
    apt-get update
    apt-get install --yes sonar
    service sonar stop
    sed -i 's(#sonar.jdbc.url=jdbc:postgresql(sonar.jdbc.url=jdbc:postgresql(g' /opt/sonar/conf/sonar.properties
    sed -i 's(sonar.jdbc.url=jdbc:h2(#sonar.jdbc.url=jdbc:h2(g' /opt/sonar/conf/sonar.properties
    sed -i 's(#sonar.jdbc.username=sonar(sonar.jdbc.username=sonar(g' /opt/sonar/conf/sonar.properties
    sed -i 's(#sonar.jdbc.password=sonar(sonar.jdbc.password=sonar(g' /opt/sonar/conf/sonar.properties
    service sonar start


Create Box
----------

.. code-block:: bash

    vagrant package --base ecosystem.local --output ecosystem.box

