Kubectl
=======

Rationale
---------
* Polecenie `kubectl` ma wiele wspólnego z poleceniem `docker`
* Pozwala na uruchamianie kontenerów Dockerowych (np. z https://hub.docker.com)
* Domyślnie Kubernetes korzysta z Dockerhub


Run
---
* Kubernetes przy `kubectl run` (jeżeli image nie był wcześniej uruchamiany)
  zaciągnie najnowszą wersję z Dockerhub
* Kubernetes samodzielnie nie będzie aktualizował obrazów
* Aby wymusić aktualizację obrazu, trzeba wykonać polecenie `kubectl update`

Składnia:

    $ kubectl run mypod --image=myrepo/myimg
    # `mypod` - nazwa Poda jak ma być widoczna z systemu
    # `myrepo/myimg` - nazwa repozytorium oraz obrazu z Dockerhub

Przykład:

    $ kubectl run alpine --image=alpine
    pod/alpine created

    $ kubectl get pods
    NAME    READY  STATUS    RESTARTS  AGE
    alpine  0/1    Completed  0       7s

    $ kubectl describe pod alpine

READY 0/1 oznacza, że w ramach Poda działa zero z jednego kontenera.
Tzn. że Pod definiuje jeden kontener, ale aktualnie nie jest uruchomiony.
Image alpine się uruchomił, ale zaraz zamknął, bo nie miał żadnego polecenia
do wykonania po uruchomieniu. Gdyby to była normalna usługa, to byłoby 1/1,
bo po uruchomieniu odpalony zostałby proces, który nasłuchiwałby na połączenia.
Jak uruchamiamy `kubectl run --image=...` to zawsze będzie 1/1, bo uruchamiamy
jeden kontener.


Wyświetl
--------
Aby wyświetlić zasoby, należy użyć polecenia `kubectl get`, np.:

    $ kubectl get pod
    $ kubectl get namespace

Wyświetlenie wszystkich Podów z danego Namespace:

    $ kubectl get pod -n myns
    Name:         alpine
    Namespace:    default
    Priority:     0
    Node:         docker-desktop/192.168.65.4
    Start Time:   Thu, 08 Apr 2021 20:35:21 +0200
    Labels:       run=alpine
    Annotations:  <none>
    Status:       Running
    IP:           10.1.0.6
    IPs:
      IP:  10.1.0.6
    Containers:
      alpine:
        Container ID:   docker://f55676bd90bc0562ab813578ec6de17abd3452559a62b78a12555dd3db663880
        Image:          alpine
        Image ID:       docker-pullable://alpine@sha256:ec14c7992a97fc11425907e908340c6c3d6ff602f5f13d899e6b7027c9b4133a
        Port:           <none>
        Host Port:      <none>
        State:          Waiting
          Reason:       CrashLoopBackOff
        Last State:     Terminated
          Reason:       Completed
          Exit Code:    0
          Started:      Thu, 08 Apr 2021 21:29:25 +0200
          Finished:     Thu, 08 Apr 2021 21:29:25 +0200
        Ready:          False
        Restart Count:  11
        Environment:    <none>
        Mounts:
          /var/run/secrets/kubernetes.io/serviceaccount from default-token-9jxj2 (ro)
    Conditions:
      Type              Status
      Initialized       True
      Ready             False
      ContainersReady   False
      PodScheduled      True
    Volumes:
      default-token-9jxj2:
        Type:        Secret (a volume populated by a Secret)
        SecretName:  default-token-9jxj2
        Optional:    false
    QoS Class:       BestEffort
    Node-Selectors:  <none>
    Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                     node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
    Events:
      Type     Reason     Age                   From               Message
      ----     ------     ----                  ----               -------
      Normal   Scheduled  58m                   default-scheduler  Successfully assigned default/alpine to docker-desktop
      Normal   Pulled     57m                   kubelet            Successfully pulled image "alpine" in 5.0393864s
      Normal   Pulled     57m                   kubelet            Successfully pulled image "alpine" in 2.5498538s
      Normal   Pulled     57m                   kubelet            Successfully pulled image "alpine" in 2.0662898s
      Normal   Created    57m (x4 over 57m)     kubelet            Created container alpine
      Normal   Pulled     57m                   kubelet            Successfully pulled image "alpine" in 2.0025227s
      Normal   Pulling    56m (x5 over 58m)     kubelet            Pulling image "alpine"
      Warning  BackOff    8m46s (x93 over 57m)  kubelet            Back-off restarting failed container
      Normal   Started    3m58s (x12 over 57m)  kubelet            Started container alpine

Aby wyświetlić definicję, która znajduje się w bazie danych, należy:

    $ kubectl get pod alpine -o yaml
    $ kubectl get pod alpine -o json

Wynik, który produkują oba polecenia, jest bardzo "gadatliwy".
Aby uzyskać bardziej przejrzysty przegląd konfiguracji, wykonaj polecenie:

    $ kubectl run alpine --image=alpine --dry-run=client -o yaml
    apiVersion: v1
    kind: Pod
    metadata:
      creationTimestamp: null
      labels:
        run: alpine
      name: alpine
    spec:
      containers:
      - image: alpine
        name: alpine
        resources: {}
      dnsPolicy: ClusterFirst
      restartPolicy: Always
    status: {}

Parametr `dry-run` spowoduje, że polecenie nawet nie dotrze do Kubernetes,
a jedynie zostanie wyświetlona konfiguracja uruchomienia. Wynik polecenia
możemy przekierować do pliku, który posłuży za opis dla następnych uruchomień.

    $ kubectl run alpine --image=alpine --dry-run=client -o yaml > pod.yaml

Sam wynik polecenia zmodyfikować plik usuwając linie:

  * `creationTimestamp: null`
  * `labels:`
  * `run: alpine`
  * `dnsPolicy: ClusterFirst`
  * `restartPolicy: Always`
  * `status: {}`


Aplikowanie konfiguracji
------------------------
Plik finalnie powinien wyglądać:

    $ cat pod.yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: alpine
    spec:
      containers:
      - image: alpine
        name: alpine

Następnie aplikujemy konfigurację:

    $ kubectl apply -f pod.yaml

Konfigurację możemy przechowywać w repozytorium GIT.


Uruchamianie poleceń
--------------------
Podobnie jak w Docker, tak i w Kubernetes można połączyć się do maszyny
w trybie interaktywnym:

    $ kubectl run -it alpine --image=alpine
    If you don't see a command prompt, try pressing enter.
    / #

Później do działającej maszyny można również podłączyć się w trybie
interaktywnym:

    $ kubectl exec -it alpine -- /bin/sh
    / #


Udostępnianie Pod
-----------------
Aby inne Pody mogły rozmawiać z naszym Podem, konieczne jest stworzenie tzw.
Service. Samo stworzenie Service nie powoduje udostępnienie Poda na zewnątrz
świata, a jedynie pozwala na rozmowę w sieci wewnętrznej (między Podami).

    $ kubectl expose pod alpine
    error: couldn't find port via --port flag or introspection
    See 'kubectl expose -h' for help and examples

Błąd spowodowany jest tym, że w pliku konfiguracyjnym nie było informacji
o porcie, na którym nasłuchuje usługa. Konieczne jest ręczne podanie portu:

    $ kubectl expose pod alpine --port 8080
    service/alpine exposed

Polecenie wyświetla wszystkie informacje o zasobach:

    $ kubectl get all
    NAME         READY   STATUS    RESTARTS   AGE
    pod/alpine   1/1     Running   1          12m

    NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
    service/alpine       ClusterIP   10.111.154.21   <none>        8080/TCP   57s
    service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP    129m

Aby wyświetlić bardziej szczegółowe informacje:

    $ kubectl describe service alpine
    Name:              alpine
    Namespace:         default
    Labels:            run=alpine
    Annotations:       <none>
    Selector:          run=alpine
    Type:              ClusterIP
    IP:                10.111.154.21
    Port:              <unset>  8080/TCP
    TargetPort:        8080/TCP
    Endpoints:         10.1.0.7:8080
    Session Affinity:  None
    Events:            <none>


Kasowanie Poda
--------------
Aby skasować Pod w Kubernetes, uruchom:

  $ kubectl delete pod alpine
  pod "alpine" deleted
