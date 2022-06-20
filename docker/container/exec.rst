Docker Exec
===========
* Execute


Attach to running containers
----------------------------
* Attach to running container and execute another process of bash

.. code-block:: console

    $ docker exec -it CONTAINER_NAME_OR_ID sh
    $ docker exec -u 0 -it CONTAINER_NAME_OR_ID sh      # as root


What application is running inside the container?
-------------------------------------------------
.. code-block:: console

    $ docker top CONTAINER_NAME_OR_ID


Stop containers
---------------
* Filesystem inside container is ephemeral (it will be deleted after stop)
* Allow container to close gracefully

.. code-block:: console

    $ docker stop CONTAINER_NAME_OR_ID


Kill container
--------------
* Terminate container instantly

.. code-block:: console

    $ docker kill CONTAINER_NAME_OR_ID


Remove container
----------------
* Remove container

    .. code-block:: console

        $ docker rm CONTAINER_NAME_OR_ID

* Remove all stopped containers

    .. code-block:: console

        $ docker rm $(docker ps -a -q)

* ``--rm`` - Automatically remove the container when it exits

    .. code-block:: console

        $ docker run --rm -it alpine sh

Inspect
-------
.. code-block:: console

    $ docker inspect alpine


Update
------
* Do not autostart ``alpine`` container after Docker engine restart (host reboot)

.. code-block:: console

    $ docker update --restart=no alpine
