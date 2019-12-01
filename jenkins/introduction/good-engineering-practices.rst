**************************
Good engineering practices
**************************


General
=======
* Skrypt releasowy trzymany w konfiguracji narzędzia
* Instalacja nadmiarowych pluginów
* Korzystanie z pluginów zamiast z linii poleceń
* Przygotowanie środowiska + provisioning
* Spawnowanie agentów w cloud i czas setupu nowego środowiska
* Długość buildów
* Ignorowanie testów ?!
* Skipowanie testów (verbose)
* Budowanie Pull Requestów
* Jak długo trzymać branche?
* Jak automatycznie czyścić branche?
* Budowanie na różnych środowiskach
* Colorful deployments (version names from colors of the first six hexes in Git ref)
* Technology radar: https://www.thoughtworks.com/radar


User Management
===============
* Always use *LDAP* (*OpenLDAP* or *Active Directory*)
* Each tool has separate *LDAP* read only account
* Connection only with *LDAPS* (secure)
* Internal and external users in one *LDAP* server
* Name groups as ``jenkins-users`` or ``jenkins-administrators``
* Local administrator ``jenkins-administrator`` only for fixing bugs with *LDAP*
* Use ``jenkins@example.com`` (for easy email filtering)
* Use ``jenkins.example.com`` as domain name with firewall blocking external access
* Wildcard *SSL* certificate (``*.example.com``)
* Only *HTTPS* access to tool!
* ``/etc/resolv.conf`` ``search example.com`` -> set by *DHCP*
* No nested groups
* All tool access groups in ``OU=ecosystem``
* Use LDAP groups for project roles from ``OU=projects``
* Do not use user accounts in project roles (only *LDAP* groups)
* Confluence page with all ``*-administrators`` + ``mailto:`` links
* Confluence page with *Jira* project leaders
* Confluence page with *Jenkins* job administrators
* Do not use technical accounts (use *SSH* keys)
* Use *SSH* keys with proper comment: ``user@example.com/computer-name``


Plugin installation
===================
* Dependencies hell
* Plugin support (especially those free ones)
* Open Source plugins
* Plugin and upgrades
* Once given out, cannot be easily taken away


Large repos
===========
* is a sign of git missuse, and should be tackled with Git LFS
* Use command line git rather than jGit
* command line git handles memory better
* Use reference repository (bare)
* Shallow clone (Git from 1.9+ can push from shallow clones)
* Don't fetch tags
* Narrow refspec - only clone specific branches (honor refspec on initial clone)
* Pipeline stash / unstash (sparse checkout on master node, and then stash checkout, and unstash on remotes)
* Sparse checkout (Subset of working tree - single directory [exclude or include on per file basis])


Behavioral Driven Tests
=======================
* Spockframework: https://www.youtube.com/watch?v=64jZVsScbU8

.. code-block:: groovy
    :caption: Spock Framework. Source: http://thejavatar.com/testing-with-spock/

    def "should return false if user does not have role required for viewing page"() {
       given:
          // context
          pageRequiresRole Role.ADMIN
          userHasRole Role.USER
       when:
          // some action is performed
          boolean authorized = authorizationService.isUserAuthorizedForPage(user, page)
       then:
          // expect specific result
          authorized == false
    }


Idea
====
* Jenkins odpalający ``git bisect`` i testy dla każdego commita z próby, tak długo aż nie znajdzie problemu
