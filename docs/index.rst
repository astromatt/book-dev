***************
DevOps Workshop
***************

Author
======

:name: `Matt Harasymczuk <http://astrotech.io>`_
:email: `devops@astrotech.io <mailto:devops@astrotech.io>`_
:www: `http://www.astrotech.io <http://astrotech.io>`_
:facebook: `https://facebook.com/matt.harasymczuk <https://facebook.com/matt.harasymczuk>`_
:linkedin: `https://linkedin.com/in/mattharasymczuk <https://linkedin.com/in/mattharasymczuk>`_

TODO
====
- instalkach i tekst na certyfikaty


1. Jenkins Job DSL and cloud slaves (approx. 0.5 day):

- Groovy basics
- Jenkins Job DSL plugin and its ecosystem
- Job DSL and it's testing
- On Demand cloud slaves with jClouds

2. Continuous Delivery (approx. 1 day):

- Strategies and best practices of defining Continuous Delivery in an organization
- Technologies and processes supporting Continuous Delivery
- High level of parallelism in Continuous Delivery
- Attention will be paid to how automated testing is embedded in the pipeline and the cycle speed

3. Microservices and Docker (approx. 1 day):

- Microservices basics - why? how? what?
- Docker:

    - introduction to containers and Docker
    - Docker images and repositories
    - Working with container
    - Building images using Dockerfile
    - Running containers as services, administration and security of containers
    - Management of interconnected containers using Docker Compose and SystemD g) Introduction to clustering

4. DevOps in the cloud (approx. 0.5 day):

- IaaS vs PaaS
- IaaS examples:

    - Amazon (i.e. EC2)
    - Google Cloud

- PaaS examples:

    - CloudFoundry
    - Heroku

5. Automation of infrastructure and Infrastructure as a Code (IaaC) (approx. 1 day):

- Vagrant
- Ansible
- Puppet (and comparison with Ansible)
- Terraform

6. Tematy z ankiety:

- Groovy, Job DSL, Docker, AWS
- ogolnego spojrzenia na szeroki aspekt tematow, podpowiedzi jakie rozwiazania beda pasowac do naszych potrzeb
- Puppet, Chef, Ansible
- ekosystem narzędziowy
- Tworzenie środowisk przy pomocy dockera
- Best practices. Przykłady rzeczywiste.
- Provisioning środowiska
- Podstawy Powershella
- automatyzacja w Jenkins, best practices
- Architektura Microservices


Wstęp
=====

.. toctree::
    :maxdepth: 3
    :numbered:
    :caption: Wstęp

    wstep/wstep.rst
    wstep/agile-vs-devops.rst
    wstep/backlog-transformacji.rst
    wstep/community.rst

Proces wytwarzania oprogramowania
=================================

.. toctree::
    :maxdepth: 3
    :numbered:
    :caption: Proces wytwarzania oprogramowania

    proces-wytwarzania-oprogramowania/wstep.rst
    proces-wytwarzania-oprogramowania/standardy-projektu.rst
    proces-wytwarzania-oprogramowania/wersjonowanie.rst
    proces-wytwarzania-oprogramowania/procesy-ci-cd.rst
    proces-wytwarzania-oprogramowania/standardy-pracy-zespolu.rst
    proces-wytwarzania-oprogramowania/jakosc-oprogramowania.rst
    proces-wytwarzania-oprogramowania/user-centric-design.rst
    proces-wytwarzania-oprogramowania/dobre-praktyki.rst
    proces-wytwarzania-oprogramowania/zarzadzanie-zmiana.rst
    proces-wytwarzania-oprogramowania/polityki-bezpieczenstwa.rst

Zalaczniki
==========

.. toctree::
    :maxdepth: 3
    :numbered:
    :caption: Zalaczniki

    zalaczniki/manifest-agile.rst
    zalaczniki/scrum.rst
    zalaczniki/technologie.rst
    zalaczniki/stawianie-srodowiska.rst

.. toctree::
    :maxdepth: 3
    :numbered:
    :caption: Rozwiązania

    rozwiazania/_.rst

Ekosystem narzędziowy
=====================

.. toctree::
    :maxdepth: 2
    :caption: Ekosystem

    ekosystem-narzedziowy/index.rst
