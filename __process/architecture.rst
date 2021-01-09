********************
Architektura systemu
********************


Wśród aplikacji tworzonych w ramach projektów informatycznych można wyróżnić co najmniej trzy główne warstwy:

    * warstwa widoku (frontendu),
    * warstwa logiki biznesowej (backendu),
    * warstwa persystencji (bazy danych).

Podział ten przyjął się jako standard na świecie. Dzięki wykorzystaniu takiego rozróżnienia w projekcie można tworzyć niezależne od siebie elementy aplikacji, które później stanowią całość oprogramowania. W każdym z poziomów abstrakcji, tj.: widoku, logiki biznesowej oraz persystencji, zastosowanie mają inne, specyficzne dla danej warstwy technologie.

System jest aplikacją internetową wykorzystującą technologie sieci *web*. Dzięki temu uzyskano łatwy, niezależny od wykorzystanego systemu operacyjnego dostęp do danych, który nie wymaga instalacji dodatkowego oprogramowania na urządzeniach użytkowników. Interfejs stworzony został przy pomocy składni języka znaczników *HTML*, technologii *JavaScript / ECMAScript* i arkusza stylów *CSS*. Po stronie serwerowej projekt wykorzystuje wiele języków programowania w celu osiągnięcia założonego celu. Główna aplikacja jest napisana w języku *Python* wykorzystując framework *Django*. Sterowniki urządzeń i sensorów napisane są w języku *C*, a skrypty i narzędzia pomocnicze wykorzystują język powłoki *sh*.

Ilość zastosowanych języków wynika z konieczności dobierania najlepszego narzędzia do rozwiązania problemu. Ponadto w projekcie wykorzystano również takie technologie jak:

    - *Docker* (środowisko uruchomieniowe),
    - *Alpine Linux* (system operacyjny środowiska uruchomieniowego),
    - *Sphinx* (system generowania dokumentacji),
    - *reStructuredText* (język formatowania i tworzenia dokumentacji),
    - *gettext* (system tłumaczeń i obsługi formatów międzynarodowych),
    - *JSON* (format przesyłu danych między warstwą serwerową a użytkownika),
    - *HTTP* (protokół przesyłu danych),
    - *REST* (protokół komunikacji klient-serwer),
    - *PostgreSQL* (relacyjny system bazodanowy).

Wszystkie zastosowane technologie w aplikacji są dostępne bez jakichkolwiek opłat na zasadach otwartego kodu źródłowego, rozpowszechniane na wolnych w sensie prawnym licencjach użytkowania i modyfikacji. Są szeroko wykorzystywane w projektach informatycznych na świecie, a bezpieczeństwo ich stosowania jest sprawdzone i potwierdzone.

Ze względu na zastosowanie oprogramowania *Open Source* jak również restrykcyjnego podejścia do wykorzystania jedynie liberalnych licencji projekt jest odporny na sytuacje, w których dostawca oprogramowania mógłby przestać rozwijać daną technologię. Taka sytuacja skutkowałoby koniecznością przepisania części systemu. Mogłoby to również wpłynąć na brak przychylności przy implementacji rozwiązania w agencjach kosmicznych.


Uzasadnienie wyboru języka programowania logiki biznesowej
==========================================================
*Python* jest obecnie najbardziej dynamicznie rozwijającym się językiem programowania i znajduje się w czołówce wiodących składni i kompilatorów :cite:`TiobeIndex2019`. Znajduje zastosowanie w środowisku akademickim, w przemyśle, przy badaniach i rozwoju, w przetwarzaniu ogromnych wolumenów danych oraz w uczeniu maszynowym. W tym ostatnim zastosowaniu jest najpopularniejszą technologią na świecie :cite:`MLBestLang2017`, :cite:`MLBestLang2016`.

Wybór tego języka jest uzasadniony ze względu na konieczność szybkiego prototypowania komponentów aplikacji oraz integracji z zewnętrznymi bibliotekami wykorzystywanymi w uczeniu maszynowym i sztucznej inteligencji. Technologia ta umożliwia łatwy rozwój systemu. W przypadku konieczności zastosowania bardziej wydajnego przetwarzania danych możliwa jest częściowa implementacja poszczególnych funkcjonalności w języku *C*, z którym *Python* jest interoperacyjny. U podstaw wyboru technologii leżała również możliwość swobodnego wymieniania poszczególnych komponentów aplikacji na rozwiązania, które są wydajniejsze lub bardziej porządne np. ze względu na zgodność ze standardami.

Obecna konwencja tworzenia oprogramowania międzynarodowej stacji kosmicznej *ISS* zakłada wykorzystanie języka *Ada*. Język ten jest najczęściej używany w zastosowaniach kosmicznych, lotniczych i wojskowych, gdyż posiada deterministyczną i dającą się udowodnić matematycznie składnię :cite:`CIA1990`, :cite:`Noskin2011`, :cite:`ISSFacts2019`. Ze względu na wąską specjalizację oraz przeznaczenie języka *Ada*, środowisko programistów nie tworzy dużej ilości oprogramowania i bibliotek w tej technologii. Brak szerokiego zastosowania języka i wsparcia znacząco obniża przydatność systemu w innych zastosowaniach i dziedzinach. Spowalnia to również proces wytwarzania oprogramowania. Język *Ada* zajmuje 36 miejsce w zestawieniu najpopularniejszych języków programowania. *Python* zajmuje 4 miejsce ze stale utrzymującym się trendem wzrostu 2.5% w skali miesiąca :cite:`TiobeIndex2019`. Obecne wykorzystanie języka *Ada* w zastosowaniach kosmicznych nie gwarantuje zastosowania tej technologii w przyszłych projektach.

