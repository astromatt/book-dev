Users and groups
================
* ``UID``
* ``GID``
* ``GECOS``


Paths
-----
* ``/etc/passwd``
* ``/etc/shadow``
* ``/etc/group``
* ``/etc/skel``


Etc Passwd
----------
* File ``/etc/passwd``

Structure:

    * Username
    * Password: ``x`` indicates that shadow passwords are used
    * UID: User ID number
    * GID: User's group ID number
    * GECOS: Full name of the user
    * Home directory
    * Login shell

.. code-block:: text

    root:x:0:0:root:/root:/bin/bash
    bin:x:1:1:bin:/bin:/sbin/nologin
    daemon:x:2:2:daemon:/sbin:/sbin/nologin
    adm:x:3:4:adm:/var/adm:/sbin/nologin
    shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
    halt:x:7:0:halt:/sbin:/sbin/halt
    nobody:x:99:99:Nobody:/:/sbin/nologin
    sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
    watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
    lewis:x:1001:1001:Melissa Lewis:/home/lewis:/bin/bash
    martinez:x:1002:1002:Rick Martinez:/home/martinez:/bin/bash


Etc Shadow
----------
* File ``/etc/shadow``

Structure:

    * Username: from ``/etc/passwd``
    * Password
    * Last Password Change: Days since 1970-01-01
    * Minimum days between password changes: 0 - changed at any time
    * Password validity: Days after which password must be changed, 99999 - many, many years
    * Warning threshold: Days to warn user of an expiring password, 7 - full week
    * Account inactive: Days after password expires and account is disabled
    * Time since account is disabled: Days since 1970-01-01
    * A reserved field for possible future use

Password field (split by ``$``):

    * algorithm
    * salt
    * password hash

Password algorithms:

    * ``1`` - MD5
    * ``2a`` - Blowfish
    * ``2y`` - Blowfish
    * ``5`` - SHA-256
    * ``6`` - SHA-512

Password special chars:

    * `` `` (blank entry) - password is not required to log in
    * ``*`` (asterisk) - account is disabled, cannot be unlocked, no password has ever been set
    * ``!`` (exclamation mark) - account is locked, can be unlocked, no password has ever been set
    * ``!<password_hash>`` - account is locked, can be unlocked, but password is set
    * ``!!`` (two exclamation marks) - account created, waiting for initial password to be set by admin

.. code-block:: text

    root:$6$Ke02nYgo.9v0SF4p$hjztYvo/M4buqO4oBX8KZTftjCn6fE4cV5o/I95QPekeQpITwFTRbDUBYBLIUx2mhorQoj9bLN8v.w6btE9xy1:16431:0:99999:7:::
    adm:$6$5H0QpwprRiJQR19Y$bXGOh7dIfOWpUb/Tuqr7yQVCqL3UkrJns9.7msfvMg4ZO/PsFC5Tbt32PXAw9qRFEBs1254aLimFeNM8YsYOv.:16431:0:99999:7:::
    watney:!!:16550::::::
    lewis:$6$P9zn0KwR$tgfvvFWJJ5FKmoXiP5rXWOjwoEBOEoAuBi3EphRbJqqjWYvhEM2wa67L9XgQ7W591FxUNklkDIQsk4kijuhE50:16632:0:99999:7:::
    martinez:$1$.QKDPc5E$SWlkjRWexrXYgc98F.:12825:0:90:5:30:13096:


Etc Group
---------
* File ``/etc/group``

Structure:

    * Group Name: from ``/etc/passwd``
    * Group Password: ``x`` indicates that shadow passwords are used)
    * GID: Group ID
    * Members: usernames from ``/etc/passwd``

.. code-block:: text

    root::0:root
    other::1:
    bin::2:root,bin,daemon
    sys::3:root,bin,sys,adm
    adm::4:root,adm,daemon
    mail::6:root
    astronauts::10:watney,lewis,martinez
    daemon::12:root,daemon
    sysadmin::14:martinez,lewis
    mars::1000:watney
    moon::1001:lewis
    nobody::60001:
    noaccess::60002:
    nogroup::65534:


useradd vs. adduser
-------------------


Commands
--------
.. csv-table:: User, Password and Groups
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``addgroup``,   "(8)",  "add a user or group to the system"
    ``adduser``,    "(8)",  "add a user or group to the system"
    ``chgpasswd``,  "(8)",  "update group passwords in batch mode"
    ``chpasswd``,   "(8)",  "update passwords in batch mode"
    ``delgroup``,   "(8)",  "remove a user or group from the system"
    ``deluser``,    "(8)",  "remove a user or group from the system"
    ``groupadd``,   "(8)",  "create a new group"
    ``groupdel``,   "(8)",  "delete a group"
    ``groupmod``,   "(8)",  "modify a group definition on the system"
    ``groups``,     "(1)",  "print the groups a user is in"
    ``id``,         "(1)",  "print real and effective user and group IDs"
    ``last``,       "(1)",  "show a listing of last logged in users"
    ``login``,      "(1)",  "begin session on the system"
    ``login``,      "(3)",  "write utmp and wtmp entries"
    ``logname``,    "(1)",  "print user's login name"
    ``logout``,     "(3)",  "write utmp and wtmp entries"
    ``nologin``,    "(5)",  "prevent unprivileged users from logging into the system"
    ``nologin``,    "(8)",  "politely refuse a login"
    ``passwd``,     "(1)",  "change user password"
    ``passwd``,     "(5)",  "the password file"
    ``su``,         "(1)",  "run a command with substitute user and group ID"
    ``sudo``,       "(8)",  "execute a command as another user"
    ``useradd``,    "(8)",  "create a new user or update default new user information"
    ``userdel``,    "(8)",  "delete a user account and related files"
    ``usermod``,    "(8)",  "modify a user account"
    ``users``,      "(1)",  "print the user names of users currently logged in to the current host"
    ``visudo``,     "(8)",  "edit the sudoers file"
    ``w``,          "(1)",  "Show who is logged on and what they are doing."
    ``who``,        "(1)",  "show who is logged on"
    ``whoami``,     "(1)",  "print effective userid"
    ``ulimit``,     "(3)",  "get and set user limits"
    ``mesg``,       "(1)",  "display (or do not display) messages from other users"
    ``wall``,       "(1)",  "write a message to all users"
    ``write``,      "(1)",  "send a message to another user"
