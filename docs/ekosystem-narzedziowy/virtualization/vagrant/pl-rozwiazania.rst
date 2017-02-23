Vagrant create virtual machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: ruby

    CPU = 2
    RAM = 8196


    Vagrant.configure("2") do |config|
        config.vm.hostname = "ubuntu.local"

        config.vm.box = "ubuntu/xenial64"
        # config.vm.box = "ubuntu-lts"
        # config.vm.box_url = "http://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-vagrant.box"

        config.vm.network :forwarded_port, guest: 80, host: 8888
        config.vm.network :forwarded_port, guest: 443, host: 8443
        config.vm.network :forwarded_port, guest: 7990, host: 7990
        config.vm.network :forwarded_port, guest: 7999, host: 7999
        config.vm.network :forwarded_port, guest: 8080, host: 8080
        config.vm.network :forwarded_port, guest: 8081, host: 8081
        config.vm.network :forwarded_port, guest: 8090, host: 8090
        config.vm.network :forwarded_port, guest: 9000, host: 9000
        config.vm.network :forwarded_port, guest: 3306, host: 3306
        config.vm.network :forwarded_port, guest: 5432, host: 5432
        config.vm.synced_folder ".", "/var/www/src/"

        config.vm.provider "virtualbox" do |v|
            v.name = "ecosystem.local"
            v.cpus = CPU
            v.memory = RAM
        end

    end

Vagrant + Puppet
^^^^^^^^^^^^^^^^

.. code-block:: sh

    cat puppet/manifests/certificates.pp

.. code-block:: puppet

    file { "/etc/ssl/ssl.example.com.cert":
        ensure => present,
        source => "/var/www/host/ssl/ssl.example.com.cert",
    }

    file { "/etc/ssl/ssl.example.com.key":
        ensure => present,
        source => "/var/www/host/ssl/ssl.example.com.key",
    }

.. code-block:: sh

    cat puppet/main.pp

.. code-block:: puppet

    import "manifests/packages.pp"
    import "manifests/users.pp"
    import "manifests/certificates.pp"
    import "manifests/apache.pp"
    import "manifests/hostname.pp"
    import "manifests/mysql.pp"
    import "manifests/tomcat.pp"
