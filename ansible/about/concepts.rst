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


Control node
============
* Any machine with Ansible installed.
* You can run commands and playbooks, invoking /usr/bin/ansible or /usr/bin/ansible-playbook, from any control node.
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
* A list of managed nodes.
* An inventory file is also sometimes called a "hostfile".
* Your inventory can specify information like IP address for each managed node.
* An inventory can also organize managed nodes, creating and nesting groups for easier scaling.


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


Playbooks
=========
* Ordered lists of tasks, saved so you can run those tasks in that order repeatedly.
* Playbooks can include variables as well as tasks.
* Playbooks are written in YAML and are easy to read, write, share and understand.

