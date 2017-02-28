Cloud
=====

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
-------------------

-  Elastic Search
-  Logstash
-  Kibana / Grafana

Microservices
-------------

Monolithic architecture
~~~~~~~~~~~~~~~~~~~~~~~

Build an application with a monolithic architecture. For example:

-  a single Java WAR file.
-  a single directory hierarchy of Rails or NodeJS code

.. figure:: ../../../_static/img/microservices-monolithic-application.jpg
    :scale: 50%
    :align: center

    Monolithic architecture

Microservices architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Architect the application by applying the Scale Cube (specifically
   y-axis scaling) and functionally decompose the application into a set
   of collaborating services. Each service implements a set of narrowly,
   related functions. For example, an application might consist of
   services such as the order management service, the customer
   management service etc.
-  Services communicate using either synchronous protocols such as
   HTTP/REST or asynchronous protocols such as AMQP.
-  Services are developed and deployed independently of one another.
-  Each service has its own database in order to be decoupled from other
   services. When necessary, consistency is between databases is
   maintained using either database replication mechanisms or
   application-level events.

.. figure:: ../../../_static/img/microservices-architecture.jpg
    :scale: 50%
    :align: center

    Microservices Architecture

API gateway
~~~~~~~~~~~

-  Implement an API gateway that is the single entry point for all
   clients. The API gateway handles requests in one of two ways. Some
   requests are simply proxied/routed to the appropriate service. It
   handles other requests by fanning out to multiple services.
-  Rather than provide a one-size-fits-all style API, the API gateway
   can expose a different API for each client. For example, the Netflix
   API gateway runs client-specific adapter code that provides each
   client with an API that’s best suited to it’s requirements.
-  The API gateway might also implement security, e.g. verify that the
   client is authorized to perform the request
-  Netflix API gateway

.. figure:: ../../../_static/img/microservices-api-gateway.jpg
    :scale: 50%
    :align: center

    Microservices API gateway

Client-side discovery
~~~~~~~~~~~~~~~~~~~~~

-  When making a request to a service, the client obtains the location
   of a service instance by querying a Service Registry, which knows the
   locations of all service instances.
-  Eureka is a Service Registry
-  Ribbon Client is an HTTP client that queries Eureka to route HTTP
   requests to an available service instance

.. figure:: ../../../_static/img/microservices-client-side-discovery.jpg
    :scale: 50%
    :align: center

    Microservices client side discovery

Server-side discovery
~~~~~~~~~~~~~~~~~~~~~

-  When making a request to a service, the client makes a request via a
   router (a.k.a load balancer) that runs at a well known location. The
   router queries a service registry, which might be built into the
   router, and forwards the request to an available service instance.
-  AWS Elastic Load Balancer (ELB), Kubernetes, Marathon

.. figure:: ../../../_static/img/microservices-server-side-discovery.jpg
    :scale: 50%
    :align: center

    Server side-discovery

Service registry
~~~~~~~~~~~~~~~~

-  Implement a service registry, which is a database of services, their
   instances and their locations. Service instances are registered with
   the service registry on startup and deregistered on shutdown. Client
   of the service and/or routers query the service registry to find the
   available instances of a service.
-  Eureka, Apache Zookeeper, Consul, Etcd

Self registration
~~~~~~~~~~~~~~~~~

-  A service instance is responsible for registering itself with the
   service registry. On startup the service instance registers itself
   (host and IP address) with the service registry and makes itself
   available for discovery. The client must typically periodically renew
   it’s registration so that the registry knows it is still alive. On
   shutdown, the service instance unregisters itself from the service
   registry.
-  Apache Zookeeper, Netflix Eureka

3rd party registration
~~~~~~~~~~~~~~~~~~~~~~

-  A 3rd party registrar is responsible for registering and
   unregistering a service instance with the service registry. When the
   service instance starts up, the registrar registers the service
   instance with the service registry. When the service instance shuts
   downs, the registrar unregisters the service instance from the
   service registry.
-  Netflix Prana - a “side car” application that runs along side a
   non-JVM application and registers the application with Eureka.
