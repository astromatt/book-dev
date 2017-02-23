Installation and Confugration
-----------------------------
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
    - Druga uruchamiana na 8006 a connector z portu 8081 przekierowywał na 8443
    - Na pierwszej uruchom WAR z lokacji ``/opt/tomcat8/webapps/docs/appdev/sample/sample.war``

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
