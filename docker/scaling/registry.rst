***************
Docker Registry
***************


Run
===
.. code-block:: console

    $ docker network create ecosystem
    $ mkdir -p /home/registry
    $ chmod 777 /home/registry

    $ docker run \
        --detach \
        --name registry \
        --restart always \
        --network ecosystem \
        --publish 5000:5000 \
        --volume /home/registry:/var/lib/registry \
        registry:2

.. code-block:: console

    $ docker pull alpine
    $ docker tag alpine localhost:5000/alpine
    $ docker push localhost:5000/alpine


Search
======
* API https://docs.docker.com/registry/spec/api/

.. code-block:: console

    # docker search <registry_host>:<registry_port>/
    docker search http://localhost:5000/

.. code-block:: console

    $ curl http://localhost:5000/v2/_catalog
    {"repositories":["alpine","debian","ubuntu"]}

    $ curl http://localhost:5000/v2/alpine/tags/list
    {"name":"alpine","tags":["latest"]}


UI
==
.. code-block:: console

    $ docker run -p 5080:8080 -e REG1=http://localhost:5000/v2/ --name registry-ui atcol/docker-registry-ui


Mirror Docker Hub
=================
* https://docs.docker.com/registry/recipes/mirror/

.. code-block:: yaml
    :caption: On Docker Registry container `/etc/docker/registry/config.yml`

    proxy:
      remoteurl: https://registry-1.docker.io
      username: [username]
      password: [password]

.. code-block:: json
    :caption: On your machine with Docker Daemon `/etc/docker/daemon.json`

    {
      "registry-mirrors": ["https://<my-docker-mirror-host>"]
    }


Auth
====
.. code-block:: console

    $ mkdir -p /home/registry/data
    $ mkdir -p /home/registry/conf
    $ mkdir -p /home/registry/auth
    $ mkdir -p /home/registry/certs

    $ docker run --entrypoint htpasswd registry:2 -Bbn myusername mypassword > /home/registry/auth/htpasswd
    $ docker container stop registry

.. code-block:: console

    $ docker run \
        --detach \
        --name registry \
        --restart always \
        --network ecosystem \
        --publish 5000:5000 \
        --volume /home/registry/auth:/auth \
        --volume /home/registry/certs:/certs \
        --env REGISTRY_AUTH=htpasswd \
        --env REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm \
        --env REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
        --env REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
        --env REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
        registry:2

.. code-block:: console

    $ docker login myregistrydomain.com:5000


Docker Compose
==============
.. code-block:: yaml

    registry:
      restart: always
      image: registry:2
      ports:
        - 5000:5000
      environment:
        REGISTRY_HTTP_TLS_CERTIFICATE: /certs/domain.crt
        REGISTRY_HTTP_TLS_KEY: /certs/domain.key
        REGISTRY_AUTH: htpasswd
        REGISTRY_AUTH_HTPASSWD_PATH: /auth/htpasswd
        REGISTRY_AUTH_HTPASSWD_REALM: Registry Realm
      volumes:
        - /path/data:/var/lib/registry
        - /path/certs:/certs
        - /path/auth:/auth

.. code-block:: console

    $ docker-compose up -d


Config
======
* Documentation: https://docs.docker.com/registry/configuration/

.. code-block:: console

    $ mkdir -p /home/registry/data
    $ mkdir -p /home/registry/conf
    $ mkdir -p /home/registry/auth
    $ mkdir -p /home/registry/certs

.. code-block:: console

    --volume /home/registry/conf/config.yml:/etc/docker/registry/config.yml

