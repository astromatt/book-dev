********
OpenLDAP
********


Docker
======
.. code-block:: console

    docker run  \
        --name openldap-server \
        --rm \
        -p 389:389 \
        -p 636:636 \
        --env LDAP_ORGANISATION="My Company" \
        --env LDAP_DOMAIN="my-company.com" \
        --env LDAP_ADMIN_PASSWORD="MyPassword" \
        --volume /home/openldap/data:/var/lib/ldap \
        --volume /home/openldap/config:/etc/ldap/slapd.d \
        osixia/openldap


Docker Compose
==============
#. Create file ``docker-compose.yaml``

    .. code-block:: yaml

        version: '3'

        networks:
            devtools-ecosystem:
                driver: bridge

        services:
            openldap:
                image: osixia/openldap
                container_name: openldap-server
                restart: "no"
                hostname: my-company.com
                environment:
                    - LDAP_ORGANISATION="My Company"
                    - LDAP_DOMAIN="my-company.com"
                    - LDAP_ADMIN_PASSWORD="MyPassword"
                    - LDAP_TLS_CRT_FILENAME="my-ldap.crt"
                    - LDAP_TLS_KEY_FILENAME="my-ldap.key"
                    - LDAP_TLS_CA_CRT_FILENAME="the-ca.crt"
                ports:
                    - "389:389"
                    - "636:636"
                networks:
                    - devtools-ecosystem
                volumes:
                    - /tmp/openldap/data:/var/lib/ldap
                    - /tmp/openldap/config:/etc/ldap/slapd.d
                    - /tmp/openldap/certs:/container/service/slapd/assets/certs

#. Run Jenkins

    .. code-block:: console

        docker-compose up

#. Run Jenkins in background (daemon)

    .. code-block:: console

        docker-compose up -d

Connect
=======
.. code-block:: console

    docker exec openldap ldapsearch -x -H ldap://localhost -b dc=example,dc=org -D "cn=admin,dc=example,dc=org" -w admin

GUI
===
.. code-block:: console

    docker run -p 6443:443 \
        --env PHPLDAPADMIN_LDAP_HOSTS=openldap \
        --detach \
        --rm \
        --name openldap-gui \
        osixia/phpldapadmin
