****
JIRA
****

Documentation
-------------
* https://confluence.atlassian.com/display/JIRA/JIRA+Documentation


Download Page
-------------
* https://www.atlassian.com/software/jira/download?b=a#allDownloads


Installation
------------

.. code-block: sql

    CREATE USER jira WITH PASSWORD 'jira';
    CREATE DATABASE jira;
    GRANT ALL PRIVILEGES ON DATABASE jira TO jira;

.. code-block: bash

    wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-6.4.11-x64.bin
    chmod +x atlassian-jira-6.4.11-x64.bin
    ./atlassian-jira-6.4.11-x64.bin
    rm -fr atlassian-jira-6.4.11-x64.bin
    echo "jira.websudo.is.disabled = true" >> /var/atlassian/application-data/jira/jira-config.properties
    service jira stop
    service jira start


API Documentation
-----------------

* https://docs.atlassian.com/jira/REST/latest/
* https://jira.atlassian.com/plugins/servlet/restbrowser#/

JIRA User Server
----------------

# Go to Jira User Server (g+g and type JIRA User Server)
# Add application
# Set application name, password and IP Addresses (paste adresses from instances which you want connect with Jira User Server)
