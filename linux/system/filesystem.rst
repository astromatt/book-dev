Filesystem
==========
* files
* directories
* sockets
* symlinks
* hardlinks
* journaling


Disk
----
* ``/dev/sda``
* ``/dev/sdb``

.. csv-table:: Disk
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``df -h``,                      "",                 ""
    ``df``,                         "(1)",              "report file system disk space usage"
    ``sync``,                       "(1)",              "Synchronize cached writes to persistent storage"
    ``sync``,                       "(2)",              "commit filesystem caches to disk"


Partitioning
------------
* ``/dev/sda1``
* ``/dev/sda2``
* ``parted``
* ``gparted``
* ``druid``

.. csv-table:: Partition
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``delpart``,                    "(8)",              "tell the kernel to forget about a partition"
    ``fdisk``,                      "(8)",              "manipulate disk partition table"
    ``grub-mkconfig``,              "(8)",              "generate a GRUB configuration file"
    ``grub``,                       "",                 ""
    ``kpartx``,                     "(8)",              "Create device maps from partition tables."
    ``parted``,                     "(8)",              "a partition manipulation program"
    ``partx``,                      "(8)",              "tell the kernel about the presence and numbering of on-disk partitions"
    ``resizepart``,                 "(8)",              "tell the kernel about the new size of a partition"
    ``update-grub``,                "(8)",              "stub for grub-mkconfig"


File Systems
------------
* ``xfs``
* ``zfs``
* ``apfs``
* ``ntfs``
* ``fat32``
* ``btrfs``
* ``ext3``
* ``ext4``
* ``vfat``

.. csv-table:: Filesystem
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``fsck``,                       "(8)",              "check and repair a Linux filesystem"
    ``journalctl``,                 "(1)",              "Query the systemd journal"
    ``mkfs``,                       "(8)",              "build a Linux filesystem"
    ``mkswap``,                     "(8)",              "set up a Linux swap area"
    ``mount``,                      "(2)",              "mount filesystem"
    ``mount``,                      "(8)",              "mount a filesystem"
    ``swapoff``,                    "(2)",              "start/stop swapping to file/device"
    ``swapoff``,                    "(8)",              "enable/disable devices and files for paging and swapping"
    ``swapon``,                     "(2)",              "start/stop swapping to file/device"
    ``swapon``,                     "(8)",              "enable/disable devices and files for paging and swapping"


Integrity
---------
* ``fdisk``


Mounting
--------
* ``mount``
* ``/etc/fstab``
* ``/etc/mtab``
