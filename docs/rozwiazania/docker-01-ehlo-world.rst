Docker Ehlo World
-----------------

.. code-block:: sh

    apt-get install docker.io

- `Vagrant` virtualizes Operating System, `Docker` run inside containers on host machine
- `Docker` uses `Linux` kernel to run and cannot be used on either `Windows` or `OS X`
- However there's a way to run a virtual machine with `Linux` on `Docker` containers on it (this is how
``boot2docker`` works)

.. code-block:: sh

    docker run echo 'Ehlo World!'
    docker ps
