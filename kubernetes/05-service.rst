Service
=======


Rationale
---------
Zasób, dzięki któremu pody widziane są przez inne pody. W momencie, kiedy
tworzymy service, tworzony jest adres IP, ale nie powinniśmy z niego korzystać
tylko po nazwach domenowych


Konfiguracja
------------
Pliki konfiguracji Service trzymane są w `service.yaml`


Tworzenie
---------
Stwórz Service:

    $ kubectl expose pod myservice --port=8080


Listowanie
----------
Wypisz aktywne usługi:

    $ kubectl get service myservice

Na 99% będziemy zawsze korzystali z ClusterIP i wystawiali go na zewnątrz za
pomocą Ingres. Z innego poda, w tym samym namespace możemy dobić się po
nazwie domenowej i porcie, np. http://myservice:8080 Nigdy nie powinno się
odwoływać bezpośrednio wykorzystując adres IP danego Poda, gdyż przy
skalowaniu wszystkie requesty omijałyby load balancing.

Wyświetl definicje Poda:

    $ kubectl get service myservice -o yaml    #  wyświetla definicja poda

Wyświetl konfigurację usługi:

    $ kubectl expose pod myservice --port=8080 --dry-run=client
    $ kubectl expose pod myservice --port=8080 --dry-run=client -o yaml

W specyfikacji pod można wpisać port, na którym usługa nasłuchuje,
ale zachowuje się to tak jak w Docker, tzn. jest to tylko w celu komunikacji
między tworzącym pod a osobą uruchamiającą i zdefiniowany tutaj port nie jest
wystawiany automatycznie.

    $ kubectl run mypod --image=myrepo/myimg --port=8080 --dry-run=client -o yaml

Wypisz aktywne usługi:

    $ kubectl get service
    $ kubectl get svc

W Kubernetes można zastosować zarówno długą nazwę "service" jak i skróconą
"svc". Jedno i drugie zadziała to samo.


Ekspozycja
----------
Wystaw pod na świat:

    $ kubectl expose pod mypod


Kasowanie
---------
Usuwanie Poda:

    $ kubectl delete pod mypod
