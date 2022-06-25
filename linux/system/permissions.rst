Permissions
===========


Understanding Permissions
-------------------------
.. csv-table:: Permissions

    "Permission", "Binary", "Octal", "Description"
    "``---``",    "000",    "0",     "Cannot read, execute or modify"
    "``--x``",    "001",    "1",     "Can execute"
    "``-w-``",    "010",    "2",     "Can write (modify)"
    "``-wx``",    "011",    "3",     "Can modify and execute"
    "``r--``",    "100",    "4",     "Can read"
    "``r-x``",    "101",    "5",     "Can read and execute"
    "``rw-``",    "110",    "6",     "Can read and write"
    "``rwx``",    "111",    "7",     "Can read, write and execute"


Changing Permissions
--------------------
* ``chmod``
* ``chown``
* ``chgrp``


UMASK
-----
* ``export UMASK=022``


Sticky bit
----------
* ``chmod +s``


ACL
---
