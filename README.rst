Developer Tools Ecosystem Workshop
==================================


Install
-------

- Download and install Virtualbox_ == 4.3
- Download and install Vagrant_ == 1.7


Configure
---------

Adjust number of CPUs and RAM for your new host.
Remember that each tool while running takes around 700MB of RAM.
If you have one or two Cores in your laptop, adjust number of Guest OS cores.

Default settings are:

- CPU = 2
- RAM = 8196


Run Host
--------

.. code-block:: bash

    vagrant up


Run Selected Tool
-----------------

.. code-block:: bash

    vagrant ssh -c 'service jira start'
    vagrant ssh -c 'service confluence start'
    vagrant ssh -c 'service stash start'
    vagrant ssh -c 'service jenkins start'
    vagrant ssh -c 'service sonar start'


Ports and services
------------------

+------------+------+------+
| Service    | HTTP | SSH  |
+============+======+======+
| Jira       | 8080 | n/a  |
+------------+------+------+
| Confluence | 8090 | n/a  |
+------------+------+------+
| Stash      | 7990 | 7999 |
+------------+------+------+
| Jenkins    | 8081 | n/a  |
+------------+------+------+
| SonarQube  | 9000 | n/a  |
+------------+------+------+
| PostgreSQL | 5432 | n/a  |
+------------+------+------+

Access
------

You may access your started service at:

    http://localhost:PORT/

Where PORT is an value from table.



.. _Virtualbox: https://www.virtualbox.org/wiki/Downloads
.. _Vagrant: https://www.vagrantup.com/downloads.html

