*****************************************
Wersjonowanie aplikacji i kodu źródłowego
*****************************************

Projekty informatyczne, w których wytwarzanie zaangażowane jest wiele osób wymagają odpowiedniego podejścia do zarządzania zarówno wersjami jak i kodem źródłowym. W każdym takim oprogramowaniu wcześniej czy później przychodzi konieczność wprowadzenia systemu do kontroli wersji takiego jak np. `GIT`. Już samo to narzędzie pozwala w prosty i efektywny sposób na scalanie i śledzenie zmian wprowadzanych przez programistów. Największą jednak zaletą tego typu oprogramowania jest możliwość równoległej pracy nad systemem przez wiele osób. W XXI wieku gdzie projekty informatyczne stały się gigantyczne i długotrwałe, a w proces ich tworzenia zaangażowane są dziesiątki osób takie podejście jest jedynym skutecznym sposobem na wytwarzanie oprogramowania.

Firma jest organizacją dbającą o jakość wytworzonych rozwiązań. Dla poprawy kodu aplikacji stworzonego w ramach działań operacyjnych mają zastosowanie ogólnie przyjęte dobre praktyki wytwarzania oprogramowania oraz konwencje nazewnicze zgodne o ogólnoświatowym standardem dla danej technologii. Aby utrzymać przejrzystość oraz możliwość szybkiego śledzenia zmian, w systemie kontroli wersji został przyjęty standard nazewnictwa kolejnych przyrostów (ang. `commit`) oraz gałęzi (ang. `branch`) z nowymi funkcjonalnościami z poprawkami błędów. Przyjęta konwencja jest standardem opartym na uproszczonym schemacie `GIT Flow`, zwanym dalej `Lean GIT Flow`.

Dzięki zastosowaniu takiej konstrukcji system do przechowywania repozytorium może wymieniać informacje z aplikacją do zarządzania zadaniami oraz przyporządkowywać dany kod odpowiednim zadaniom. Umożliwia to także łatwą weryfikację oraz śledzenie postępu pracy nad konkretną funkcjonalnością.

Konwencja opisu zmian w systemie kontroli wersji
================================================

Każda zmiana w systemie kontroli wersji powinna zostać opisana według następującego przykładu:

    ``ID-1337 Poprawka arkusza css formularza w module X``

Powyższy przykład wymaga zastosowania odpowiedniego identyfikatora zadania w systemie do zarządzania projektem. W swoim opisie zestaw zmian (`commit`) powinien być zawierać znacznik konkretnego zlecenia na wykonanie zmian. Pozostała część opisu powinna jak najlepiej oddawać charakter wprowadzonej poprawki opisując dokładnie dokonaną zmianę. Zaleca się nieużywanie polskich znaków diakrytycznych oraz innych znaków specjalnych w opisie ze względu na możliwą niekompatybilność pomiędzy systemami. Polskie znaki specjalne należy zmienić na ich odpowiedniki. Długość pierwszej linii opisu wraz z identyfikatorem nie powinna przekraczać 80 znaków.

Dzięki zastosowaniu takiej konstrukcji system do hostowania repozytorium może wymieniać informacje z aplikacją do zarządzania zadaniami oraz przyporządkowywać dany kod odpowiednim zadaniom. Umożliwia to także łatwą weryfikację oraz śledzenie postępu pracy nad konkretną funkcjonalnością.

Konwencja nazewnicza wersji
===========================

W ramach projektów ma zastosowanie następująca konwencja nazewnicza wersji, tzw. `Semantic Versioning`:

    ``X.Y.Z``

Każda z kolejnych części rozdzielonych kropką jest liczbą naturalną (przykład ``1.23.1``). Pierwszy segment oznacza tzw. wersję ``major``, środkowy ``minor`` a ostatni ``bugfix``.

Wszystkie narzędzia produkowane zewnętrznie oraz wewnętrznie powinny być opatrzone odpowiednią zależnością od konkretnej wersji. Nie przewiduje się wprowadzenia wersji "latest" ze względu ma możliwość niekompatybilności aplikacji ze zmianami.

Wersja major
------------

Wersja ``major`` jest używana do określania zmian niekompatybilnych wstecznie lub przełomowych względem publicznego `API` aplikacji. Wszystkie narzędzia produkowane wewnętrznie lub zewnętrznie powinny precyzyjnie określać wersję ``major`` aplikacji, gdyż ma to krytyczny wpływ na ich działanie oraz kompatybilność.

