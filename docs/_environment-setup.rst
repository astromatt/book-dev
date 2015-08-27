Environment Access
==================


Server Access
-------------

  .. code-block: bash

    ssh -i workshop.pem -l ubuntu HOST_IP_ADDRESS

Environment Setup
-----------------

.. code-block: bash

    apt-get install --yes git vim nmap htop wget curl unzip

Locale
------

.. code-block: bash

    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale
    echo 'LANG="en_US.UTF-8"' >> /etc/default/locale
    locale-gen en_US.UTF-8
    dpkg-reconfigure locales

TODO
----

* Enable password login in /etc/ssh/sshd_config (easy for windows users with putty)

.. code-block: bash

    sudo passwd ubuntu

