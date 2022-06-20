Docker Volumes
==============

* A data volume is a specially-designated directory within one or more containers that bypasses the Union File System.
* Data volumes provide several useful features for persistent or shared data:

    - Volumes are initialized when a container is created.
    - If the container’s base image contains data at the specified mount point, that existing data is copied into the new volume upon volume initialization. (Note that this does not apply when mounting a host directory.)
    - Data volumes can be shared and reused among containers.
    - Changes to a data volume are made directly.
    - Changes to a data volume will not be included when you update an image.
    - Data volumes persist even if the container itself is deleted.

* Data volumes are designed to persist data, independent of the container’s life cycle.
* Docker therefore never automatically deletes volumes when you remove a container, nor will it “garbage collect” volumes that are no longer referenced by a container.

.. note:: You can also use the VOLUME instruction in a Dockerfile to add one or more new volumes to any container created from that image.


Creating persistent storage
---------------------------
``-v``, ``--volume`` - Bind mount a volume

.. code-block:: console

    $ docker run -it -v /data alpine sh
    $ echo 'hello' > /data/hello.txt
    # exit with ``ctrl+q + ctrl+p``

.. code-block:: console

    $ ls /var/lib/docker/containers/volumes/.../


Attaching local dir to docker container
---------------------------------------
* Will mount ``/tmp/my_host`` from host to ``/data`` inside container

.. code-block:: console

    $ docker run -v <host path>:<container path>[:FLAG]

.. code-block:: console

    $ docker run -v /home/myproject:/data alpine sh


Mount read-only filesystem
--------------------------
.. code-block:: console

    $ docker run -v /home/myproject:/data:ro alpine sh


Creating Volumes
----------------
.. code-block:: console

    $ docker volume create -d flocker --opt o=size=20GB myvolume
    $ docker run -v myvolume:/data alpine sh


Volume container
----------------
.. code-block:: console

    $ docker create -v /data --name dbstore postgres /bin/true
    $ docker run --detach --volumes-from dbstore --name db1 postgres
