CI/CD Python
============

Setup
-----
.. code-block:: sh

    git clone https://github.com/sages-pl/src-python /home/ubuntu/src
    sudo apt update
    sudo apt install -y uidmap
    curl https://get.docker.com/rootless |sh
    echo 'export PATH=/home/ubuntu/.local/bin:$PATH' >> ~/.profile
    echo 'export DOCKER_HOST=unix:///run/user/1000/docker.sock' >> ~/.profile
    echo 'export IP=$(curl -s ipecho.net/plain)' >> ~/.profile
    source ~/.profile
    docker network create ecosystem


Gitea
-----
.. code-block:: sh

    cat > /home/ubuntu/bin/run-gitea << EOF

    docker run \\
        --name gitea \\
        --detach \\
        --restart always \\
        --env USER_UID=1000 \\
        --env USER_GID=1000 \\
        --env GITEA__server__ROOT_URL=http://$IP:3000/ \\
        --env GITEA__database__DB_TYPE=sqlite3 \\
        --env GITEA__database__PATH=/var/lib/gitea/data/gitea.db \\
        --env GITEA__database__HOST=... \\
        --env GITEA__database__NAME=... \\
        --env GITEA__database__USER=... \\
        --env GITEA__database__PASSWD=... \\
        --network ecosystem \\
        --publish 3000:3000 \\
        --publish 2222:22 \\
        --volume gitea_data:/var/lib/gitea \\
        --volume gitea_config:/etc/gitea \\
        --volume /etc/timezone:/etc/timezone:ro \\
        --volume /etc/localtime:/etc/localtime:ro \\
        gitea/gitea:latest-rootless

    docker exec -itu root gitea ash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'

    echo "Gitea running on: http://$IP:3000/"

    EOF

    chmod +x /home/ubuntu/bin/run-gitea
    run-gitea


Jenkins
-------
.. code-block:: sh

    cat > /home/ubuntu/bin/run-jenkins << EOF

    chmod o+rw /run/user/1000/docker.sock
    sudo ln -s /usr/bin/python3 /usr/bin/python
    sudo ln -s /home/ubuntu/.local/share/docker/volumes/jenkins_data/_data/ /var/jenkins_home

    docker run \\
        --name jenkins \\
        --detach \\
        --restart always \\
        --network ecosystem \\
        --publish 8080:8080 \\
        --volume jenkins_data:/var/jenkins_home \\
        --volume /run/user/1000/docker.sock:/var/run/docker.sock \\
        jenkinsci/blueocean:latest

    docker exec -u root jenkins apk add python3 py3-pip

    echo "Jenkins running on: http://$IP:8080/"

    EOF

    chmod +x /home/ubuntu/bin/run-jenkins
    run-jenkins


SonarQube
---------
.. code-block:: sh

    cat > /home/ubuntu/bin/run-sonarqube << EOF

    docker run \\
        --name sonarqube \\
        --detach \\
        --restart always \\
        --network ecosystem \\
        --publish 9000:9000 \\
        --volume sonarqube_data:/opt/sonarqube/data \\
        --volume sonarqube_logs:/opt/sonarqube/logs \\
        --volume sonarqube_extensions:/opt/sonarqube/extensions \\
        sonarqube

    echo "SonarQube running on: http://$IP:9000/"

    EOF

    chmod +x /home/ubuntu/bin/run-sonarqube
    run-sonarqube


SonarScanner
------------
.. code-block:: sh

    docker pull sonarsource/sonar-scanner-cli


Docker Registry
---------------
.. code-block:: sh

    cat > /home/ubuntu/bin/run-registry << EOF

    docker run \\
        --detach \\
        --restart always \\
        --name registry \\
        --net ecosystem \\
        --publish 5000:5000 \\
        --volume registry_data:/var/lib/registry \\
        registry:2

    echo "Registry running on: http://$IP:5000/"

    EOF

    chmod +x /home/ubuntu/bin/run-registry
    run-registry


Registry UI
-----------
.. code-block:: sh

    cat > /home/ubuntu/registry-ui.yml << EOF

    listen_addr: 0.0.0.0:8888
    base_path: /

    registry_url: http://registry:5000
    verify_tls: true

    # registry_username: user
    # registry_password: pass

    # The same one should be configured on Docker registry as Authorization Bearer token.
    event_listener_token: token
    event_retention_days: 7

    event_database_driver: sqlite3
    event_database_location: data/registry_events.db
    # event_database_driver: mysql
    # event_database_location: user:password@tcp(localhost:3306)/docker_events

    cache_refresh_interval: 10

    # If users can delete tags.
    # If set to False, then only admins listed below.
    anyone_can_delete: false

    # Users allowed to delete tags.
    # This should be sent via X-WEBAUTH-USER header from your proxy.
    admins: []

    # Debug mode. Affects only templates.
    debug: true

    # How many days to keep tags but also keep the minimal count provided no matter how old.
    purge_tags_keep_days: 90
    purge_tags_keep_count: 2

    EOF

