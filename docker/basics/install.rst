Docker Install
==============

Versions
--------
.. glossary::

    Rootfull
        Docker daemon is running with root privileges

    Rootless
        Docker daemon is running with user privileges

    LTS version
        Docker Long Term Support version

    Edge version
        Docker up-to-date (newest) version


Rootfull
--------
.. code-block:: console

    $ curl https://get.docker.com |sudo sh
    $ sudo usermod -aG docker $(whoami)
    $ logout


Rootless
--------
* https://docs.docker.com/engine/security/rootless/

.. code-block:: console

    $ sudo apt update
    $ sudo apt install -y uidmap
    $ curl https://get.docker.com/rootless |sh
    $ echo 'export PATH=/home/ubuntu/bin:$PATH' >> ~/.bashrc
    $ echo 'export DOCKER_HOST=unix:///run/user/1000/docker.sock' >> ~/.bashrc
    $ echo 'net.ipv4.ping_group_range = 0 2147483647' |sudo tee --append /etc/sysctl.conf
    $ sudo sysctl --system
    $ logout


Further Reading
---------------
* macOS: https://docs.docker.com/docker-for-mac/install/
* Ubuntu: https://docs.docker.com/engine/getstarted/linux_install_help/
* Linux: https://docs.docker.com/engine/installation/
* Windows: https://docs.docker.com/docker-for-windows/


Assignments
-----------
#. Zainstaluj ``Docker``
#. Czym różni się ``Docker`` od ``Vagrant``?
