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


I. Jenkins Job DSL and cloud slaves (approx. 0.5 day)
1. Groovy basics
2. Jenkins Job DSL plugin and its ecosystem
3. Job DSL and it's testing
4. On Demand cloud slaves with jClouds

II. Continuous Delivery (approx. 1 day)
1. Strategies and best practices of defining Continuous Delivery in an organization
2. Technologies and processes supporting Continuous Delivery
3. High level of parallelism in Continuous Delivery
4. Attention will be paid to how automated testing is embedded in the pipeline and the cycle speed

III. Microservices and Docker (approx. 1 day) 1. Microservices basics - why? how? what? 2. Docker
a) introduction to containers and Docker
b) Docker images and repositories
c) Working with container
d) Building images using Dockerfile
e) Running containers as services, administration and security of containers
f) Management of interconnected containers using Docker Compose and SystemD g) Introduction to clustering

IV. DevOps in the cloud (approx. 0.5 day)
1. IaaS vs PaaS
2. IaaS examples: Amazon (i.e. EC2), Google Cloud 3. PaaS examples: CloudFoundry, Heroku
V. Automation of infrastructure and Infrastructure as a Code (IaaC) (approx. 1 day) 1. Vagrant
2. Ansible
3. Puppet (and comparison with Ansible)
4. Terraform



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