-  AWS Autoscaling Groups automatically (un)registers EC2 instances with
   Elastic Load Balancer
-  Joyent’s Container buddy runs in a Docker container as the parent
   process for the service and registers it with the registry
-  Registrator - registers and unregisters Docker containers with
   various service registries
-  Clustering frameworks such as Kubernetes and Marathon (un)register
   service instances with the built-in/implicit registry

Multiple service instances per host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Run multiple instances of different services on a host (Physical or
   Virtual machine).
-  There are various ways of deploying a service instance on a shared
   host including:
-  Deploy each service instance as a JVM process. For example, a Tomcat
   or Jetty instances per service instance.
-  Deploy multiple service instances in the same JVM. For example, as
   web applications or OSGI bundles.

Single service instance per host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Deploy each single service instance on it’s own host

Service instance per VM
~~~~~~~~~~~~~~~~~~~~~~~

-  Package the service as a virtual machine image and deploy each
   service instance as a separate VM

Service instance per Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Package the service as a (Docker) container image and deploy each
   service instance as a container
- Kubernetes, Marathon/Mesos, Amazon EC2 Container Service


Serverless deployment
~~~~~~~~~~~~~~~~~~~~~

-  Use a deployment infrastructure that hides any concept of servers
   (i.e. reserved or preallocated resources)- physical or virtual hosts,
   or containers. The infrastructure takes your service’s code and runs
   it. You are charged for each request based on the resources consumed.
-  To deploy your service using this approach, you package the code
   (e.g. as a ZIP file), upload it to the deployment infrastructure and
   describe the desired performance characteristics.
-  The deployment infrastructure is a utility operated by a public cloud
   provider. It typically uses either containers or virtual machines to
   isolate the services. However, these details are hidden from you.
   Neither you nor anyone else in your organization is responsible for
   managing any low-level infrastructure such as operating systems,
   virtual machines, etc.
-  AWS Lambda, Google Cloud Functions, Azure Functions

Database per Service
~~~~~~~~~~~~~~~~~~~~

-  Keep each microservice’s persistent data private to that service and
   accessible only via its API.

.. figure:: ../../../_static/img/microservices-database-per-service.png
    :scale: 50%
    :align: center

    Database per Service

Microservice chassis
~~~~~~~~~~~~~~~~~~~~

-  Build your microservices using a microservice chassis framework,
   which handles cross-cutting concerns
-  Spring Boot, Spring Cloud, Dropwizard

Shared database
~~~~~~~~~~~~~~~

-  Use a (single) database that is shared by multiple services. Each
   service freely accesses data owned by other services using local ACID
   transactions.

.. figure:: ../../../_static/img/microservices-database-shared.png
    :scale: 50%
    :align: center

    Shared database

Event-driven architecture
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Use an event-driven, eventually consistent approach. Each service
   publishes an event whenever it update it’s data. Other service
   subscribe to events. When an event is received, a service updates
   it’s data.

Event sourcing
~~~~~~~~~~~~~~

-  Reliably publish events whenever state changes by using Event
   Sourcing. Event Sourcing persists each business entity as a sequence
   of events, which are replayed to reconstruct the current state.

.. figure:: ../../../_static/img/microservices-event-sourcing.png
    :scale: 50%
    :align: center

    Event sourcing

CQRS - Command Query Responsibility Segregation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Split the system into two parts. The command side handles create,
   update and delete requests. The query side handles queries using one
   or more materialized views of the application’s data.

Transaction log tailing
~~~~~~~~~~~~~~~~~~~~~~~

-  Reliably publish events whenever state changes by tailing the
   transaction log.

Database triggers
~~~~~~~~~~~~~~~~~

-  Reliably publish events whenever state changes by using database
   triggers. Each trigger inserts an event into an EVENTS table, which
   is polled by a separate process that publishes the events.



Application events
~~~~~~~~~~~~~~~~~~

-  Reliably publish events whenever state changes by having the
   application insert events into an EVENTS table as part of the local
   transaction. A separate process polls the EVENTS table and publishes
   the events to a message broker.

