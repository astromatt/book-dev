*****
Tasks
*****


Running
=======
.. code-block:: yaml

    tasks:
      - name: run this command and ignore the result
        shell: /usr/bin/somecommand || /bin/true

.. code-block:: yaml

    tasks:
      - name: run this command and ignore the result
        shell: /usr/bin/somecommand
        ignore_errors: True

.. code-block:: yaml

    tasks:
      - name: Copy ansible inventory file to client
        copy: src=/etc/ansible/hosts dest=/etc/ansible/hosts
                owner=root group=root mode=0644

.. code-block:: yaml
    :caption: Variables can be used in action lines. Suppose you defined a variable called vhost in the vars section

    tasks:
      - name: create a virtual host file for {{ vhost }}
        template:
          src: somefile.j2
          dest: /etc/httpd/conf.d/{{ vhost }}

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


Examples
========

Firewall
--------
.. code-block:: yaml

    - hosts: dbservers
      tasks:
      - name: allow access from 10.0.0.1
        iptables:
          chain: INPUT
          jump: ACCEPT
          source: 10.0.0.1
