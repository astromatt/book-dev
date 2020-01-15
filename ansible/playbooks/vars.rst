****
Vars
****


Definition
==========
Can be defined from:

    * Playbooks
    * Files
    * Inventories (group vars, host vars)
    * Command line
    * Discovered variables (facts)
    * Ansible Tower

.. code-block:: yaml

    # The variables file used by the playbooks in the dbservers group.
    # These don't have to be explicitly imported by vars_files: they are autopopulated.

    mysqlservice: mysqld
    mysql_port: 3306
    dbuser: foouser
    dbname: foodb
    upassword: abc


Environment Variables
=====================
.. code-block:: yaml

    - hosts: all
      remote_user: root

      # here we make a variable named "env" that is a dictionary
      vars:
        env:
           HI: test2
           http_proxy: http://proxy.example.com:8080

      tasks:

        # here we just define the dictionary directly and use it
        # (here $HI is the shell variable as nothing in Ansible will replace it)

        - shell: echo $HI
          environment:
             HI: test1

        # here we are using the "env" map variable above

        - shell: echo $HI
          environment: "{{ env }}"


Best Practices
==============
* Use descriptive unique human-meaningful variable names
* Prefer flat variables over nested

    .. code-block:: yaml
        :caption: Nested variables

        apache:
            startservers: 2
            maxclients: 2

    .. code-block:: yaml
        :caption: Flat variables

        apache_startservers: 2
        apache_maxclients: 2
