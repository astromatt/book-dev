Directory Structure
===================


Directory Structure
-------------------
.. csv-table:: Directory Structure
    :widths: 20, 80
    :header: "Path", "Description"

    ``/``,                "Main directory"
    ``/bin``,             "Built-in executable files"
    ``/boot``,            "Boot files and kernel"
    ``/etc``,             "Configuration directory"
    ``/etc/init.d``,      "Runtime scripts"
    ``/dev``,             "Devices and drivers"
    ``/home``,            "User files"
    ``/lib``,             "Shared libraries"
    ``/opt``,             "Optional applications"
    ``/root``,            "Superuser home directory"
    ``/sbin``,            "Superuser built-in binary files"
    ``/srv``,             "Optional services"
    ``/tmp``,             "Temporary files (removed on startup)"
    ``/usr``,             "User installed files"
    ``/usr/bin``,         "Application executable files"
    ``/usr/lib``,         "Applications data files"
    ``/usr/local/bin``,   "User installed applications executable files"
    ``/usr/local/sbin``,  "Superuser installed applications executable files"
    ``/usr/sbin``,        "Application superuser executable files"
    ``/usr/src``,         "Application source codes"
    ``/var``,             "Installed applications files"
    ``/var/lock``,        "Application lock files"
    ``/var/log``,         "Applications and system log files"
    ``/var/pid``,         "Application PID files"
    ``/var/spool``,       "System spool files (crontab, mail, printer)"


Root Directory
--------------
* Top Level Directory

.. code-block:: console

    $ tree -fdL 1 /
    /
    ├── /bin -> usr/bin
    ├── /boot
    ├── /dev
    ├── /etc
    ├── /home
    ├── /lib -> usr/lib
    ├── /lib32 -> usr/lib32
    ├── /lib64 -> usr/lib64
    ├── /libx32 -> usr/libx32
    ├── /lost+found
    ├── /media
    ├── /mnt
    ├── /opt
    ├── /proc
    ├── /root
    ├── /run
    ├── /sbin -> usr/sbin
    ├── /snap
    ├── /srv
    ├── /sys
    ├── /tmp
    ├── /usr
    └── /var

23 directories, 0 files

