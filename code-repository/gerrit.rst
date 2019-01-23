******
Gerrit
******

.. todo:: Blokujące code review

Install
=======
.. code-block:: console

    $ docker run --rm --name gerrit -d -p 8001:8080 gerritcodereview/gerrit

Using persistent volumes
------------------------

:docker-compose.yml:
    .. code-block:: yaml

        version: '3'

        services:
          gerrit:
            image: gerritcodereview/gerrit
            volumes:
               - git-volume:/var/gerrit/git
               - db-volume:/var/gerrit/db
               - index-volume:/var/gerrit/index
               - cache-volume:/var/gerrit/cache
            ports:
               - "8022:29418"
               - "8001:8080"

        volumes:
          git-volume:
          db-volume:
          index-volume:
          cache-volume:

.. code-block:: console

    $ docker-compose up

Using Gerrit in production
--------------------------
* https://github.com/GerritCodeReview/docker-gerrit

:docker-compose.yml:
    .. code-block:: yaml

        version: '3'

        services:
          gerrit:
            image: gerritcodereview/gerrit
            ports:
              - "29418:29418"
              - "80:8080"
            links:
              - postgres
            depends_on:
              - postgres
              - ldap
            volumes:
             - /external/gerrit/etc:/var/gerrit/etc
             - /external/gerrit/git:/var/gerrit/git
             - /external/gerrit/index:/var/gerrit/index
             - /external/gerrit/cache:/var/gerrit/cache
        #    entrypoint: java -jar /var/gerrit/bin/gerrit.war init -d /var/gerrit

          postgres:
            image: postgres:9.6
            environment:
              - POSTGRES_USER=gerrit
              - POSTGRES_PASSWORD=secret
              - POSTGRES_DB=reviewdb
            volumes:
              - /external/gerrit/postgres:/var/lib/postgresql/data

          ldap:
            image: osixia/openldap
            ports:
              - "389:389"
              - "636:636"
            environment:
              - LDAP_ADMIN_PASSWORD=secret
            volumes:
              - /external/gerrit/ldap/var:/var/lib/ldap
              - /external/gerrit/ldap/etc:/etc/ldap/slapd.d

          ldap-admin:
            image: osixia/phpldapadmin
            ports:
              - "6443:443"
            environment:
              - PHPLDAPADMIN_LDAP_HOSTS=ldap

:/external/gerrit/etc/gerrit.config:
    .. code-block:: ini

        [gerrit]
          basePath = git
          canonicalWebUrl = http://localhost

        [database]
          type = postgresql
          hostname = postgres
          database = reviewdb
          username = gerrit

        [index]
          type = LUCENE

        [auth]
          type = ldap
          gitBasicAuth = true

        [ldap]
          server = ldap://ldap
          username=cn=admin,dc=example,dc=org
          accountBase = dc=example,dc=org
          accountPattern = (&(objectClass=person)(uid=${username}))
          accountFullName = displayName
          accountEmailAddress = mail

        [sendemail]
          smtpServer = localhost

        [sshd]
          listenAddress = *:29418

        [httpd]
          listenUrl = http://*:8080/

        [cache]
          directory = cache

        [container]
          user = root

:/external/gerrit/etc/secure.config:
    .. code-block:: ini

        [database]
          password = secret

        [ldap]
          password = secret


Using with Jenkins
==================
* Jenkins ``Gerrit Trigger`` plugin


