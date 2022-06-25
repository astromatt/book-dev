Boot
====


Modes
-----
* LiveCD
* RamFS


GRUB
----
* Kernel
* Initramfs
* Splashscreen
* Multiple OSes
* Hard disk naming convention


Runlevel
--------
* ``0``
* ``1``
* ``2``
* ``3``
* ``4``
* ``5``
* ``6``


Paths
-----
* ``/boot/vmlinuz``
* ``/boot/initrd.img``
* ``/boot/efi/``
* ``/boot/grub/``
* ``/boot/grub/grub.cfg``


Commands
--------
.. csv-table:: System
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``uptime``,         "",     "print time since last reboot"
    ``vmstat``,         "(8)",  "Report virtual memory statistics"
    ``shutdown``,       "(2)",  "shut down part of a full-duplex connection"
    ``shutdown``,       "(8)",  "Halt, power-off or reboot the machine"
    ``runlevel``,       "(8)",  "Print previous and current SysV runlevel"
    ``readlink``,       "(1)",  "print resolved symbolic links or canonical file names"
    ``readlink``,       "(2)",  "read value of a symbolic link"
    ``reboot``,         "(2)",  "reboot or enable/disable Ctrl-Alt-Del"
    ``reboot``,         "(8)",  "Halt, power-off or reboot the machine"
    ``poweroff``,       "(8)",  "Halt, power-off or reboot the machine"
    ``lsb_release``,    "(1)",  "print distribution-specific information"
    ``free``,           "(1)",  "Display amount of free and used memory in the system"
    ``halt``,           "(8)",  "Halt, power-off or reboot the machine"
    ``hostname``,       "(1)",  "show or set the system's host name"
    ``hostname``,       "(5)",  "Local hostname configuration file"
    ``hostname``,       "(7)",  "hostname resolution description"
    ``hostnamectl``,    "(1)",  "Control the system hostname"
    ``suspend``,        "",     ""
