Puppet
======

.. todo:: sprawdzić czy działają tematy związane z tworzeniem faktów
.. todo:: sprawdzić jak zachowa się to z Facter
.. todo:: sprawdzić deklarowanie i używanie zmiennych
.. todo:: podzielić Puppet na osobne pliki per temat (zadanie do rozwiązania)
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

    file { "/var/www":
        ensure => "directory",
        owner => "www-data",
        group => "www-data",
        mode  => "0755",
    }

.. code-block:: ruby

    exec { "package definition update":
        command => "/usr/bin/apt update",
    }

    package { ["nmap", "htop", "git"]:
        ensure => "latest",
        require => Exec["package definition update"],
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

Templates
---------
* ERB templates

Comment
^^^^^^^
.. code-block:: erb

    <%# This is a comment. %>

Variables
^^^^^^^^^
There are two ways to access variables in an ERB template:

.. code-block:: erb

    @variable

.. code-block:: erb

    scope["variable"]

Example:

    .. code-block:: erb

        scope["ntp::tinker"]

Printing variables
^^^^^^^^^^^^^^^^^^
.. code-block:: erb

    ServerName <%= @fqdn %>
    ServerAlias <%= @hostname %>

If
^^
.. code-block:: text

    if <CONDITION>
      ... code ...
    elsif <CONDITION>
      ... other code ...
    end

.. code-block:: erb

    <% if @broadcast != "NONE" %>
        broadcast <%= @broadcast %>
    <% end %>

For
^^^
.. code-block:: erb

    <% @values.each do |val| -%>
        Some stuff with <%= val %>
    <% end -%>

If $values was set to ["one", "two"], this example would produce:

.. code-block:: text

    Some stuff with one
    Some stuff with two


Instalacja i konfiguracja
-------------------------
.. code-block:: console

    sudo apt update
    sudo apt install puppet

Zaglądnij do katalogu ``/etc/puppet``.
Co się tam znajduje?

Jeżeli nie ma katalogu ``/etc/puppet/manifests`` to go stwórz.

    .. code-block:: console

        mkdir -p /etc/puppet/manifests

Przejdź do katalogu ``/etc/puppet/manifests``, jeżeli.

.. warning:: Uwaga, puppet od wersji 4 ma inną składnię. W Ubuntu 16.04 (LTS) instaluje się Puppet 3.8.5. Wersja ta może być niekompatybilna z modułami pobieranymi przez Puppet (np. Apache, Tomcat, Java). Rozwiązaniem jest ściąganie modułów w niższych wersjach (pasujących do wersji 3.8.5) lub instalacja Puppet w wersji wyższej niż ta w LTS.

    .. code-block:: console

        # Instalacja puppet w ostatniej wersji

        # Yum-based systems (np. Enterprise Linux 7)
        sudo rpm -Uvh https://yum.puppet.com/puppet5/puppet5-release-el-7.noarch.rpm
        sudo yum -y install puppet-agent
        export PATH=/opt/puppetlabs/bin:$PATH

        # Apt-based systems (np. Ubuntu 16.04 Xenial Xerus)
        wget https://apt.puppetlabs.com/puppet5-release-xenial.deb
        sudo dpkg -i puppet5-release-xenial.deb
        sudo apt update
        sudo apt -y install puppet-agent
        export PATH=/opt/puppetlabs/bin:$PATH

Resources
---------

File
^^^^
.. code-block:: ruby

    file { "resource title":
      path                    => # (namevar) The path to the file to manage.  Must be fully...
      ensure                  => # Whether the file should exist, and if so what...
      backup                  => # Whether (and how) file content should be backed...
      checksum                => # The checksum type to use when determining...
      checksum_value          => # The checksum of the source contents. Only md5...
      content                 => # The desired contents of a file, as a string...
      ctime                   => # A read-only state to check the file ctime. On...
      force                   => # Perform the file operation even if it will...
      group                   => # Which group should own the file.  Argument can...
      ignore                  => # A parameter which omits action on files matching
      links                   => # How to handle links during file actions.  During
      mode                    => # The desired permissions mode for the file, in...
      mtime                   => # A read-only state to check the file mtime. On...
      owner                   => # The user to whom the file should belong....
      provider                => # The specific backend to use for this `file...
      purge                   => # Whether unmanaged files should be purged. This...
      recurse                 => # Whether to recursively manage the _contents_ of...
      recurselimit            => # How far Puppet should descend into...
      replace                 => # Whether to replace a file or symlink that...
      selinux_ignore_defaults => # If this is set then Puppet will not ask SELinux...
      selrange                => # What the SELinux range component of the context...
      selrole                 => # What the SELinux role component of the context...
      seltype                 => # What the SELinux type component of the context...
      seluser                 => # What the SELinux user component of the context...
      show_diff               => # Whether to display differences when the file...
      source                  => # A source file, which will be copied into place...
      source_permissions      => # Whether (and how) Puppet should copy owner...
      sourceselect            => # Whether to copy all valid sources, or just the...
      target                  => # The target for creating a link.  Currently...
      type                    => # A read-only state to check the file...
      validate_cmd            => # A command for validating the file's syntax...
      validate_replacement    => # The replacement string in a `validate_cmd` that...
      # ...plus any applicable metaparameters.
    }

ensure

(Property: This attribute represents concrete state on the target system.)

Whether the file should exist, and if so what kind of file it should be. Possible values are present, absent, file, directory, and link.

:present: accepts any form of file existence, and creates a normal file if the file is missing. (The file will have no content unless the content or source attribute is used.)
:absent: ensures the file doesn’t exist, and deletes it if necessary.
:file: ensures it’s a normal file, and enables use of the content or source attribute.
:directory: ensures it’s a directory, and enables use of the source, recurse, recurselimit, ignore, and purge attributes.
:link: ensures the file is a symlink, and requires that you also set the target attribute. Symlinks are supported on all Posix systems and on Windows Vista / 2008 and higher. On Windows, managing symlinks requires Puppet agent’s user account to have the “Create Symbolic Links” privilege; this can be configured in the “User Rights Assignment” section in the Windows policy editor. By default, Puppet agent runs as the Administrator account, which has this privilege.


.. code-block:: ruby

    # Equivalent resources:

    file { "/etc/inetd.conf":
      ensure => "/etc/inet/inetd.conf",
    }

    file { "/etc/inetd.conf":
      ensure => link,
      target => "/etc/inet/inetd.conf",
    }


HTTPS problem
-------------
Gdyby wystąpił problem z certyfikatem ``ssl`` przy instalacji modułów należy:

- postaw maszynę w Amazonie (Ubuntu LTS)
- zainstaluj squid

.. code-block:: console

    sudo apt update
    sudo apt install squid

- na maszynie gościa (tam gdzie chcesz instalować moduł Puppet ustaw:


.. code-block:: console

    export http_proxy=http://<IP>:3128
    export https_proxy=http://<IP>:3128

Lub:

.. code-block:: ini

    [user]
    http_proxy = http://<IP>:3128
    https_proxy = http://<IP>:3128

.. code-block:: console

    sudo service puppet restart
    sudo su -
    puppet module install


Narzędzia pomocnicze
--------------------

Facter
^^^^^^
Przyjrzyj się wynikom poleceń:

.. code-block:: console

    facter
    facter ipaddress
    facter lsbdistdescription

Co zauważyłeś? Jak można wykorzystać te informacje?

Kod przedstawia wynik polecenia ``facter`` na świeżej maszynie `Ubuntu` postawionej w `Amazon AWS`

.. literal-include:: src/facter.txt
    :language: console

Korzystanie z faktów w manifestach:

:Sposób klasyczny, jako zmienne na głównym poziomie:

.. code-block:: ruby

    # Definicja
    operatingsystem = "Ubuntu"

    # Wykorzystanie
    case $::operatingsystem {
      "CentOS": { include centos }
      "MacOS":  { include mac }
    }

:Jako zmienne w tablicy faktów:

.. code-block:: ruby

    # Definicja
    $facts["fact_name"] = "Ubuntu"

    # Wykorzystanie
    case $facts["fact_name"] {
      "CentOS": { include centos }
      "MacOS":  { include mac }
    }

Tworzenie nowych faktów:

.. code-block:: ruby

    require "facter"

    Facter.add(:system_role) do
      setcode "cat /etc/system_role"
    end

.. code-block:: ruby

    require "facter"

    Facter.add(:system_role) do
      setcode do
        Facter::Util::Resolution.exec("cat /etc/system_role")
      end
    end

Druga metoda tworzenia faktów:

.. code-block:: console

    export FACTER_system_role=$(cat /etc/system_role); facter

Hiera
^^^^^
* ``/etc/puppet/hiera.yaml``

.. code-block:: yaml

    ---
    :backends:
      - yaml

    :hierarchy:
      - "nodes/%{::fqdn}"
      - "roles/%{::role}"
      - common

    :yaml:
      :datadir: /etc/puppet/hiera/

    :logging:
      - console

.. code-block:: yaml

    nginx::nginx_servers:
         "devops-alldomains":
             server_name:
                 - "~^(?<fqdn>.+?)$"
             www_root: "/var/www/$fqdn"
             index_files:
                 - "index.php"
             try_files:
                 - "$uri"
                 - "$uri/"
                 - "/index.php?$args"
             access_log: "/var/log/nginx/devops-alldomains-access.log"
             error_log: "/var/log/nginx/devops-alldomains-error.log"

         "devops-alldomains-ssl":
             server_name:
                 - "~^(?<fqdn>.+?)$"
             listen_port: "443"
             ssl_port: "443"
             www_root: "/var/www/$fqdn"
             ssl: true
             ssl_key: "/etc/ssl/www/$fqdn.key"
             ssl_cert: "/etc/ssl/www/$fqdn.crt"
             index_files:
                 - "index.php"
             try_files:
                 - "$uri"
                 - "$uri/"
                 - "/index.php?$args"
             access_log: "/var/log/nginx/devops-alldomains-access-ssl.log"
             error_log: "/var/log/nginx/devops-alldomains-error-ssl.log"

     nginx::nginx_locations:
         "devops-alldomains-loc":
             location: "~ \.php$"
             www_root: "/var/www/$fqdn"
             server: "devops-alldomains"
             fastcgi: "unix:/var/run/php7-fpm.sock"
             fastcgi_split_path: "^(.+\.php)(/.*)$"
             fastcgi_index: "index.php"
             fastcgi_param:
                 "SCRIPT_FILENAME": "$document_root$fastcgi_script_name"

         "devops-alldomains-ssl-loc":
             location: "~ \.php$"
             www_root: "/var/www/$fqdn"
             server: "devops-alldomains-ssl"
             ssl: true
             ssl_only: true
             fastcgi: "unix:/var/run/php7-fpm.sock"
             fastcgi_split_path: "^(.+\.php)(/.*)$"
             fastcgi_index: "index.php"
             fastcgi_param:
                 "SCRIPT_FILENAME": "$document_root$fastcgi_script_name"

Augias
^^^^^^


Przykłady
---------
.. code-block:: ruby

    Exec {
        path => "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }

    group { "www-data":
        ensure => present
    }

    user { "www-data":
        ensure => present,
        gid => "www-data"
    }

    exec { "update package definition":
        command => "/usr/bin/apt update"
    }

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
        "postgresql-client",
        "postgresql",
        "postgresql-server-dev-all",
        "libmemcached-dev"
      ] :
        ensure => latest,
        require => Exec["update package definition"],
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
        owner => "www-data",
        group => "www-data",
        mode => "0755",
    }

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
        mode => "0755",
    }

    file { "/var/www/database":
        ensure => directory,
        owner => "vagrant",
        group => "vagrant",
        mode => "0700",
    }

    service { "nginx":
        ensure => running,
        enable => true,
        require => Package["nginx"],
    }

    service { "uwsgi":
        ensure => running,
        enable => true,
        require => [Package["uwsgi"], Exec["python requirements"], File["/var/www/tmp"]],
    }

    file { "/etc/nginx/sites-enabled/default":
        content => template("/var/www/src/conf/nginx.conf"),
        require => Package["nginx"],
        notify => Service["nginx"],
        ensure => file,
    }

    file { "/etc/uwsgi/apps-enabled/default.ini":
        content => template("/var/www/src/conf/uwsgi.ini"),
        require => Package["uwsgi"],
        notify => Service["uwsgi"],
        ensure => file,
    }

    exec { "python requirements":
        command => "pip3 install -r /var/www/src/requirements.txt",
        require => Package["python3-pip", "python3-dev", "libmemcached-dev", "postgresql-9.3", "postgresql-server-dev-9.3"],
    }

    exec { "collectstatic":
        command => "python3 /var/www/src/manage.py collectstatic --noinput",
        require => Exec["python requirements"],
    }

    # postgres
    # updatedb

