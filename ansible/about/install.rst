*******
Install
*******

* https://github.com/ansible/ansible


Requirements
============
* Can be run from any machine with Python 2.7, Python 3.5 or higher
* Windows is not supported for the control node
* Some modules and plugins have additional requirements


Installation
============

PIP
---
* Preferred way

.. code-block:: console

    $ pip3 install ansible

Alpine
------
.. code-block:: console
    :caption: 175MB

    $ apk add --no-cache ansible

.. code-block:: console
    :caption: 337MB

    $ apk add --no-cache python3 python3-dev gcc musl-dev libffi-dev openssl-dev
    $ pip3 --no-cache-dir install ansible

Ubuntu
------
.. code-block:: console
    :caption: Install version provided by Ubuntu (older)

    $ sudo apt install ansible

.. code-block:: console
    :caption: Install version provided by Ansible (newer)

    $ sudo apt update
    $ sudo apt install software-properties-common
    $ sudo apt-add-repository --yes --update ppa:ansible/ansible
    $ sudo apt install ansible

Debian
------
.. code-block:: console

    $ echo 'deb http://ppa.launchpad.net/ansible/ansible/ubuntu jammy main' > /etc/apt/sources.list.d/ansible
    $ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
    $ sudo apt update
    $ sudo apt install ansible


Client Dependencies
===================
* Ansible modules depends on Python 3 installed on machine
* ``raw`` and ``script`` modules do not depend on a client side install of Python to run
* You can use Ansible to install a compatible version of Python using the ``raw`` module, which then allows you to use everything else

.. code-block:: console

    $ ansible localhost --become -m raw -a 'apt install -y python3'
    localhost | CHANGED | rc=0 >>
    Reading package lists...
    Building dependency tree...
    Reading state information...
    python3 is already the newest version (3.10.4-0ubuntu2).
    0 upgraded, 0 newly installed, 0 to remove and 47 not upgraded.

    WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

.. code-block:: console

    $ ansible 127.0.0.1 --become -m raw -a 'apt install -y python3'
    127.0.0.1 | CHANGED | rc=0 >>
    Reading package lists...
    Building dependency tree...
    Reading state information...
    python3 is already the newest version (3.10.4-0ubuntu2).
    0 upgraded, 0 newly installed, 0 to remove and 47 not upgraded.

    WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

.. code-block:: console

    $ cat > hosts << EOF
    [myserver]
    127.0.0.1
    EOF

    $ ansible -i hosts myserver --become -m raw -a 'apt install -y python3'
    $ ansible -i hosts all --become -m raw -a 'apt install -y python3'
