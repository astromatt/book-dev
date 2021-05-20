Kubernetes
==========


Słowniczek
----------
.. glossary::

    Pod
        Najmniejsza jednostka w Kubernetes, grupuje kontenery. Na 99% jest to
        jeden pod jeden kontener, ale można mieć wiele kontenerów np. bazy
        danych. ``kubectl run`` tworzy jednego poda (jedną instancję). Do
        niedawna to polecenie tworzyło również deployment, ale już nie.

    Namespace
        Grupuje pody i inne zasoby (resource)

    Service
        Zasób, dzięki któremu pody widziane są przez inne pody. W momencie
        kiedy tworzymy service tworzony jest adres IP, ale nie powinniśmy z
        niego korzystać tylko po nazwach domenowych

    Istio
        Service mesh. Razem z podem wdrażany jest kontener który
        odpowiedzialny jest za komunikację między podami. Istio pomija
        mechanizm Service i służy do monitoringu ruchu, obciążenia oraz
        heart-beat i load balancing.

    Ingress
        Umożliwia komunikację z podem z zewnątrz. Na poziomie definicji
        ingresu definiujemy service do którego dopuszcza

    Deployment
        Instrukcja o tym jak wdrażany jest jeden pod. W deployment zapisane
        są: liczba instancji, template poda, strategie (jak wygląda: reload,
        recreate...), health check, rollback, rozmiar pamięci, informacje
        dotyczące skalowania. Deployment tworzy się za pomocą polecenia:
        ``kubectl create deployment``

    Minikube
        Jedno-node'owy klaster Kubernetes, który pozwala testować rozwiązania
        bez konieczności posiadania wielu serwerów. Minikube może z
        powodzeniem być wykorzystany do wszystkich czynności związanych z
        tworzeniem i zarządzaniem podami. W miarę zwiększania złożoności
        Ingresów i sieciowych elementów konfiguracyjnych jego przydatność
        spada.

    Replica
    Replica Set
        Zbiór podów. Deployment tworzy Replica Sety.

    Label
        To nic innego niż klucz-wartość. Labelki mają cel informacyjny (np.
        version). Pozwalają także np. wspólnie usuwać zasoby. Każdy resource
        może mieć labelkę. Niektóre usługi mogą się wiązać po labelkach.
        Service jest powiązany z podem przez labelki.


Zarządzanie podami
------------------
Wyświetl pody w namespace mynamespace:

.. code-block:: console

    $ kubectl -n mynamespace get pod

Uruchamia pod na podstawie image

.. code-block:: console

    $ kubectl run --image myrepository/myimage

Stwórz pod w namespace `mynamespace` na podstawie ``pod.yaml``

.. code-block:: console

    $ cat pod.yaml
    $ kubectl apply -n mynamespace -f pod.yaml

Jeżeli nie określisz namespace, to jest brana wartość domyślna z ``~/.kube/``

.. code-block:: console

    $ ls ~/.kube/...

Wyświetl pody:

.. code-block:: console

    $ kubectl get pod

Usuń pody:

.. code-block:: console

    $ kubectl delete pod mypod

Zmiana domyślnego namespace. Od teraz wszystkie polecenia dotyczące podów (tworzenie, listowanie itp.). Będą pobierały dotyczyły namespace `mynamespace`:

.. code-block:: console

    $ kubectl config set-context --current --namespace=mynamespace
    $ kubectl get pod

Wyświetl logi w trybie nieskończonego streamu

.. code-block:: console

    $ kubectl logs -f NAME


Service
-------
Pliki konfiguracji Service trzymane są w `service.yaml`

Stwórz Service:

.. code-block:: console

    $ kubectl expose pod myservice --port=8080

Wypisz aktywne usługi:

.. code-block:: console

    $ kubectl get service myservice

