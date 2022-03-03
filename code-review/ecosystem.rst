DevTools Ecosystem
==================


Rationale
---------
* Ekosystem narzędziowy
* Architektura
* Skalowanie


Ekosystem wewnętrzny i zewnętrzny
---------------------------------
* Dla subkontraktorów
* Musi być wpięty do wspólnego LDAP lub AD
* Czy jest sens robienia i utrzymywania dwóch ekosystemów
* Czy dając subontraktorowi dostęp do naszego ekosystemu, to on nie wie za dużo
* Czy na 100% mamy wszystko ukryte by default, i to się nie zmieni (np. któryś z liderów zespołów współpracujący z innym zespołem zbyt obszernie otworzy dostęp (dla wszystkich)
* Tworzymy template repozytorium, z wszystkim skonfigurowanym i wpiętym
* Ważniejsze jest robienie Code Review na kodzie podkontraktorów, niż na własnym, bo w zespole rozmawiamy, a kontraktor dostarcza Wam gotowe rozwiązanie, a jak wcześnie nie zrobicie inspekcji, to może: a) robić kod niezrozumiały b) wybrać technologie, frameworki lub praktyki u Was nie stosowane co podniesie koszt utrzymania
* System Code Review, ale również SonarQube pokazują problemy w kodzie
* W tych systemach da się by default zobaczyć kontekst problemu (czytaj zobaczyć kod źródłowy pliku) co w konsekwencji prowadzi do tego, że ktoś inny ma całkowity dostęp do Twojego kodu źródłowego
* Configuration as a Code jest life-saver


Architecture
------------
.. figure:: img/ecosystem-big-picture.png


Alternatives
------------
.. figure:: img/ecosystem-tools.png
