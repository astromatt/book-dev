*****************
Program Szkolenia
*****************

.. todo:: stworzyć podział na dni szkolenia i bardziej dokładny opis agendy
.. todo:: stworzyć ankietę nie tylko do poszczególnych osób, ale także do grupy, poziom zaawansowania, zainteresowanie technologiami, doświadczenie zespołu, technologie w których zespół robi, grupa docelowa

Tematy na szkolenie
-------------------

Jenkins Job DSL and cloud slaves
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Groovy basics
- Jenkins Job DSL plugin and its ecosystem
- Job DSL and it's testing
- On Demand cloud slaves with jClouds

Continuous Delivery
^^^^^^^^^^^^^^^^^^^
- Strategies and best practices of defining Continuous Delivery in an organization
- Technologies and processes supporting Continuous Delivery
- High level of parallelism in Continuous Delivery

.. warning:: Attention will be paid to how automated testing is embedded in the pipeline and the cycle speed

Microservices and Docker
^^^^^^^^^^^^^^^^^^^^^^^^
- Microservices basics:

    - why?
    - how?
    - what?

- Docker:

    - introduction to containers and Docker
    - Docker images and repositories
    - Working with container
    - Building images using Dockerfile
    - Running containers as services, administration and security of containers
    - Management of interconnected containers using Docker Compose and SystemD g)
    - Introduction to clustering

DevOps in the cloud
^^^^^^^^^^^^^^^^^^^
- IaaS vs PaaS
- IaaS examples:

    - Amazon (i.e. EC2)
    - Google Cloud

- PaaS examples:

    - CloudFoundry
    - Heroku

Automation of infrastructure and Infrastructure as a Code (IaaC)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Vagrant
- Ansible
- Puppet (and comparison with Ansible)
- Terraform

Dodatkowe tematy
^^^^^^^^^^^^^^^^
- ogolnego spojrzenia na szeroki aspekt tematow, podpowiedzi jakie rozwiazania beda pasowac do naszych potrzeb
- ekosystem narzędziowy
- Tworzenie środowisk przy pomocy dockera
- Best practices. Przykłady rzeczywiste.
- automatyzacja w Jenkins, best practices

- ELK i logowanie (pisanie filtrów Logstash)
- statsd i graphite


Agenda
------

Dzień 1 - Provisioning
^^^^^^^^^^^^^^^^^^^^^^
- Agile i DevOps
- Vagrant
- Puppet
- Git Flow

Dzień 2 - Ecosystem
^^^^^^^^^^^^^^^^^^^
- Stawianie i łączenie narzędzi:

    - Bitbucket
    - Jenkins
    - SonarQube

- Konfiguracja:

    - Budowanie gałęzi Git Flow

Dzień 3 - Cloud
^^^^^^^^^^^^^^^
- Microservices
- IaaS

    - Amazon AWS
    - Google Cloud

- PaaS

    - Heroku
    - Cloud Foundry


Dzień 4 - All together
^^^^^^^^^^^^^^^^^^^^^^
- Docker
- jClouds
- Continuous Delivery
- Ansible
- Terraform
- ELK
- statsd i graphite
