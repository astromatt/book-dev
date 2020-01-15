*****
Usage
*****


Arguments
=========
.. code-block:: text

    usage: ansible [-h] [--version] [-v] [-b] [--become-method BECOME_METHOD]
                   [--become-user BECOME_USER] [-K] [-i INVENTORY] [--list-hosts]
                   [-l SUBSET] [-P POLL_INTERVAL] [-B SECONDS] [-o] [-t TREE] [-k]
                   [--private-key PRIVATE_KEY_FILE] [-u REMOTE_USER]
                   [-c CONNECTION] [-T TIMEOUT]
                   [--ssh-common-args SSH_COMMON_ARGS]
                   [--sftp-extra-args SFTP_EXTRA_ARGS]
                   [--scp-extra-args SCP_EXTRA_ARGS]
                   [--ssh-extra-args SSH_EXTRA_ARGS] [-C] [--syntax-check] [-D]
                   [-e EXTRA_VARS] [--vault-id VAULT_IDS]
                   [--ask-vault-pass | --vault-password-file VAULT_PASSWORD_FILES]
                   [-f FORKS] [-M MODULE_PATH] [--playbook-dir BASEDIR]
                   [-a MODULE_ARGS] [-m MODULE_NAME]
                   pattern

Positional arguments
====================
* Define and run a single task 'playbook' against a set of hosts

.. code-block:: text

      pattern               host pattern

Optional arguments
==================
.. code-block:: text

      --ask-vault-pass      ask for vault password
      --list-hosts          outputs a list of matching hosts; does not execute
                            anything else
      --playbook-dir BASEDIR
                            Since this tool does not use playbooks, use this as a
                            substitute playbook directory.This sets the relative
                            path for many features including roles/ group_vars/
                            etc.
      --syntax-check        perform a syntax check on the playbook, but do not
                            execute it
      --vault-id VAULT_IDS  the vault identity to use
      --vault-password-file VAULT_PASSWORD_FILES
                            vault password file
      --version             show program's version number, config file location,
                            configured module search path, module location,
                            executable location and exit
      -B SECONDS, --background SECONDS
                            run asynchronously, failing after X seconds
                            (default=N/A)
      -C, --check           don't make any changes; instead, try to predict some
                            of the changes that may occur
      -D, --diff            when changing (small) files and templates, show the
                            differences in those files; works great with --check
      -M MODULE_PATH, --module-path MODULE_PATH
                            prepend colon-separated path(s) to module library (def
                            ault=~/.ansible/plugins/modules:/usr/share/ansible/plu
                            gins/modules)
      -P POLL_INTERVAL, --poll POLL_INTERVAL
                            set the poll interval if using -B (default=15)
      -a MODULE_ARGS, --args MODULE_ARGS
                            module arguments
      -e EXTRA_VARS, --extra-vars EXTRA_VARS
                            set additional variables as key=value or YAML/JSON, if
                            filename prepend with @
      -f FORKS, --forks FORKS
                            specify number of parallel processes to use
                            (default=5)
      -h, --help            show this help message and exit
      -i INVENTORY, --inventory INVENTORY, --inventory-file INVENTORY
                            specify inventory host path or comma separated host
                            list. --inventory-file is deprecated
      -l SUBSET, --limit SUBSET
                            further limit selected hosts to an additional pattern
      -m MODULE_NAME, --module-name MODULE_NAME
                            module name to execute (default=command)
      -o, --one-line        condense output
      -t TREE, --tree TREE  log output to this directory
      -v, --verbose         verbose mode (-vvv for more, -vvvv to enable
                            connection debugging)

Privilege Escalation Options
============================
* control how and which user you become as on target hosts

.. code-block:: text

      --become-method BECOME_METHOD
                            privilege escalation method to use (default=sudo), use
                            `ansible-doc -t become -l` to list valid choices.
      --become-user BECOME_USER
                            run operations as this user (default=root)
      -K, --ask-become-pass
                            ask for privilege escalation password
      -b, --become          run operations with become (does not imply password
                            prompting)

Connection Options
==================
* control as whom and how to connect to hosts

.. code-block:: text

      --private-key PRIVATE_KEY_FILE, --key-file PRIVATE_KEY_FILE
                            use this file to authenticate the connection
      --scp-extra-args SCP_EXTRA_ARGS
                            specify extra arguments to pass to scp only (e.g. -l)
      --sftp-extra-args SFTP_EXTRA_ARGS
                            specify extra arguments to pass to sftp only (e.g. -f,
                            -l)
      --ssh-common-args SSH_COMMON_ARGS
                            specify common arguments to pass to sftp/scp/ssh (e.g.
                            ProxyCommand)
      --ssh-extra-args SSH_EXTRA_ARGS
                            specify extra arguments to pass to ssh only (e.g. -R)
      -T TIMEOUT, --timeout TIMEOUT
                            override the connection timeout in seconds
                            (default=10)
      -c CONNECTION, --connection CONNECTION
                            connection type to use (default=smart)
      -k, --ask-pass        ask for connection password
      -u REMOTE_USER, --user REMOTE_USER
                            connect as this user (default=None)

Config
======
* ``/etc/ansible/ansible.cfg`` – Config file, used if present
* ``~/.ansible.cfg`` – User config file, overrides the default config if present


Ansible Pull
============
* The ansible-pull is a small script that will checkout a repo of configuration instructions from git, and then run ``ansible-playbook`` against that content.

.. code-block:: yaml

    # ansible-pull setup
    #
    # on remote hosts, set up ansible to run periodically using the latest code
    # from a particular checkout, in pull based fashion, inverting Ansible's
    # usual push-based operating mode.
    #
    # This particular pull based mode is ideal for:
    #
    # (A) massive scale out
    # (B) continual system remediation
    ---

    - hosts: pull_mode_hosts
      remote_user: root

      vars:

        # schedule is fed directly to cron
        schedule: '*/15 * * * *'

        # User to run ansible-pull as from cron
        cron_user: root

        # File that ansible will use for logs
        logfile: /var/log/ansible-pull.log

        # Directory to where repository will be cloned
        workdir: /var/lib/ansible/local

        # Repository to check out
        # repo must contain a local.yml file at top level
        repo_url: git://github.com/myuser/ansible-playbooks.git

      tasks:

        - name: Install ansible
          apt: pkg=ansible state=installed

        - name: Create local directory to work from
          file: path={{workdir}} state=directory owner=root group=root mode=0751

        - name: Copy ansible inventory file to client
          copy: src=/etc/ansible/hosts dest=/etc/ansible/hosts
                  owner=root group=root mode=0644

        - name: Create crontab entry to clone/pull git repository
          template: src=templates/etc_cron.d_ansible-pull.j2 dest=/etc/cron.d/ansible-pull owner=root group=root mode=0644

        - name: Create logrotate entry for ansible-pull.log
          template: src=templates/etc_logrotate.d_ansible-pull.j2 dest=/etc/logrotate.d/ansible-pull owner=root group=root mode=0644
