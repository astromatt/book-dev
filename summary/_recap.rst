Recap
=====

.. code-block:: sh

    sudo apt update
    sudo apt install -y uidmap
    curl https://get.docker.com/rootless |sh
    echo 'export PATH=/home/ubuntu/bin:$PATH' >> ~/.profile
    echo 'export DOCKER_HOST=unix:///run/user/1000/docker.sock' >> ~/.profile
    exit


Source
------
.. code-block:: sh

    sudo apt install openjdk-8-jdk maven
    sudo update-alternatives --config java
    git clone https://github.com/sages-pl/example-helloworld-java.git src/java
    git remote set-url origin http://localhost:3000/root/java.git
    mvn compile && mvn test && mvn verify
    cp -a ~/.m2 .m2
    docker build -f Dockerfile.cicd -t myapp:cicd .

.. literalinclude:: src-java/Dockerfile.cicd
    :language: dockerfile

.. literalinclude:: src-java/Dockerfile.runtime
    :language: dockerfile

.. literalinclude:: src-java/Jenkinsfile
    :language: groovy

.. literalinclude:: src-java/sonar-project.properties
    :language: properties


Gitea
-----
* Gitea Base URL
* Change Administrator Account Settings: username, password, email

.. code-block:: sh

    vim ~/bin/run-gitea.sh
    chmod +x ~/bin/run-gitea.sh
    ~/bin/run-gitea.sh

.. code-block:: sh

    git push origin -u main

.. literalinclude:: src/run-gitea.sh
    :language: sh


Jenkins
-------
* Install ``Docker Pipeline`` plugin

.. code-block:: sh

    docker exec -itu root jenkins apk add mvn openjdk8

.. literalinclude:: src/run-jenkins.sh
    :language: sh


SonarQube
---------
* Create user ``myjavaproject``
* Create token
* Add user to the project
* Edit ``pom.xml`` in section: ``<project><build><plugins>`` add:

.. code-block:: xml

    <plugin>
        <groupId>org.pitest</groupId>
        <artifactId>pitest-maven</artifactId>
        <version>1.6.1</version>
        <dependencies>
            <dependency>
                <groupId>org.pitest</groupId>
                <artifactId>pitest-junit5-plugin</artifactId>
                <version>0.12</version>
            </dependency>
        </dependencies>
    </plugin>

.. literalinclude:: src/run-sonarqube.sh
    :language: sh


Registry
--------
.. literalinclude:: src/run-registry.sh
    :language: sh


Registry UI
-----------
.. code-block:: sh

    docker volume create registry_ui
    vim /home/ubuntu/.local/share/docker/volumes/registry_ui/_data/config.yml

.. code-block:: yaml

    listen_addr: 0.0.0.0:8888
    base_path: /
    registry_url: http://registry:5000
    verify_tls: true
    event_listener_token: token
    event_retention_days: 7
    event_database_driver: sqlite3
    event_database_location: data/registry_events.db
    cache_refresh_interval: 10
    anyone_can_delete: false
    admins: []
    debug: true
    purge_tags_keep_days: 90
    purge_tags_keep_count: 2
    # registry_username: user
    # registry_password: pass
    # event_database_driver: mysql
    # event_database_location: user:password@tcp(localhost:3306)/docker_events

.. literalinclude:: src/run-registry-ui.sh
    :language: sh


Other
-----
Ping

.. code-block:: sh

    echo 'net.ipv4.ping_group_range = 0 2147483647' |sudo tee -a /etc/sysctl.d/99-docker.conf
    sudo sysctl --system
