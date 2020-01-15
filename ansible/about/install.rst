*******
Install
*******

* https://github.com/ansible/ansible

Requirements
============
* Currently Ansible can be run from any machine with Python 2 (version 2.7) or Python 3 (versions 3.5 and higher) installed.
* Windows is not supported for the control node.
* Please note that some modules and plugins have additional requirements.
* Ansible’s raw module, and the script module, do not depend on a client side install of Python to run.
* You can use Ansible to install a compatible version of Python using the raw module, which then allows you to use everything else.

.. code-block:: console

    $ ansible myhost --become -m raw -a "apt install -y python3"


PIP
===
* Preferred way

.. code-block:: console

    $ pip3 install ansible

Alpine
======
.. code-block:: console

    $ apk add python3 python3-dev gcc musl-dev libffi-dev openssl-dev
    $ pip3 install ansible

Ubuntu
======
.. code-block:: console
    :caption: Install older version (provided by Ubuntu)

    $ apt install ansible

.. code-block:: console
    :caption: Install current version (provided by Ansible)

    $ sudo apt update
    $ sudo apt install software-properties-common
    $ sudo apt-add-repository --yes --update ppa:ansible/ansible
    $ sudo apt install ansible


Debian
======
Add the following line to /etc/apt/sources.list:

.. code-block:: text

    deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main

Then run these commands:

.. code-block:: console

    $ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
    $ sudo apt update
    $ sudo apt install ansible

