Deployment
==========


Rationale
---------
Instrukcja o tym, jak wdrażany jest jeden pod. W deployment zapisane są:
liczba instancji, template poda, strategie (jak wygląda: reload, recreate...),
health check, rollback, rozmiar pamięci, informacje dotyczące skalowania.
Deployment tworzy się za pomocą polecenia: ``kubectl create deployment``

Pliki deployment trzymane są w YAML.
Deployment tworzy zasób: Replica Set (zbiór Podów).


Konfiguracja
------------
Przykładowy plik ``deployment.yaml``:

    $ cat deployment.yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: jenkins
      labels:
        app: jenkins
    spec:
      template:
        metadata:
          labels:
            app: jenkins
        spec:
          containers:
            - name: jenkins
              resources:
                limits:
                  cpu: 1
                  memory: 2Gi
                requests:
                  cpu: 1
                  memory: 2Gi


Tworzenie
---------
    $ kubectl create deployment mypod --image=myrepo/myimg
    $ kubectl get deployments
    $ kubectl get pod


Skalowanie
----------
Zwróć uwagę, że na końcu Poda jest hash i identyfikator
Jak będziesz skalował, to podów będzie coraz więcej i idki muszą być unikalne.

    $ kubectl scale deployment mypod --replicas=3

Skalowanie w dół:

    $ kubectl scale deployment mypod --replicas=1

Istnieje możliwość automatycznego skalowania, tzw. Autoscaler.


Listowanie
----------
Listuje wszystkie pody

    $ kubectl get pod

Wyświetla liczbę podów w ramach deploymentu:

    $ kubectl get deployment
    $ kubectl get all

Namespace pozwala nam na grupowanie aplikacji. Np. w ramach DTM mamy namespace
tracking i tam mamy pody: adaptery (Creotech, ADSB). W tym Namespace jest
także RabbitMQ.

    $ kubectl describe deployments mypod
    $ kubectl get all -l app=mypod

Jeżeli apka ma bazę danych, to możemy ją olabelować wspólnie w ramach jednego
namespace:

    $ kubectl label pod mypod --list
    $ kubectl label deployments mypod --list


Ekspozycja
----------
    $ kubectl expose pod mypod --port=8080
    $ kubectl expose pod mypod --port=8080 --dry-run=client

Najważniejsze jest `selector`. Service sam w sobie jest głupi i nie analizuje z
czym jest związany. Jeżeli powołam do życia 5 różnych aplikacji i dam im
labelkę np. mylabel i stworzę service i przydzielę mu selector mylabel to
będzie robił round robin między serwisami (mimo tego, że są to niezależne
apki). Są to tzw. referencje miękkie. Kubernetes nie waliduje czy to są to są
instancje tej samej usługi czy przez przypadek mają ten sam label.

Jeżeli powołam instancje które będą miały inny hash
(gdy korzysta z selector.pod-template-hash) to każdy pod powołany z tego
template będzie miał ten sam hash.

Usunięcie deploymentu nie usunie serwisu. Po prostu serwis przestanie działać.
W momencie gdy mamy deployment, to robimy ``kubectl expose`` na deploymencie
a nie na podzie. Wewnątrz deployment jest pod-template-hash i wszystko co jest
powołane do życia w jego ramach ma tą samą labelkę.

    $ kubectl expose deployment mypod --port=8080 --dry-run=client -o yaml

Tzn. instancje aplikacji powinny mieć ten sam label. Wtedy requesty wchodzą do
Service, (który ma selektor) i SVC rozrzuca requesty (round-robin) po
wszystkich instancjach, których labelka pasuje do selektora.

Kubectl-neat jest toolem stworzonym przez community, który ładniej wyświetla
wyniki kubectl

    $ kubectl get deployments mypod -o yaml
    $ kubectl-neat get deployments mypod -o yaml


Label
-----
W metadanych mamy labelkę. To nic innego niż klucz-wartość. Labelki mają cel
informacyjny (np. version). Pozwalają także np. wspólnie usuwać zasoby. Każdy
resource może mieć labelkę. Niektóre usługi mogą się wiązać po labelkach.
Service jest powiązany z podem przez labelki.

Jak tworzymy deployment, to kubernetes tworzy replica set, który patrzy
i widzi, że ma trzy repliki, więc tworzy trzy repliki.


Annotation
----------
Definicja anotacji wygląda jak definicja labelki. Są podobne do anotacji
w Javie i służą do dodatkowych informacji dla 3rd party narzędzi. Np. jakieś
parametry konfiguracyjne dla parserów itp. Anotacje są specyficzne dla
konkretnych narzędzi i przez inne są ignorowane.


Inne
----
Przy deploymencie on nie usuwa starych, tylko zachowuje je na potrzebę
ewentualnego rollbacku. Można ustalić `spec.revisionHistoryLimit`
w `deployment.yaml` ile takich wersji zostawić

W definicji deploymentu definiujemy nazwę wolumenu i jego miejsce na systemie
operacyjnym.

W definicji pod dajemy informację o podmontowanych wolumentach (o nazwach) i
gdzie one się linkują w ramach poda.

Zmienne środowiskowe definiujemy w definicji poda.


Strategie
---------
* Rolling update
* Zero-downtime
* Blue-green deployment

