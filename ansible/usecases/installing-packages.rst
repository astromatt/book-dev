*******************
Installing Packages
*******************


Package
=======
.. code-block:: yaml

    - name: install ntpdate
      package:
        name: ntpdate
        state: present

.. code-block:: yaml
    :caption: This uses a variable as this changes per distribution.

    - name: remove the apache package
      package:
        name: "{{ apache }}"
        state: absent

.. code-block:: yaml

    - name: install the latest version of Apache and MariaDB
      package:
        name:
          - httpd
          - mariadb-server
        state: latest
