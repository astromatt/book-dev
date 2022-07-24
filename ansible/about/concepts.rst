**************
Basic Concepts
**************


Core concepts
=============
* Human readable configuration files
* Tasks executed in order
* Configuration management
* Workflow orchestration
* App deployment
* Agentless architecture (no need to install anything on managed nodes)
* Uses OpenSSH
* Secure
* Playbooks
* Make change only when needed (if there was a change)
* Changes can be incremental or wholesale
* Schedule tasks daily, weekly, or monthly
* Perform regular state check and validation
* Automate backup and restore


Control node
============
* Any machine with Ansible installed.
* You can run commands and playbooks, invoking ``/usr/bin/ansible`` or ``/usr/bin/ansible-playbook``, from any control node.
* You can use any computer that has Python installed on it as a control node - laptops, shared desktops, and servers can all run Ansible.
* However, you cannot use a Windows machine as a control node.
* You can have multiple control nodes.


Managed nodes
=============
* The network devices (and/or servers) you manage with Ansible.
* Managed nodes are also sometimes called "hosts".
* Ansible is not installed on managed nodes.


Inventory
=========
* Filename: ``hosts``
* A list of managed nodes.
* An inventory file is also sometimes called a "hostfile".
* Your inventory can specify information like IP address for each managed node.
* An inventory can also organize managed nodes, creating and nesting groups for easier scaling.
* Default inventory file location ``/etc/ansible/hosts``
* If any other location, then specify ``ansible -i hosts ...`` for file named: ``hosts``
* `More info <https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html>`_

.. code-block:: ini
    :caption: Inventory file named ``hosts``

    [dbservers]
    db01.example.com
    db02.example.com

    [webservers]
    10.13.37.1
    10.13.37.2
    10.13.37.3


Modules
=======
* The units of code Ansible executes.
* Each module has a particular use, from administering users on a specific type of database to managing VLAN interfaces on a specific type of network device.
* You can invoke a single module with a task, or invoke several different modules in a playbook.

Categories:

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

More info at: https://docs.ansible.com/ansible/latest/modules/modules_by_category.html#modules-by-category


Tasks
=====
* The units of action in Ansible.
* You can execute a single task once with an ad-hoc command.

.. code-block:: yaml
    :caption: Ansible tasks

    - name: Install
      package: name=nginx state=latest


Roles
=====
* Specialized list of commands to perform

.. code-block:: yaml
    :caption: Ansible tasks

        - name: Install
          package: name=nginx state=latest

        - name: Configuration
          template: src=nginx.conf dest=/etc/nginx/http.d/default.conf

        - name: Setup
          file: path=/var/www state=directory owner=myuser group=www-data mode=755

        - name: Enable
          service: name=nginx enabled=yes

        - name: Start
          command: nginx -c /etc/nginx/nginx.conf


Playbook
========
* Ordered lists of tasks, saved so you can run those tasks in that order repeatedly.
* Playbooks can include variables as well as tasks.
* Playbooks are written in YAML and are easy to read, write, share and understand.

.. code-block:: yaml
    :caption: ``nginx.yaml`` (ansible playbook)

    - name: Install and configure nginx
      hosts: all
      become: yes
      vars:
        http_port: 80
      tasks:
        - name: Install
          package: name=nginx state=latest
        - name: Configuration
          template: src=nginx.conf dest=/etc/nginx/http.d/default.conf
        - name: Setup
          file: path=/var/www state=directory owner=myuser group=www-data mode=755
        - name: Enable
          service: name=nginx enabled=yes
        - name: Start
          command: nginx -c /etc/nginx/nginx.conf


Templates
=========
* Jinja2 templates
* Similar to Django templates

.. code-block:: jinja

    <ul>
    {% for item in sequence %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
