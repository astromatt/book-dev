Vagrant
=======

Tworzenie i konfigurowanie maszyny
----------------------------------

- Poniższe polecenia wykonaj w pliku Vagrantfile
- Stwórz maszynę z oficjalnego obrazu 32 bitowej wersji Ubuntu LTS (Long Time Support)
- Ustaw hostname na `ubuntu.local`
- Jeżeli masz słabszą maszynę (2 CPU core, 4 GB RAM):

    - 1 CPU core
    - 1024 MB Ram

- Jeżeli masz lepszy komputer:

    - 2 CPU core
    - 4096 MB RAM

- Ustaw forwarding portu 80 na 8080 hosta oraz 443 na 8443
- Ustaw aby ten katalog był synchronizowany na maszynie gościa w `/var/www/host`
- Zrób by maszyna była stawiana z manifestu Puppeta
- Podnieś maszynę i rozpocznij pobieranie obrazu

.. code-block:: shell

    vagrant init ubuntu/trusty32

.. code-block:: ruby

    CPU = 1
    RAM = 1024

    Vagrant.configure("2") do |config|
        config.vm.hostname = "ubuntu.local"

        config.vm.box = "ubuntu/xenial64"
        # config.vm.box = "ubuntu-lts"
        # config.vm.box_url = "http://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-vagrant.box"

        config.vm.network :forwarded_port, guest: 80, host: 8080
        config.vm.network :forwarded_port, guest: 443, host: 8443
        config.vm.synced_folder ".", "/var/www/host"

        config.vm.provider "virtualbox" do |v|
            v.name = "ubuntu.local"
            v.cpus = CPU
            v.memory = RAM
        end

        config.vm.provision :puppet do |puppet|
            puppet.manifests_path = "puppet/manifests"
            puppet.manifest_file = "site.pp"
            puppet.module_path = "puppet/modules"
        end
    end

.. code-block:: shell

    vagrant up


Exercises
---------

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

Ćwiczenia
---------

Automatyzacja tworzenia wirtualnej maszyny
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Użyj pliku ``Vagrantfile`` do przetrzymywania następującej konfiguracji
- Stwórz maszynę z oficjalnego obrazu 32 bitowej wersji `Ubuntu LTS` (Long Time Support)
- Ustaw hostname na ``ubuntu.local``
- Ustaw zasoby przydzielane towjej maszynie wirtialnej w zależności od mocy komputera:

    - 1 CPU core, 1024 MB RAM (jeżeli masz około 2 CPU core, 4 GB RAM)
    - 2 CPU core, 8196 MB RAM (jeżeli masz mocniejszą maszynę)

- Ustaw forwarding portów:

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

- Ustaw aby ten katalog był synchronizowany na maszynie gościa w ``/var/www/host``
- Podnieś maszynę z ``Vagrantfile`` i rozpocznij pobieranie obrazu `Ubuntu`


Vagrant + Puppet
^^^^^^^^^^^^^^^^

- Skopiuj dotychczasowe manifesty z poprzednich zadań (``/etc/puppet/manifests/*``) na swój komputer do katalogu ``puppet/manifests/``
- Skopiuj certyfikaty SSL, które wygenerowałeś na swój komputer do katalogu ``ssl/``
- Wyłącz maszynę ``vagrant halt``, a następnie ją usuń ``vagrant destroy``
- Edytuj plik ``Vagrantfile`` i dopisz, by maszyna była stawiana z manifestów `Puppet`
- W pliku ``Vagrantfile`` trzymaj jak najmniej logiki i wszystko rób za pomocą `Puppet`
- Zrób by certyfikaty były przenoszone z twojego komputera na maszynę gościa (nie generuj nowych, tylko wykorzystaj stare!) oczywiście za pomocą `Puppet`, umieść to w pliku ``puppet/manifests/certificates.pp``
- Każdy z manifestów powinien być w osobnych plikach a jeden ``puppet/main.pp`` powinien includować pozostałe z katalogu ``puppet/manifests/*``



