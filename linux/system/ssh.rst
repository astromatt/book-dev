SSH
===


Generate Key
------------
* ``ssh-keygen``
* Add comment
- ``~/.id_rsa``
- ``~/.id_rsa.pub``


Connect
-------
* ``ssh -i myprivatekey.pem -l myuser myhost``


Authorized Keys
---------------
* Comments


Known Hosts
-----------


Port Forwarding
---------------
* Reverse Tunnel
* ``-L``
* ``-R``


Config and Host Aliases
-----------------------
* ``~/.ssh/config``

.. code-block:: text

    Host myhost1
        HostName 10.13.37.1
        Port 22
        User myuser

    Host myhost2
        HostName 10.13.37.2
        Port 22
        User myuser
        LocalForward 3000 127.0.0.1:3000
        LocalForward 8083 127.0.0.1:8083
        LocalForward 8084 127.0.0.1:8084
        IdentityFile ~/.id_rsa

    Host *
        ServerAliveInterval 30
        ServerAliveCountMax 2


SSHd
----
* Disabling password authentication
* ``/etc/ssh/sshd_config``
* ``sudo service sshd restart``
