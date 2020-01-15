*****
Tests
*****


Debug
=====
.. code-block:: yaml

    - debug:
        msg: "This always displays"

    - debug:
        msg: "This only displays with ansible-playbook -vv+"
        verbosity: 2


Smoke Tests
===========
* You can use ``waitfor`` module
* You can use logfile and regexp expressions

.. code-block:: yaml

    - name: check for proper response
      uri:
        url: http://localhost:8080/
        return_content: yes
      register: result
      until: '"Hello World" in result.content'
      retries: 10
      delay: 1


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


References
==========
* https://docs.ansible.com/ansible/latest/reference_appendices/test_strategies.html
* https://docs.ansible.com/ansible/latest/dev_guide/testing/sanity/index.html