.. code-block:: console

    $ tree -fdL 2 --noreport /
    /
    ├── /bin -> usr/bin
    ├── /boot
    │   ├── /boot/efi
    │   └── /boot/grub
    ├── /dev
    │   ├── /dev/block
    │   ├── /dev/char
    │   ├── /dev/cpu
    │   ├── /dev/disk
    │   ├── /dev/dma_heap
    │   ├── /dev/fd -> /proc/self/fd
    │   ├── /dev/hugepages
    │   ├── /dev/input
    │   ├── /dev/mapper
    │   ├── /dev/mqueue
    │   ├── /dev/net
    │   ├── /dev/pts
    │   ├── /dev/shm
    │   ├── /dev/snd
    │   ├── /dev/vfio
    │   └── /dev/xen
    ├── /etc
    │   ├── /etc/ModemManager
    │   ├── /etc/NetworkManager
    │   ├── /etc/PackageKit
    │   ├── /etc/X11
    │   ├── /etc/acpi
    │   ├── /etc/alternatives
    │   ├── /etc/apache2
    │   ├── /etc/apparmor
    │   ├── /etc/apparmor.d
    │   ├── /etc/apport
    │   ├── /etc/apt
    │   ├── /etc/bash_completion.d
    │   ├── /etc/binfmt.d
    │   ├── /etc/byobu
    │   ├── /etc/ca-certificates
    │   ├── /etc/chrony
    │   ├── /etc/cloud
    │   ├── /etc/console-setup
    │   ├── /etc/cron.d
    │   ├── /etc/cron.daily
    │   ├── /etc/cron.hourly
    │   ├── /etc/cron.monthly
    │   ├── /etc/cron.weekly
    │   ├── /etc/cryptsetup-initramfs
    │   ├── /etc/dbus-1
    │   ├── /etc/default
    │   ├── /etc/depmod.d
    │   ├── /etc/dhcp
    │   ├── /etc/dpkg
    │   ├── /etc/fonts
    │   ├── /etc/fwupd
    │   ├── /etc/groff
    │   ├── /etc/grub.d
    │   ├── /etc/gss
    │   ├── /etc/init.d
    │   ├── /etc/initramfs-tools
    │   ├── /etc/iproute2
    │   ├── /etc/iscsi
    │   ├── /etc/kernel
    │   ├── /etc/landscape
    │   ├── /etc/ld.so.conf.d
    │   ├── /etc/ldap
    │   ├── /etc/libblockdev
    │   ├── /etc/libnl-3
    │   ├── /etc/lighttpd
    │   ├── /etc/logcheck
    │   ├── /etc/logrotate.d
    │   ├── /etc/lvm
    │   ├── /etc/mdadm
    │   ├── /etc/modprobe.d
    │   ├── /etc/modules-load.d
    │   ├── /etc/multipath
    │   ├── /etc/needrestart
    │   ├── /etc/netplan
    │   ├── /etc/network
    │   ├── /etc/networkd-dispatcher
    │   ├── /etc/newt
    │   ├── /etc/opt
    │   ├── /etc/pam.d
    │   ├── /etc/perl
    │   ├── /etc/pki
    │   ├── /etc/pm
    │   ├── /etc/polkit-1
    │   ├── /etc/pollinate
    │   ├── /etc/ppp
    │   ├── /etc/profile.d
    │   ├── /etc/python3
    │   ├── /etc/python3.10
    │   ├── /etc/rc0.d
    │   ├── /etc/rc1.d
    │   ├── /etc/rc2.d
    │   ├── /etc/rc3.d
    │   ├── /etc/rc4.d
    │   ├── /etc/rc5.d
    │   ├── /etc/rc6.d
    │   ├── /etc/rcS.d
    │   ├── /etc/rsyslog.d
    │   ├── /etc/security
    │   ├── /etc/selinux
    │   ├── /etc/skel
    │   ├── /etc/sos
    │   ├── /etc/ssh
    │   ├── /etc/ssl
    │   ├── /etc/sudoers.d
    │   ├── /etc/sysctl.d
    │   ├── /etc/systemd
    │   ├── /etc/terminfo
    │   ├── /etc/tmpfiles.d
    │   ├── /etc/ubuntu-advantage
    │   ├── /etc/udev
    │   ├── /etc/udisks2
    │   ├── /etc/ufw
    │   ├── /etc/update-manager
    │   ├── /etc/update-motd.d
    │   ├── /etc/update-notifier
    │   ├── /etc/usb_modeswitch.d
    │   ├── /etc/vim
    │   ├── /etc/vmware-tools
    │   └── /etc/xdg
    ├── /home
    │   └── /home/ubuntu
    ├── /lib -> usr/lib
    ├── /lib32 -> usr/lib32
    ├── /lib64 -> usr/lib64
    ├── /libx32 -> usr/libx32
    ├── /lost+found  [error opening dir]
    ├── /media
    ├── /mnt
    ├── /opt
    ├── /proc
    │   ├── ...
    │   ├── /proc/acpi
    │   ├── /proc/bus
    │   ├── /proc/driver
    │   ├── /proc/dynamic_debug
    │   ├── /proc/fs
    │   ├── /proc/irq
    │   ├── /proc/net -> self/net
    │   ├── /proc/pressure
    │   ├── /proc/scsi
    │   ├── /proc/self -> 55952
    │   ├── /proc/sys
    │   ├── /proc/sysvipc
    │   ├── /proc/thread-self -> 55952/task/55952
    │   ├── /proc/tty
    │   └── /proc/xen
    ├── /root  [error opening dir]
    ├── /run
    │   ├── /run/NetworkManager
    │   ├── /run/blkid
    │   ├── /run/chrony
    │   ├── /run/cloud-init
    │   ├── /run/console-setup
    │   ├── /run/credentials
    │   ├── /run/cryptsetup
    │   ├── /run/dbus
    │   ├── /run/irqbalance
    │   ├── /run/lock
    │   ├── /run/log
    │   ├── /run/lvm
    │   ├── /run/mount
    │   ├── /run/needrestart
    │   ├── /run/netns
    │   ├── /run/screen
    │   ├── /run/sendsigs.omit.d
    │   ├── /run/shm -> /dev/shm
    │   ├── /run/snapd
    │   ├── /run/sshd
    │   ├── /run/sudo
    │   ├── /run/systemd
    │   ├── /run/tmpfiles.d
    │   ├── /run/udev
    │   ├── /run/udisks2
    │   ├── /run/user
    │   └── /run/uuidd
    ├── /sbin -> usr/sbin
    ├── /snap
    │   ├── /snap/amazon-ssm-agent
    │   ├── /snap/bin
    │   ├── /snap/core18
    │   ├── /snap/core20
    │   ├── /snap/lxd
    │   └── /snap/snapd
    ├── /srv
    ├── /sys
    │   ├── /sys/block
    │   ├── /sys/bus
    │   ├── /sys/class
    │   ├── /sys/dev
    │   ├── /sys/devices
    │   ├── /sys/firmware
    │   ├── /sys/fs
    │   ├── /sys/hypervisor
    │   ├── /sys/kernel
    │   ├── /sys/module
    │   └── /sys/power
    ├── /tmp
    │   ├── ...
    ├── /usr
    │   ├── /usr/bin
    │   ├── /usr/games
    │   ├── /usr/include
    │   ├── /usr/lib
    │   ├── /usr/lib32
    │   ├── /usr/lib64
    │   ├── /usr/libexec
    │   ├── /usr/libx32
    │   ├── /usr/local
    │   ├── /usr/sbin
    │   ├── /usr/share
    │   └── /usr/src
    └── /var
        ├── /var/backups
        ├── /var/cache
        ├── /var/crash
        ├── /var/lib
        ├── /var/local
        ├── /var/lock -> /run/lock
        ├── /var/log
        ├── /var/mail
        ├── /var/opt
        ├── /var/run -> /run
        ├── /var/snap
        ├── /var/spool
        └── /var/tmp


.. figure:: ../_img/directory-tree.gif
    :align: center
    :scale: 100%

    Linux directory tree

.. figure:: ../_img/unix-directory-structure.png
    :align: center
    :scale: 100%

    Linux directory tree
