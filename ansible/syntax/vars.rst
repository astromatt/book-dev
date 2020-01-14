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
