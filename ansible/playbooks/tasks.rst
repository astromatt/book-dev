*****
Tasks
*****

Modules
=======
* Cloud modules
* Clustering modules
* Commands modules
* Crypto modules
* Database modules
* Files modules
* Identity modules
* Inventory modules
* Messaging modules
* Monitoring modules
* Net Tools modules
* Network modules
* Notification modules
* Packaging modules
* Remote Management modules
* Source Control modules
* Storage modules
* System modules
* Utilities modules
* Web Infrastructure modules
* Windows modules

.. note:: More info at: https://docs.ansible.com/ansible/latest/modules/modules_by_category.html#modules-by-category


Install Packages
================

Single Package
--------------
.. code-block:: yaml

    - name: install ntpdate
      package:
        name: ntpdate
        state: present

Install Multiple Packages
-------------------------
.. code-block:: yaml

    - name: install the latest version of Apache and MariaDB
      package:
        name:
          - httpd
          - mariadb-server
        state: latest

Install HTTPd server
--------------------
* In some distributions ``apache`` is named ``httpd``

.. code-block:: yaml
    :caption: This uses a variable as this changes per distribution

    - name: remove the apache package
      package:
        name: "{{ apache }}"
        state: absent

Tasks
-----
.. code-block:: yaml

    - name: "Install Nginx"
      become: yes
      package:
        name: nginx
        state: latest

    - name: "Update Nginx config"
      become: yes
      copy:
        src: ./conf/nginx-conf
        dest: /etc/nginx/nginx.conf
      notify:
        - restart nginx

    - name: "Create sites-available directory"
      become: yes
      file: path=/etc/nginx/sites-available state=directory

    - name: "Create sites-enabled directory"
      become: yes
      file: path=/etc/nginx/sites-enabled state=directory

    - name: "Update Nginx default config"
      become: yes
      copy:
        src: ./conf/nginx-default
        dest: /etc/nginx/sites-available/default
      notify:
        - restart nginx

    - name: "Enable Nginx site config"
      become: yes
      file:
        src: /etc/nginx/sites-available/default
        dest: /etc/nginx/sites-enabled/default
        state: link
      notify:
        - restart nginx

    - name: "Restart nginx"
      become: yes
      service: name=nginx state=restarted


Running Commands
================

Copy
----
.. code-block:: yaml

    - name: Copy ansible inventory file to client
      copy: src=/etc/ansible/hosts dest=/etc/ansible/hosts owner=root group=root mode=0644

.. code-block:: yaml

    - name: Copy ansible inventory file to client
      copy:
        src: /etc/ansible/hosts
        dest: /etc/ansible/hosts
        owner: root
        group: root
        mode: 0644

.. code-block:: yaml
    :caption: Variables can be used in action lines. Suppose you defined a variable called vhost in the vars section

    - name: create a virtual host file for {{ vhost }}
      template:
        src: myfile.j2
        dest: /etc/httpd/conf.d/{{ vhost }}
        owner: root
        group: root
        mode: 0644

Shell
-----
.. code-block:: yaml

    - name: show date
      shell: /bin/date

.. code-block:: yaml

    - name: run this command and ignore the result
      shell: /usr/bin/somecommand || /bin/true

.. code-block:: yaml

    - name: run this command and ignore the result
      shell: /usr/bin/somecommand
      ignore_errors: True

Iptables
--------
.. code-block:: yaml

    - name: allow access from 10.0.0.1
      iptables:
        chain: INPUT
        jump: ACCEPT
        source: 10.0.0.1


Order
=====
* ``inventory`` - The default. The order is ‘as provided’ by the inventory
* ``reverse_inventory`` - As the name implies, this reverses the order ‘as provided’ by the inventory
* ``sorted`` - Hosts are alphabetically sorted by name
* ``reverse_sorted`` - Hosts are sorted by name in reverse alphabetical order
* ``shuffle`` - Hosts are randomly ordered each run

.. code-block:: yaml

    - hosts: all
      order: sorted
      gather_facts: False
      tasks:
        - debug:
            var: inventory_hostname
