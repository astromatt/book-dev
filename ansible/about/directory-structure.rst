*******************
Directory Structure
*******************


Basic Project
=============
* ``provision.yaml`` for providers

.. code-block:: text

    project
    ├── config.yaml
    ├── inventory
    │   ├── group_vars
    │   ├── host_vars
    │   └── hosts
    ├── provision.yaml
    └── site.yaml

.. code-block:: console
    :caption: Separate provisioning from deployment and configuration tasks

    $ cat site.yaml
    - include: provision.yaml
    - include: configure.yaml


Roles
=====
* Roles should be independent
* ``requirements.yaml`` for Ansible Galaxy dependencies

.. code-block:: text

    project
    ├── config.yaml
    ├── provision.yaml
    ├── roles
    │   └── requirements.yaml
    └── setup.yaml


Other Directories
=================
- files
- filter_plugins
- group_vars
- handlers
- hosts
- playbooks
- roles
- tasks
- vars
