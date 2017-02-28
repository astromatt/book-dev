Bitbucket Server
================

Zadania
-------

Instalacja
^^^^^^^^^^
* Zainstaluj `Bitbucket`
* Skonfiguruj licencję wykorzystując evaluation license z https://my.atlassian.com/products/index
* Załóż konto na https://id.atlassian.com/:

.. toggle-code-block:: sh
    :label: Instalacja za pomocą archiwów `zip`

    wget -O atlassian-bitbucket.zip https://www.atlassian.com/software/stash/downloads/binary/atlassian-bitbucket-4.14.0.zip
    unzip atlassian-bitbucket.zip
    rm -fr atlassian-bitbucket.zip
    sh atlassian-bitbucket*/bin/start-bitbucket.sh

.. toggle-code-block:: sh
    :label: Instalacja za pomocą `Docker`

    docker volume create --name bitbucketVolume
    docker run -v bitbucketVolume:/var/atlassian/application-data/bitbucket --name="bitbucket" -d -p 7990:7990 -p 7999:7999 atlassian/bitbucket-server

Konfiguracja
^^^^^^^^^^^^
* Stwórz projekt ``Ecosystem Workshop`` o kluczu ``ECO``
* Zaciągnij projekty:

    * https://github.com/SonarSource/sonar-examples
    * https://github.com/SonarSource/sonar-scanning-examples
    * https://github.com/SonarSource/sonar-custom-rules-examples
    * https://github.com/SonarSource/sonar-custom-plugin-example

* Zablokuj ``git push --force`` dla ``sonar-examples``
* W jakim katalogu na dysku znajdują się repozytoria?

Operacje na poziomie systemu operacyjnego
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Z poziomu systemu operacyjnego dopisz do ``sonar-examples`` ``pre-receive`` `Git hook` aby:

    * do pliku ``/tmp/sonar-examples.log``
    * dokładał linię z obecną datą w formacie ISO ``date --iso-8601=seconds``
    * wysyłał maila (subject: commit message, body: diff commita) do Ciebie
    * do czego jeszcze możesz wykorzystać tą funkcjonalność?

`Yet Another Commit Checker`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Zainstaluj plugin ``Yet Another Commit Checker``
* W konfiguracji wymuś sprawdzanie:

    * branchy w konwencji `GIT Flow`
    * commit messages zawierające link do zadania w Jira
    * zadanie w jirze musi istnieć

`Jenkins` integration
^^^^^^^^^^^^^^^^^^^^^
* Skonfiguruj Bitbucket tak, aby wyświetlał informacje na temat budowania branchy i commitów

.. tip:: Webhook plugin to Jenkins

`Jira` integration
^^^^^^^^^^^^^^^^^^
* Zakładanie branchy z poziomu Jiry
* Wyświetlanie kodu oraz informacji o `Pull Request`

`SonarQube` integration
^^^^^^^^^^^^^^^^^^^^^^^
* Skonfiguruj tak, by w każdym `Pull Request` jako komentarz do linii kodu wyświetlały się uwagi z `SonarQube`
* Dostosuj poziom komentarzy, aby nie zalać programisty ich zbyt dużą ilością, np. wyświetlaj tylko ``Blocker`` i ``Critical``

Changelog
^^^^^^^^^
* Za pomocą skryptu wygeneruj changelog pomiędzy dwoma wersjami
* Opisy i dane (priorytet, komponenty itp) zaciągnij z Jiry
* Dlaczego tak jest lepiej?
* za pomocą git hook zrób aby takie informacje przychodziły na maila przy pushu do mastera