Unless
^^^^^^
.. code-block:: ruby

    exec { "set hostname":
        command => "/bin/hostname -F /etc/hostname",
        unless  => "/usr/bin/test $(hostname) = $(/bin/cat /etc/hostname)",
    }

Podmiana zawartości w pliku
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: ruby

    file { "/tmp/my-file.pp":
        ensure  => present,
        owner   => root,
        group   => root,
        mode    => "0644",
        content => "Lorem ipsum...\n",
    }

Moduły
------
.. code-block:: console

    puppet module search apache
    puppet module install puppetlabs-apache

Java
^^^^
.. code-block:: ruby

    class { "java" :
      package => "java-1.8.0-openjdk-devel",
    }

.. code-block:: ruby

    java::oracle { "jdk8" :
      ensure  => "present",
      version => "8",
      java_se => "jdk",
    }

.. code-block:: ruby

    java::oracle { "jdk8" :
      ensure  => "present",
      version_major => "8u101",
      version_minor => "b13",
      java_se => "jdk",
    }

JBoss
^^^^^
* https://github.com/coi-gov-pl/puppet-jboss

To install JBoss Application Server you can use just, it will install Wildfly 8.2.0.Final by default:

.. code-block:: ruby

    include jboss

To install JBoss EAP or older JBoss AS use:

