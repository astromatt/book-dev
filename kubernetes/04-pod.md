Pody
====


Rationale
---------
Najmniejsza jednostka w Kubernetes. Pody grupują kontenery. Na 99% jest to
jeden pod jeden kontener, ale można mieć wiele kontenerów np. bazy danych.
Polecenie ``kubectl run`` tworzy jednego Poda, tj. jedną instancję aplikacji.
Do niedawna to polecenie tworzyło również deployment, ale już nie.


Organizacja
-----------
* Kubernetes organizuje pody w namespace'ach
* Przy uruchamianiu podów można podać w namespace ma być uruchomiony


Tworzenie
---------
Uruchamia pod na podstawie image

    $ kubectl run --image=myrepo/myimg


Zarządzanie podami
------------------
Wyświetl pody w namespace `myns`:

    $ kubectl -n myns get pod


Wyświetl pody
-------------

    $ kubectl get pod


Usuń pody
---------

    $ kubectl delete pod mypod

Zmiana domyślnego namespace. Od teraz wszystkie polecenia dotyczące podów
(tworzenie, listowanie itp.). Będą pobierały dotyczyły namespace `myns`:

    $ kubectl config set-context --current --namespace=myns
    $ kubectl get pod

Wyświetl logi w trybie nieskończonego streamu

    $ kubectl logs -f NAME
