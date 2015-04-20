How to setup a new box
======================

.. code-block:: bash

    sudo su -
    apt-get update
    apt-get install --yes git vim nmap htop wget curl unzip maven openjdk-7-jdk

    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale
    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    locale-gen en_US.UTF-8
    dpkg-reconfigure locales

    apt-get install linux-headers-generic build-essential dkms
    wget http://dlc-cdn.sun.com/virtualbox/4.3.26/VBoxGuestAdditions_4.3.26.iso
    mkdir /media/VBoxGuestAdditions
    mount -o loop,ro VBoxGuestAdditions_4.3.26.iso /media/VBoxGuestAdditions
    sh /media/VBoxGuestAdditions/VBoxLinuxAdditions.run
    rm VBoxGuestAdditions_4.3.26.iso
    umount /media/VBoxGuestAdditions
    rmdir /media/VBoxGuestAdditions

    su postgres -
    psql
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

    wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-6.4.2-x64.bin
    chmod +x atlassian-jira-6.4.2-x64.bin
    ./atlassian-jira-6.4.2-x64.bin

    wget https://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-5.7.3-x64.bin
    chmod +x atlassian-confluence-5.7.3-x64.bin
    ./atlassian-confluence-5.7.3-x64.bin

    wget https://www.atlassian.com/software/stash/downloads/binary/atlassian-stash-3.8.0-x64.bin
    chmod +x atlassian-stash-3.8.0-x64.bin
    ./atlassian-stash-3.8.0-x64.bin

    rm -fr atlassian-jira-6.4.2-x64.bin
    rm -fr atlassian-stash-3.8.0-x64.bin
    rm -fr atlassian-confluence-5.7.3-x64.bin

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

    vagrant package --base ecosystem.local --output ecosystem.box

