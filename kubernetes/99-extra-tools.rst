Extra Tools
===========


Configuration
-------------
* Kustomize


Networking
----------
* Nvoy - szyfruje komunikację pomiędzy kontenerami


Building
--------
* Jeeb - plugin do maven, który tworzy kontener
* Docker Maven Plugin
* Kaniko - nie potrzebuje Docker deamon do budowania
* Scopio - pozwala na pushowanie obrazów do Docker Registry i nie trzeba mieć dockerdeamon
* Source2Image

  * część projektu OpenShift
  * polecenie `s2i build . java-11-maven database-application`
  * obsługuje również URLe do projektu
  * umożliwia clean buildy oraz incremental buildy


CI/CD
-----
* https://tekton.dev