Hearthbeat detecting
--------------------

-  statsd + graphite
-  nagios
-  zabbix

Bazy danych
-----------

-  Document: MongoDB
-  RDBMS: PostgreSQL, MySQL, Oracle, MSSQL
-  KV: Redis
-  Graph: neo4j

Kontenery i wirtualizacja
-------------------------

-  Vagrant
-  Docker
-  Mesos, Swarm, Kubernetes

Netflix
-------

-  chaos gorilla
-  chaos monkey
-  hystrix

Service Discovery
-----------------

-  DNS
-  AWS Elastic Load Balancer
-  Własne usługi

Configuration
-------------

-  Zookeeper

IaaS
----

-  Google Compute Engine
-  Amazon AWS
-  Rackspace
-  ecloud24

PaaS
----

-  Github Pages
-  Google App Engine
-  Heroku
-  Cloudera
-  Open Shift

SaaS
----

-  Force

Inne \*aaS
----------

-  Data
-  Security
-  Logging
-  Payment

Tworzenie aplikacji w oparciu o platformę Amazon AWS
----------------------------------------------------

-  Provisioning środowiska
-  Tworzenie aplikacji
-  Storage
-  Cache
-  Bazy danych
-  Zarządzanie hostami
-  Tworzenie reguł

Tworzenie aplikacji w oparciu o platformę Heroku
------------------------------------------------

-  Tworzenie aplikacji
-  Storage
-  Cache
-  Bazy danych

Set up
~~~~~~

.. code:: sh

    heroku login

Prepare the app
~~~~~~~~~~~~~~~

.. code:: sh

    git clone https://github.com/heroku/python-getting-started.git
    cd python-getting-started

Deploy the app
~~~~~~~~~~~~~~

.. code:: sh

    heroku create
    git push heroku master
    heroku ps:scale web=1

View logs
~~~~~~~~~

.. code:: sh

    heroku logs --tail

Define a Procfile
~~~~~~~~~~~~~~~~~

.. code:: text

    web: gunicorn gettingstarted.wsgi --log-file -
    web: python manage.py runserver 0.0.0.0:5000

Scale the app
~~~~~~~~~~~~~

.. code:: sh

    heroku ps
    heroku ps:scale web=0
    heroku ps:scale web=1

Declare app dependencies
~~~~~~~~~~~~~~~~~~~~~~~~

-  ``requirements.txt``

Run the app locally
~~~~~~~~~~~~~~~~~~~

.. code:: sh

    heroku local web -f Procfile.windows
    heroku local web

Push local changes
~~~~~~~~~~~~~~~~~~

.. code:: sh

    git commit -am "Changes"
    git push heroku master

Provision add-ons
~~~~~~~~~~~~~~~~~

.. code:: sh

    heroku addons:create papertrail
    heroku addons
    heroku addons:open papertrail

Start a console
~~~~~~~~~~~~~~~

.. code:: sh

    heroku run python manage.py shell
    heroku run bash

Define config vars
~~~~~~~~~~~~~~~~~~

.. code:: sh

    heroku config:set TIMES=2
    heroku config

Provision a database
~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    heroku addons
    heroku config
    heroku pg
    heroku pg:psql

Tworzenie aplikacji w oparciu o platformę Google App Engine
-----------------------------------------------------------

-  Tworzenie aplikacji
-  Storage
-  Cache
-  Bazy danych

Tworzenie aplikacji
~~~~~~~~~~~~~~~~~~~

.. code:: sh

    app.yaml
    git clone https://github.com/GoogleCloudPlatform/appengine-guestbook-python.git
    dev_appserver.py .

-  http://localhost:8000 - admin console
-  http://localhost:8080 - app

App.yaml for static pages
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: yaml

    runtime: php55
    api_version: 1
    threadsafe: true

    handlers:
     - url: /
       static_files: www/index.html
       upload: www/index.html

     - url: /(.*)
       static_files: www/\1
       upload: www/(.*)