Na 99% będziemy zawsze korzystali z ClusterIP i wystawiali go na zewnątrz za pomocą Ingres. Z innego poda w tym samym namespace możemy dobić się po nazwie domenowej i porcie, np. http://myservice:8080 Nigdy nie powinniśmy się odwoływać bezpośrednio po adresie IP do danego poda, gdyż przy skalowaniu wszystkie requesty omijały by load balancing.

Wyświetl definicje poda:

.. code-block:: console

    $ kubectl get service myservice -o yaml    #  wyświetla definicja poda

Wyświetl konfigurację usługi:

.. code-block:: console

    $ kubectl expose pod myservice --port=8080 --dry-run=client
    $ kubectl expose pod myservice --port=8080 --dry-run=client -o yaml

W specyfikacji pod można wpisać port na którym usługa nasłuchuje, ale zachowuje się to tak jak w Docker, tzn. jest to tylko w celu komunikacji między tworzącym pod a osobą uruchamiającą i zdefiniowany tutaj port nie jest wystawiany automatycznie.

.. code-block:: console

    $ kubectl run mypod --image=myrepository/myimage --port=8080 --dry-run=client -o yaml

Wypisz aktywne usługi:

.. code-block:: console

    $ kubectl get service
    $ kubectl get svc

W Kubernetes można zastosować zarówno długą nazwę "service" jak i skróconą "svc". Jedno i drugie zadziała to samo.

Wystaw pod na świat:

.. code-block:: console

    $ kubectl expose pod mypod

Skasuj pod:

.. code-block:: console

    $ kubectl delete pod mypod


Ingress
-------
Pliki Ingress trzymane są w ``ingress.yaml``, przykład:

.. code-block:: yaml

    apiVersion: extensions/v1beta1
    kind: Ingress
    metadata:
      labels:
        app: jenkins
      annotations:
        kubernetes.io/ingress.class: nginx
      name: jenkins
      namespace: jenkins
    spec:
      rules:
        - host: jenkins.example.com
          http:
            paths:
              - backend:
                  serviceName: jenkins
                  servicePort: 8080
                path: /

Tworzenie Ingress na podstawie konfiguracji z pliku yaml:

.. code-block:: console

    $ cat ingress.yaml
    $ kubectl apply -f ingress.yaml

Wypisz aktywne Ingress:

.. code-block:: console

    $ kubectl get ingress


Minikube
--------
Uruchamianie:

.. code-block:: console

    $ minikube start

Wypisanie wszystkich aktywnych node'ów:

.. code-block:: console

    $ kubectl get node

Na liście powinien być widoczny tylko jeden node Minikube.

Listowanie wszystkich podów:

.. code-block:: console

    $ kubectl get pod

.. code-block:: console

    $ kubectl run mypod --image=myrepository/myimage --port=8080
    $ kubectl get pod

Wyświetl wszystkie wydarzenia w systemie:

.. code-block:: console

    $ kubectl get events
    $ kubectl describe pod mypod

Wystaw usługę na świat:

.. code-block:: console

    $ kubectl expose pod mypod
    $ kubectl get pod
    $ kubectl get svc

Podczas poprzednich poleceń nie został podany namespace, więc k8s wrzucił nam do default.

Usunięcie:

.. code-block:: console

    $ kubectl get svc
    $ kubectl -n mynamespace default delete pod mypod
    $ kubectl get svc

W minikube ciężko jest definiować ingresy, także łatwiej jest użyć forwardowania portu:

.. code-block:: console

    $ kubectl port-forward mypod 8080:8000

Testowanie narzędzi, ArgoCD wszystko jest uruchamiane na minikube i ładnie działa

Tworzenie namespace:

.. code-block:: console

    $ kubectl create namespace mynamespace
    $ kubectl get namespaces
    $ kubectl config set-context --current --namespace=mynamespace


Deployment
----------
Pliki deployment trzymane są w YAML
Deployment tworzy zasób: Replica Set

Przykładowy plik ``deployment.yaml``:

.. code-block:: yaml

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

.. code-block:: console

    $ kubectl create deployment mypod --image=myrepository/myimage
    $ kubectl get deployments
    $ kubectl get pod

