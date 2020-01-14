********
Handlers
********

.. glossary::

    Handlers
        Running Operations On Change


Definition
==========
.. code-block:: yaml

    handlers:

        - name: restart memcached
          service:
            name: memcached
            state: restarted

        - name: restart apache
          service:
            name: apache
            state: restarted

Usage
=====
.. code-block:: yaml

    - name: template configuration file
      template:
        src: template.j2
        dest: /etc/foo.conf
      notify:
         - restart memcached
         - restart apache

Examples
========
.. code-block:: yaml

    tasks:
      - name: Set host variables based on distribution
        include_vars: "{{ ansible_facts.distribution }}.yml"

    handlers:
      - name: restart web service
        service:
          name: "{{ web_service_name | default('httpd') }}"
          state: restarted

.. code-block:: yaml

    tasks:
        - name: restart everything
          command: echo "this task will restart the web services"
          notify: "restart web services"

    handlers:

        - name: restart memcached
          service:
            name: memcached
            state: restarted
          listen: "restart web services"

        - name: restart apache
          service:
            name: apache
            state: restarted
          listen: "restart web services"