Wersja ``minor``
----------------

Wersja "minor" jest używana do określenia kolejnych przyrostów funkcjonalności aplikacji. Zgodnie z konwencją nazewniczą funkcjonalności w publicznym `API` dla danej wersji powinny wyłącznie przyrastać, chyba że jest to jasno określone i przeprowadzone zgodnie z polityką wyprowadzania zmian z użycia (ang. `deprecation`). Wprowadzone zmiany w wersji ``minor`` nie powinny powodować niekompatybilności pomiędzy oprogramowaniem zewnętrznym i wewnętrznym.

Wersja ``bugfix``
-----------------

Wersja ``bugfix`` jest przeznaczona do użytku wyłącznie dla poprawek bezpieczeństwa oraz funkcjonalności, wprowadzonych omyłkowo lub zauważonych podczas zwiększenia wersji ``minor``.

Zarządzanie gałęziami
=====================

W ramach Firmy została wdrożona konwencja nazewnicza zwana `GIT Flow`. W ramach jej zastosowania wyróżnia się kilka specyficznych gałęzi rozwojowych oprogramowania. Każda z nich posiada unikalną rolę.

Branch produkcyjny ``master``
-----------------------------

W repozytorium główną gałęzią (ang. `branch`) jest ``master``. Przechowywana jest w nim stabilna wersja kodu będąca odpowiednikiem wersji znajdującej się na środowisku produkcyjnym. Scalenie kodu do brancha ``master`` jest równoważne z wydaniem nowej wersji i jest dopuszczalne jedynie, gdy testy automatyczne, funkcjonalne, regresyjne i jednostkowe nie pozostawiają wątpliwości na temat stabilności oraz braku defektów we wprowadzonych zmianach. Branch ten odpowiada 1 do 1 sytuacji na produkcji.

Gdy kod pobierany jest z ``Github.com`` lub ``Bitbucket.com`` zwykle nie zmienia się domyślnego brancha (domyślnie jest ``master``). Po ściągnięciu oczekujesz, że kod będzie stabilny i się uruchamiał. Tym samym przesłaniem kierujemy się w Firmie. Domyślny branch z repozytorium, które klonujesz musi być stabilny i zielony.

W wersji odchudzonej podejścia gałęzie z funkcjonalnościami bezpośrednio są scalane z ``master`` dzięki czemu integracja kodu przebiega szybko i często. Dzięki częstemu scalaniu kodu funkcjonalności są mniejsze a problemy integracyjne ujawniają się zdecydowanie szybciej. Rozwiązywanie małych konfliktów jest nie tylko łatwiejsze ale również nie wymaga dużej ingerencji w projekt.

Dopuszcza się możliwość niewykorzystywania gałęzi ``develop`` w projekcie, gdy wielkość projektu jest nieznaczna a wprowadzenie dodatkowego procesu przejściowego jest nadmierne. Nie zwalnia to z obowiązku utrzymywania stabilnego kodu w gałęzi głównej (``master``) i wymaga wprowadzenia podobnego procesu weryfikacji zmian dla każdej poprawki lub/i funkcjonalności, co w przypadku wdrożenia na środowisko produkcyjne.

.. figure:: ../../_static/img/git-flow-paper-04.jpg
    :scale: 50%

    Schemat scalania funkcjonalności z gałęzią ``master``.

Gałąź integracyjna ``develop``
------------------------------

W dużych repozytoriach, nad którymi pracuje wiele osób na raz (np. kilka 6±3 osobowych zespołów) zachodzi konieczność wprowadzenie integracyjnej gałęzi rozwojowej (ang. `branch`). Zabieg ten ma na celu zabezpieczenie mastera przez scalaniem kodu, który mógłby go zdestabilizować. Dzięki takiemu podejściu proces staje się trochę bardziej skomplikowany ale za to pewniejszy i przewidywalny.

W takim przypadku w repozytorium główną gałęzią rozwojową staje się branch ``develop``. Przechowywana jest w nim najnowsza wersja oprogramowania ze scalonymi ukończonymi funkcjonalnościami. Gałąź ``develop`` powinna przechowywać kod, co do którego poprawności nie ma zastrzeżeń. Kod powinien się budować oraz być odpowiednio przetestowany. Z gałęzi rozwojowej ``develop`` w każdym momencie można stworzyć tzw. kandydata do wdrożenia (ang. `release candidate`).

