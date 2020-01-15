*****
Tests
*****

* https://docs.ansible.com/ansible/latest/reference_appendices/test_strategies.html
* https://docs.ansible.com/ansible/latest/dev_guide/testing/sanity/index.html


Playbook Syntax
===============
* ``yamllint``
* ``ansible-playbook --syntax-check``
* ``ansible-lint``


Pre-deployment
==============
* ``molecule test`` (integration)
* Run entire Playbook on fresh environment
* Molecule become de-facto standard
* It will be an official Ansible project


Dry Mode
========
* ``ansible-playbook --check`` (against prod)
* ``ansible-playbook -C``
* Run playbook, but do not make modifications


Deployment
==========
* Parallel infrastructure
* Deploy at small subset of servers first
* If deployment succeed, switchover
