Developer Tools Ecosystem Workshop
==================================


Clone the Repository with Submodules
------------------------------------

.. code-block:: bash

    git clone --recursive https://github.com/MattAgile/ecosystem-workshop.git


Install Dependencies
--------------------

- Download and install Virtualbox_ >= 4.3
- Download and install Vagrant_ >= 1.7

.. _Virtualbox: https://www.virtualbox.org/wiki/Downloads
.. _Vagrant: https://www.vagrantup.com/downloads.html


Configure Guest Environment
---------------------------

Edit :code:`Vagrantfile`.

Adjust number of CPUs and RAM for your new host.
Remember that each tool while running takes around 700MB of RAM.
If you have one or two Cores in your laptop, adjust number of Guest OS cores.

Default settings are:

- CPU = 2
- RAM = 8196


Run Guest
---------

At the workshop you'll receive an Developer Tools Ecosystem already set-up and configured!
All you need is cloned git repository and ecosystem.box image in root folder (./ecosystem-workshop), 
and open those ports:
	- 7990 (Stash)
	- 7999 (SSH Stash)
	- 8080 (Jira)
	- 8081 (Jenkins)
	- 8090 (Confluence)
	- 9000 (SonarQube)
	- 5432 (PostgreSQL)
Otherwise you will not be able to run Guest Ecosystem.
Then to run this you have to simply type:

.. code-block:: bash

    vagrant up

If you want to setup your own ecosystem from scratch, read the following instructions in :code:`docs/how-to-setup-new-box.rst` file.


Run Selected Tool
-----------------

If you set small amount of RAM, your machine might be killed.
Remember that each tool while running takes around 700MB of RAM.
Please run only one/two selected services for small RAM sizes.
8196 MB RAM should be enough to handle load for each of this machines run simultaneously.

.. code-block:: bash

    vagrant ssh -c 'sudo service confluence start'
    vagrant ssh -c 'sudo service jenkins start'
    vagrant ssh -c 'sudo service jira start'
    vagrant ssh -c 'sudo service sonar start'
    vagrant ssh -c 'sudo service stash start'

If you have a Windows operating system you might not have SSH installed.
Go ahead and download Putty_ and then connect to:

- host: :code:`127.0.0.1`
- port: :code:`2222`
- username: :code:`vagrant`
- password: :code:`vagrant`

First thing you do after connecting to the new host might be to switch to the root:

.. code-block:: bash

    sudo su -

Then you do not need to run commands with :code:`sudo` prefix.
To run services type one of the following:

.. code-block:: bash

    service confluence start
    service jenkins start
    service jira start
    service sonar start
    service stash start

.. _Putty: http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe


Ports and Services
------------------

+------------+------+------+
| Service    | HTTP | SSH  |
+============+======+======+
| Confluence | 8090 | n/a  |
+------------+------+------+
| Jenkins    | 8081 | n/a  |
+------------+------+------+
| Jira       | 8080 | n/a  |
+------------+------+------+
| SonarQube  | 9000 | n/a  |
+------------+------+------+
| Stash      | 7990 | 7999 |
+------------+------+------+
| PostgreSQL | 5432 | n/a  |
+------------+------+------+


Access
------

You may access your started service at:

    http://localhost:PORT/

Where PORT is an value from table.


Stop Service
------------

When you do not need the service anymore you may kill the instance to save some RAM for other tools.

.. code-block:: bash

    vagrant ssh -c 'service confluence stop'
    vagrant ssh -c 'service jenkins stop'
    vagrant ssh -c 'service jira stop'
    vagrant ssh -c 'service sonar stop'
    vagrant ssh -c 'service stash stop'


Stop Guest Machine
------------------

This will preserve state of the machine.

.. code-block:: bash

    vagrant halt

This will destroy the machine and free some space from your hard drive.

.. code-block:: bash

    vagrant destroy