Stan powyżej opisany jest wysoce pożądany w przypadku każdego projektu bez względu na jego wielkość wraz z wprowadzeniem tzw. `Continuous Delivery`. Do czasu uzyskania odpowiedniej dojrzałości procesowej, zaleca się stosowanie pośredniczącej gałęzi ``develop`` w celu integrowania zmian.

.. figure:: ../../_static/img/git-flow-paper-10.jpg
    :scale: 50%

    Schemat scalania funkcjonalności z gałęzią ``develop``.

Gałąź tymczasowa ``release/X.Y``
--------------------------------

Wprowadzenie brancha integracyjnego, który w standardzie `GIT Flow` nazywany jest ``develop`` nakłada konieczność wprowadzenia sposobu wdrażania kodu, tj. scalania go z branchem produkcyjnym (``master``). W tym celu tymczasowo powoływany jest branch ``release/X.Y`` (`X.Y.Z` oznaczają numer wersji zgodnie z wcześniejszym opisem, tzw. `semantic versioning`: ``major.minor``), który jest tzw. kandydatem wydania (ang. `release candidate`). Na tej gałęzi odpalane są wszystkie testy, podnoszona jest wersja w ``pom.xml`` oraz w razie konieczności wprowadzane są poprawki. Po pozytywnym przejściu przez proces testów gałąź ``release/X.Y`` jest scalana z gałęzią ``master`` a zmiana (ang. ``commit``) jest otagowywany numerem wersji wdrożenia.

Obrazek poniżej przedstawia graficzną reprezentację procesu wdrożenia, tj. scalenia kodu z brancha integracyjnego ``develop`` do brancha stabilnego master. 

.. figure:: ../../_static/img/git-flow-paper-22.jpg
    :scale: 50%

    Schemat scalania gałęzi ``develop`` z ``master`` za pośrednictwem ``release``.

Rodziny branchy
---------------

Aby ułatwić wyszukiwanie wprowadzanych zmian w repozytorium oraz powiązania ich ze zleceniami i zadaniami w systemie do zarządzania projektami, Firma przyjęła konwencję nazywania gałęzi według następującego schematu:

    ``feature/ID-1337-dodanie-nowej-funkcjonalnosci-do-modulu``

    ``bugfix/ID-1337-poprawka-wyswietlania-dokumentu-formularza``

    ``hotfix/ID-1337-poprawka-krytycznego-bledu-na-produkcji``

Zgodnie z powyższym przykładem, nowa funkcjonalność powinna być poprzedzona stosownym przedrostkiem ``feature/`` a poprawka błędów ``bugfix/``. Następnie po prefiksie następuje unikalny identyfikator zadania. Po identyfikatorze następuje zwięzły kilkuwyrazowy opis wprowadzonych modyfikacji. W opisie nie należy stosować polskich znaków diakrytycznych, aby uniknąć możliwości wystąpienia niekompatybilności pomiędzy systemami. Spacje w opisie funkcjonalności lub błędu powinny być zamienione na myślniki. Długość całego opisu wraz z identyfikatorem nie powinna przekraczać 80 znaków.

Dzięki zastosowaniu powyższej konwencji w repozytorium wszystkie zmiany będą należały do odpowiednich gałęzi funkcjonalności lub błędów i będą jednoznacznie opisane. Umożliwia to dokładne śledzenie wszystkich zmian i łączenie ich z odpowiednimi zleceniami w systemie do zarządzania projektem.

