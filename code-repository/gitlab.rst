******
GITLab
******


Install
=======
.. warning:: Machine must have at least 2 GB RAM, otherwise freezes. Amazon ``t2.micro`` is not good.

.. code-block:: console

    $ mkdir -p /home/gitlab
    $ chmod 777 /home/gitlab
    $ docker network create ecosystem
    $ docker run \
        --name gitlab \
        --detach \
        --restart always \
        --network ecosystem \
        --publish 2222:22 \
        --publish 2280:80 \
        --publish 22443:443 \
        --volume /home/gitlab/config:/etc/gitlab \
        --volume /home/gitlab/logs:/var/log/gitlab \
        --volume /home/gitlab/data:/var/opt/gitlab \
        gitlab/gitlab-ce:latest

Run from docker-compose
-----------------------
.. code-block:: yaml
    :caption: ``gitlab.yaml``

    version: '3'

    networks:
        ecosystem:
            driver: bridge

    services:
        gitlab:
            image: gitlab/gitlab-ce
            container_name: gitlab
            restart: "always"
            ports:
                - "2222:22"
                - "2280:80"
                - "22443:443"
            networks:
                - ecosystem
            volumes:
                - /home/gitlab/config:/etc/gitlab
                - /home/gitlab/logs:/var/log/gitlab
                - /home/gitlab/data:/var/opt/gitlab

.. code-block:: console

    $ docker-compose -f gitlab.yaml up


Configuration
=============
.. code-block:: console

    $ docker exec -it gitlab vi /etc/gitlab/gitlab.rb
    $ docker restart gitlab

Login
=====
.. warning:: Username do zalogowania to ``root``
