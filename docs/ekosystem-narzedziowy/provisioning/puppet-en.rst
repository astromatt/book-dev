Tasks to solve
==============

Puppet package installation
---------------------------
- Create manifest in ``/etc/puppet/manifests/packages.pp``
- `Puppet` should install those packages:

    - ``nmap``
    - ``htop``
    - ``git``

- Make sure that ``apt-get update`` command is run before

Hostname change
---------------
- Create manifest in ``/etc/puppet/manifests/hostname.pp``
- Using manifest change the hostname to ``ecosystem.local``
- Make sure that command ``hostname`` returns valid output
- Make sure that ``hostname`` do not restores to default after reboot

Users, Groups and Directories management
----------------------------------------
- Create manifest in ``/etc/puppet/manifests/users.pp``
- Make suer group ``mygroup`` exists and has ``gid=99``
- Make sure user ``myuser`` exists and has ``uid=1337`` and belongs to ``mygroup``
- Make sure:

    - Directory ``/var/www`` exists
    - Owner is set to ``myuser``
    - Group is set to ``mygroup``
    - Has ``rwxr-xr-x`` permissions

Puppet Apache2 installation
---------------------------
- Create manifest in ``/etc/puppet/manifests/apache.pp``
- Install and confugure `Apache 2` using `Puppet` module
- Using terminal generate self-signed OpenSSL certificates and put them in ``/etc/ssl/``:

    - ``/etc/ssl/ssl.example.com.cert``
    - ``/etc/ssl/ssl.example.com.key``

- Using `Puppet` create two vhosts:

    - ``insecure.example.com`` using port ``80`` and with document root in ``/var/www/insecure.example.com``
    - ``ssl.example.com` using port ``443`` with document root in ``/var/www/ssl.example.com`` using certificates from ``/etc/ssl/``

- Create file:

    - ``/var/www/insecure.example.com/index.html`` with content ``Ehlo World! - Insecure``
    - ``/var/www/ssl.example.com/index.html`` with content ``Ehlo World! - SSL!``

- Run browser on your localhost:

    - http://127.0.0.1:8080
    - https://127.0.0.1:8443

Puppet MySQL installation and configuration
-------------------------------------------
- Create manifest in ``/etc/puppet/manifests/mysql.pp``
- Install `MySQL` database using `Puppet` module
- Set ``root`` password to ``mypassword``
- Set ``mysqld`` to listen on all interfaces (``0.0.0.0``)
- Create database ``mydb`` with ``utf-8``
- Create user ``myusername`` with password ``mypassword``
- Grant all privileges to ``myusername`` for ``mydb``
- Setup database backup to ``/tmp/mysql-backup``

Puppet Tomcat installation and configuration
--------------------------------------------
- Create manifest in ``/etc/puppet/manifests/mysql.pp``
- Install `Java` using `Puppet` module
- Install `Tomcat 8` using `Puppet` module in ``/opt/tomcat8``
- Configure to `Tomcat` instances running simultanously on your hostname:

    - One instance is running on default ports
    - Another instance is using ``8006`` port for connector and ``8081`` to redirect to ``8443``
    - On the first instance deploy `WAR` from ``/opt/tomcat8/webapps/docs/appdev/sample/sample.war``

