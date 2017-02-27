Puppet
======

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

    file {
      '/var/www':
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

* facts
* manifests (pliki z rozszerzeniem ``.pp``)
* classes
* resources

Puppet language
^^^^^^^^^^^^^^^
* DSL
* rubby
* ruby ERD templates



Instalacja i konfiguracja
-------------------------
.. code-block:: sh

    sudo apt-get install puppet

Zaglądnij do katalogu ``/etc/puppet``.
Co się tam znajduje?

Przejdź do katalogu ``/etc/puppet/manifests``.

HTTPS problem
-------------
Gdyby wystąpił problem z certyfikatem ``ssl`` przy instalacji modułów należy:

- postaw maszynę w Amazonie (Ubuntu LTS)
- zainstaluj squid

.. code-block:: sh

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


.. code-block:: ruby

    # facter
    architecture => i386
    ...
    ipaddress => 172.16.182.129
    is_virtual => true
    kernel => Linux
    kernelmajversion => 2.6
    ...
    operatingsystem => CentOS
    operatingsystemrelease => 5.5
    physicalprocessorcount => 0
    processor0 => Intel(R) Core(TM)2 Duo CPU     P8800  @ 2.66GHz
    processorcount => 1
    productname => VMware Virtual Platform
    ...

Korzystanie z faktów w manifestach:

.. code-block:: ruby

    # Classic
    $fact_name

    # new
    $facts['fact_name']

.. code-block:: ruby

    case $::operatingsystem {
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


JBoss
-----
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

Moduły
------

puppet

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


.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie 1 - Instalacja pakietów za pomocą Puppet

    exec { 'package definition update':
        command => '/usr/bin/apt-get update',
    }

    package { ['nmap', 'htop', 'git']:
        ensure => 'latest',
        require => Exec['package definition update'],
    }

.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie 2 - Instalacja pakietów za pomocą Puppet

    exec { 'package definition update':
      command => '/usr/bin/apt-get update';
    }

    Exec['package definition update'] -> Package <| |>

    package { ['htop', 'nmap', 'git']:
      ensure => present;
    }

.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie 3 - Instalacja pakietów za pomocą Puppet

    exec { 'package definition update':
      command => '/usr/bin/apt-get update',
    }

    Exec['package definition update'] -> Package <| |>

    package { 'htop':
        ensure => 'latest',
    }

    package { 'nmap':
        ensure => 'latest',
    }

    package { 'git':
        ensure => 'latest',
    }


Zmiana hostname
^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/hostname.pp``
- Za pomocą manifestu zmień hostname maszyny na ``ecosystem.local``
- Upewnij się, że po wpisaniu polecenia ``hostname`` będzie ustawiona na odpowiednią wartość
- Upewnij się, że hostname nie przywróci się do domyślnej wartości po ponownym uruchomieniu


.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie 1 - Zmiana hostname

    file { "/etc/hostname":
            ensure  => present,
            owner   => root,
            group   => root,
            mode    => '0644',
            content => "ecosystem.local\n",
            notify  => Exec["set hostname"],
    }

    exec { "set hostname":
            command => '/bin/hostname -F /etc/hostname',
            unless  => "/usr/bin/test `hostname` = `/bin/cat /etc/hostname`",
    }


.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie 2 - Zmiana hostname

    exec { 'set hostname':
        command => '/usr/bin/hostnamectl set-hostname ecosystem.local'
    }


Zarządzanie użytkownikami, grupami i katalogami
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/users.pp``
- Upewnij się, że użytkownik ``myuser`` istnieje, ma ``uid=1337`` i należy do grupy ``mygroup``
- Upewnij się, że grupa ``mygroup`` istnieje i ma ``gid=99``
- Upewnij się, że:

    - Katalog ``/var/www`` istnieje
    - Właścicielem jego jest user ``myuser``
    - Właścicielem jego jest grupa ``mygroup``
    - Ma uprawnienia ``rwxr-xr-x``

.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie - Zarządzanie użytkownikami, grupami i katalogami

    group { 'mygroup':
        ensure => 'present',
        gid    => 99,
    }

    user { 'myuser':
        ensure           => 'present',
        groups           => ['mygroup'],
        home             => '/home/myuser',
        password         => '*',
        password_max_age => 99999,
        password_min_age => 0,
        shell            => '/usr/sbin/nologin',
        uid              => 1337,
    }

    file { '/var/www':
        ensure => 'directory',
        owner  => 'myuser',
        group  => 'mygroup',
        mode   => 0755
    }


Konfiguracja Apache2
^^^^^^^^^^^^^^^^^^^^
- Za pomocą Puppet upewnij się by był użytkownik ``www-data`` i miał ``uid=33``
- Za pomocą Puppet upewnij się by była grupa ``www-data`` i miała ``gid=33``
- Upewnij się że katalog ``/var/www`` istnieje i właścicielem jego są user ``www-data`` i grupa ``www-data`` i że ma uprawnienia ``rwxr-xr-x``
- Zainstaluj i skonfiguruj Apache2 wykorzystując moduł Puppet
- Z terminala wygeneruj certyfikaty self signed OpenSSL (``.cert`` i ``.key``) (za pomocą i umieść je w ``/etc/ssl/``)
- Za pomocą Puppet Stwórz dwa vhosty:

    - ``insecure.example.com`` na porcie 80 i z katalogiem domowym ``/var/www/insecure.example.com``
    - ``ssl.example.com`` na porcie 443 i z katalogiem domowym ``/var/www/ssl.example.com`` + używanie certyfikatów SSL wcześniej wygenerowanych

- Stwórz pliki z treścią:

    - ``/var/www/insecure.example.com/index.html`` z treścią ``Ehlo World! - Insecure``
    - ``/var/www/ssl.example.com/index.html`` z treścią ``Ehlo World! - SSL!``

- W przeglądarce na komputerze lokalnym wejdź na stronę:

    - http://127.0.0.1:8080
    - https://127.0.0.1:8443


.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie katalog - Konfiguracja Apache2

    file {
      '/var/www':
        ensure => 'directory',
        owner => 'www-data',
        group => 'www-data',
        mode  => '0755',
    }

.. toggle-code-block:: sh
    :label: Pokaż rozwiązanie terminal - Konfiguracja Apache2

    puppet module install apache
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout self-signed.key -out self-signed.cert
    cat /etc/puppet/manifests/apache.pp

.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie puppet - Konfiguracja Apache2

    class { 'apache':
        default_vhost => false,
    }

    # The non-ssl virtual host
    apache::vhost { 'insecure.example.com':
        servername => 'insecure.example.com',
        port       => 80,
        docroot    => '/var/www/insecure',
    }

    # The SSL virtual host at the same domain
    apache::vhost { 'ssl.example.com':
        servername => 'ssl.example.com',
        port       => 443,
        docroot    => '/var/www/ssl',
        ssl        => true,
        ssl_cert   => '/etc/ssl/ssl.example.com.cert',
        ssl_key    => '/etc/ssl/ssl.example.com.key',
    }

    file { '/var/www/insecure.example.com/index.html':
      ensure  => 'present',
      replace => 'no',
      content => 'Ehlo World! - Insecure\n',
      mode    => 0644,
    }

    file { '/var/www/ssl.example.com/index.html':
      ensure  => 'present',
      replace => 'no',
      content => 'Ehlo World! - SSL\n',
      mode    => 0644,
    }

.. toggle-code-block:: sh
    :label: Pokaż rozwiązanie terminal 2 - Konfiguracja Apache2

    puppet apply /etc/puppet/manifests/apache.pp
    ls /var/www
    cat /etc/apache2/sites-enabled/*



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

.. code-block:: sh
    :label: Pokaż rozwiązanie instalacji pakietu - Instalacja i konfiguracja MySQL

    puppet module install puppetlabs-mysql


.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie manifestu - Instalacja i konfiguracja MySQL

    class { "mysql::server":
        root_password => "mypassword",
        #remove_default_accounts => true,
        override_options => {
            mysqld => {
                "bind_address"  => "0.0.0.0",
            }
        },
        databases => {
          'mydb' => {
            ensure  => 'present',
            charset => 'utf8',
          },
        },
        users => {
          'myusername@%' => {
            ensure          => 'present',
            password_hash   => mysql_password("mypassword"),
          },
        },
        grants => {
          'myusername@%/mydb.*' => {
            ensure      => 'present',
            privileges  => ["all"],
            table       => "mydb.*",
            user        => "myusername@%",
          },
        },
    }

    # Enable MySQL Backups
    class { "mysql::server::backup":
        backupuser      => "myusername",
        backuppassword  => "mypassword",
        backupdir       => "/tmp/mysql_backup",
    }


Instalacja i konfiguracja Tomcat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/tomcat.pp``
- Zainstaluj język `Java` za pomocą modułu `Puppet`
- Zainstaluj `Tomcat 8` za pomocą `Puppet` w katalogu ``/opt/tomcat8``
- Skonfiguruj dwie instancje `Tomcat` działające jednocześnie:

    - Jedna uruchamiana na domyślnych portach
    - Druga uruchamiana na ``8006`` a connector z portu ``8081`` przekierowywał na ``8443``
    - Na pierwszej uruchom ``war`` z lokacji ``/opt/tomcat8/webapps/docs/appdev/sample/sample.war``

.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie manifestu - Instalacja i konfiguracja Tomcat

    class { 'java': }

    tomcat::install { '/opt/tomcat8':
      source_url => 'https://www.apache.org/dist/tomcat/tomcat-8/v8.0.33/bin/apache-tomcat-8.0.33.tar.gz'
    }

    tomcat::instance { 'tomcat8-first':
      catalina_home => '/opt/tomcat8',
      catalina_base => '/opt/tomcat8/first',
    }

    tomcat::instance { 'tomcat8-second':
      catalina_home => '/opt/tomcat8',
      catalina_base => '/opt/tomcat8/second',
    }

    # Change the default port of the second instance server and HTTP connector
    tomcat::config::server { 'tomcat8-second':
      catalina_base => '/opt/tomcat8/second',
      port          => '8006',
    }

    tomcat::config::server::connector { 'tomcat8-second-http':
      catalina_base         => '/opt/tomcat8/second',
      port                  => '8081',
      protocol              => 'HTTP/1.1',
      additional_attributes => {
        'redirectPort' => '8443'
      },
    }

    tomcat::war { 'sample.war':
      catalina_base => '/opt/tomcat8/first',
      war_source    => '/opt/tomcat8/webapps/docs/appdev/sample/sample.war',
    }
