*******
Install
*******


Versions
========
.. glossary::

    LTS version
        Docker Long Term Support version

    Edge version
        Docker up-to-date (newest) version

macOS
-----
* https://docs.docker.com/docker-for-mac/install/

.. code-block:: console

    $ curl https://get.docker.com |sh

Ubuntu
------
* https://docs.docker.com/engine/getstarted/linux_install_help/

.. code-block:: console
    :caption: Preferred

    $ curl https://get.docker.com |sh

.. code-block:: console
    :caption: Alternative

    $ sudo apt update
    $ sudo apt install docker.io

Linux
-----
* https://docs.docker.com/engine/installation/

.. code-block:: console

    $ curl https://get.docker.com |sh

Windows
-------
* https://docs.docker.com/docker-for-windows/


Logs
====
* Ubuntu (old using `upstart`) - ``/var/log/upstart/docker.log``
* Ubuntu (new using `systemd`) - ``sudo journalctl -fu docker.service``
* Amazon Linux AMI - ``/var/log/docker``
* Boot2Docker - ``/var/log/docker.log``
* Debian GNU/Linux - ``/var/log/daemon.log``
* CentOS - ``/var/log/message | grep docker``
* CoreOS - ``journalctl -u docker.service``
* Fedora - ``journalctl -u docker.service``
* Red Hat Enterprise Linux Server - ``/var/log/messages | grep docker``
* OpenSuSE - ``journalctl -u docker.service``
* OSX - ``~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/log/docker.log``
* Windows - ``Get-EventLog -LogName Application -Source Docker -After (Get-Date).AddMinutes(-5) | Sort-Object Time``


Assignments
===========

Install
-------
#. Zainstaluj ``Docker``
#. Czym różni się ``Docker`` od ``Vagrant``?
