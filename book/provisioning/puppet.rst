Puppet
======

.. todo:: sprawdzić czy działają tematy związane z tworzeniem faktów
.. todo:: sprawdzić jak zachowa się to z Facterem
.. todo:: sprawdzić deklarowanie i używanie zmiennych
.. todo:: podzielić puppeta na osobne pliki per temat (zadanie do rozwiązania)
.. todo:: co z tematem odpalania jako user a nie root?
.. todo:: uspójnić wszędzie nazwy userów i grup (vagrant, ubuntu, www-data, myuser) wybrać jeden
.. todo:: błąd ze sprawdzaniem czy user i grupa www-data istnieją, kiedy wykorzystujemy moduł apache

.. contents::

Architektura
------------

* zasada działania
* infrastructure as a code
* ad hoc changes
* scaling
* wprowadzanie zmian w zależności od faktów
* developer env changes
* instalacja ręczna pakietów

Jak działa
^^^^^^^^^^
manifest.pp

.. code-block:: ruby

    file { '/var/www':
        ensure => 'directory',
        owner => 'www-data',
        group => 'www-data',
        mode  => '0755',
    }

.. code-block:: ruby

    exec { 'package definition update':
        command => '/usr/bin/apt-get update',
    }

    package { ['nmap', 'htop', 'git']:
        ensure => 'latest',
        require => Exec['package definition update'],
    }

Model
^^^^^
* klient server
* standalone - puppet apply

* fakty i kolejność wykonywania manifestów

Components
^^^^^^^^^^
* manifests (pliki z rozszerzeniem ``.pp``)
* zmienne
* classes
* resources
* facts

Puppet language
^^^^^^^^^^^^^^^
* DSL
* ruby
* ERB templates


Instalacja i konfiguracja
-------------------------
.. code-block:: sh

    sudo apt-get update
    sudo apt-get install puppet

Zaglądnij do katalogu ``/etc/puppet``.
Co się tam znajduje?

Przejdź do katalogu ``/etc/puppet/manifests``.

.. warning:: Uwaga, puppet od wersji 4 ma inną składnię. W Ubuntu 16.04 (LTS) instaluje się Puppet 3.8.5. Wersja ta może być niekompatybilna z modułami pobieranymi przez puppeta (np. apache, tomcat, java). Rozwiązaniem jest ściąganie modułów w niższych wersjach (pasujących do wersji 3.8.5) lub instalacja puppeta w wersji wyższej niż ta w LTS.

    .. code-block:: console
    
        #Instalacja puppet w ostatniej wersji

        #Yum-based systems (np. Enterprise Linux 7)
        sudo rpm -Uvh https://yum.puppet.com/puppet5/puppet5-release-el-7.noarch.rpm
        sudo yum -y install puppet-agent
        export PATH=/opt/puppetlabs/bin:$PATH

        #Apt-based systems (np. Ubuntu 16.04 Xenial Xerus)
        wget https://apt.puppetlabs.com/puppet5-release-xenial.deb
        sudo dpkg -i puppet5-release-xenial.deb
        sudo apt update
        sudo apt-get -y install puppet-agent
        export PATH=/opt/puppetlabs/bin:$PATH

HTTPS problem
-------------
Gdyby wystąpił problem z certyfikatem ``ssl`` przy instalacji modułów należy:

- postaw maszynę w Amazonie (Ubuntu LTS)
- zainstaluj squid

.. code-block:: sh

    sudo apt-get update
    sudo apt-get install squid

