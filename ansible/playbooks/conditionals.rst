************
Conditionals
************



``with_items``
==============
.. code-block:: yaml
    :caption: Ansible tasks

    - name: install packages
      package: name={{ item }} state=latest
      with_items:
      - git
      - htop
      - nmap


``failed_when``
===============


``changed_when``
================


``until``
=========


``ignore_errors``
=================


