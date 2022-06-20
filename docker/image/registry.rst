Docker Registry
===============


Docker Registry
---------------
.. code-block:: sh

    docker run \
        --name registry \
        --detach \
        --rm \
        --network ecosystem \
        --publish 5000:5000 \
        --volume registry:/var/lib/registry \
        registry:2


Docker Registry UI
------------------
* ``registry-ui.yml``

.. code-block:: yaml

    listen_addr: 0.0.0.0:8888
    base_path: /

    registry_url: http://registry:5000
    verify_tls: true

    # registry_username: user
    # registry_password: pass

    # The same one should be configured on Docker registry as Authorization Bearer token.
    event_listener_token: token
    event_retention_days: 7

    event_database_driver: sqlite3
    event_database_location: data/registry_events.db
    # event_database_driver: mysql
    # event_database_location: user:password@tcp(localhost:3306)/docker_events

    cache_refresh_interval: 10

    # If users can delete tags.
    # If set to False, then only admins listed below.
    anyone_can_delete: false

    # Users allowed to delete tags.
    # This should be sent via X-WEBAUTH-USER header from your proxy.
    admins: []

    # Debug mode. Affects only templates.
    debug: true

    # How many days to keep tags but also keep the minimal count provided no matter how old.
    purge_tags_keep_days: 90
    purge_tags_keep_count: 2

.. code-block:: sh

    docker run \
        --name=registry-ui \
        --detach \
        --rm \
        --network ecosystem \
        --publish 8888:8888 \
        --volume $(pwd)/registry-ui.yml:/opt/config.yml:ro \
        quiq/docker-registry-ui


Automation
----------
.. code-block:: sh
    :caption: ``make-artifact.sh``

    #!/bin/sh

    REGISTRY='localhost:5000'
    NAME='myapp'
    VERSION="$(git log -1 --format='%h')"

    IMAGE="$REGISTRY/$NAME:$VERSION"

    docker build . -t $IMAGE
    docker push $IMAGE
    docker rmi $IMAGE
