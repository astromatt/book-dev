*****
Facts
*****


Running
=======
.. code-block:: console

    $ ansible localhost -m setup
    [WARNING]: No inventory was parsed, only implicit localhost is available

    localhost | SUCCESS => {
        "ansible_facts": {
            "ansible_apparmor": {
                "status": "disabled"
            },
            "ansible_architecture": "x86_64",
            "ansible_bios_date": "08/24/2006",
            "ansible_bios_version": "4.2.amazon",
            "ansible_cmdline": {
                "BOOT_IMAGE": "/boot/vmlinuz-4.15.0-1051-aws",
                "console": "ttyS0",
                "nvme_core.io_timeout": "4294967295",
                "ro": true,
                "root": "LABEL=cloudimg-rootfs"
            },
            "ansible_date_time": {
                "date": "2020-01-14",
                "day": "14",
                "epoch": "1578965724",
                "hour": "01",
                "iso8601": "2020-01-14T01:35:24Z",
                "iso8601_basic": "20200114T013524843393",
                "iso8601_basic_short": "20200114T013524",
                "iso8601_micro": "2020-01-14T01:35:24.843473Z",
                "minute": "35",
                "month": "01",
                "second": "24",
                "time": "01:35:24",
                "tz": "UTC",
                "tz_offset": "+0000",
                "weekday": "Tuesday",
                "weekday_number": "2",
                "weeknumber": "02",
                "year": "2020"
            },
            "ansible_device_links": {
                "ids": {},
                "labels": {},
                "masters": {},
                "uuids": {}
            },
            "ansible_devices": {
                "loop0": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "none",
                    "sectors": "182280",
                    "sectorsize": "512",
                    "size": "89.00 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "loop1": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "none",
                    "sectors": "36824",
                    "sectorsize": "512",
                    "size": "17.98 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "loop2": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "none",
                    "sectors": "182456",
                    "sectorsize": "512",
                    "size": "89.09 MB",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "loop3": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "none",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "4096",
                    "vendor": null,
                    "virtual": 1
                },
                "loop4": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "none",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                },
                "loop5": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "none",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                },
                "loop6": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "none",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                },
                "loop7": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {},
                    "removable": "0",
                    "rotational": "1",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "none",
                    "sectors": "0",
                    "sectorsize": "512",
                    "size": "0.00 Bytes",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                },
                "xvda": {
                    "holders": [],
                    "host": "",
                    "links": {
                        "ids": [],
                        "labels": [],
                        "masters": [],
                        "uuids": []
                    },
                    "model": null,
                    "partitions": {
                        "xvda1": {
                            "holders": [],
                            "links": {
                                "ids": [],
                                "labels": [],
                                "masters": [],
                                "uuids": []
                            },
                            "sectors": "16775135",
                            "sectorsize": 512,
                            "size": "8.00 GB",
                            "start": "2048",
                            "uuid": null
                        }
                    },
                    "removable": "0",
                    "rotational": "0",
                    "sas_address": null,
                    "sas_device_handle": null,
                    "scheduler_mode": "cfq",
                    "sectors": "16777216",
                    "sectorsize": "512",
                    "size": "8.00 GB",
                    "support_discard": "0",
                    "vendor": null,
                    "virtual": 1
                }
            },
            "ansible_distribution": "Ubuntu",
            "ansible_distribution_file_parsed": true,
            "ansible_distribution_file_path": "/etc/os-release",
            "ansible_distribution_file_variety": "Debian",
            "ansible_distribution_major_version": "18",
            "ansible_distribution_release": "bionic",
            "ansible_distribution_version": "18.04",
            "ansible_dns": {
                "nameservers": [
                    "172.31.0.2"
                ],
                "search": [
                    "eu-central-1.compute.internal"
                ]
            },
            "ansible_domain": "",
            "ansible_effective_group_id": 0,
            "ansible_effective_user_id": 0,
            "ansible_env": {
                "HOME": "/root",
                "HOSTNAME": "0ec55af56aea",
                "LS_COLORS": "rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:",
                "OLDPWD": "/",
                "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "PWD": "/home",
                "SHLVL": "1",
                "TERM": "xterm",
                "_": "/usr/local/bin/ansible"
            },
            "ansible_fibre_channel_wwn": [],
            "ansible_fips": false,
            "ansible_form_factor": "Other",
            "ansible_fqdn": "0ec55af56aea",
            "ansible_hostname": "0ec55af56aea",
            "ansible_hostnqn": "",
            "ansible_is_chroot": false,
            "ansible_iscsi_iqn": "",
            "ansible_kernel": "4.15.0-1051-aws",
            "ansible_kernel_version": "#53-Ubuntu SMP Wed Sep 18 13:35:53 UTC 2019",
            "ansible_local": {},
            "ansible_lsb": {
                "codename": "bionic",
                "description": "Ubuntu 18.04.3 LTS",
                "id": "Ubuntu",
                "major_release": "18",
                "release": "18.04"
            },
            "ansible_machine": "x86_64",
            "ansible_machine_id": "86d87f18c3075347550131775e1cff4e",
            "ansible_memfree_mb": 8831,
            "ansible_memory_mb": {
                "nocache": {
                    "free": 15078,
                    "used": 961
                },
                "real": {
                    "free": 8831,
                    "total": 16039,
                    "used": 7208
                },
                "swap": {
                    "cached": 0,
                    "free": 0,
                    "total": 0,
                    "used": 0
                }
            },
            "ansible_memtotal_mb": 16039,
            "ansible_mounts": [
                {
                    "block_available": 300924,
                    "block_size": 4096,
                    "block_total": 2016361,
                    "block_used": 1715437,
                    "device": "/dev/xvda1",
                    "fstype": "ext4",
                    "inode_available": 786890,
                    "inode_total": 1024000,
                    "inode_used": 237110,
                    "mount": "/etc/resolv.conf",
                    "options": "rw,relatime,discard,data=ordered,bind",
                    "size_available": 1232584704,
                    "size_total": 8259014656,
                    "uuid": "N/A"
                },
                {
                    "block_available": 300924,
                    "block_size": 4096,
                    "block_total": 2016361,
                    "block_used": 1715437,
                    "device": "/dev/xvda1",
                    "fstype": "ext4",
                    "inode_available": 786890,
                    "inode_total": 1024000,
                    "inode_used": 237110,
                    "mount": "/etc/hostname",
                    "options": "rw,relatime,discard,data=ordered,bind",
                    "size_available": 1232584704,
                    "size_total": 8259014656,
                    "uuid": "N/A"
                },
                {
                    "block_available": 300924,
                    "block_size": 4096,
                    "block_total": 2016361,
                    "block_used": 1715437,
                    "device": "/dev/xvda1",
                    "fstype": "ext4",
                    "inode_available": 786890,
                    "inode_total": 1024000,
                    "inode_used": 237110,
                    "mount": "/etc/hosts",
                    "options": "rw,relatime,discard,data=ordered,bind",
                    "size_available": 1232584704,
                    "size_total": 8259014656,
                    "uuid": "N/A"
                }
            ],
            "ansible_nodename": "0ec55af56aea",
            "ansible_os_family": "Debian",
            "ansible_pkg_mgr": "apt",
            "ansible_proc_cmdline": {
                "BOOT_IMAGE": "/boot/vmlinuz-4.15.0-1051-aws",
                "console": [
                    "tty1",
                    "ttyS0"
                ],
                "nvme_core.io_timeout": "4294967295",
                "ro": true,
                "root": "LABEL=cloudimg-rootfs"
            },
            "ansible_processor": [
                "0",
                "GenuineIntel",
                "Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz",
                "1",
                "GenuineIntel",
                "Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz",
                "2",
                "GenuineIntel",
                "Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz",
                "3",
                "GenuineIntel",
                "Intel(R) Xeon(R) CPU E5-2686 v4 @ 2.30GHz"
            ],
            "ansible_processor_cores": 4,
            "ansible_processor_count": 1,
            "ansible_processor_threads_per_core": 1,
            "ansible_processor_vcpus": 4,
            "ansible_product_name": "HVM domU",
            "ansible_product_serial": "ec2839b2-8bf3-61f7-2614-f3684b909686",
            "ansible_product_uuid": "EC2839B2-8BF3-61F7-2614-F3684B909686",
            "ansible_product_version": "4.2.amazon",
            "ansible_python": {
                "executable": "/usr/bin/python3",
                "has_sslcontext": true,
                "type": "cpython",
                "version": {
                    "major": 3,
                    "micro": 9,
                    "minor": 6,
                    "releaselevel": "final",
                    "serial": 0
                },
                "version_info": [
                    3,
                    6,
                    9,
                    "final",
                    0
                ]
            },
            "ansible_python_version": "3.6.9",
            "ansible_real_group_id": 0,
            "ansible_real_user_id": 0,
            "ansible_selinux": {
                "status": "Missing selinux Python library"
            },
            "ansible_selinux_python_present": false,
            "ansible_service_mgr": "sysvinit",
            "ansible_swapfree_mb": 0,
            "ansible_swaptotal_mb": 0,
            "ansible_system": "Linux",
            "ansible_system_vendor": "Xen",
            "ansible_uptime_seconds": 59059,
            "ansible_user_dir": "/root",
            "ansible_user_gecos": "root",
            "ansible_user_gid": 0,
            "ansible_user_id": "root",
            "ansible_user_shell": "/bin/bash",
            "ansible_user_uid": 0,
            "ansible_userspace_architecture": "x86_64",
            "ansible_userspace_bits": "64",
            "ansible_virtualization_role": "guest",
            "ansible_virtualization_type": "docker",
            "gather_subset": [
                "all"
            ],
            "module_setup": true
        },
        "changed": false
    }
