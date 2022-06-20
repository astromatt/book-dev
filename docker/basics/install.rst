*******
Install
*******


Versions
========
* macOS: https://docs.docker.com/docker-for-mac/install/
* Ubuntu: https://docs.docker.com/engine/getstarted/linux_install_help/
* Linux: https://docs.docker.com/engine/installation/
* Windows: https://docs.docker.com/docker-for-windows/

.. glossary::

    LTS version
        Docker Long Term Support version

    Edge version
        Docker up-to-date (newest) version

    Rootfull
        Docker daemon is running with root privileges

    Rootless
        Docker daemon is running with user privileges


Rootfull
--------
.. code-block:: console

    $ curl https://get.docker.com |sudo sh
    $ sudo usermod -aG docker $(whoami)
    $ logout


Rootless
--------
.. code-block:: console

    $ sudo apt update
    $ sudo apt install -y uidmap
    $ curl https://get.docker.com/rootless |sh
    $ echo 'export PATH=/home/ubuntu/bin:$PATH' >> ~/.bashrc
    $ echo 'export DOCKER_HOST=unix:///run/user/1000/docker.sock' >> ~/.bashrc
    $ echo 'net.ipv4.ping_group_range = 0 2147483647' |sudo tee --append /etc/sysctl.conf
    $ sudo sysctl --system
    $ logout


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
