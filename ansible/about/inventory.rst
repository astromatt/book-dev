*********
Inventory
*********


What is Inventory?
==================
* Static lines of servers
* Ranges
* Other custom things (generated automatically)
* Dynamic lists of servers: AWS, Azure, Google Cloud Platform


Static hosts
============
* Create file ``hosts``
* Roles are defined in square brackets
* Hosts are below roles
* There are two default groups: all and ungrouped.
* The all group contains every host.
* The ungrouped group contains all hosts that don’t have another group aside from all

INI format
==========

Simple list
-----------
.. code-block:: ini
    :caption: ``cat hosts``

    [myhost]
    127.0.0.1

.. code-block:: ini
    :caption: ``cat hosts``

    [dbservers]
    db01.staging.example.com
    db02.staging.example.com

    [appservers]
    app01.staging.example.com
    app02.staging.example.com
    app03.staging.example.com

.. code-block:: ini

    [dc1]
    db01.test.example.com
    app01.test.example.com

    [dc2]
    db02.test.example.com

Range
-----
.. code-block:: ini
    :caption: Range

    [myservers]
    www[01:50].example.com

    [databases]
    db-[a:f].example.com

.. code-block:: ini

    ~(web|db).*\.example\.com

Host variables
--------------
.. code-block:: ini

    [myservers]
    host1 http_port=80 maxRequestsPerChild=808
    host2 http_port=303 maxRequestsPerChild=909

.. code-block:: ini

    [myservers]
    localhost                ansible_connection=local
    other1.example.com       ansible_connection=ssh        ansible_user=myuser
    other2.example.com:2222  ansible_connection=ssh        ansible_user=myotheruser

.. code-block:: ini

    some_host         ansible_port=2222     ansible_user=manager
    aws_host          ansible_ssh_private_key_file=/home/example/.ssh/aws.pem
    freebsd_host      ansible_python_interpreter=/usr/local/bin/python
    ruby_module_host  ansible_ruby_interpreter=/usr/bin/ruby.1.9.3

Inventory aliases
-----------------
* In the above example, running Ansible against the host alias "jumper" will connect to 192.0.2.50 on port 5555.
* This only works for hosts with static IPs, or when you are connecting through tunnels.

.. code-block:: ini

    jumper ansible_port=5555 ansible_host=192.0.2.50

Group variables
---------------
.. code-block:: ini

    [myservers]
    host1
    host2

    [myservers:vars]
    ntp_server=ntp.myhost.example.com
    proxy=proxy.myhost.example.com

.. code-block:: ini

    [atlanta]
    host1
    host2

    [raleigh]
    host2
    host3

    [southeast:children]
    atlanta
    raleigh

    [southeast:vars]
    some_server=foo.southeast.example.com
    halon_system_timeout=30
    self_destruct_countdown=60
    escape_pods=2

    [usa:children]
    southeast
    northeast
    southwest
    northwest


YAML format
===========
.. code-block:: yaml

    all:
      hosts:
        mail.example.com:
      children:
        myservers:
          hosts:
            foo.example.com:
            bar.example.com:
        databases:
          hosts:
            one.example.com:
            two.example.com:
            three.example.com:

.. code-block:: yaml

    all:
      hosts:
        mail.example.com:
      children:
        myservers:
          hosts:
            foo.example.com:
            bar.example.com:
        databases:
          hosts:
            one.example.com:
            two.example.com:
            three.example.com:
        dev:
          hosts:
            foo.example.com:
            one.example.com:
            two.example.com:
        test:
          hosts:
            bar.example.com:
            three.example.com:
        prod:
          hosts:
            foo.example.com:
            one.example.com:
            two.example.com:

Host variables
--------------
.. code-block:: yaml

    atlanta:
      host1:
        http_port: 80
        maxRequestsPerChild: 808
      host2:
        http_port: 303
        maxRequestsPerChild: 909

Inventory aliases
-----------------
* In the above example, running Ansible against the host alias “jumper” will connect to 192.0.2.50 on port 5555.
* This only works for hosts with static IPs, or when you are connecting through tunnels.

.. code-block:: yaml

    ...
      hosts:
        jumper:
          ansible_port: 5555
          ansible_host: 192.0.2.50

Group variables
---------------
.. code-block:: yaml

    myservers:
      hosts:
        host1:
        host2:
      vars:
        ntp_server: ntp.myhost.example.com
        proxy: proxy.myhost.example.com


Files
=====
* You can store variables in the main inventory file
* Storing separate host and group variables files may help you organize your variable values more easily
* Host and group variable files must use YAML syntax
* Valid file extensions include ``.yml``, ``.yaml``, ``.json``, or no file extension.
* Ansible loads host and group variable files by searching paths relative to the inventory file or the playbook file
* If your inventory file at ``/etc/ansible/hosts`` contains a host named ‘foosball’ that belongs to two groups, ``raleigh`` and ``webservers``, that host will use variables in YAML files at the following locations:

.. code-block:: text
    :caption: Filenames can optionally end in ``.yml``, ``.yaml``, or ``.json``

    /etc/ansible/group_vars/raleigh
    /etc/ansible/group_vars/webservers
    /etc/ansible/host_vars/foosball

.. code-block:: yaml

    ntp_server: acme.example.org
    database_server: storage.example.org

* You can also add ``group_vars/`` and ``host_vars/`` directories to your playbook directory
* The ``ansible-playbook`` command looks for these directories in the current working directory by default
* Other Ansible commands (for example, ``ansible``, ``ansible-console``, etc.) will only look for ``group_vars/`` and ``host_vars/`` in the inventory directory
* If you want other commands to load group and host variables from a playbook directory, you must provide the ``--playbook-dir`` option on the command line
* If you load inventory files from both the playbook directory and the inventory directory, variables in the playbook directory will override variables set in the inventory directory


Connection Parameters
=====================
* https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters


Docker
======
.. code-block:: yaml

    - name: create jenkins container
      docker_container:
        docker_host: myserver.net:4243
        name: my_jenkins
        image: jenkins

    - name: add container to inventory
      add_host:
        name: my_jenkins
        ansible_connection: docker
        ansible_docker_extra_args: "--tlsverify --tlscacert=/path/to/ca.pem --tlscert=/path/to/client-cert.pem --tlskey=/path/to/client-key.pem -H=tcp://myserver.net:4243"
        ansible_user: jenkins
      changed_when: false

    - name: create directory for ssh keys
      delegate_to: my_jenkins
      file:
        path: "/var/jenkins_home/.ssh/jupiter"
        state: directory
