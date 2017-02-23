Excercises
==========

Vagrant create virtual machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Use ``Vagrantfile`` to store following configuration
- Create virtual machine from the official 32 bits `Ununtu LTS` (Long Time Support) image
- Set the hostname to ``ubuntu.local``
- Adjust virtual machine resources according to your computer power:

    - 1 CPU core, 1024 MB RAM (if your computer has around 2 CPU core, 4 GB RAM)
    - 2 CPU core, 8196 MB RAM (if you have more powerfull machine)

- Setup port forwarding:

    - 80 -> 8888
    - 443 -> 8443
    - 7990 -> 7990
    - 7999 -> 7999
    - 8080 -> 8080
    - 8081 -> 8081
    - 8090 -> 8090
    - 9000 -> 9000
    - 5432 -> 5432
    - 3306 -> 3306

- Synchronize current directory to ``/var/www/host``
- Run machine from ``Vagrantfile`` and start downloading an `Ubuntu` image

Vagrant + Puppet
^^^^^^^^^^^^^^^^

- Copy manifests from the previous tasks (stored in ``/etc/puppet/manifests/*``) to ``puppet/manifests/`` directory on your local machine
- Copy SSL certificates generated to ``ssl/`` directory on your local machine
- Power-off machine ``vagrant halt`` and destroy it ``vagrant destroy``
- Edit ``Vagrantfile`` and modify to provision from `Puppet` manifests
- Do not put any logic to ``Vagrantfile`` use `Puppet` manifests instead
- Copy SSL certificates from your local computer to the guest machine using `Puppet` (do not generate new certificates!) put the configuration in ``puppet/manifests/certificates.pp``
- Use one ``puppet/main.pp`` to include others manifests from ``puppet/manifests/*`` - do not put everything in the onefile
