Vagrant
=======

.. todo:: https://www.youtube.com/watch?v=kbarwyun-c4

.. contents::

.. warning:: Na windows installer może się pod koniec instalacji wywalać. Wtedy trzeba uruchomić ``cmd`` jako Administrator i uruchomić installer z terminala.


Tworzenie maszyny
-----------------

Uruchamianie maszyny
^^^^^^^^^^^^^^^^^^^^
#. Stwórz na pulpicie katalog ``szkolenie``
#. Przejdź za pomocą terminala do tego katalogu i wykonaj:

    .. code-block:: console

        vagrant init ubuntu/bionic64

#. Spowoduje to wygenerowanie pliku, który po usunięciu komentarzy będzie wyglądał następująco:

    .. code-block:: text

        Vagrant.configure("2") do |config|
          config.vm.box = "ubuntu/bionic64"
        end

#. Uruchom maszynę

    .. code-block:: console

        vagrant up

#. Stworzy to maszynę z oficjalnego obrazu 64 bitowej wersji `Ubuntu LTS` (`Long Time Support`)
#. Aby zalogować się na maszynę należy wykonać:

    .. code-block:: console

        vagrant ssh

.. note:: Standard tworzenia boxów Vagrant wymaga posiadanie w systemie użytkownika ``vagrant`` z hasłem ``vagrant``

Update vagrant boxes
^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    vagrant box update

Usuwanie maszyny
^^^^^^^^^^^^^^^^
.. code-block:: console

    vagrant halt
    vagrant destroy

Uruchamianie innego providera
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: console

    vagrant up --provider virtualbox


Konfiguracja maszyny
--------------------

Konfiguracja forwardingu portów
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: ruby

    config.vm.network "forwarded_port", guest: 8080, host: 8080
    config.vm.network "forwarded_port", guest: 9000, host: 9000

Synchronizowanie katalogów
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: ruby

    config.vm.synced_folder ".", "/vagrant"


Konfiguracja zasobów
--------------------
- Poniższe polecenia wykonaj w pliku ``Vagrantfile``

Słaby komputer
^^^^^^^^^^^^^^
* np. 2 CPU core, 4 GB RAM

Zalecana konfiguracja maszyny wirtualnej:

    - 1 CPU core
    - 1024 MB Ram

Średni komputer
^^^^^^^^^^^^^^^
Zalecana konfiguracja maszyny wirtualnej:

    - 66% CPU core
    - 66% MB RAM

Dobry komputer
^^^^^^^^^^^^^^
Zalecana konfiguracja maszyny wirtualnej:

    - 75% CPU core
    - 75% MB RAM


Provisioning
------------

Provisioning za pomocą shell
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: ruby

    Vagrant.configure("2") do |config|
      config.vm.provision "shell" do |s|
        s.inline = "echo $1"
        s.args   = ["hello, world!"]
      end
    end

.. code-block:: ruby

    config.vm.provision "shell", inline: <<- SHELL
        /usr/bin/whoami > /tmp/whoami
    SHELL

.. code-block:: ruby

    Vagrant.configure("2") do |config|
      config.vm.provision "shell", path: "script.sh"
    end

.. code-block:: ruby

    Vagrant.configure("2") do |config|
      config.vm.provision "shell", path: "https://example.com/provisioner.sh"
    end

Provisioning za pomocą `Puppet`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: ruby

    config.vm.provision :puppet do |puppet|
        puppet.module_path = "puppet/modules"
        puppet.manifests_path = "puppet/manifests"
        puppet.manifest_file = "default.pp"
    end


Finalna konfiguracja
^^^^^^^^^^^^^^^^^^^^
Twoja konfuguracja `Vagrant` powinna wyglądać tak:

.. code-block:: ruby

    CPU = 1
    RAM = 1024

    Vagrant.configure("2") do |config|
        config.vm.hostname = "ubuntu.local"

        config.vm.box = "ubuntu/bionic64"
        # config.vm.box = "ubuntu-lts"
        # config.vm.box_url = "http://cloud-images.ubuntu.com/releases/18.04/release/ubuntu-18.04-server-cloudimg-amd64-vagrant.box"

        config.vm.network "forwarded_port", guest: 80, host: 8080
        config.vm.network "forwarded_port", guest: 443, host: 8443
        config.vm.synced_folder ".", "/var/www/host"

        config.vm.provider "virtualbox" do |v|
            v.name = "ubuntu.local"
            v.cpus = CPU
            v.memory = RAM
        end

        config.vm.provision "shell", path: "script.sh"

    end

.. code-block:: console

    vagrant provision


Zadania do rozwiązania
----------------------

Automatyzacja tworzenia wirtualnej maszyny
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Użyj pliku ``Vagrantfile`` do przetrzymywania następującej konfiguracji
- Stwórz maszynę z oficjalnego obrazu 64 bitowej wersji `Ubuntu LTS` (Long Time Support)
- Ustaw hostname na ``ubuntu.local``
- Ustaw zasoby przydzielane maszynie wirtualnej w zależności od mocy komputera:

    - 75% CPU core,
    - 75% MB RAM

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

- Ustaw aby obecny katalog był synchronizowany na maszynie gościa w ``/var/www/host``
- Podnieś maszynę z ``Vagrantfile`` i rozpocznij pobieranie obrazu `Ubuntu LTS`


Vagrant + Puppet
^^^^^^^^^^^^^^^^
- Skopiuj dotychczasowe manifesty z poprzednich zadań (``/etc/puppet/code/*``) na swój komputer do katalogu ``puppet/code/``
- Skopiuj certyfikaty SSL, które wygenerowałeś na swój komputer do katalogu ``ssl/``
- Wyłącz maszynę ``vagrant halt``, a następnie ją usuń ``vagrant destroy``
- Edytuj plik ``Vagrantfile`` i dopisz, by maszyna była stawiana z manifestów `Puppet`
- W pliku ``Vagrantfile`` trzymaj jak najmniej logiki i wszystko rób za pomocą `Puppet`
- Zrób by certyfikaty były przenoszone z twojego komputera na maszynę gościa (nie generuj nowych, tylko wykorzystaj stare!) oczywiście za pomocą `Puppet`, umieść to w pliku ``puppet/code/certificates.pp``
- Każdy z manifestów powinien być w osobnych plikach a jeden ``puppet/main.pp`` powinien includować pozostałe z katalogu ``puppet/code/*``

.. warning:: Ubuntu 16.04 (LTS) nie zawiera w sobie puppeta, co jest sprzeczne z wymaganiem (standardem) vagrantowym. Trzeba go zainstalować za pomocą provisioningu shella, a później odpalać manifesty puppetowe.
