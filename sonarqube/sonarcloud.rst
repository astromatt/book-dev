**********
SonarCloud
**********


Rationale
=========
* Online hosting
* Free for open source projects
* Easy integration with github and bitbucket


Bitbucket Integration
=====================
* Sonar for Bitbucket
* https://marketplace.atlassian.com/apps/1212735/sonar-for-bitbucket-server?hosting=server&tab=overview
* https://ch-mibex-sonar4bitbucket.herokuapp.com/webhook

.. code-block:: json
    :caption: sonar.json

    {
      "sonarHost": "https://sonarcloud.io",
      "sonarProjectKey": "MyProjectKey"
    }
