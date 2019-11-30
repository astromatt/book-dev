*************
Jenkins Setup
*************




Installation
============
* https://github.com/jenkinsci/docker/blob/master/README.md

Installing on Docker
--------------------
#. Set-up environment:

    .. code-block:: console

        $ mkdir -p /home/jenkins
        $ chmod 777 /home/jenkins
        $ chmod 777 /var/run/docker.sock

#. Run Docker container:

    .. code-block:: console

        $ docker run \
            --detach  \
            --name jenkins \
            --rm \
            --publish 8100:8080 \
            --volume /home/jenkins:/var/jenkins_home \
            --volume /var/run/docker.sock:/var/run/docker.sock \
            jenkins/jenkins

#. Get admin password:

    .. code-block:: console

        $ cat /home/jenkins/secrets/initialAdminPassword


Installing using Docker Compose
-------------------------------
#. Create ``/home/jenkins.yaml``:

    .. code-block:: yaml
        :caption: ``jenkins.yaml``

        version: '3'

        networks:
            ecosystem:
                driver: bridge

        services:
            jenkins:
                image: jenkins/jenkins
                container_name: jenkins
                restart: "no"
                ports:
                    - "8100:8080"
                networks:
                    - ecosystem
                volumes:
                    - /home/jenkins:/var/jenkins_home/
                    - /var/run/docker.sock:/var/run/docker.sock

#. Run Jenkins

    .. code-block:: console

        $ cd /home/
        $ docker-compose -f jenkins.yaml up --detach


Configuration
=============

User Management
---------------
- Always use *LDAP* (*OpenLDAP* or *Active Directory*)
- Each tool has separate *LDAP* read only account
- Connection only with *LDAPS* (secure)
- Internal and external users in one *LDAP* server
- Name groups as ``jenkins-users`` or ``jenkins-administrators``
- Local administrator ``jenkins-administrator`` only for fixing bugs with *LDAP*
- Use ``jenkins@example.com`` (for easy email filtering)
- Use ``jenkins.example.com`` as domain name with firewall blocking external access
- Wildcard *SSL* certificate (``*.example.com``)
- Only *HTTPS* access to tool!
- ``/etc/resolv.conf`` ``search example.com`` -> set by *DHCP*
- No nested groups
- All tool access groups in ``OU=ecosystem``
- Use LDAP groups for project roles from ``OU=projects``
- Do not use user accounts in project roles (only *LDAP* groups)
- Confluence page with all ``*-administrators`` + ``mailto:`` links
- Confluence page with *Jira* project leaders
- Confluence page with *Jenkins* job administrators
- Do not use technical accounts (use *SSH* keys)
- Use *SSH* keys with proper comment: ``user@example.com/computer-name``

Plugin installation
-------------------
- Dependencies hell
- Plugin support (especially those free ones)
- Open Source plugins
- Plugin and upgrades
- Once given out, cannot be easily taken away
