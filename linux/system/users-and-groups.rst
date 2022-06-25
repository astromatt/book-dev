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
