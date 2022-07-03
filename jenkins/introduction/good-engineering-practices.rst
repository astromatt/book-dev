**************************
Good engineering practices
**************************


General
=======
* Zawsze trzymaj skrypty releasowe w repozytorium a nie w panelu administracyjnym narzędzia (np. Jenkins, Bamboo, Gitlab)
* Nie instaluj pluginów (najlepiej żadnych dodatkowych)
* Zamiast pluginów korzystaj z uruchamiania tasków z linii poleceń, jest to bardziej przenaszalne oraz w sytuacji awarii systemu CI/CD pozwoli Ci na odtworzenie pipeline ręcznie
* Cała konfiguracja oraz provisioning środowiska powinien być w repozytorium
* Spawnowanie agentów w cloud trwa, czasami lepiej jest trzymać działające hosty niż stawiać je on-demand
* Spawnowanie agentów w docker trwa około 0.05 sekundy (tak, 5 setnych sekundy), lepiej jest tworzyć nowego workera dla każdego builda i nie trzymać ich po zakończeniu
* Testy nie powinny trwać dłużej niż 2-3 minut, bo programiści zmieniają kontekst
* Ignorowane testy powinny być bardzo widocznie zaznaczone, jest to mechanizm awaryjny i nie powinien być nadużywany
* Pull Requesty powinny być budowane i to na nie przeniesie się cały ciężar CI/CD
* Tworzymy jeden branch per User Story, to znaczy, że branche nie powinny być większe niż 1, 3 lub w wyjątkowych okolicznościach 5 dni
* Preferuj używanie feature flags oraz wszystko-do-main
* Automatycznie usuwaj starsze branche niż tydzień
* Buduj na różnych środowiskach aby wykluczyć syndrom "u mnie działa"
* Colorful deployments (version names from colors of the first six hexes in Git ref)
* Technology radar: https://www.thoughtworks.com/radar


User Management
===============
* Always use *LDAP* (*OpenLDAP* or *Active Directory*)
* Each tool has separate *LDAP* read only account
* Connection only with *LDAPS* (secure)
* No nested groups in *LDAP*
* Internal and external users in one *LDAP* server
* All tool access groups in ``OU=ecosystem``
* Use LDAP groups for project roles from ``OU=projects``
* Do not use user accounts in project roles (only *LDAP* groups)
* Create automatically wiki page (via ``cron`` and ``atlassian-python-api``) with all ``*-administrators`` + ``mailto:`` links
* Create automatically wiki page (via ``cron`` and ``atlassian-python-api``) with *Jira* project leaders
* Create automatically wiki page (via ``cron`` and ``atlassian-python-api``) with *Jenkins* job administrators
* Name groups as ``jenkins-users`` or ``jenkins-administrators``
* Use local administrator ``jenkins-administrator`` only for fixing bugs with *LDAP*, nothing else!
* Use email address ``jenkins@example.com`` (for easy email filtering)
* Use domain name ``jenkins.example.com`` with firewall blocking access from external network
* Use wildcard *SSL* certificate (``*.example.com``)
* Use `Let's Encrypt <https://letsencrypt.org>`_ to create a free SSL certificate over generating self-signed
* Use only *HTTPS* access with tools!
* Using *DHCP* add ``search example.com`` to ``/etc/resolv.conf``
* Do not use technical accounts (use *SSH* keys)
* Always use *SSH* keys with proper comment: ``user@example.com/computer-name``


Plugin installation
===================
* Dependencies hell
* Bad plugin support (especially those free ones)
* Open source plugins usually has lagging support
* Plugins usually prevents upgrades to newer version, especially important with security releases
* Once given out, cannot be easily taken away; it is very hard to uninstall plugin


Large repos
===========
* Is a sign of git misuse, and should be handled with Git LFS
* Use command line git rather than jGit
* Command line git handles memory better
* Use reference repository (bare)
* Shallow clone (Git from 1.9+ can push from shallow clones)
* Don't fetch tags
* Narrow refspec - only clone specific branches (honor refspec on initial clone)
* Pipeline stash / unstash (sparse checkout on master node, and then stash checkout, and unstash on remotes)
* Sparse checkout (Subset of working tree - single directory [exclude or include on per file basis])


Behavioral Driven Tests
=======================


Tests
=====
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