.. code-block:: ruby

    class { "jboss":
      product => "jboss-eap",
      version => "6.4.0.GA",
    }

or use hiera:

.. code-block:: ruby

    jboss::params::product: "jboss-as"
    jboss::params::version: "7.1.1.Final"

.. code-block:: ruby

    $user = "jb-user"
    $passwd = "SeC3eT!1"

    node "controller" {
      include jboss::domain::controller
      include jboss
      jboss::user { $user:
        ensure   => "present",
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
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/code/packages.pp``
- Zainstaluj następujące pakiety za pomocą `Puppet`:

    - ``nmap``
    - ``htop``
    - ``git``

- Upewnij się by `Puppet` wykonał polecenie ``apt update`` na początku

Zmiana hostname
^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/code/hostname.pp``
- Za pomocą manifestu zmień hostname maszyny na ``ecosystem.local``
- Upewnij się, że po wpisaniu polecenia ``hostname`` będzie ustawiona na odpowiednią wartość
- (jeżeli korzystasz z Vagrant) Upewnij się, że hostname nie przywróci się do domyślnej wartości po ponownym uruchomieniu
- Hostname zmienia się na dwa sposoby:

    * podmiana zawartości pliku ``/etc/hostname`` i uruchomienie ``hostname -F /etc/hostname``
    * uruchomienie polecenia ``hostnamectl set-hostname ...``

Zarządzanie użytkownikami, grupami i katalogami
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/code/jenkins.pp``
- Upewnij się, że użytkownik ``jenkins`` istnieje, ma ``uid=1337`` i należy do grupy ``jenkins``
- Upewnij się, że grupa ``jenkins`` istnieje i ma ``gid=1337``
- Upewnij się, że:

    - Katalog ``/home/jenkins`` istnieje
    - Właścicielem jego jest user ``jenkins``
    - Właścicielem jego jest grupa ``jenkins``
    - Ma uprawnienia ``rwxr-xr-x``

Konfiguracja nginx
^^^^^^^^^^^^^^^^^^
- Za pomocą Puppet upewnij się by był użytkownik ``www-data`` i miał ``uid=33``
- Za pomocą Puppet upewnij się by była grupa ``www-data`` i miała ``gid=33``
- Upewnij się że katalog ``/var/www`` istnieje i właścicielem jego są user ``www-data`` i grupa ``www-data`` i że ma uprawnienia ``rwxr-xr-x``
- Zainstaluj i skonfiguruj ``nginx`` wykorzystując moduł Puppet
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

Konfiguracja Apache2 (opcjonalnie)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

.. warning:: Uwaga, puppet od wersji 4 ma inną składnię. W Ubuntu 16.04 (LTS) instaluje się Puppet 3.8.5. Puppet module instaluje zawsze najnowszą (w tym wypadku niekompatybilną z naszym Puppet)! Aby zainstalować apache należy wymusić odpowiednią wersję (ostatnia supportująca Puppet 3.8 to 1.10.

    .. code-block:: console

        $ puppet module install puppetlabs-apache --version 1.10.0

Instalacja i konfiguracja MySQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/code/mysql.pp``
- Zainstaluj bazę danych `MySQL` wykorzystując moduł `Puppet`
- Ustaw hasło dla użytkownika ``root`` na ``mypassword``
- Ustaw nasłuchiwanie serwera ``mysqld`` na wszystkich interfejsach (``0.0.0.0``)
- Stwórz bazę danych ``mydb`` z ``utf-8``
- Stwórz usera ``myusername`` z hasłem ``mypassword``
- Nadaj wszystkie uprawnienia dla usera ``myusername`` dla bazy ``mydb``
- Ustaw backupowanie bazy danych do ``/tmp/mysql-backup``

Instalacja i konfiguracja Tomcat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Manifest do tego zadania zapisz w pliku ``/etc/puppet/code/tomcat.pp``
- Zainstaluj język `Java` za pomocą modułu `Puppet`
- Zainstaluj `Tomcat 8` za pomocą `Puppet` w katalogu ``/opt/tomcat8``
- Skonfiguruj dwie instancje `Tomcat` działające jednocześnie:

    - Jedna uruchamiana na domyślnych portach
    - Druga uruchamiana na ``8006`` a connector z portu ``8081`` przekierowywał na ``8443``
    - Na pierwszej uruchom ``war`` z lokacji ``/opt/tomcat8/webapps/docs/appdev/sample/sample.war``
