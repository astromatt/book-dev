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

    $ apt install ansible

.. code-block:: console
    :caption: Install version provided by Ansible (newer)

    $ apt update
    $ apt install software-properties-common
    $ apt-add-repository --yes --update ppa:ansible/ansible
    $ apt install ansible

Debian
------
.. code-block:: console

    $ echo 'deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main' > /etc/apt/sources.list.d/ansible
    $ apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
    $ apt update
    $ apt install ansible


Client Dependencies
===================
* Ansible modules depends on Python 3 installed on machine
* Ansible’s raw module, and the script module, do not depend on a client side install of Python to run
* You can use Ansible to install a compatible version of Python using the raw module, which then allows you to use everything else

.. code-block:: console

    $ ansible myhost --become -m raw -a 'apt install -y python3'