System jest przygotowany na możliwość przepisania fragmentu lub nawet całości aplikacji. Stworzenie systemu w języku *Python* z wyraźnie odseparowanymi elementami jest rozwiązaniem przyszłościowym. Zastosowanie tego języka jest nie tylko wydajniejsze, ale również pozwala na przeprojektowywanie systemu w trakcie jego używania. Zwiększa szybkość wdrażania nowych funkcjonalności i pozostawia system otwartym na wsparcie ogromnego środowiska programistycznego.


Uzasadnienie wyboru szkieletu aplikacji
=======================================
Szkielet aplikacji (ang. *framework*) *Django* jest najbardziej rozbudowanym projektem tego typu dla języka *Python*. Ze względu na dużą popularność tego oprogramowania oraz jasno określoną konwencję tworzenia aplikacji w oparciu o to rozwiązanie istnieje bardzo duże prawdopodobieństwo znalezienia osób mogących rozwijać oprogramowanie oraz naprawiać błędy. Obecnie technologia ta jest wykorzystywana m.in. przy tworzeniu wiodących platform społecznościowych na świecie co pozwala na twierdzenie, że rozwiązanie to będzie wspierane i rozwijane przez wiele lat.

*Django* pozwala na tworzenie modularnych komponentów. Dzieli system na niezależne i dające się łatwo wykorzystać ponownie aplikacje. Każda z aplikacji składa się z modułów:

    - *admin* (konfiguracja panelu administracyjnego modułu),
    - *api* (metody udostępniające czyste dane do integracji),
    - *apps* (konfiguracja danej aplikacji),
    - *locale* (pliki językowe z tłumaczeniem komponentu),
    - *migrations* (pliki migracji schematu bazy danych),
    - *models* (opis modelu danych),
    - *serializers* (definicja metod konwertujących dane modelu do formatu udostępniania),
    - *static* (pliki statyczne, tj. skrypty *JavaScript*, obrazki i arkusze stylów *CSS*),
    - *templates* (pliki szablonów języka *HTML* formatującego dane),
    - *templatetags* (biblioteki makr szablonów),
    - *tests* (testy jednostkowe, regresyjne i dymne aplikacji),
    - *urls* (routing adresów URL dla aplikacji),
    - *views* (metody generujące strony na podstawie szablonów i modelowanych danych).


Uzasadnienie wyboru platformy uruchomieniowej
=============================================
Do automatyzacji budowania projektu oraz zarządzania zależnościami projektu zostało wybrane rozwiązanie *Docker*. Technologia ta jest obecnie wiodącym systemem parawirtualizacji. Umożliwia tworzenie obrazów z zapisanym stanem całego systemu operacyjnego i środowiska uruchomieniowego aplikacji. Na podstawie obrazów tworzone są tzw. kontenery, tj. środowiska uruchomieniowe. Zastosowanie tej technologii pozwala na prostą instalację aplikacji niewymagającą żadnych zależności zewnętrznych poza samą platformą *Docker*.


Uzasadnienie wyboru języka programowania warstwy widoku
=======================================================
Wybór *ECMAScript* jako standaryzowanej wersji języka *JavaScript* jest obecnie jedynym praktycznym wyborem. Język ten obsługują wszystkie przeglądarki internetowe oraz urządzenia mobilne tj. tablety, smartfony i inteligentne zegarki. *ECMAScript* posiada unormowaną składnię w ramach międzynarodowego standardu *ISO/IEC 16262* :cite:`ECMA2019`. Język ten jest niekwestionowanym liderem standardu tworzenia interfejsu użytkownika.


Uzasadnienie wyboru systemu kontroli wersji
===========================================
W ramach projektu jako standard systemu kontroli wersji wybrano rozwiązanie *Git*. Aplikacja ta jest narzędziem pozwalającym na śledzenie zmian oraz ich autorów. Na chwilę obecną jest to najpopularniejsze rozwiązanie tego typu na rynku. Posiada również największe wsparcie wśród narzędzi deweloperskich i zintegrowanych środowisk programistycznych (ang. *IDE*). Ponadto w sieci *Internet* zgromadzone są duże zasoby wiedzy dotyczącej korzystania z tego oprogramowania. Na forach i portalach społecznościowych rozwiązanych jest wiele najczęściej spotykanych problemów.

Zastosowanie *Git* w projekcie wiąże się z przestrzeganiem odpowiednich konwencji nazewniczych oraz procesu wprowadzania funkcjonalności w aplikacji. Temat jest szczegółowo omówiony w rozdziale ":ref:`Proces kontroli wersji i zmian`".
