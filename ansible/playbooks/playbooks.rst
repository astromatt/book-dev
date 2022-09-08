*********
Playbooks
*********


Concepts
========
* :term:`Playbook` is composed out of :term:`plays`
* :term:`plays` contain :term:`tasks`
* :term:`tasks` call :term:`modules`
* :term:`tasks` run sequentially
* :term:`handlers` are triggered by :term:`tasks`, and are run once, at the end of plays

Run
===
* ``ansible <inventory> -m ...``
* ``ansible-playbook``
* Ansible Tower


Playbook
========
.. code-block:: yaml

    - name: "Install and configure nginx"
      hosts: all
      become: yes

      vars:
        http_port: 80

      tasks:
        - name: "Install"
          package: name=nginx state=latest

        - name: "Configuration"
          template: src=nginx.conf dest=/etc/nginx/http.d/default.conf

        - name: "Setup"
          file: path=/var/www state=directory owner=myuser group=www-data mode=755

        - name: "Enable"
          service: name=nginx enabled=yes

        - name: "Start"
          command: nginx -c /etc/nginx/nginx.conf

.. code-block:: yaml

    - hosts: webservers
      user: root
      become: yes
      tasks:
        - name: add nginx ppa
          action: apt_repository repo=ppa:nginx/stable state=present

        - name: install common packages needed for python application development
          action: apt pkg={{item}} state=installed
          with_items:
            - libpq-dev
            - libmysqlclient-dev
            - libxml2-dev
            - libxslt1-dev
            - mysql-client
            - python-dev
            - python-setuptools
            - python-mysqldb
            - build-essential
            - git
            - nginx

        - name: install various libraries with pip
          action: pip name={{item}} state=present
          with_items:
            - uwsgi

      handlers:
        - name: restart nginx
          service: name=nginx state=restarted

Plays
=====
* Variables in playbook can be used in templates
* Use extension ``.j2`` for ``Jinja2`` templates

.. code-block:: yaml
    :caption: Example Playbook: 1 play, 3 tasks, 1 handler

    - name: install and start apache
      hosts: web
      remote_user: myuser
      become_method: sudo
      become_user: root
      vars:
        http_port: 80
        max_clients: 200

      tasks:
      - name: install httpd
        apt: name=apache2 state=latest
      - name: write apache config file
        template: src=srv/httpd.j2 dest=/etc/httpd.conf
      - name: start httpd
        service: name=httpd state=running

      handlers:
      - name: restart http
        service: name=httpd state=restarted

Tasks
=====
.. code-block:: yaml

    - hosts: dbservers
      tasks:
      - name: allow access from 10.0.0.1
        iptables:
          chain: INPUT
          jump: ACCEPT
          source: 10.0.0.1


Ansible Lint
============
* Rules: https://docs.ansible.com/ansible-lint/rules/default_rules.html

.. code-block:: console
    :caption: Installation

    $ pip3 install ansible-lint

.. code-block:: console
    :caption: Usage

    $ ansible-lint .

.. code-block:: console

    Usage: ansible-lint playbook.yml|roledirectory ...

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -L                    list all the rules
      -q                    quieter, although not silent output
      -p                    parseable output in the format of pep8
      -r RULESDIR           specify one or more rules directories using one or
                            more -r arguments. Any -r flags override the default
                            rules in ['/path/to/ansible-
                            lint/lib/ansiblelint/rules'], unless -R is also used.
      -R                    Use default rules ['/path/to/ansible-
                            lint/lib/ansiblelint/rules'] in addition to any extra
                            rules directories specified with -r. There is no need
                            to specify this if no -r flags are used
      -t TAGS               only check rules whose id/tags match these values
      -T                    list all the tags
      -x SKIP_LIST          only check rules whose id/tags do not match these
                            values
      --exclude=EXCLUDE_PATHS
                            path to directories or files to skip. This option is
                            repeatable.
      --force-color         Try force colored output (relying on ansible's code)
      --nocolor             disable colored output
      -c /path/to/file      Specify configuration file to use.  Defaults to
                              ".ansible-lint"

.. code-block:: yaml
    :caption: Configuration file ``.ansible-lint``

    exclude_paths:
      - ./my/excluded/directory/
      - ./my/other/excluded/directory/
      - ./last/excluded/directory/
    parseable: true
    quiet: true
    rulesdir:
      - ./rule/directory/
    skip_list:
      - skip_this_tag
      - and_this_one_too
      - skip_this_id
      - '401'
    tags:
      - run_this_tag
    use_default_rules: true
    verbosity: 1
