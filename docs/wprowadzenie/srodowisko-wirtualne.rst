Środowisko wirtualne
====================

Korzystanie ze środowiska
-------------------------

Clone the Repository with Submodules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

    git clone --recursive https://github.com/AstroTech/workshop-devops.git

Configure Guest Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Edit ``Vagrantfile`` and adjust number of CPUs and RAM for your new host.
Remember that each tool while running takes around 700MB of RAM.
If you have one or two Cores in your laptop, adjust number of Guest OS cores.

Default settings are::

    CPU = 2
    RAM = 8196

Test your configuration and run

At the workshop you'll receive an Developer Tools Ecosystem already set-up and configured!
All you need is cloned git repository and ``ecosystem.box`` image in root folder (``./ecosystem-workshop``).
Otherwise you can set up your own ecosystem-workshop.

For that check documentation in ``./setup`` folder and follow those instructions for each service you want to install.

Be sure that no services on the host machine is running on those ports:

==== =============
Port Service
==== =============
8088
8443
7990 Bitbucket
7999 SSH Bitbucket
8080 Jira
8081 Jenkins
8090 Confluence
9000 SonarQube
5432 PostgreSQL
3306 MySQL
==== =============

Otherwise you will not be able to run Guest Ecosystem or you have to change ``Vagrantfile``.

Then to run this you have to simply type:

    vagrant up

Warning: if you see warning message like this: ``Warning: Authentication failure. Retrying...`` exit the process(``ctrl+c`` on `Linux/Windows` or `cmd+c` on `OS X`) and start `ssh` connection by:

.. code-block:: sh

    vagrant ssh

If you want to setup your own ecosystem from scratch, read the following instructions in ``setup/_how-to-setup-new-box.md`` file.

Run Selected Tool
^^^^^^^^^^^^^^^^^

If you set small amount of RAM, your machine might be killed.
Remember that each tool while running takes around ``700 MB`` of RAM.
Please run only one/two selected services for small RAM sizes.
``8196 MB RAM`` should be enough to handle load for each of this machines run simultaneously.

.. code-block:: sh

    vagrant ssh -c 'sudo service confluence start'
    vagrant ssh -c 'sudo service jenkins start'
    vagrant ssh -c 'sudo service jira start'
    vagrant ssh -c 'sudo service sonar start'
    vagrant ssh -c 'sudo service stash start'

If you have a `Windows` operating system you might not have ``ssh`` installed.
Go ahead and download http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe and then connect to:

- host: ``127.0.0.1``
- port: ``2222``
- username: ``vagrant``
- password: ``vagrant``

First thing you do after connecting to the new host might be to switch to the ``root``:

.. code-block:: sh

    sudo su -

Then you do not need to run commands with ``sudo`` prefix.
To run services type one of the following:

.. code-block:: sh

    service confluence start
    service jenkins start
    service jira start
    service sonar start
    service stash start

Ports and Services
^^^^^^^^^^^^^^^^^^

============== ========= ====
Service        HTTP      SSH
============== ========= ====
Confluence     8090      n/a
Jenkins        8081      n/a
Jira           8080      n/a
SonarQube      9000      n/a
Stash          7990      7999
PostgreSQL     5432      n/a
============== ========= ====

Access
^^^^^^

You may access your started service at:

    http://localhost:PORT/

Where PORT is an value from table.

Stop Service
^^^^^^^^^^^^

When you do not need the service anymore you may kill the instance to save some RAM for other tools.

.. code-block:: sh

    vagrant ssh -c 'service confluence stop'
    vagrant ssh -c 'service jenkins stop'
    vagrant ssh -c 'service jira stop'
    vagrant ssh -c 'service sonar stop'
    vagrant ssh -c 'service stash stop'

Be patient, service should start in around 60 sek. (per service)

Stop Guest Machine
^^^^^^^^^^^^^^^^^^

This will preserve state of the machine.

.. code-block:: sh

    vagrant halt

This will destroy the machine and free some space from your hard drive.

.. code-block:: sh

    vagrant destroy


How to setup a new box
----------------------

.. warning:: If you are using Linux and provided pendrive cannot be mounted on your system, install exfat-fuse and exfat-util by typing in your console:

.. code-block:: sh

    sudo apt-get install exfat-fuse exfat-utils

At the workshop you'll receive an Developer Tools Ecosystem already set-up and configured!
Then to run this you have to simply type:

.. code-block:: sh

    vagrant up

If you want to setup your own ecosystem from scratch, read and execute the following instructions.


Create and Setup the Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

    sudo su -
    apt-get update
    apt-get install --yes git vim nmap htop wget curl unzip maven openjdk-7-jdk

    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale
    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    locale-gen en_US.UTF-8
    dpkg-reconfigure locales

Install VirtualBox Guest Additions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

    apt-get install linux-headers-generic build-essential dkms
    wget http://dlc-cdn.sun.com/virtualbox/4.3.26/VBoxGuestAdditions_4.3.26.iso
    mkdir /media/VBoxGuestAdditions
    mount -o loop,ro VBoxGuestAdditions_4.3.26.iso /media/VBoxGuestAdditions
    sh /media/VBoxGuestAdditions/VBoxLinuxAdditions.run
    rm VBoxGuestAdditions_4.3.26.iso
    umount /media/VBoxGuestAdditions
    rmdir /media/VBoxGuestAdditions

Install and Setup Database For All Tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

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


Create New Box
^^^^^^^^^^^^^^

.. code-block:: sh

    vagrant package --base ecosystem.local --output ecosystem.box
