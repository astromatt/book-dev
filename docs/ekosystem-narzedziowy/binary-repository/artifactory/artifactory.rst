***********
Artifactory
***********

Installation
============

.. code-block:: sh

    useradd artifactory
    cd /opt/
    wget -O artifactory.zip https://api.bintray.com/content/jfrog/artifactory/jfrog-artifactory-oss-$latest-sources.tar.gz;bt_package=jfrog-artifactory-oss-zip
    unzip artifactory.zip
    rm -fr artifactory.zip
    chown -R artifactory:artifactory artifactory*/
    cd artifactory*/bin/
    su artifactory
    screen
    ./artifactory.sh
    (detach screen)

