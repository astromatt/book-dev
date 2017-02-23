Puppet package installation
---------------------------
.. code-block:: sh

    cat /etc/puppet/manifests/packages.pp

Method 1
^^^^^^^^
.. code-block:: puppet

    exec { 'package definition update':
        command => '/usr/bin/apt-get update',
    }

    package { ['nmap', 'htop', 'git']:
        ensure => 'latest',
        require => Exec['package definition update'],
    }


Method 2
^^^^^^^^
.. code-block:: puppet

    exec { 'package definition update':
      command => '/usr/bin/apt-get update';
    }

    Exec['package definition update'] -> Package <| |>

    package { ['htop', 'nmap', 'git']:
      ensure => present;
    }

Method 3
^^^^^^^^
.. code-block:: puppet

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

Change hostname
---------------
.. code-block:: sh

    cat /etc/puppet/manifests/hostname.pp

Method 1
^^^^^^^^
.. code-block:: puppet

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

Method 2
^^^^^^^^
.. code-block:: puppet

    exec { 'set hostname':
        command => '/usr/bin/hostnamectl set-hostname ecosystem.local'
    }

Users, Groups and Directories management
----------------------------------------
.. code-block:: puppet

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

Puppet Apache2 installation
---------------------------
.. code-block:: sh

    puppet module install apache
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout self-signed.key -out self-signed.cert
    cat /etc/puppet/manifests/apache.pp

.. code-block:: puppet

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

.. code-block:: sh

    puppet apply /etc/puppet/manifests/apache.pp
    ls /var/www
    cat /etc/apache2/sites-enabled/*

Puppet MySQL installation and configuration
-------------------------------------------
.. code-block:: puppet

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

Puppet Tomcat installation and configuration
--------------------------------------------
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

    tomcat::war { 'sample.war':
      catalina_base => '/opt/tomcat8/first',
      war_source    => '/opt/tomcat8/webapps/docs/appdev/sample/sample.war',
    }
