******
GITLab
******

Install
-------
.. warning:: for non-training use change ``/tmp`` to other persistent directory

.. code-block:: console

    docker run --detach \
        --hostname gitlab.example.com \
        --publish 443:443 --publish 80:80 --publish 22:22 \
        --name gitlab \
        --restart always \
        --volume /tmp/gitlab/config:/etc/gitlab \
        --volume /tmp/gitlab/logs:/var/log/gitlab \
        --volume /tmp/gitlab/data:/var/opt/gitlab \
        gitlab/gitlab-ce:latest

Configuration
-------------
.. code-block:: console

    docker exec -it gitlab vi /etc/gitlab/gitlab.rb
    docker restart gitlab
