Install Confluence
==================

.. code-block:: bash

    wget https://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-5.8.9-x64.bin
    chmod +x atlassian-confluence-5.8.9-x64.bin
    ./atlassian-confluence-5.8.9-x64.bin
    rm -fr atlassian-confluence-5.8.9-x64.bin


Documentation
-------------

* https://confluence.atlassian.com/display/DOC/Confluence+Documentation+Home

Download Page
-------------

* https://www.atlassian.com/software/confluence/download

Installation
------------

    .. block-code: sql

    CREATE USER confluence WITH PASSWORD 'confluence';
    CREATE DATABASE confluence;
    GRANT ALL PRIVILEGES ON DATABASE confluence TO confluence;


    .. block-code: bash

    wget https://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-5.7.3-x64.bin
    chmod +x atlassian-confluence-5.7.3-x64.bin
    ./atlassian-confluence-5.7.3-x64.bin
    rm -fr atlassian-confluence-5.7.3-x64.bin


API Documentation
-----------------

* https://docs.atlassian.com/atlassian-confluence/REST/latest/
* https://confluence.atlassian.com/plugins/servlet/restbrowser#/


Set JIRA User Directory
-----------------------

# Go to User Directories
# Add directory
# Choose directory type: 'Atlassian JIRA'
# Set
** directory name
** paste jira url
** application name (application name from Jira User Server)
** application password (application password from Jira User Server)
# Test connetion
# Save configuration
# Synchronize directory

