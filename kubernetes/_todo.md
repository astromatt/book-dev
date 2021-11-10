TODO
====

Tworzenie Kontenerów

* To co chcemy wrzucić na Kubernetes, musi być kontenerem, którego Kubernetes wrzuca sobie w Poda


Push
----
* Docker push

    $ docker login
    $ docker tag ...
    $ docker push


Uruchamianie
------------
* `kubectl run`
* `kubectl create deployment` - powstanie replication i będzie pozwalał na kontrolowanie

    $ kubectl create deployment myapp --image=myrepo/myapp
    $ kubectl get all

Nie dotykamy Replica Setów oraz nie dotykamy Podów.
Jeżeli chcemy skalować lub zmieniać Pody, to robimy to tylko przez deployment.

    $ kubectl logs myapp


Aplikacja ma application.yaml

    spring:
      datasource:
      validation-query: SELECT 1
      test-on-borrow: true
      url: ${database.url}
      username: ${database.user}
      password: ${database.password}
      driverClassName: ${database.driver}

I później:

    $ kubectl create deployment database --image=postgres
    deployment.app/database created

    $ kubectl get pod
    $ kubectl logs database

Baza danych się wywali, bo brakuje zmiennych środowiskowych `POSTGRES_USER`

    $ kubectl create secret generic database \
        --from-literal POSTGRES_DB=mydb \
        --from-literal POSTGRES_USER=myusername \
        --from-literal POSTGRES_PASSWORD=mypassword

Aktualizuje deployment o informacje z Secret:

    $ kubectl set env --from=secret/database deployment/database

Za każdym razem, kiedy modyfikujemy jakiś zasób, Kubernetes robi jeszcze raz
deployment.

    $ kubectl exec database-* printenv
    $ kubectl describe deployments.apps database

Wyświetli informację o kontenerach w ramach Poda oraz informację o zmiennych
środowiskowych i sekretach, oraz skąd te dane pochodzą (secrets, configmap).

    $ kubectl-neat get deployment -o yaml
    $ kubectl get pod
    $ kubectl get logs

Po stworzeniu podów, aby komunikowały się ze sobą (aplikacja z bazą), konieczne
jest stworzenie Service. Baza danych musi wystawić Service, bo

Koniecznie trzeba pamiętać, aby nie zrobić expose na podzie. To zadziała,
ale jak tylko pod się zmieni (np. przy redeployment), to Service się rozwali.
Aby zadziałało to poprawnie, to robimy Service na deploymencie.

    $ kubectl expose deployment database --port=5432
    $ kubectl get all

Czas pomiędzy restartami rośnie w sposób wykładniczy (coraz większe odstępy
między restartami).

Nigdy nie łączyć się do aplikacji za pomocą IP, bo ten adres może się zmienić.

Wprowadzanie zmiennej środowiskowej:

    $ kubectl set env deployment database-application \
        -e DATABASE_URL=jdbc:postgresql://database:5432/test
    deployment.apps/database-application env updated

SpringBoot potrafi sobie przetłumaczyć DATABASE_URL na database.url

    $ kubectl describe deployments.apps database-application

Wstrzykiwanie sekretów:

    $ kubectl set env --from=secret/database deployment/database-application
    deployment.apps/database-application env updated

Zmieniamy nazwę definicję zmiennych środowiskowych.
Name z POSTGRES_USER na DATABASE_USER itp.

    $ kubectl edit deployments.apps database-application
    $ kubectl get pod


Montowanie Configów
-------------------
ConfigMapy i Secrets można montować jako zasoby dyskowe do podów.

    $ kubectl create configmap database-application --from-file=application.yaml
    configmap/database-application created

Montowanie wolumenów:

    $ kubectl edit deployments.app database-application

    volumes:
      - name: config-volume
        configMap:
          name: myconfigmap

Klucz będzie plikiem, a zawartością pliku będzie wartość tego klucza.

    volumeMounts:
      - name: config-volume
        mountPath: /config/

Jak wejdziemy na kontener to w `/config` będziemy mogli zobaczyć plik:
application.yaml. Jeżeli podmontowanych jest wiele zmiennych, to każda z nich
będzie osobnym plikiem w katalogu `/config`

    $ kubectl get pod
    $ kubectl exec -it database-* /bin/bash

Następnie na kontenerze wykonujemy polecenia:

    $ cd /
    $ ls -la /config
    $ cat /config/application.yaml


Zapisywanie
-----------

    $ kubectl get all

Jeżeli weksportujemy czystym kubectl, to będziemy mieli problem, bo przy
imporcie powie nam, że niektóre

Ekportujemy w tej kolejności:

  * namespace
  * secret (bo niczego nie wymaga)
  * deployment
  * service

Eksport danych

    $ kubectl-neat get secret database -o yaml > secret.yaml
    $ kubectl-neat get deployment database -o yaml > deployment.yaml
    $ kubectl-neat get service -o yaml > service.yaml
    $ kubectl-neat get configmap database-application -o yaml > configmap.yaml
    $ kubectl-neat get deployment database-application -o yaml > deployment.yaml
    $ kubectl-neat get namespaces cicd -o yaml > deployment.yaml

Plik nazywamy `resources.yaml`. Jeżeli chcemy w ramach jednego pliku trzymać
wszystkie zasoby, to rozdzielamy je trzema myślnikami `---` w jednym pliku
yaml. Z Service wyrzucić ClusterIP.

    $ kubectl apply -f resources.yaml

Struktura katalogu:

    project
      - k8s
        - dev
          - resources.yaml