Branche ``bugfix/*`` i ``hotfix/*``
------------------------------------

Proces obsługi branchy ``bugfix/*`` i ``hotfix/*`` nieco się różni, chociaż schemat na rysunku wygląda bardzo podobnie.

Branche ``bugfix/*`` służą do poprawy błędów znalezionych podczas produkcji oprogramowania a system scalania ich z kodem źródłowym jest podobny do obsługi ``feature/*``.

Branche ``hotfix/*`` natomiast odpowiadają za poprawkę błędów znalezionych na środowisku produkcyjnym. Dzięki takiej konwencji nazewniczej i separacji gałęzi ich obsługa, np. wdrożenie na środowisko, może być przyspieszona. Wszystkie zmiany które znajdą się w gałęziach ``hotfix/*`` mogą omijać standardową procedurę wdrożenia, tj. stworzenie brancha ``release/X.Y`` i odpalenie testów. Zmiany priorytetowe mają na celu natychmiastowe przywrócenie działania oprogramowania, np. po krytycznym błędzie na produkcji, gdzie każda sekunda zwłoki powoduje straty. Zmiany te, dopiero w późniejszym etapie poddawane są normalnemu procesowi testowania i weryfikacji. Mechanizm ten pozwala na szybkie "ugaszenie pożaru" i przywrócenie stabilności systemu. Ta funkcjonalność powinna być używana jedynie w uzasadnionych przypadkach.

.. figure:: ../../_static/img/git-flow-paper-29.jpg
    :scale: 50%

    Schemat scalania zmian z gałęzi z rodziny ``bugfix/*`` i ``hotfix/*`` do kodu źródłowego aplikacji.

Branche ``feature/*``
---------------------

Branche z rodziny ``feature/*`` służą do wprowadzania funkcjonalności do systemu. Ich nazewnictwo jest ściśle powiązane z systemem kontroli zadań (ang. `issue tracker`). Dzięki takiej separacji mamy pełną transparentność i możliwość śledzenia historii wprowadzanych zmian w projekcie.

.. figure:: ../../_static/img/git-flow-paper-04.jpg
    :scale: 50%

    Schemat scalania funkcjonalności ``feature/*`` z gałęzią ``master``.

.. figure:: ../../_static/img/git-flow-paper-10.jpg
    :scale: 50%

    Schemat scalania funkcjonalności ``feature/*`` z gałęzią ``develop``.

Nazwa gałęzi dla kodu przeznaczonego do wdrożenia
-------------------------------------------------

Podczas procesu wdrożenia następuje moment wydzielenia gałęzi tzw. kandydata do wdrożenia (ang. `release candidate`) o nazwie:

    ``release/X.Y``

gdzie numery odpowiadają kolejnej wersji np. ``release/1.4``. Konwencja nazewnicza wersji przedstawiona jest w osobnym podpunkcie.

Na wyżej wymienionej gałęzi przeprowadzane są testy i wprowadzane ewentualne poprawki zgodnie z procesem wprowadzania zmian i poprawek błędów przedwdrożeniowych. Po pomyślnej weryfikacji automatycznej następuje faza testów manualnych, zgodnie z procedurą i ścieżką ich przeprowadzania.

W miarę możliwości wszelkie akcje użytkownika końcowego lub testera powinno się automatyzować tak, aby proces weryfikacji odbywał się bezdotykowo a do jego wyników nie było zastrzeżeń.

Tagowanie
=========

Po scaleniu gałęzi ``release/X.Y`` następuje proces oznaczania odpowiedniego momentu w historii przez tzw. tagowanie z etykietką o nazwie wersji zgodnej z odpowiednią konwencją. Dzięki temu w każdej chwili istnieje możliwość szybkiego powrotu do krytycznego momentu w repozytorium oraz zobaczenie logów zmian.

Proces Pull Request
===================

Przed wprowadzeniem jakichkolwiek zmian do gałęzi integracyjnych wymagany jest proces tzw. `Pull Request`. Polega on na stworzeniu strony na której znajduje się wylistowany zmieniony kod, tj. dodane i usunięte linijki wraz ze zmodyfikowaną treścią. Na karcie `Pull Requesta` system do Ciągłej Integracji zamieszcza informacje o wyniku analizy i testów. Gdy wszystkie testy przejdą a zmiana uzyska zgodę (ang. `aproove`) przynajmniej dwóch osób pojawia się możliwość scalenia funkcjonalności do docelowego miejsca. Proces ten uodparnia kod na przypadkowe błędy. Większa ilość osób zaangażowanych w przegląd kodu procentuje w przyszłości w postaci zmniejszenia długu technicznego. Ponadto to rozwiązanie spełnia funkcję edukacyjną gdzie osoby z większym doświadczeniem mogą przekazać informacje swoim młodszym kolegom na temat konsekwencji zmian.

.. figure:: ../../_static/img/git-pull-request-05.jpg
    :scale: 50%

    Schemat momentu tworzenia `Pull Requesta` przy scalaniu zmian.

.. figure:: ../../_static/img/git-pull-request-09.jpg
    :scale: 50%

    Karta podsumowania `Pull Request` z informacjami wynikowymi z systemu budowania.
