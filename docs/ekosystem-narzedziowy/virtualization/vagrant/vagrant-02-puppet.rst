Vagrant + Puppet
----------------

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
