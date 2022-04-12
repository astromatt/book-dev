Version Control System
======================


.. contents::


Gitea
-----
.. code-block:: sh

    docker network create ecosystem

.. code-block:: sh

    docker run \
        --name gitea \
        --detach \
        --rm \
        --env USER_UID=1000 \
        --env USER_GID=1000 \
        --network ecosystem \
        --publish 3000:3000 \
        --publish 2222:22 \
        --volume /home/gitea:/data \
        --volume /etc/timezone:/etc/timezone:ro \
        --volume /etc/localtime:/etc/localtime:ro \
        gitea/gitea

.. code-block:: sh

    --env GITEA__database__DB_TYPE=postgres
    --env GITEA__database__HOST=db:5432
    --env GITEA__database__NAME=gitea
    --env GITEA__database__USER=gitea
    --env GITEA__database__PASSWD=gitea


Gitea Rootless
--------------
.. code-block:: sh

    docker network create ecosystem

    docker run \
        --name gitea \
        --detach \
        --rm \
        --network ecosystem \
        --publish 3000:3000 \
        --publish 2222:22 \
        --volume /home/gitea/data:/var/lib/gitea \
        --volume /home/gitea/config:/etc/gitea \
        --volume /etc/timezone:/etc/timezone:ro \
        --volume /etc/localtime:/etc/localtime:ro \
        gitea/gitea:latest-rootless


Git and Git Flow in CI/CD
-------------------------
.. figure:: img/gitflow-all.png
    :width: 90%
    :align: center

.. figure:: img/gitflow-github.png
    :width: 90%
    :align: center

.. figure:: img/gitflow-lean.png
    :width: 90%
    :align: center


GitOps
------
* Argo CD - https://argoproj.github.io/argo-cd/
* Flux CD - https://fluxcd.io



Code Repository
---------------
Version Control System:

    * GIT
    * Mercurial
    * SVN
    * Perforce
    * CVS

Server:

    * GitLab
    * Gitea
    * Bitbucket Server
    * Github Enterprise
    * Gerrit

Cloud:

    * GitLab
    * Gitea
    * GitHub
    * Bitbucket Cloud
