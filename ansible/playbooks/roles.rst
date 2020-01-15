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
