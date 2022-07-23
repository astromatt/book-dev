Docker Env Vars
===============
* Environmental variables


Env
---
* ``-e``, ``--env`` - Set environment variables

.. code-block:: console

    $ docker run -e NAME='Mark Watney' alpine env
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    HOSTNAME=f5f93be44865
    HOME=/root
    NAME=Mark Watney

.. code-block:: console

    $ docker run -e FIRSTNAME='Mark' -e LASTNAME='Watney' alpine env
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    HOSTNAME=0c9bf0f8ae0e
    HOME=/root
    FIRSTNAME=Mark
    LASTNAME=Watney


Env-file
--------
* ``--env-file`` - Read in a file of environment variables
* ``.env`` name convention
* Add ``.env`` to ``.gitignore``
* ``.env-sample`` in your repository

.. code-block:: text
    :caption: Contents of ``prod.env`` file

    DATABASE_ENGINE=sqlite3
    DATABASE_HOST=localhost
    DATABASE_PORT=1337
    DATABASE_NAME=/tmp/db.sqlite3
    DATABASE_USER=mwatney
    DATABASE_PASSWORD=ares3

.. code-block:: console

    $ docker run --env-file=prod.env alpine env
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    HOSTNAME=bb04daae4875
    HOME=/root
    DATABASE_ENGINE=sqlite3
    DATABASE_HOST=localhost
    DATABASE_PORT=1337
    DATABASE_NAME=/tmp/db.sqlite3
    DATABASE_USER=mwatney
    DATABASE_PASSWORD=ares3


Secrets
-------
* https://www.hashicorp.com/products/vault
* https://docs.docker.com/engine/swarm/secrets/
* ``/run/secrets/<secret_name>``
* ``C:\ProgramData\Docker\secrets``

.. note:: Docker secrets are only available to swarm services, not to standalone containers. To use this feature, consider adapting your container to run as a service. Stateful containers can typically run with a scale of 1 without changing the container code.

In terms of Docker Swarm services, a secret is a blob of data, such as a password, SSH private key, SSL certificate, or another piece of data that should not be transmitted over a network or stored unencrypted in a Dockerfile or in your application’s source code.

A given secret is only accessible to those services which have been granted explicit access to it, and only while those service tasks are running.

You can use secrets to manage any sensitive data which a container needs
at runtime but you don’t want to store in the image or in source control,
such as:

* Usernames and passwords
* TLS certificates and keys
* SSH keys
* Other important data such as the name of a database or internal server
* Generic strings or binary content (up to 500 kb in size)

The location of the mount point within the container defaults to /run/secrets/<secret_name> in Linux containers, or C:\ProgramData\Docker\secrets in Windows containers.

You can add or inspect an individual secret at any time, or list all secrets. You cannot remove a secret that a running service is using.

.. code-block:: console

    $ docker secret create
    $ docker secret inspect
    $ docker secret ls
    $ docker secret rm

.. code-block:: console

    $ echo "This is a secret" | docker secret create my_secret_data -
    $ docker service create --name redis --secret my_secret_data redis:alpine
    $ docker service ps redis
    $ docker ps --filter name=redis -q
    $ docker container exec $(docker ps --filter name=redis -q) ls -l /run/secrets
    $ docker container exec $(docker ps --filter name=redis -q) cat /run/secrets/my_secret_data
    $ docker secret ls
    $ docker secret rm my_secret_data
    $ docker service update --secret-rm my_secret_data redis
    $ docker container exec -it $(docker ps --filter name=redis -q) cat /run/secrets/my_secret_data
    cat: can't open '/run/secrets/my_secret_data': No such file or directory
    $ docker service rm redis
    $ docker secret rm my_secret_data

.. code-block:: console

    $ openssl genrsa -out "root-ca.key" 4096
    $ openssl req \
              -new -key "root-ca.key" \
              -out "root-ca.csr" -sha256 \
              -subj '/C=US/ST=CA/L=San Francisco/O=Docker/CN=Swarm Secret Example CA'
    $ openssl x509 -req  -days 3650  -in "root-ca.csr" \
                   -signkey "root-ca.key" -sha256 -out "root-ca.crt" \
                   -extfile "root-ca.cnf" -extensions \
                   root_ca
    $ openssl genrsa -out "site.key" 4096
    $ openssl req -new -key "site.key" -out "site.csr" -sha256 \
              -subj '/C=US/ST=CA/L=San Francisco/O=Docker/CN=localhost'
    $ openssl x509 -req -days 750 -in "site.csr" -sha256 \
        -CA "root-ca.crt" -CAkey "root-ca.key"  -CAcreateserial \
        -out "site.crt" -extfile "site.cnf" -extensions server

    $ cat /etc/nginx/nginx.conf
    server {
        listen                443 ssl;
        server_name           localhost;
        ssl_certificate       /run/secrets/site.crt;
        ssl_certificate_key   /run/secrets/site.key;

        location / {
            root   /usr/share/nginx/html;
            index  index.html index.htm;
        }
    }
    $ docker secret create site.key site.key
    $ docker secret create site.crt site.crt
    $ docker secret create site.conf site.conf
    $ docker secret ls
    $ docker service create \
        --name nginx \
        --secret site.key \
        --secret site.crt \
        --secret site.conf \
        --publish published=3000,target=443 \
        nginx:latest \
        sh -c "ln -s /run/secrets/site.conf /etc/nginx/conf.d/site.conf && exec nginx -g 'daemon off;'"
    $ docker service rm nginx
    $ docker secret rm site.crt site.key site.conf

Further Reading
---------------
* https://12factor.net


Assignments
-----------
#. Stwórz plik ``test.env`` oraz ``prod.env``
#. Zapisz dwie różne konfiguracje bazy danych do obu plików
#. Uruchom kontener z parametrami testowymi
#. Uruchom kontener z parametrami produkcyjnymi
