Install Jenkins
---------------

.. code-block:: bash

    wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
    echo "deb http://pkg.jenkins-ci.org/debian binary/" >> /etc/apt/sources.list
    apt-get update
    apt-get install --yes jenkins
    sudo su - jenkins
    ssh-keygen
    cat ~/.ssh/id_rsa.pub
    exit
    service jenkins stop
    sed -i 's/HTTP_PORT=8080/HTTP_PORT=8081/g' /etc/default/jenkins
    service jenkins start

