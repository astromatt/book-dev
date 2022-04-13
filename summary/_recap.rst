Recap
=====

.. code-block:: console

    sudo apt update
    sudo apt install -y uidmap
    curl https://get.docker.com/rootless |sh
    echo 'export PATH=/home/ubuntu/bin:$PATH' >> ~/.profile
    echo 'export DOCKER_HOST=unix:///run/user/1000/docker.sock' >> ~/.profile
    sudo mkdir -p /home/run/
    sudo chown ubuntu:ubuntu /home/run


Repository
----------
.. literalinclude:: src/Dockerfile.cicd
    :language: dockerfile

.. literalinclude:: src/Dockerfile.runtime
    :language: dockerfile

.. literalinclude:: src/Jenkinsfile
    :language: groovy

.. literalinclude:: src/sonar-project.properties
    :language: properties


Gitea
-----
.. literalinclude:: src/run-gitea.sh
    :language: sh


Jenkins
-------
.. literalinclude:: src/run-jenkins.sh
    :language: sh


SonarQube
---------
.. literalinclude:: src/run-sonarqube.sh
    :language: sh


Registry
--------
.. literalinclude:: src/run-registry.sh
    :language: sh


Registry UI
-----------
.. literalinclude:: src/run-registry-ui.sh
    :language: sh