.. code-block:: sh

    cat > /home/ubuntu/bin/run-registry-ui << EOF

    docker run \\
        --name registry-ui \\
        --detach \\
        --restart always \\
        --network ecosystem \\
        --publish 8888:8888 \\
        --volume /home/ubuntu/registry-ui.yml:/opt/config.yml:ro \\
        quiq/docker-registry-ui

    echo "Registry UI running on: http://$IP:8888/"

    EOF

    chmod +x /home/ubuntu/bin/run-registry-ui
    run-registry-ui


Files
-----
.. code-block:: sh

    cat > /home/ubuntu/src/Dockerfile << EOF
    FROM python:3.10
    COPY game.pyz /game.pyz
    CMD python3 /game.pyz
    EOF

.. code-block:: sh

    cat > /home/ubuntu/src/sonar-project.properties << EOF
    ## Sonar Server
    sonar.host.url=http://sonarqube:9000/
    sonar.login=TOKEN

    ## Software Configuration Management
    sonar.scm.enabled=true
    sonar.scm.provider=git

    ## SonarScanner Config
    sonar.sourceEncoding=UTF-8
    sonar.verbose=false
    sonar.log.level=INFO
    sonar.showProfiling=false
    sonar.projectBaseDir=/usr/src/
    sonar.working.directory=/tmp/

    ## Quality Gates
    sonar.qualitygate.wait=true
    sonar.qualitygate.timeout=300

    ## About Project
    sonar.projectKey=mypythonproject
    sonar.projectName=MyPythonProject

    ## Python
    sonar.language=py
    sonar.python.version=3.10
    sonar.sources=src
    sonar.tests=test
    sonar.inclusions=**/*.py
    sonar.exclusions=**/migrations/**,**/*.pyc,**/__pycache__/**
    sonar.python.xunit.skipDetails=false
    sonar.python.xunit.reportPath=.tmp/xunit.xml
    sonar.python.coverage.reportPaths=.tmp/coverage.xml,./cobertura.xml
    sonar.python.bandit.reportPaths=.tmp/bandit.json
    sonar.python.pylint.reportPaths=.tmp/pylint.txt
    sonar.python.flake8.reportPaths=.tmp/flake8.txt

    EOF

.. code-block:: sh

    cat > /home/ubuntu/src/Jenkinsfile << EOF
    pipeline {
      agent any
      triggers { pollSCM('* * * * *') }

      stages {
        stage('Env Prepare')            { steps { sh 'run/env-prepare' }}
        stage('Env Setup')              { steps { sh 'run/env-setup' }}
        stage('Env Debug')              { steps { sh 'run/env-debug' }}

        stage('Test') {
        parallel {
            stage('Test Code Style')    { steps { sh 'run/test-codestyle' }}
            stage('Test Functional')    { steps { sh 'run/test-functional' }}
            stage('Test Integration')   { steps { sh 'run/test-integration' }}
            stage('Test Lint')          { steps { sh 'run/test-lint' }}
            stage('Test Load')          { steps { sh 'run/test-load' }}
            stage('Test Mutation')      { steps { sh 'run/test-mutation' }}
            stage('Test Regression')    { steps { sh 'run/test-regression' }}
            stage('Test Security')      { steps { sh 'run/test-security' }}
            stage('Test Smoke')         { steps { sh 'run/test-smoke' }}
            stage('Test Static')        { steps { sh 'run/test-static' }}
            stage('Test UI')            { steps { sh 'run/test-ui' }}
            stage('Test Unit')          { steps { sh 'run/test-unit' }}
        }}
        stage('Test Report')            { steps { sh 'run/test-report' }}

        stage('Artifact Prepare')       { steps { sh 'run/artifact-prepare' }}
        stage('Artifact Build')         { steps { sh 'run/artifact-create' }}
        stage('Artifact Publish')       { steps { sh 'run/artifact-publish' }}
        stage('Artifact Cleanup')       { steps { sh 'run/artifact-cleanup' }}

        stage('Deploy Dev')             { steps { sh 'run/deploy-dev' }}
        stage('Deploy Test')            { steps { sh 'run/deploy-test' }}
        stage('Deploy Preprod')         { steps { sh 'run/deploy-preprod' }}
        stage('Deploy Prod')            { steps { sh 'run/deploy-prod' }}
      }
    }

    // To run all:
    // grep -Po "^[^/].*sh '\K.+(?=')" Jenkinsfile |sh -x

    EOF

.. code-block:: sh

    cd /home/ubuntu/src
    mkdir -p run/
    touch run/test-codestyle
    touch run/test-coverage
    touch run/test-functional
    touch run/test-integration
    touch run/test-lint
    touch run/test-load
    touch run/test-mutation
    touch run/test-regression
    touch run/test-report
    touch run/test-security
    touch run/test-smoke
    touch run/test-static
    touch run/test-ui
    touch run/test-unit
    touch run/artifact-prepare
    touch run/artifact-create
    touch run/artifact-publish
    touch run/artifact-cleanup
    touch run/deploy-dev
    touch run/deploy-test
    touch run/deploy-preprod
    touch run/deploy-prod
    chmod +x run/*


Tests
-----
.. code-block:: sh

    cat > run/env-prepare << EOF
    env |sort
    EOF

.. code-block:: sh

    cat > run/env-setup << EOF
    python3 -m pip install --upgrade -r requirements.dev
    EOF

.. code-block:: sh

    cat > run/env-debug << EOF
    which python3
    python3 --version
    python3 -m pip freeze
    EOF

.. code-block:: sh

    cat > run/test-codestyle << EOF
    export PYTHONPATH=src
    python3 -m flake8 --exit-zero --doctest --output-file=.tmp/flake8.txt src
    EOF

.. code-block:: sh

    cat > run/test-coverage << EOF
    export PYTHONPATH=src
    python3 -m coverage run src
    python3 -m coverage xml -o .tmp/coverage.xml
    EOF

.. code-block:: sh

    cat > run/test-functional << EOF
    echo 'Not Implemented'
    EOF

.. code-block:: sh

    cat > run/test-integration << EOF
    export PYTHONPATH=src
    python3 -m doctest -v test/*.py
    EOF

.. code-block:: sh

    cat > run/test-lint << EOF
    export PYTHONPATH=src
    python3 -m pylama --verbose --async src || true
    python3 -m pylint --exit-zero --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" --output=.tmp/pylint.txt --disable=C0114,C0115,C0116,E0401,C0103 src
    EOF

.. code-block:: sh

    cat > run/test-load << EOF
    echo 'Not Implemented'
    EOF

.. code-block:: sh

    cat > run/test-mutation << EOF
    mutmut run || true
    mutmut results
    mutmut junitxml --suspicious-policy=ignore --untested-policy=ignore > .tmp/xunit.xml
    EOF

.. code-block:: sh

    cat > run/test-regression << EOF
    echo 'Not Implemented'
    EOF

.. code-block:: sh

    cat > run/test-report << EOF
    docker run --rm --net ecosystem -v $(pwd):/usr/src sonarsource/sonar-scanner-cli
    EOF

.. code-block:: sh

    cat > run/test-security << EOF
    export PYTHONPATH=src
    python3 -m bandit --format json --output=.tmp/bandit.json --recursive src
    EOF

.. code-block:: sh

    cat > run/test-smoke << EOF
    echo 'Not Implemented'
    EOF

.. code-block:: sh

    cat > run/test-static << EOF
    export PYTHONPATH=src
    python3 -m mypy --ignore-missing-imports --cobertura-xml-report=.tmp src || test
    EOF

.. code-block:: sh

    cat > run/test-ui << EOF
    echo 'Not Implemented'
    EOF

.. code-block:: sh

    cat > run/test-unit << EOF
    export PYTHONPATH=src
    python3 -m unittest discover -v test
    EOF


Artifact
--------
.. code-block:: sh

    cat > run/artifact-prepare << EOF
    python3 -m pip install --upgrade --no-cache-dir -r requirements.prod --target src
    rm -fr src/*.dist-info
    python3 -m compileall -f src
    # find src -name '*.py' -not -name '__main__.py' -not -name '__init__.py' -delete  # not working for now
    python3 -m zipapp --python="/usr/bin/env python3" --output=game.pyz src
    EOF

.. code-block:: sh

    cat > run/artifact-create << EOF
    docker build . -t localhost:5000/myapp:$(git log -1 --format='$h')
    EOF

.. code-block:: sh

    cat > run/artifact-publish << EOF
    docker push localhost:5000/myapp:$(git log -1 --format='$h')
    EOF

.. code-block:: sh

    cat > run/artifact-cleanup << EOF
    docker rmi localhost:5000/myapp:$(git log -1 --format='$h')
    EOF


Deployment
----------
.. code-block:: sh

    cat > run/deploy-dev << EOF
    echo 'Not Implemented'
    EOF

.. code-block:: sh

    cat > run/deploy-test << EOF
    echo 'Not Implemented'
    EOF

.. code-block:: sh

    cat > run/deploy-preprod << EOF
    echo 'Not Implemented'
    EOF

.. code-block:: sh

    cat > run/deploy-prod << EOF
    echo 'Not Implemented'
    EOF