- na maszynie gościa (tam gdzie chcesz instalować moduł puppeta ustaw:


.. code-block:: sh

    export http_proxy=http://<IP>:3128
    export https_proxy=http://<IP>:3128

Lub:

.. code-block:: ini

    [user]
    http_proxy = http://<IP>:3128
    https_proxy = http://<IP>:3128

.. code-block:: sh

    sudo service puppet restart
    sudo su -
    puppet module install


Ćwiczenia Praktyczne
--------------------

Facter
^^^^^^
Przyjrzyj się wynikom poleceń:

.. code-block:: sh

    facter
    facter ipaddress
    facter lsbdistdescription

Co zauważyłeś? Jak można wykorzystać te informacje?

Kod przedstawia wynik polecenia ``facter`` na świerzej maszynie `Ubuntu` postawionej w `Amazon AWS`

.. code-block:: text

    architecture => amd64
    augeasversion => 1.4.0
    bios_release_date => 12/01/2006
    bios_vendor => innotek GmbH
    bios_version => VirtualBox
    blockdevice_sda_model => HARDDISK
    blockdevice_sda_size => 10737418240
    blockdevice_sda_vendor => VBOX
    blockdevice_sdb_model => HARDDISK
    blockdevice_sdb_size => 10485760
    blockdevice_sdb_vendor => VBOX
    blockdevices => sda,sdb
    boardmanufacturer => Oracle Corporation
    boardproductname => VirtualBox
    boardserialnumber => 0
    domain => local
    facterversion => 2.4.6
    filesystems => btrfs,ext2,ext3,ext4,iso9660,squashfs,vfat
    fqdn => ecosystem.local
    gid => root
    hardwareisa => x86_64
    hardwaremodel => x86_64
    hostname => ecosystem
    id => root
    interfaces => enp0s3,lo
    ipaddress => 10.0.2.15
    ipaddress_enp0s3 => 10.0.2.15
    ipaddress_lo => 127.0.0.1
    is_virtual => true
    kernel => Linux
    kernelmajversion => 4.4
    kernelrelease => 4.4.0-64-generic
    kernelversion => 4.4.0
    lsbdistcodename => xenial
    lsbdistdescription => Ubuntu 16.04.2 LTS
    lsbdistid => Ubuntu
    lsbdistrelease => 16.04
    lsbmajdistrelease => 16.04
    macaddress => 02:9a:e7:4d:41:74
    macaddress_enp0s3 => 02:9a:e7:4d:41:74
    manufacturer => innotek GmbH
    memoryfree => 844.15 MB
    memoryfree_mb => 844.15
    memorysize => 992.18 MB
    memorysize_mb => 992.18
    mtu_enp0s3 => 1500
    mtu_lo => 65536
    netmask => 255.255.255.0
    netmask_enp0s3 => 255.255.255.0
    netmask_lo => 255.0.0.0
    network_enp0s3 => 10.0.2.0
    network_lo => 127.0.0.0
    operatingsystem => Ubuntu
    operatingsystemmajrelease => 16.04
    operatingsystemrelease => 16.04
    os => {"name"=>"Ubuntu", "family"=>"Debian", "release"=>{"major"=>"16.04", "full"=>"16.04"}, "lsb"=>{"distcodename"=>"xenial", "distid"=>"Ubuntu", "distdescription"=>"Ubuntu 16.04.2 LTS", "distrelease"=>"16.04", "majdistrelease"=>"16.04"}}
    osfamily => Debian
    partitions => {"sda1"=>{"uuid"=>"7ed30d1a-9225-48c6-b835-31d7fb6d36c0", "size"=>"20969439", "mount"=>"/", "label"=>"cloudimg-rootfs", "filesystem"=>"ext4"}}
    path => /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
    physicalprocessorcount => 1
    processor0 => Intel(R) Core(TM) i7-2620M CPU @ 2.70GHz
    processor1 => Intel(R) Core(TM) i7-2620M CPU @ 2.70GHz
    processorcount => 2
    processors => {"models"=>["Intel(R) Core(TM) i7-2620M CPU @ 2.70GHz", "Intel(R) Core(TM) i7-2620M CPU @ 2.70GHz"], "count"=>2, "physicalcount"=>1}
    productname => VirtualBox
    ps => ps -ef
    puppetversion => 3.8.5
    rubyplatform => x86_64-linux-gnu
    rubysitedir => /usr/local/lib/site_ruby/2.3.0
    rubyversion => 2.3.1
    selinux => false
    serialnumber => 0
    sshdsakey => AAAAB...l4NA==
    sshecdsakey => AAAAE....+vE=
    sshed25519key => AAAAC3...ZWVG
    sshfp_dsa => SSHFP 2 1 26e..e4b
    SSHFP 2 2 a00e6f...25a4d
    sshfp_ecdsa => SSHFP 3 1 326...0ef
    SSHFP 3 2 b52....97a
    sshfp_ed25519 => SSHFP 4 1 897....6d1
    SSHFP 4 2 75c...580
    sshfp_rsa => SSHFP 1 1 036d...74ad
    SSHFP 1 2 d41...dd25
    sshrsakey => AAAAB3....svzP
    swapfree => 0.00 MB
    swapfree_mb => 0.00
    swapsize => 0.00 MB
    swapsize_mb => 0.00
    system_uptime => {"seconds"=>14947, "hours"=>4, "days"=>0, "uptime"=>"4:09 hours"}
    timezone => UTC
    type => Other
    uniqueid => 007f0100
    uptime => 4:09 hours
    uptime_days => 0
    uptime_hours => 4
    uptime_seconds => 14947
    uuid => B0ACC1E7-052A-4BA8-A68E-5CC6E6A5F56B
    virtual => kvm

Korzystanie z faktów w manifestach:

:Sposób klasyczny, jako zmienne na głównym poziomie:

.. code-block:: ruby

    # Definicja
    operatingsystem = 'Ubuntu'

    # Wykorzystanie
    case $::operatingsystem {
      'CentOS': { include centos }
      'MacOS':  { include mac }
    }

:Jako zmienne w tablicy faktów:

.. code-block:: ruby

    # Definicja
    $facts['fact_name'] = 'Ubuntu'

    # Wykorzystanie
    case $facts['fact_name'] {
      'CentOS': { include centos }
      'MacOS':  { include mac }
    }

Tworzenie nowych faktów:

.. code-block:: ruby

    require 'facter'

    Facter.add(:system_role) do
      setcode "cat /etc/system_role"
    end

.. code-block:: ruby

    require 'facter'

    Facter.add(:system_role) do
      setcode do
        Facter::Util::Resolution.exec("cat /etc/system_role")
      end
    end

Druga metoda tworzenia faktów:

.. code-block:: sh

    export FACTER_system_role=$(cat /etc/system_role); facter

Przykłady
---------
.. code-block:: ruby

    Exec    { path => "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin" }
    group   { "vagrant": ensure => present }
    user    { "vagrant": ensure => present, gid => "vagrant" }
    exec    { "apt-get update": command => "/usr/bin/apt-get update" }

    package { [
        "git",
        "vim",
        "nmap",
        "htop",
        "wget",
        "curl",
        "nginx",
        "python3",
        "python3-dev",
        "python3-pip",
        "p7zip-full",
        "uwsgi",
        "uwsgi-plugin-python3",
        "postgresql-9.3",
        "postgresql-server-dev-9.3",
        "libmemcached-dev"
      ] :
        ensure => latest,
        require => Exec["apt-get update"],
    }

    file { [
        "/var/www",
        "/var/www/log",
        "/var/www/public",
        "/var/www/public/media",
        "/var/www/public/static",
        "/var/www/tmp",
        "/var/www/src"
      ]:
        ensure => directory,
        owner => "vagrant",
        group => "vagrant",
        mode => 0755,
    }


Moduły
------
.. code-block:: sh

    puppet module search apache
    puppet module install puppetlabs-apache

JBoss
^^^^^
* https://github.com/coi-gov-pl/puppet-jboss

To install JBoss Application Server you can use just, it will install Wildfly 8.2.0.Final by default:

.. code-block:: ruby

    include jboss

To install JBoss EAP or older JBoss AS use:

.. code-block:: ruby

    class { 'jboss':
      product => 'jboss-eap',
      version => '6.4.0.GA',
    }

or use hiera:

.. code-block:: ruby

    jboss::params::product: 'jboss-as'
    jboss::params::version: '7.1.1.Final'

.. code-block:: ruby

    $user = 'jb-user'
    $passwd = 'SeC3eT!1'

    node 'controller' {
      include jboss::domain::controller
      include jboss
      jboss::user { $user:
        ensure   => 'present',
        password => $passwd,
      }
    }


Przydatny linki
---------------
* https://docs.puppet.com/puppet/4.9/lang_facts_and_builtin_vars.html#language:-facts-and-built-in-variables


Zadania do rozwiązania
----------------------

Instalacja pakietów za pomocą `Puppet`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/packages.pp``
- Zainstaluj następujące pakiety za pomocą `Puppet`:

    - ``nmap``
    - ``htop``
    - ``git``

- Upewnij się by `Puppet` wykonał polecenie ``apt-get update`` na początku

Zmiana hostname
^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/hostname.pp``
- Za pomocą manifestu zmień hostname maszyny na ``ecosystem.local``
- Upewnij się, że po wpisaniu polecenia ``hostname`` będzie ustawiona na odpowiednią wartość
- Upewnij się, że hostname nie przywróci się do domyślnej wartości po ponownym uruchomieniu

Zarządzanie użytkownikami, grupami i katalogami
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/users.pp``
- Upewnij się, że użytkownik ``vagrant`` istnieje, ma ``uid=1337`` i należy do grupy ``vagrant``
- Upewnij się, że grupa ``vagrant`` istnieje i ma ``gid=1337``
- Upewnij się, że:

    - Katalog ``/var/www`` istnieje
    - Właścicielem jego jest user ``vagrant``
    - Właścicielem jego jest grupa ``vagrant``
    - Ma uprawnienia ``rwxr-xr-x``

Konfiguracja Apache2
^^^^^^^^^^^^^^^^^^^^
- Za pomocą Puppet upewnij się by był użytkownik ``www-data`` i miał ``uid=33``
- Za pomocą Puppet upewnij się by była grupa ``www-data`` i miała ``gid=33``
- Upewnij się że katalog ``/var/www`` istnieje i właścicielem jego są user ``www-data`` i grupa ``www-data`` i że ma uprawnienia ``rwxr-xr-x``
- Zainstaluj i skonfiguruj Apache2 wykorzystując moduł Puppet
- Z terminala wygeneruj certyfikaty self signed OpenSSL (``.cert`` i ``.key``) (za pomocą i umieść je w ``/etc/ssl/``)
- Za pomocą Puppet Stwórz dwa vhosty:

    - ``insecure.example.com`` na porcie 80 i z katalogiem domowym ``/var/www/insecure-example-com``
    - ``ssl.example.com`` na porcie 443 i z katalogiem domowym ``/var/www/ssl-example-com`` + używanie certyfikatów SSL wcześniej wygenerowanych

- Stwórz pliki z treścią:

    - ``/var/www/insecure-example-com/index.html`` z treścią ``Ehlo World! - Insecure``
    - ``/var/www/ssl-example-com/index.html`` z treścią ``Ehlo World! - SSL!``

- W przeglądarce na komputerze lokalnym wejdź na stronę:

    - http://127.0.0.1:8080
    - https://127.0.0.1:8443

.. warning:: Uwaga, puppet od wersji 4 ma inną składnię. W Ubuntu 16.04 (LTS) instaluje się Puppet 3.8.5. Puppet module instaluje zawsze najnowszą (w tym wypadku niekompatybilną z naszym puppetem)! Aby zainstalować apache należy wymusić odpowiednią wersję (ostatnia supportująca Puppeta 3.8 to 1.10.

    .. code-block:: console

        $ puppet module install puppetlabs-apache --version 1.10.0

Instalacja i konfiguracja MySQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/mysql.pp``
- Zainstaluj bazę danych `MySQL` wykorzystując moduł `Puppet`
- Ustaw hasło dla użytkownika ``root`` na ``mypassword``
- Ustaw nasłuchiwanie serwera ``mysqld`` na wszystkich interfejsach (``0.0.0.0``)
- Stwórz bazę danych ``mydb`` z ``utf-8``
- Stwórz usera ``myusername`` z hasłem ``mypassword``
- Nadaj wszystkie uprawnienia dla usera ``myusername`` dla bazy ``mydb``
- Ustaw backupowanie bazy danych do ``/tmp/mysql-backup``

Instalacja i konfiguracja Tomcat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/tomcat.pp``
- Zainstaluj język `Java` za pomocą modułu `Puppet`
- Zainstaluj `Tomcat 8` za pomocą `Puppet` w katalogu ``/opt/tomcat8``
- Skonfiguruj dwie instancje `Tomcat` działające jednocześnie:

    - Jedna uruchamiana na domyślnych portach
    - Druga uruchamiana na ``8006`` a connector z portu ``8081`` przekierowywał na ``8443``
    - Na pierwszej uruchom ``war`` z lokacji ``/opt/tomcat8/webapps/docs/appdev/sample/sample.war``
