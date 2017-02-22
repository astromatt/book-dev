****************
Bitbucket Server
****************

Install
=======

Download official ZIP archive
-----------------------------

.. code-block:: sh

    wget -O atlassian-bitbucket.zip https://www.atlassian.com/software/stash/downloads/binary/atlassian-bitbucket-4.14.0.zip
    unzip atlassian-bitbucket.zip
    rm -fr atlassian-bitbucket.zip
    sh atlassian-bitbucket*/bin/start-bitbucket.sh

Install using Docker
--------------------

.. code-block:: sh

    $ docker pull atlassian/bitbucket-server

    $ docker run -u root -v /data/bitbucket:/var/atlassian/application-data/bitbucket atlassian/bitbucket-server chown -R daemon  /var/atlassian/application-data/bitbucket

    $ docker run -v /data/bitbucket:/var/atlassian/application-data/bitbucket --name="bitbucket" -d -p 7990:7990 -p 7999:7999 atlassian/bitbucket-server
