Minikube
========


Rationale
---------
Jedno-node'owy klaster Kubernetes, który pozwala testować rozwiązania bez
konieczności posiadania wielu serwerów. Minikube może z powodzeniem być
wykorzystany do wszystkich czynności związanych z tworzeniem i zarządzaniem
podami. W miarę zwiększania złożoności Ingresów i sieciowych elementów
konfiguracyjnych jego przydatność spada.


Uruchamianie
------------
    $ minikube start


Listowanie
----------
Wypisanie wszystkich aktywnych node'ów:

    $ kubectl get node

Na liście powinien być widoczny tylko jeden node Minikube.

Listowanie wszystkich podów:

    $ kubectl get pod

    $ kubectl run mypod --image=myrepo/myimg --port=8080
    $ kubectl get pod


Logi
----
Wyświetl wszystkie wydarzenia w systemie:

    $ kubectl get events
    $ kubectl describe pod mypod


Ekspozycja
----------
Wystaw usługę na świat:

    $ kubectl expose pod mypod
    $ kubectl get pod
    $ kubectl get svc

Podczas poprzednich poleceń nie został podany namespace, więc k8s wrzucił nam
do default.


Usunięcie
---------
    $ kubectl get svc
    $ kubectl -n myns default delete pod mypod
    $ kubectl get svc


Forwarding Portów
-----------------
W minikube ciężko jest definiować ingresy, także łatwiej jest użyć
forwardowania portu:

    $ kubectl port-forward mypod 8080:8000


Zastosowanie
------------
Testowanie narzędzi, ArgoCD wszystko jest uruchamiane na minikube
i ładnie działa
