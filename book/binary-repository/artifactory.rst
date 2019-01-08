Artifactory
===========

Installation
------------

From Docker
^^^^^^^^^^^
- Prefered

.. code-block:: console

    $ docker run --rm --name artifactory -d -p 8002:8081 docker.bintray.io/jfrog/artifactory-oss:latest

From zip
^^^^^^^^
.. code-block:: console

    $ useradd artifactory
    $ cd /opt/
    $ wget -O artifactory.zip https://api.bintray.com/content/jfrog/artifactory/jfrog-artifactory-oss-$latest-sources.tar.gz;bt_package=jfrog-artifactory-oss-zip
    $ unzip artifactory.zip
    $ rm -fr artifactory.zip
    $ chown -R artifactory:artifactory artifactory*/
    $ cd artifactory*/bin/
    $ su artifactory
    $ screen
    $ ./artifactory.sh
    (detach screen)

