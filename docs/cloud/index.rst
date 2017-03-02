Introduction
============

.. contents::

Wprowadzenie do technologii i platform chmurowych
-------------------------------------------------
- zapoznanie uczestników z podstawowymi pojęciami oraz standardami związanymi z chmurami obliczeniowymi,
- zapoznanie z dobrymi praktykami,
- wprowadzenie w problematykę projektowania rozproszonych aplikacji opartych na infrastrukturze chmury obliczeniowej,
- przybliżenie zagadnień związanych z usługami chmury Amazon Web Services. Szkolenie kładzie główny nacisk na architekturę i projektowanie systemów. Składa się z teoretycznych prezentacji dobrych praktyk i przykładowych systemów oraz praktycznych warsztatów z projektowania systemów. W programie są także ćwiczenia z podstaw konfiguracji i administracji kluczowymi usługami w chmurze – ćwiczenia te mają na celu zapoznanie od strony praktycznej z podstawowymi usługami i wprowadzenie w kontekst techniczny (jednak nie jest to szkolenie z administracji usługami AWS).
- Wprowadzenie do tworzenia aplikacji na Heroku i Google App Engine
- Porównanie platform Amazon AWS, Heroku, Google App Engine
- IaaS, PaaS, SaaS

Określenie potrzeb i wybór platformy
------------------------------------
-  PaaS, IaaS, SaaS
-  jakie są dostępne platformy?
-  jakie mam potrzeby?
-  jak dobrać odpowiednią platformę do moich potrzeb?
-  szczegółowa charakterystyka PaaS, Iaas, SaaS

.. figure:: ../../_static/img/cloud-devops.png
    :scale: 50%
    :align: center

    Cloud DevOps

Przykłady platform
------------------

IaaS
^^^^
-  Google Compute Engine
-  Amazon AWS
-  Rackspace
-  ecloud24
-  Open Stack

PaaS
^^^^
-  Github Pages
-  Google App Engine
-  Heroku
-  Cloudera
-  Open Shift

SaaS
^^^^
- Force
- Google Apps

Inne \*aaS
----------
-  Data
-  Security
-  Logging
-  Payment


Ekosystem narzędziowy a cloud
-----------------------------
-  CI/CD: Travis, Bitbucket, CircleCI
-  IM: Rocket, HipChat, Slack
-  SCM: Github, Bitbucket
-  Service Discovery

   -  server side, client side
   -  DNS, Amazon ELB, Route 53, Netflix Eureka (client side), własne
      rozwiązania

-  Load Ballancing: Elastic Load Ballancers (AWS)
-  Service Catallogue
-  Authentication: OAuth
-  Messaging: Kafka, Hermes

Distributed Logging
^^^^^^^^^^^^^^^^^^^
-  Elastic Search
-  Logstash
-  Kibana

Hearthbeat detecting
^^^^^^^^^^^^^^^^^^^^
- statsd + graphite (Grafana)
- pingdom

Monitoring
^^^^^^^^^^
- new relic
- nagios
- zabbix
- `tessera <http://tessera-metrics.github.io/tessera/>`_ - dashboard statystyk z Graphite
- `selena <https://github.com/allegro/selena>`_

Alerting
^^^^^^^^
- `cabot <http://cabotapp.com>`_

Bazy danych
^^^^^^^^^^^
-  Document: MongoDB
-  RDBMS: PostgreSQL, MySQL, Oracle, MSSQL
-  KV: Redis
-  Graph: neo4j

Kontenery i wirtualizacja
^^^^^^^^^^^^^^^^^^^^^^^^^
-  Vagrant
-  Docker
-  Rockit
-  Mesos, Swarm, Kubernetes

Netflix
^^^^^^^
-  chaos gorilla
-  chaos monkey
-  hystrix

Service Discovery
^^^^^^^^^^^^^^^^^
-  DNS
-  AWS Elastic Load Balancer
-  Własne usługi

Configuration
^^^^^^^^^^^^^
-  Zookeeper
