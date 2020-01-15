*****
Roles
*****


Ansible Roles
=============
:term:`Ansible Roles` are special kind of :term:`Playbook` that are fully self-contained with:

    * :term:`tasks`
    * :term:`variables`
    * configuration :term:`templates`
    * other supporting files


Ansible Galaxy
==============
* Repository of user defined :term:`Roles`

Example
=======
.. code-block:: yaml

    - name: "Installing packages"
      package: name={{item}} state=installed
      with_items:
      - gunicorn
      - supervisor
      - python-mysqldb
      - python-falcon

    - name: "Making sure supervisor is enabled and started"
      service: name=supervisor state=started enabled=yes

    - name: "Creating the base folder of the application"
      file: path=/opt/myapp state=directory owner=nobody group=nobody mode=0755

    - name: "Copying the application"
      copy: src=../myapp.py dest=/opt/myapp/myapp.py owner=nobody group=nobody mode=0755
      notify:
      - restart-app

    - name: "Copying the supervisor config file"
      template: src=../files/myapp.conf dest=/etc/supervisor/conf.d/myapp.conf owner=nobody group=nobody mode=0644
      notify:
      - reload-config
      - restart-app

    - name: "Adding IP od dbserver to /etc/hosts"
      lineinfile: name=/etc/hosts line="{{ hostvars['dbserver']['ansible_eth0']['ipv4']['address'] }} dbserver"

    handlers:
    - name: reload-config
      shell: supervisorctl reread
    - name: restart-app
      supervisorctl: name=myapp state=restarted


Best Practices
==============
* Keep roles purpose and function focus
* Used a ``roles/`` subdirectory for roles developed for organizational clarity in a single project
* Follow the Ansible Galaxy pattern for roles that are to be shared beyond a single project
* Start your roles with ``ansible-galaxy init`` (it will generate directory structure)
* Remove unneeded directories and stub files (after ``ansible-galaxy init``)
* ``ansible-galaxy`` can point to your internal private repo
* Use ``ansible-galaxy`` to install your roles -- even private ones
* Manage your roles in your applications repo
* As a part of build process, "push" role to artifact repository
* Use ``ansible-galaxy`` to install role from artifact repository