.. code-block:: yaml

    version: 0.1
    log:
      accesslog:
        disabled: true
      level: debug
      formatter: text
      fields:
        service: registry
        environment: staging
      hooks:
        - type: mail
          disabled: true
          levels:
            - panic
          options:
            smtp:
              addr: mail.example.com:25
              username: mailuser
              password: password
              insecure: true
            from: sender@example.com
            to:
              - errors@example.com
    loglevel: debug # deprecated: use "log"
    storage:
      filesystem:
        rootdirectory: /var/lib/registry
        maxthreads: 100
      azure:
        accountname: accountname
        accountkey: base64encodedaccountkey
        container: containername
      gcs:
        bucket: bucketname
        keyfile: /path/to/keyfile
        credentials:
          type: service_account
          project_id: project_id_string
          private_key_id: private_key_id_string
          private_key: private_key_string
          client_email: client@example.com
          client_id: client_id_string
          auth_uri: http://example.com/auth_uri
          token_uri: http://example.com/token_uri
          auth_provider_x509_cert_url: http://example.com/provider_cert_url
          client_x509_cert_url: http://example.com/client_cert_url
        rootdirectory: /gcs/object/name/prefix
        chunksize: 5242880
      s3:
        accesskey: awsaccesskey
        secretkey: awssecretkey
        region: us-west-1
        regionendpoint: http://myobjects.local
        bucket: bucketname
        encrypt: true
        keyid: mykeyid
        secure: true
        v4auth: true
        chunksize: 5242880
        multipartcopychunksize: 33554432
        multipartcopymaxconcurrency: 100
        multipartcopythresholdsize: 33554432
        rootdirectory: /s3/object/name/prefix
      swift:
        username: username
        password: password
        authurl: https://storage.myprovider.com/auth/v1.0 or https://storage.myprovider.com/v2.0 or https://storage.myprovider.com/v3/auth
        tenant: tenantname
        tenantid: tenantid
        domain: domain name for Openstack Identity v3 API
        domainid: domain id for Openstack Identity v3 API
        insecureskipverify: true
        region: fr
        container: containername
        rootdirectory: /swift/object/name/prefix
      oss:
        accesskeyid: accesskeyid
        accesskeysecret: accesskeysecret
        region: OSS region name
        endpoint: optional endpoints
        internal: optional internal endpoint
        bucket: OSS bucket
        encrypt: optional data encryption setting
        secure: optional ssl setting
        chunksize: optional size valye
        rootdirectory: optional root directory
      inmemory:  # This driver takes no parameters
      delete:
        enabled: false
      redirect:
        disable: false
      cache:
        blobdescriptor: redis
      maintenance:
        uploadpurging:
          enabled: true
          age: 168h
          interval: 24h
          dryrun: false
        readonly:
          enabled: false
    auth:
      silly:
        realm: silly-realm
        service: silly-service
      token:
        autoredirect: true
        realm: token-realm
        service: token-service
        issuer: registry-token-issuer
        rootcertbundle: /root/certs/bundle
      htpasswd:
        realm: basic-realm
        path: /path/to/htpasswd
    middleware:
      registry:
        - name: ARegistryMiddleware
          options:
            foo: bar
      repository:
        - name: ARepositoryMiddleware
          options:
            foo: bar
      storage:
        - name: cloudfront
          options:
            baseurl: https://my.cloudfronted.domain.com/
            privatekey: /path/to/pem
            keypairid: cloudfrontkeypairid
            duration: 3000s
            ipfilteredby: awsregion
            awsregion: us-east-1, use-east-2
            updatefrenquency: 12h
            iprangesurl: https://ip-ranges.amazonaws.com/ip-ranges.json
      storage:
        - name: redirect
          options:
            baseurl: https://example.com/
    reporting:
      bugsnag:
        apikey: bugsnagapikey
        releasestage: bugsnagreleasestage
        endpoint: bugsnagendpoint
      newrelic:
        licensekey: newreliclicensekey
        name: newrelicname
        verbose: true
    http:
      addr: localhost:5000
      prefix: /my/nested/registry/
      host: https://myregistryaddress.org:5000
      secret: asecretforlocaldevelopment
      relativeurls: false
      draintimeout: 60s
      tls:
        certificate: /path/to/x509/public
        key: /path/to/x509/private
        clientcas:
          - /path/to/ca.pem
          - /path/to/another/ca.pem
        letsencrypt:
          cachefile: /path/to/cache-file
          email: emailused@letsencrypt.com
          hosts: [myregistryaddress.org]
      debug:
        addr: localhost:5001
        prometheus:
          enabled: true
          path: /metrics
      headers:
        X-Content-Type-Options: [nosniff]
      http2:
        disabled: false
    notifications:
      events:
        includereferences: true
      endpoints:
        - name: alistener
          disabled: false
          url: https://my.listener.com/event
          headers: <http.Header>
          timeout: 1s
          threshold: 10
          backoff: 1s
          ignoredmediatypes:
            - application/octet-stream
          ignore:
            mediatypes:
               - application/octet-stream
            actions:
               - pull
    redis:
      addr: localhost:6379
      password: asecret
      db: 0
      dialtimeout: 10ms
      readtimeout: 10ms
      writetimeout: 10ms
      pool:
        maxidle: 16
        maxactive: 64
        idletimeout: 300s
    health:
      storagedriver:
        enabled: true
        interval: 10s
        threshold: 3
      file:
        - file: /path/to/checked/file
          interval: 10s
      http:
        - uri: http://server.to.check/must/return/200
          headers:
            Authorization: [Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==]
          statuscode: 200
          timeout: 3s
          interval: 10s
          threshold: 3
      tcp:
        - addr: redis-server.domain.com:6379
          timeout: 3s
          interval: 10s
          threshold: 3
    proxy:
      remoteurl: https://registry-1.docker.io
      username: [username]
      password: [password]
    compatibility:
      schema1:
        signingkeyfile: /etc/registry/key.json
        enabled: true
    validation:
      manifests:
        urls:
          allow:
            - ^https?://([^/]+\.)*example\.com/
          deny:
            - ^https?://www\.example\.com/
