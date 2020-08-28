*********
SonarQube
*********


Issues
======
* Cykl życia
* Poziom istotności
* Zagadnienia ręczne


Quality Profiles
================
* Reguły jakościowe
* Dostosowanie do potrzeb projektu
* Jednonolita polityka jakościowa
* Zasady dziedziczenia


Quality Gates
=============
* Statusy
* Notyfikacje
* Definiowanie bram


Kokpity
=======
* Widgety


Widoki różnicowe
================
* W zakresie miar
* W zakresie zagadnień


Administracja i bezpieczeństwo
==============================
* Konta użytkowników
* Grupy
* System uprawnień
* Konfiguracje globalne


Rozszerzenia systemu
====================
* Integracja
* Zarządzanie
* Języki
* Analizatory zewnętrzne
* Metryki
* Wizualizacja i raportowanie


Dobre i złe praktyki
====================
* Pre-commit check


Bitbucket Integration
=====================
* Sonar for Bitbucket
* https://www.sonarqube.org/atlassian-bitbucket-integration/
* https://github.com/mibexsoftware/sonar-bitbucket-plugin
* https://marketplace.atlassian.com/apps/1212735/sonar-for-bitbucket-server?hosting=server&tab=overview
* https://ch-mibex-sonar4bitbucket.herokuapp.com/webhook

.. code-block:: json
    :caption: sonar.json

    {
      "sonarHost": "https://sonarcloud.io",
      "sonarProjectKey": "MyProjectKey"
    }


SonarQube Commercial Editions tightly integrate with Atlassian Bitbucket Server so your team can write clean, quality code all day long!

.. figure:: img/sonarqube-integrations-bitbucket-a.png
    :scale: 66%
    :align: center

    Atlassian Bitbucket Server integration [sqbb]_

.. figure:: img/sonarqube-integrations-bitbucket-b.png
    :scale: 50%
    :align: center

    Atlassian Bitbucket Server integration [sqbb]_

.. figure:: img/sonarqube-integrations-bitbucket-c.png
    :scale: 75%
    :align: center

    Atlassian Bitbucket Server integration [sqbb]_


Project News and Updates
========================
* https://www.sonarqube.org/whats-new/


Roadmap
=======
The 8.x LTS, which is expected in early 2021, will add significant value in the areas of security, operability, integration, and Python analysis.

**Security**
For the 7.9 LTS we entered the SAST (Static Application Security Testing) arena with taint analysis rules for Java, C#, and PHP, and Hotspots for those languages plus another three. For the 8.x LTS, we’ll expand that offering with more rules and more languages. Expect to see taint analysis expanded to Python, C++, C, JavaScript, and TypeScript, and expect to see the range of covered vulnerabilities expand too. We’ll also add more Hotspot rules and make the Hotspot concept more intuitive and easier to use. (Because not everything that might be a Vulnerability actually is a Vulnerability.)

**Python**
Speaking of Python, we’re planning to really bring it this year. Expect top-notch analysis with high-value rules - quality and security - out of the box, no other tools required.

**Integration**
We’ve done a good job so far providing integrations with major ALM and CI/CD tool chains, but “good” isn’t good enough. By the end of 2020, we expect to have seamless integration - both on-prem and in the cloud - with GitHub, Azure, BitBucket, and GitLab, as well as making it easier to get all your code (branches) analyzed via Jenkins.

**Operability**
On the DevOps side, we’ll make life easier with an official, supported Docker Scanner image, as well as an official, supported image for each SonarQube edition. On top of that, we’ll add support for an orchestration system such as Kubernetes monitoring geographical (active/passive) redundancy

**And more...**
As usual, we’ll add plenty of smaller features too. A sampling of the current short-list: tests as first-class citizens (e.g. analyzed with “real” rules), support for mono repos, and Portfolio branches.


References
==========
.. [sqbb] https://www.sonarqube.org/atlassian-bitbucket-integration/
