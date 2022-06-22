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


Further Reading
---------------
* https://12factor.net


Assignments
-----------
#. Stwórz plik ``test.env`` oraz ``prod.env``
#. Zapisz dwie różne konfiguracje bazy danych do obu plików
#. Uruchom kontener z parametrami testowymi
#. Uruchom kontener z parametrami produkcyjnymi
