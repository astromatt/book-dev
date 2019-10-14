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


Install docker from terminal
============================

Preferred
---------

Alternative
-----------


Requirements for workshop
=========================
.. code-block:: console

    $ docker pull python:3.7 \
        && docker pull postgres \
        && docker pull ubuntu \
        && docker pull bash