Zwróć uwagę, że na końcu poda jest hash i identyfikator
Jak będziesz skalował, to podów będzie coraz więcej i idki muszą być unikalne.

.. code-block:: console

    $ kubectl scale deployment mypod --replicas=3

Listuje wszystkie pody

.. code-block:: console

    $ kubectl get pod

Wyświetla liczbę podów w ramach deploymentu:

.. code-block:: console

    $ kubectl get deployment

.. code-block:: console

    $ kubectl get all

Skalowanie w dół:

.. code-block:: console

    $ kubectl scale deployment mypod --replicas=1

Istnieje możliwość automatycznego skalowania, tzw. autoscaler.

Namespace pozwala nam na grupowanie aplikacji. Np. w ramach DTM mamy namespace tracking i tam mamy pody: adaptery (Creotech, ADSB). W tym Namespace jest także RabbitMQ.

.. code-block:: console

    $ kubectl describe deployments mypod
    $ kubectl get all -l app=mypod

Jeżeli apka ma bazę danych, to możemy ją olabelować wspólnie w ramach jednego namespace.

.. code-block:: console

    $ kubectl label pod mypod --list
    $ kubectl label deployments mypod --list

.. code-block:: console

    $ kubectl expose pod mypod --port=8080
    $ kubectl expose pod mypod --port=8080 --dry-run=client

Najważniejsze jest `selector`. Service sam w sobie jest głupi i nie analizuje z czym jest związany. Jeżeli powołam do życia 5 różnych aplikacji i dam im labelkę np. mylabel i stworzę service i przydzielę mu selector mylabel to będzie robił round robin między serwisami (mimo tego, że są to niezależne apki). Są to tzw. referencje miękkie. Kubernetes nie waliduje czy to są to są instancje tej samej usługi czy przez przypadek mają ten sam label.

Jeżeli powołam instancje które będą miały inny hash (gdy korzysta z selector.pod-template-hash) to każdy pod powołany z tego template będzie miał ten sam hash.

Usunięcie deploymentu nie usunie serwisu. Po prostu serwis przestanie działać.
W momencie gdy mamy deployment, to robimy ``kubectl expose`` na deploymencie a nie na podzie. Wewnątrz deployment jest pod-template-hash i wszystko co jest powołane do życia w jego ramach ma tą samą labelkę.

.. code-block:: console

    $ kubectl expose deployment mypod --port=8080 --dry-run=client -o yaml

Tzn. instancje aplikacji powinny mieć ten sam label. Wtedy requesty wchodzą do Service, (który ma selektor) i SVC rozrzuca requesty (round-robin) po wszystkich instancjach, których labelka pasuje do selektora.

Kubectl-neat jest toolem stworzonym przez community, który ładniej wyświetla wyniki kubectl

.. code-block:: console

    $ kubectl get deployments mypod -o yaml
    $ kubectl-neat get deployments mypod -o yaml

W metadanych mamy labelkę.
Jak tworzymy deployment, to kubernetes tworzy replica set, który patrzy i widzi, że ma trzy repliki, więc tworzy trzy repliki.

Definicja anotacji wygląda jak definicja labelki. Są podobne do anotacji w Javie i służą do dodatkowych informacji dla 3rd party narzędzi. Np. jakieś parametry konfiguracyjne dla parserów itp. Anotacje są specyficzne dla konkretnych narzędzi i przez inne są ignorowane.

Przy deploymencie on nie usuwa starych, tylko zachowuje je na potrzebę ewentualnego rollbacku. Można ustalić spec.revisionHistoryLimit (deployment.yaml) ile takich wersji zostawić

W definicji deploymentu definiujemy nazwę wolumenu i jego miejsce na systemie operacyjnym.

W definicji pod dajemy informację o podmontowanych wolumentach (o nazwach) i gdzie one się linkują w ramach poda.

Zmienne środowiskowe definiujemy w definicji poda.
