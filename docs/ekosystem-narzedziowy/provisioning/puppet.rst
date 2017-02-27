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

.. code-block:: puppet

    file {
      '/var/www':
        ensure => 'directory',
        owner => 'www-data',
        group => 'www-data',
        mode  => '0755',
    }

.. code-block:: puppet

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

Components
^^^^^^^^^^

* facts
* manifests
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

.. code-block:: puppet

    file {
      '/var/www':
        ensure => 'directory',
        owner => 'www-data',
        group => 'www-data',
        mode  => '0755',
    }

Instalacja i konfiguracja MySQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- zainstaluj moduł bazy MySQL wykorzystując Puppeta
- ustaw hasło roota na mypassword
- ustaw nasłuchiwanie serwera ``mysqld`` na ``0.0.0.0``
- stwórz bazę danych ``mydb`` z ``utf-8``
- stwórz usera ``myusername`` z hasłem ``mypassword``
- nadaj wszystkie uprawnienia dla usera ``myusername`` dla bazy ``mydb``
- ustaw backupowanie bazy danych do ``/tmp/mysql-backup``

.. code-block:: sh

    puppet module install puppetlabs-mysql

.. code-block:: puppet

    # Install and configure MySQL
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

Instalacja Java i Tomcat
^^^^^^^^^^^^^^^^^^^^^^^^
- zainstaluj Javę za pomocą Puppeta
- zainstaluj Tomcat8 za pomocą Puppeta do ``/opt/tomcat8``
- Skonfiguruj dwie instancje Tomcata działające jednocześnie:

    - Jedna uruchamiana na domyślnych portach
    - Druga uruchamiana na ``8006`` a connector z portu ``8081`` przekierowywał na ``8443``
    - Na pierwszej uruchom ``war`` z lokacji ``/opt/tomcat8/webapps/docs/appdev/sample/sample.war``

.. code-block:: sh

    puppet module install puppetlabs/java
    puppet module install puppetlabs/tomcat
    cat /etc/puppet/manifests/tomcat.pp

.. code-block:: puppet

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
    :label: Pokaż rozwiązanie 1

    exec { 'package definition update':
        command => '/usr/bin/apt-get update',
    }

    package { ['nmap', 'htop', 'git']:
        ensure => 'latest',
        require => Exec['package definition update'],
    }

.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie 2

    exec { 'package definition update':
      command => '/usr/bin/apt-get update';
    }

    Exec['package definition update'] -> Package <| |>

    package { ['htop', 'nmap', 'git']:
      ensure => present;
    }

.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie 3

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
    :label: Pokaż rozwiązanie 1

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
    :label: Pokaż rozwiązanie 2

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
    :label: Pokaż rozwiązanie

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

Instalacja i konfiguracja Apache2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/manifests/apache.pp``
- Zainstaluj i skonfiguruj `Apache 2` wykorzystując moduł `Puppet`
- Z terminala wygeneruj certyfikaty self signed OpenSSL i umieść je w ``/etc/ssl/``:

    - ``/etc/ssl/ssl.example.com.cert``
    - ``/etc/ssl/ssl.example.com.key``

- Za pomocą `Puppet` stwórz dwa vhosty:

    - ``insecure.example.com`` na porcie ``80`` i z katalogiem domowym ``/var/www/insecure.example.com``
    - ``ssl.example.com`` na porcie ``443`` i z katalogiem domowym ``/var/www/ssl.example.com`` + używanie certyfikatów SSL wcześniej wygenerowanych

- Stwórz pliki z treścią:

    - ``/var/www/insecure.example.com/index.html`` z treścią ``Ehlo World! - Insecure``
    - ``/var/www/ssl.example.com/index.html`` z treścią ``Ehlo World! - SSL!``

- W przeglądarce na komputerze lokalnym wejdź na stronę:

    - http://127.0.0.1:8080
    - https://127.0.0.1:8443

.. toggle-code-block:: sh
    :label: Pokaż rozwiązanie w terminalu

    puppet module install apache
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout self-signed.key -out self-signed.cert
    cat /etc/puppet/manifests/apache.pp

.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie w puppet

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
    :label: Pokaż rozwiązanie w terminalu

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

.. toggle-code-block:: ruby
    :label: Pokaż rozwiązanie

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
    :label: Pokaż rozwiązanie

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
