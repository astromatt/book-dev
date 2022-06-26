Services
========
* Daemons
* SystemV
* SystemD
* Upstart


Runlevel
--------
.. csv-table:: Runlevels
    :header: "Run Level", "Mode", "Action"
    :widths: 5, 20, 75

    "0", "Halt",                            "Shuts down system"
    "1", "Single-User Mode",                "Does not configure network interfaces, start daemons, or allow non-root logins"
    "2", "Multi-User Mode",                 "Does not configure network interfaces or start daemons"
    "3", "Multi-User Mode with Networking", "Starts the system normally"
    "4", "Undefined",                       "Not used/User-definable"
    "5", "X11",                             "As runlevel 3 + display" manager(X)"
    "6", "Reboot",                          "Reboots the system"


Initialization
--------------
* ``/etc/init.d``
* ``/etc/rc0.d``
* ``/etc/rc1.d``
* ``/etc/rc2.d``
* ``/etc/rc3.d``
* ``/etc/rc4.d``
* ``/etc/rc5.d``
* ``/etc/rc6.d``
* ``/etc/rcS.d``
* ``/etc/rc.d``
* ``/etc/rc.local``


Configuration
-------------
* ``/etc/default/``


Management
----------
* Systemd
* System-V
* Init-d
* Upstart
* ``/etc/sysctl.d``
* ``/etc/systemd``


Commands
--------
.. csv-table:: Services
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``service``,    "(8)",  "run a System V init script"
    ``sysctl``,     "(2)",  "read/write system parameters"
    ``sysctl``,     "(8)",  "configure kernel parameters at runtime"
    ``systemctl``,  "(1)",  "Control the systemd system and service manager"
    ``systemd``,    "(1)",  "systemd system and service manager"
