********
Examples
********


Single Play
===========
.. code-block:: yaml
    :caption: verify-apache.yml

    - hosts: webservers
      remote_user: root

      vars:
        http_port: 80
        max_clients: 200

      tasks:
      - name: ensure apache is at the latest version
        package:
          name: httpd
          state: latest
      - name: write the apache config file
        template:
          src: /srv/httpd.j2
          dest: /etc/httpd.conf
        notify:
        - restart apache
      - name: ensure apache is running
        service:
          name: httpd
          state: started

      handlers:
        - name: restart apache
          service:
            name: httpd
            state: restarted


Multiple Plays
==============
.. code-block:: yaml

    - hosts: webservers
      remote_user: root
      tasks:
      - name: ensure apache is at the latest version
        package:
          name: httpd
          state: latest
      - name: write the apache config file
        template:
          src: /srv/httpd.j2
          dest: /etc/httpd.conf

    - hosts: databases
      remote_user: root
      tasks:
      - name: ensure postgresql is at the latest version
        package:
          name: postgresql
          state: latest
      - name: ensure that postgresql is started
        service:
          name: postgresql
          state: started
