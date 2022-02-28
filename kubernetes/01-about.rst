Kubernetes
==========


Rationale
---------
Kubernetes to narzędzie do orkiestracji kontenerów.


Funkcjonalności
---------------
* Schedulowanie kontenerów - dba, aby kontenery działały,
  aby miały miejsce i zasoby itp
* Zbieranie logów
* Zarządzanie ruchem
* Korzysta z bazy danych etcd
* Posiada wbudowany heart-beat (oraz definiowane strategie,
  np. jeżeli nie żyję, to przekieruj ruch na inną instancję,
  lub spróbuj podnieść ponownie)
* Self-healing
* Autoscaling - możliwe po ustawieniu progów granicznych np. na CPU lub RAM
  (chodzi tu o skalowanie instancji, a nie node'ów - bo tego akurat Kubernetes
  nie potrafi)


Paradygmaty konfiguracji
------------------------
* Kubernetes ma konfigurację deklaratywną.
* Tworzymy plik yaml, a następnie aplikujemy tę konfigurację (apply).

Przykład: chcę mieć uruchomiony kontener dockerowy w trzech instancjach.
Kubernetes sam wybiera, na których node'ach powinien to uruchomić, Sprawdza
jego obciążenie, zajętość oraz dostępne zasoby. Gdy zmieniam stan,
np. ustawiając na dwie instancje, Kubernetes będzie preferował node'y,
na których aplikacja jeszcze nie działa (aby w przypadku niedostępności node'a,
nie zakłóciło to działania systemu).

Konfiguracja imperatywna:

  * specyfikuje dokładne kroki (polecenia) do wykonania,
  * np. zestaw skryptów do wykonania,
  * wykonywana zwykle raz,
  * najczęściej nie może być wykonywana wielokrotnie, bo kończy się błędem,
  * można pisać skrypty obsługujące błędy, ale mocno zwiększa i gmatwa kod,
  * może istnieć wiele przypadków brzegowych, które trzeba pokryć,
  * code review takiego kodu jest trudny.

Konfiguracja deklaratywna:

  * definiuje oczekiwany stan,
  * nie specyfikujemy krok-po-kroku, jak narzędzie ma osiągnąć ten stan,
  * a może się to różnić np. w zależności od systemu operacyjnego,
  * najczęściej w postaci plików yaml (czytelnych przez człowieka),
  * dużo łatwiej robi się code review,
  * można wykonać tylko takie rzeczy (funkcjonalności), które zostały
    udostępnione przez dostawcę rozwiązania.


Architektura
------------
* Master (jedna lub wiele instancji zawiadująca)
* Worker Node
* Kubelet (agencji, aplikacje zainstalowane na worker nodach; cały czas
  komunikują się z Masterem)


Działanie
---------
* Kubernetes zarządza Podami
* W ramach jednego Poda, może być jeden lub wiele kontenerów

Oddzielne Pody:

  * Wszystko, co może gadać po sieci, powinno być oddzielnie
  * Przykład: Wordpress i baza danych, każde może działać niezależnie

Wspólne Pody:

  * Wszystko, co powinno mieć dostęp do jednego filesystemu
  * Wszystko, co musi być na tym samym hoście (wewnątrz jednego Poda).

Uwaga, co gdyby kilka WordPressów ma mieś dostęp do jednej bazy?


Init container
--------------
* Wstaje
* Pobiera konfigurację z repozytorium zewnętrznego
* Zmyka się

Służy tylko do zaciągania konfiguracji ze zdalnego systemu i odłożenia jej
na filesystemie do wykorzystania przez następne kontenery. Takie rozwiązanie
stosuje się np. aby nie mieszać logiki aplikacji z zaciąganiem danych z repo
konfiguracji.


Sidecar
-------
Oddzielne Pody, których rola służy do pomocy innym Podom.

Przykład: szyfrowanie ruchu, np. Istio. Aplikacja sama w sobie nie posiada
żadnych mechanizmów szyfrowania komunikacji. Dzięki temu developerzy nie muszą
sobie zaprzątać tym głowy. Natomiast tworzony jest Pod sidecar - pomocniczy,
który zajmie się szyfrowaniem ruchu. Sam w sobie nie posiada logiki biznesowej,
natomiast odciąża developera od implementacji.


Resource
--------
* `resource` - zasób
* Czasami nazywane `object`
* Pod
* Namespace
* Deployment

Aby wyświetlić wszystkie zasoby w danym Namespace:

    $ kubectl get all
    NAME         READY   STATUS             RESTARTS   AGE
    pod/alpine   0/1     CrashLoopBackOff   13         68m

    NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
    service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   87m

Istio
-----
Service mesh. Razem z podem wdrażany jest kontener, który odpowiedzialny jest
za komunikację między podami. Istio pomija mechanizm Service i służy do
monitoringu ruchu, obciążenia oraz heart-beat i load balancing.
