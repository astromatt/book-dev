******
GITLab
******


Install
-------
.. warning:: Machine must have at least 2 GB RAM, otherwise freezes. Amazon ``t2.micro`` is not good.

.. code-block:: console

    mkdir -p /home/gitlab
    chmod 777 /home/gitlab

.. code-block:: console

    docker run \
        --detach \
        --hostname gitlab.example.com \
        --publish 22:22 \
        --publish 80:80 \
        --publish 443:443 \
        --name gitlab \
        --restart always \
        --volume /home/gitlab/config:/etc/gitlab \
        --volume /home/gitlab/logs:/var/log/gitlab \
        --volume /home/gitlab/data:/var/opt/gitlab \
        gitlab/gitlab-ce:latest

Run from docker-compose
^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: yaml

    version: '3'

    networks:
        devtools-ecosystem:
            driver: bridge

    services:
        gitlab:
            image: gitlab/gitlab-ce
            container_name: gitlab
            hostname: gitlab.example.com
            restart: "always"
            ports:
                - "22:22"
                - "80:80"
                - "443:443"
            networks:
                - devtools-ecosystem
            volumes:
                - /home/gitlab/config:/etc/gitlab
                - /home/gitlab/logs:/var/log/gitlab
                - /home/gitlab/data:/var/opt/gitlab


Configuration
-------------
.. code-block:: console

    docker exec -it gitlab vi /etc/gitlab/gitlab.rb
    docker restart gitlab

Login
-----
.. warning:: Username do zalogowania to ``root``
