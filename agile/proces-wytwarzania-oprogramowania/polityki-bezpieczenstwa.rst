Bezpieczeństwo aplikacji, kodu źródłowego i danych
==================================================

Ataki na systemy informatyczne mają z reguły u swoich podstaw wprowadzenie do systemu danych, których typ nie został przewidziany w czasie jego tworzenia.

Istotą ataków bardzo często jest wprowadzenie takich danych, które system informatyczny, w którejś ze swoich warstw, zinterpretuje jako komendy lub polecenia, zmieniając w ten sposób jego działanie. Dane te wówczas mogą: nie wpływać bezpośrednio na działanie systemu, ale powodować udostępnienie danych, które nie miały być dostępne, przekształcać działanie systemu na skutek modyfikacji parametrów kontrolujących jego działanie.

Bez względu na charakter jaki posiadają niedozwolone dane wprowadzane do systemu - w zabezpieczaniu systemów przed atakami kluczowe jest weryfikowanie danych wejściowych.


Ogólne środki zaradcze
----------------------
Akceptacja tylko tych danych, które zostały przewidziane w fazie projektowania systemu.

Metoda ta polega na weryfikacji danych wejściowych i zbadaniu czy spełniają one założone z reguły biznesowe kryteria jakości. Jeżeli nie - są odrzucane i nie mogą dostać się głębiej do struktur systemu. Jednym z przykładów może być zaimplementowanie w systemie weryfikacji poprawności danych w polu reprezentującym PESEL, która sprawdzi i wykluczy możliwości wprowadzenia w tym polu innych znaków niż cyfry (np. litery, znak plus).

Weryfikacja i odrzucanie danych wejściowych, przez wzgląd na zawartość złośliwą
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Weryfikacja ta opiera się sprawdzeniu czy dane wejściowe nie noszą znamion próby ataku. Np. próba wykrywania w danych komend systemu operacyjnego (np. ``su``), elementów języka SQL, czy też kont użytkowników systemowych (np. ``root``).

Dla niektórych pól zastosowanie tej techniki jest w ogóle niemożliwe. Ingeruje ona w treść wprowadzanych danych również, kiedy nie stanowią one zagrożenia, a wyeliminowanie wszystkich potencjalnie groźnych słów kluczowych jest zadaniem trudnym w implementacji i utrzymaniu. Z tego powodu stosuje się sprawdzenia wystąpień jedynie symboli sterujących i oznaczanie ich jako nieaktywne - wówczas słowa kluczowe nie będą interpretowane jako polecenia systemowe, czy też kod wykonywalny.

Weryfikacja danych po stronie serwera
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Weryfikacja danych po stronie serwera powinna odbywać się zawsze, nawet wtedy, kiedy została zaimplementowana po stronie aplikacji klienckiej, gdyż weryfikacja ta po stronie klienta jest bardzo słabym zabezpieczeniem. Weryfikację po stronie klienta należy traktować jako informację dla użytkownika, że system nie pozwoli na wprowadzenie danej treści, a nie realne zabezpieczenie.

Przekazywanie danych w systemie przez warstwy abstrakcji
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Posługiwanie się warstwami abstrakcji w systemie nie tylko ułatwia wytwarzanie kodu źródłowego, ale również powoduje modyfikację danych w procesie komunikacji między warstwami. Zjawisko to zwiększa szansę na dostrzeżenie nieprawidłowości w danych np. poprzez błędy w procesie analizy składniowej (ang. *parsing*), a także zabezpiecza przed jednym z najbardziej powszechnych ataków jakim jest SQL injection.

Sposoby weryfikacji danych wejściowych
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Możliwa weryfikacja:

    * długości danych wejściowych oraz czy mieszczą się one w dopuszczalnych zakresach wartości i słownikach,
    * czy dane wejściowe zawierają znaki niedozwolone,
    * danych po stronie serwerowej systemu, nawet wtedy, kiedy po stronie klienckiej wykonuje się identyczne weryfikacje,
    * plików cookie,
    * danych wprowadzonych w pola ukryte,
    * wartości ze względu na występowanie niedozwolonych słów i znaków, sugerujących próbę wprowadzenia danych złośliwych (np. elementów języka SQL, Java, itp.),
    * parametrów wejściowych we wszystkich metodach publicznych klas, a także ich relacji do innych parametrów wejściowych oraz aktualnego stanu obiektu danej klasy,
    * źródła pochodzenia danych (zabezpieczenie przed atakami typu *CSRF - Cross-Site Request Forgery*).


Kontrola dostępu
----------------
Podstawową kwestią ochrony systemów centralnych i końcowych oraz danych jest wprowadzenie odpowiedniej kontroli dostępu, którą należy stosować w celu:

    * Ograniczenia możliwości działania użytkowników,
    * Ograniczenia dostępu użytkowników do zasobów,
    * Definicji funkcji, które użytkownicy mogą stosować do danych.

Mechanizmy kontroli dostępu powinny uniemożliwiać nieuprawnionym: przeglądania, modyfikowania i kopiowania danych. Dodatkowo, mogą powstrzymać przed zastosowaniem złośliwego kodu lub nieuprawnionych działań przez napastnika, wykorzystującego zależności infrastruktury.

Dostęp do informacji w systemach oraz dokumentacji a informacja publiczna
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Udostępnieniu danych na podstawie "Ustawy o dostępie do informacji publicznym" nie podlegają informacje oraz kod źródłowy aplikacji zgromadzony w Bazie Wiedzy, Systemie Zgłoszeń, Repozytorium Kodu Źródłowego i w dokumentacji!

Wyżej wymienione repozytoria są objęte tzw. klauzulą informacji zastrzeżonej przedsiębiorstwa i nie powinny być udostępniane dla osób powołujących się na tą ustawę. W przypadku wstąpienia roszczącego na drogę sądową informacje te nie powinny zostać udostępnione bez prawomocnego wyroku sądu.

Użytkowanie sprzętu prywatnego
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Aby zapewnić bezpieczeństwo środowiska pracy w organizacji regulamin polityki bezpieczeństwa Firmy zabrania używania urządzeń prywatnych do wykorzystania w celu służbowym w Firmie.

Odstępstwo od tej reguły może mieć miejsce tylko i wyłącznie za zgodą kierownika, architekta lub stosownego zastępcy Dyrektora i musi być dobrze umotywowane. W powyższych i uzasadnionych przypadkach muszą zostać spełnione obowiązujące w Firmie standardy bezpieczeństwa, w stopniu nie niższym niż te, dotyczące pracy na służbowych komputerach.

Na szczególną uwagę należy zwrócić aby:

    * dysk musi być szyfrowany bezpiecznie,
    * firewall musi być skonfigurowany,
    * praca na użytkowniku musi się odbywać na użytkowniku pozbawionym praw administratora,
    * system musi być bezpieczny, aktualny, wspierany przez producenta,
    * w systemie nie ma malware'u (oprogramowanie antywirusowe w systemie Windows, ``chrootkit/debsums`` w Linux/\*nix),
    * nie przechowywanie danych/kopii zapasowych na zdalnych chmurach.

Weryfikacja i sprawdzanie danych wejściowych
--------------------------------------------
Ataki na systemy informatyczne mają z reguły u swoich podstaw wprowadzenie do systemu danych, których typ nie został przewidziany w czasie jego tworzenia.

Istotą ataków bardzo często jest wprowadzenie takich danych, które system informatyczny, w którejś ze swoich warstw, zinterpretuje jako komendy lub polecenia, zmieniając w ten sposób jego działanie. Dane te wówczas mogą nie wpływać bezpośrednio na działanie systemu, ale powodować udostępnienie danych, które nie miały być dostępne, przekształcać działanie systemu na skutek modyfikacji parametrów kontrolujących jego działanie.

Bez względu na charakter jaki posiadają niedozwolone dane wprowadzane do systemu - w zabezpieczaniu systemów przed atakami kluczowe jest weryfikowanie danych wejściowych.


Ogólne środki zaradcze
----------------------

Akceptacja tylko tych danych, które zostały przewidziane w fazie projektowania systemu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Metoda ta polega na weryfikacji danych wejściowych i zbadaniu czy spełniają one założone z reguły biznesowe kryteria jakości. Jeżeli nie - są odrzucane i nie mogą dostać się głębiej do struktur systemu. Jednym z przykładów może być zaimplementowanie w systemie weryfikacji poprawności danych w polu reprezentującym PESEL, która sprawdzi i wykluczy możliwości wprowadzenia w tym polu innych znaków niż cyfry (np. litery, znak plus).

Weryfikacja i odrzucanie danych wejściowych, przez wzgląd na zawartość złośliwą
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Weryfikacja ta opiera się sprawdzeniu czy dane wejściowe nie noszą znamion próby ataku. Np. próba wykrywania w danych komend systemu operacyjnego (np. ``su``), elementów języka SQL, czy też kont użytkowników systemowych (np. ``root``).

Dla niektórych pól zastosowanie tej techniki jest w ogóle niemożliwe. Ingeruje ona w treść wprowadzanych danych również, kiedy nie stanowią one zagrożenia, a wyeliminowanie wszystkich potencjalnie groźnych słów kluczowych jest zadaniem trudnym w implementacji i utrzymaniu. Z tego powodu stosuje się sprawdzenia wystąpień jedynie symboli sterujących i oznaczanie ich jako nieaktywne - wówczas słowa kluczowe nie będą interpretowane jako polecenia systemowe, czy też kod wykonywalny.

Weryfikacja danych po stronie serwera
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Weryfikacja danych po stronie serwera powinna odbywać się zawsze, nawet wtedy, kiedy została zaimplementowana po stronie aplikacji klienckiej, gdyż weryfikacja ta po stronie klienta jest bardzo słabym zabezpieczeniem. Weryfikację po stronie klienta należy traktować jako informację dla użytkownika, że system nie pozwoli na wprowadzenie danej treści, a nie realne zabezpieczenie.

Przekazywanie danych w systemie przez warstwy abstrakcji
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Posługiwanie się warstwami abstrakcji w systemie nie tylko ułatwia wytwarzanie kodu źródłowego, ale również powoduje modyfikację danych w procesie komunikacji między warstwami. Zjawisko to zwiększa szansę na dostrzeżenie nieprawidłowości w danych np. poprzez błędy w procesie analizy składniowej (ang. parsing), a także zabezpiecza przed jednym z najbardziej powszechnych ataków jakim jest SQL injection.

Sposoby weryfikacji danych wejściowych
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Możliwa weryfikacja:

    * długości danych wejściowych oraz czy mieszczą się one w dopuszczalnych zakresach wartości i słownikach,
    * czy dane wejściowe zawierają znaki niedozwolone,
    * danych po stronie serwerowej systemu, nawet wtedy, kiedy po stronie klienckiej wykonuje się identyczne weryfikacje,
    * plików cookie,
    * danych wprowadzonych w pola ukryte,
    * wartości ze względu na występowanie niedozwolonych słów i znaków, sugerujących próbę wprowadzenia danych złośliwych (np. elementów języka SQL, Java, itp.),
    * parametrów wejściowych we wszystkich metodach publicznych klas, a także ich relacji do innych parametrów wejściowych oraz aktualnego stanu obiektu danej klasy,
    * źródła pochodzenia danych (zabezpieczenie przed atakami typu CSRF - Cross-Site Request Forgery).


Szczegółowy opis zagrożeń i obrony
----------------------------------

Cross-site Scripting
^^^^^^^^^^^^^^^^^^^^
Atakiem typu cross-site scripting zagrożone są serwery sieci, serwery aplikacji i środowiska aplikacji. Ataki te są możliwe, kiedy napastnik używa aplikacji internetowej do wprowadzenia złośliwego kodu, często języka skryptowego JavaScript lub aktywnych zawartości, takich jak: ActiveX, VBscript, Shockwave, Flash, itp.

Złośliwy kod ukrywany jest często przez używanie technik kodujących, takich jak: Unicode.

Do dwóch głównych kategorii cross-site scripting zalicza się:

    * przechowywanie: kod wejściowy przechowywany jest w bazie danych na stałe (np. login użytkownika, wiadomość, itp.),
    * odbijanie: kod wejściowy wybiera trasę alternatywą do ofiary, np. e-mail.

Do głównych zagrożeń zalicza się:

    * proste zakłócenia np. wyświetlanie nieoczekiwanej zawartości,
    * przeadresowywanie użytkownika do innej strony,
    * "porwania" (hijack) sesji,
    * ujawnienia nieautoryzowanej zawartości i zmian zawartości witryny.

:Środki kontrolno-zaradcze:

    Należy sprawdzać czy nagłówki, pliki cookie, pola formularza, ciągi zapytań zawierają dozwolone parametry/treści.
    Aplikacje mogą zyskać znaczną ochronę przez konwersję następujących znaków w generowanych danych wyjściowych (języki mogą posiadać funkcje umożliwiające wykonanie tego w sposób automatyczny):

    == =====
    z  do
    == =====
    <  &lt;
    >  &gt;
    (  &#40;
    )  &#41;
    #  &#35;
    &  &#38;
    == =====

SQL Injection
^^^^^^^^^^^^^
Napastnicy mogą bezpośrednio przesyłać zapytania lub polecenia do silnika bazy danych, kiedy dane wejściowe użytkownika nie są rygorystycznie sprawdzane.

Niedostatecznie zweryfikowane parametry mogą zawierać polecenie SQL, które w momencie skierowania do aplikacji zostaną umieszczone w  dynamicznym zapytaniu bazy danych, wykonywanym zgodnie z uprawnieniami konta aplikacji. Poziom zagrożenia wzrasta wraz z poziomem uprzywilejowania konta.

Skutkami mogą być:

    * narażenie prywatności danych klienta,
    * dostęp do osobistych danych klienta (dane finansowe, medyczne, itp.),
    * nieuprawniona zmiana hasła administratora albo innych haseł klienta,
    * nieautoryzowana zmiana danych i oddziaływanie na integralność bazy danych,
    * utrata podstawowych tabel.

:Środki kontrolno zaradcze:

    * Należy sprawdzać czy dane wejściowe są akceptowalne; jeśli nie - odrzucać je.
    * Nigdy nie należy nadawać uprawnień administratora bazy danych użytkownikom aplikacyjnym. Aplikacja sieciowa powinna funkcjonować z minimalnymi przywilejami wymaganymi do wykonywania jej funkcji.
    * Należy sprawdzać poprawność kodów wyjściowych i zwrotnych, aby zapewnić oczekiwane przetwarzanie.
    * Należy weryfikować uprawnienia użytkownika do wykonywania zapytań na wybranych tabelach.
    * Należy konwertować dane wejściowe do systemu do bezpiecznej postaci.

Wprowadzanie poleceń systemowych
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Większość języków programowania zapewnia używanie poleceń systemowych i wiele aplikacji korzysta z tej funkcjonalności. Interfejsy systemowe w języku programowania i skryptowania przekazują polecenia wejścia do podległego systemu operacyjnego. Z kolei OS przetwarza dane wejściowe i zwraca wyniki do aplikacji (lub pliku bądź innego uchwytu systemowego) w formie binarnej lub tekstowej.

Zależnie od języka programowania lub skryptu i systemu operacyjnego, możliwa jest:

    * wykonanie dowolnego polecenia przez system,
    * zmiana parametrów przekazanych do komend systemu,
    * wywołania dodatkowych poleceń w ramach poprawnie wykonywanych poleceń.

:Środki kontrolno-zaradcze:

    * Należy sprawdzać czy dane wejściowe są akceptowalne; jeśli nie - odrzucać je.
    * Nigdy nie należy pozwalać serwerowi sieci pracować jako ADMINISTRATOR  lub ROOT.
    * Aplikacja sieci powinna funkcjonować z minimalnymi uprawnieniami wymaganymi do wykonywania jej funkcji.
    * Jeżeli polecenia OS muszą zostać użyte, wszystkie parametry wprowadzane do nich powinny być bardzo dokładnie sprawdzone. Dane wprowadzane przez użytkownika nie mogą być przekazywane wprost do polecenia systemowego bez analizy składniowej.
    * Należy zaimplementować odpowiednie mechanizmy obsługi ewentualnych błędów, upływu przewidzianego czasu lub blokad podczas prośby.
    * Należy sprawdzać poprawność kodów wyjściowych i zwrotnych, aby zapewnić właściwe przetwarzanie.
    * Należy ograniczyć dostęp do programów wykonujących polecenia systemowe, np. cmd.exe.


Obchodzenie ścieżek
^^^^^^^^^^^^^^^^^^^
System plików serwera sieciowego może być użytkowany do czasowego lub trwałego zbierania informacji.

Jeżeli aplikacje i serwery sieciowe nie sprawdzają albo nie obsługują prawidłowo meta-znaków do opisu ścieżek (np. '../'), aplikacja może być narażona na atak obejścia ścieżki. Napastnik może stworzyć żądanie podania danych z fizycznej lokalizacji pliku, takie jak /etc/passwd (nazywane też groźbą ujawnienia pliku). Ataki takie są często wykonywane w połączeniu z wykonywaniem poleceń systemowych i SQL Injection.

:Środki kontrolno-zaradcze:

    * Należy wykorzystywać funkcje normalizacji ścieżki zawartej w języku programowania.
    * Należy usuwać niebezpieczne elementy ścieżek, takie jak '../' oraz ich warianty Unicode z danych wejściowych systemu.
    * Należy używać bezwzględnych ścieżek, wykorzystując zmienne środowiskowe lub konfigurację do określenia lokalizacji plików i katalogów.
    * Należy sprawdzać czy dane wejściowe są akceptowalne; jeśli nie - odrzucać je.


Meta-znaki
----------

Znaki niedrukowalne i drukowalne, oddziałujące na zachowanie poleceń: systemu operacyjnego, języka programowania, procedur programu i pytań baz danych, są zwykle wprowadzane do parametrów kodowanych przez URL w ciągach zapytań.

Przykłady meta-znaków
^^^^^^^^^^^^^^^^^^^^^

==== ===========================================================================================
Znak Znaczenie
==== ===========================================================================================
 ;   Dla dodatkowego wykonywania poleceń
 |   Dla przekierowań strumienia wynikowego z programu do innych poleceń
 !   Dla ponownego wykonywania poprzednio używanych poleceń
 &   Dla dodatkowego wykonywania poleceń
x20  Spacje dla fałszowania URL i innych nazw
x00  Puste bajty dla odcinania ciągów znaków i nazw pliku
x04  EOF dla fałszowania zakończeń pliku
x0a  Nowe linie dla dodatkowego wykonania poleceń,
x0d  Nowe linie dla dodatkowego wykonania poleceń,
x1b  Klawisz Escape - zależny od OS
x08  Klawisz Backspace - zależny od OS (usuwanie plików logujących, zmienianie zawartości pliku)
x7f  Klawisz Delete - zależny od OS
 ~   Tylda - zależna od OS (automatyczne rozszerzenia nazw)
==== ===========================================================================================

:Środki kontrolno-zaradcze:

    * Wszędzie, gdzie to możliwe należy usuwać meta-znaki z danych wejściowych.
    * Należy sprawdzać czy dane wejściowe posiadają oczekiwany typ danych.
    * Analiza składniowa parametrów URL oraz danych formularzy w celu zablokowania, substytucji przez bezpieczne encje lub wyłączenia (ang. escape) takich znaków.

Bajty zerowe
^^^^^^^^^^^^
Wiele aplikacji programowych dla dalszego postępowania i funkcjonowania, często przekazuje dane bezpośrednio do niższego poziomu funkcji C.

Jeżeli ciąg "XXX\0YYY" zostanie poprawnie przyjęty przez aplikację, zostanie skrócony do postaci "XXX". Dzieje się tak dlatego, że zerowe bajty (\0) są interpretowane jako zakończenie ciągu.

Aplikacje, które nie sprawdzają adekwatnie danych wejściowych mogą zostać oszukane poprzez wprowadzenie bajtów zerowych w "kluczowych" parametrach. Jest to zwykle wykonywane przez kodowanie URL bajtów zerowych (%00). W wyjątkowych sytuacjach możliwe jest użycie znaków Unicode.

Skutkami ataku mogą być:

    * Udostępnienie ścieżki fizycznej, plików oraz informacji operacyjnych systemu
    * Obcięcie ścieżki
    * Wykonanie poleceń OS
    * Wydanie polecenia parametrom
    * Ominięcie kontroli podczas szukania podciągów w parametrach
    * Odcięcie ciągów przekazanych do zapytań SQL

:Środki kontrolno-zaradcze:

    * Przed czynnościami aplikacyjnymi należy sprawdzić wszystkie dane wejściowe i zapewnić poprawną interpretację danych.

Przepełnione bufory
^^^^^^^^^^^^^^^^^^^
Zjawisko to wiąże się z przekazaniem dużej ilości danych, przekraczających ilość oczekiwaną przez aplikację dla danego wejścia lub parametrów ciągu zapytań. Jedynym ze skutków przepełnienia bufora może być nieoczekiwane zachowanie aplikacji, która pozwoli napastnikowi wykonywać polecenia w jej kontekście. Ryzyko jest większe wtedy, kiedy aplikacja działa na poziomie systemu lub konta administratora systemu operacyjnego.

:Środki kontrolno-zaradcze:

    * Należy sprawdzać ciągi danych wejściowych oraz odrzucać żądania wykraczające poza rozmiar wcześniej zdefiniowanego ciągu,
    * Należy sprawdzać ciągi zapytań URL, zawartość oraz nagłówki i odrzucać jakiekolwiek żądania wykraczające poza ustalone wcześniej rozmiary zbioru,
    * Uruchamiać aplikacje w kontekście konta o ograniczonych uprawnieniach, jeśli to możliwe.

Normalizacja
------------
Normalizacja (ang. normalization lub canonicalization, c14n - dotyczące normalizacji do postaci kanonicznej) jest to proces konwersji na prostszą formę. Aplikacje sieciowe muszą obsługiwać normalizacje różnych danych wejściowych oraz wyjściowych, od kodowania URL do tłumaczenia adresu IP.

Unicode
^^^^^^^
Kodowanie Unicode jest sposobem przechowywania znaków z wieloma bajtami. Jeżeli dane wejściowe są dopuszczone, Unicode może zostać wykorzystany w celu ukrycia złośliwego kodu. Wiele sposobów kodowania tekstu wskazuje RFC2279.

:Środki kontrolno-zaradcze:

    * Należy wybierać odpowiednią formę normalizacji i upewniać się czy wszystkie wprowadzane dane użytkownika są ustandaryzowane do tej formy, zanim jakakolwiek zatwierdzona decyzja zostanie wykonana.
    * Kontrola bezpieczeństwa powinna być przeprowadzona po zakończeniu procesu kodowania.

Kodowanie URL
^^^^^^^^^^^^^
Tradycyjne aplikacje sieciowe przenoszą dane pomiędzy serwerem a klientem używającym protokołów HTTP lub HTTPS. Do głównych metod odbioru zalicza się:

====== ============================================
Metoda Opis
====== ============================================
GET    kiedy dane są przekazywane w URL
POST   kiedy dane są przekazywane w nagłówkach HTTP
====== ============================================

Jeżeli dane zawarte są w URL, konieczne jest kodowanie zachowujące odpowiednią składnię URL. RFC1738 definiuje URL a RFC2396 definiuje URI. Obydwa ograniczają dozwolone znaki w URL lub URI do podzbiorów zbiorów znaków US-ASCII. RFC1738 oznacza:

* Tylko alfanumeryczne, specjalne znaki "$-_.+!*’()," oraz znaki zastrzeżone używane do zastrzeżonych celów mogą zostać użyte jako niekodowane w obrębie URL.

Jednakże dane używane przez aplikacje sieciowe nie są ograniczane w ten sposób. Wcześniejsza wersja HTML pozwalała na pełen zakres zbioru znaków ISO-8859-1 (ISO Latin-1). Specyfikacja HTML 4.0 została rozszerzona, aby zezwolić na dowolne znaki w zbiorze Unicode.

Dla kodowania znaku w URL, 8-bitowy kod szesnastkowy poprzedzany jest prefiksem %. Do przykładów zalicza się: zbiór znaków US-ASCII, który reprezentuje spację z dziesiętnym kodem 32 (20 w kodzie szesnastkowym). Korzystający z aplikacji sieciowych mają zatem możliwość widzieć spacje, które zostały zamienione na następujący ciąg znaków "%20" w URL.

Choć niektóre znaki nie potrzebują kodowania URL, kod 8 bitowy może być zakodowany.

W związku z tym, że kodowanie URL zezwala w rzeczywistości na przekazywanie dowolnych danych serwerowi, koniczne okazuje się podjęcie stosownych środków ostrożności przez aplikacje sieciowe. Brak ich może spowodować stan, w którym aplikacja będzie podatna na złośliwe działania.

:Środki kontrolno-zaradcze:

    * Nie należy używać metody GET do zatwierdzania zmiany w formularzu; aby uniknąć dodawania danych do URL używaj HTTP POST.
    * Jeśli URL ma być użyty do przekazywania danych do serwera sieci, należy ograniczyć rodzaje przekazywanych danych i nie zezwalać na dane tekstowe. Należy stosować zasady sprawdzenia w celu wyczyszczenia danych i zapewnienia ich poprawnego typu i rozmiaru.
    * Nie należy opierać się na sprawdzeniu po stronie klienta.
    * Dane wrażliwe, związane z bezpieczeństwem, lub obszerne objętościowo należy wysyłać wyłącznie za pomocą metody POST, ze względu na przechowywanie URL w logach dostępowych serwera.

Manipulacja parametrami
-----------------------
Napastnik może przeprowadzić atak na niewystarczająco zabezpieczone aplikacje, modyfikując dane zawarte w plikach cookie, nagłówkach HTTP lub URL w sposób niezgodny z zamierzeniami twórców aplikacji. Jeżeli aplikacja pozwoli na przyjęcie tak zmodyfikowanych danych (np. tokenu sesji), może dojść do przełamania zabezpieczeń.

Nie można zatem przyjąć, że dane przesłane do przeglądarki pozostaną niezmienione, chyba, że są kryptograficznie chronione na poziomie aplikacji. SSL nie chroni przed tego typu atakami, ponieważ dane są zmienione po stronie klienta, przed ich wysłaniem do serwera.

Manipulacja plikami cookie
^^^^^^^^^^^^^^^^^^^^^^^^^^
Każda forma plików cookie przed odesłaniem ich do serwera może zostać zmanipulowana. Rozmiar manipulacji zależy od celów, do których zostały one użyte. Wiele plików cookie jest kodowanych jako Base64, co nie zapewnia kryptograficznej ochrony.

:Środki kontrolno-zaradcze:

    * Nie należy ufać danym wejściowym użytkownika dla wartości, które są już znane.
    * Należy używać jednego tokenu dla zidentyfikowania zbioru danych charakterystycznych dla danej sesji użytkownika zmagazynowanych w pamięci po stronie serwera.

Manipulacja polami formularza
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Wybrane lub wprowadzone informacje są zwykle magazynowane jako wartości pola formularza i wysyłane do aplikacji przez polecenia HTTP (GET lub POST). HTML również może przechowywać wartości pola jako ukryte, które nie są wyświetlane na ekranie przez przeglądarkę, ale są gromadzone i przedstawione jako parametry podczas przesyłania formularzy.

Niezależnie od typu pola formularza (pole rozwijane, zaznaczenie lub bloki tekstowe), wszystkie mogą być zmodyfikowane przez użytkownika. W większości przypadków jest to możliwe przez edycję źródła strony.

Do przykładów manipulacji polem formularza od strony klienta zalicza się m.in.:

Zwiększenie przywilejów: zmiana wartości z 0 na 1 po to, aby móc przejść na tryb debugowania, co może powodować uruchomienie dodatkowych funkcji aplikacji, ujawnić hasła systemu i bazy danych, układu logicznego aplikacji, itp.

Kod początkowy:

    ``<input name="debug" type="hidden" value="0">``

Kod zmieniony:

    ``<input name="debug" type="hidden" value="1">``

Przepełnienie bufora: napastnik usuwa maksymalną długość wprowadzanych danych, aby usunąć po stronie klienta limit 10 znaków w polu ID użytkownika i próbować zastosować przeładowanie bufora.

Kod początkowy:

    ``<input name="userid" type="hidden" maxlength="10">``

Kod zmieniony:

    ``<input name="userid" type="hidden">``

Zwiększenie przywilejów: zmiana wartości ‘n’ na ‘y’ powodująca, stan, w którym aplikacja zwiększa przywileje dostępu do poziomu administratora.

Kod początkowy:

    ``<input name="adminaccess" type="hidden" value="n">``

Kod zmieniony:

    ``<input name="adminaccess" type="hidden" value="y">``

:Środki kontrolno-zaradcze:

    * Zawsze należy sprawdzać dane wejściowe po stronie serwera. Nie należy polegać na sprawdzeniu ze strony klienta.
    * Należy unikać pól ukrytych, używać pojedynczych tokenów sesji do wskazywania danych zmagazynowanych w cache po stronie serwera. Jeśli aplikacja wymaga sprawdzenia cech użytkownika, weryfikuje sesję plików cookie z tabelą sesji oraz wskazuje dane użytkownika w cache / bazie danych.
    * Jeżeli nie ma możliwości wprowadzenia powyższych rozwiązań i konieczne jest użycie pól ukrytych, należy połączyć pary nazw i wartości w pojedynczy ciąg i dopisać tajny klucz (który nigdy nie pojawi się w danym formularzu) na końcu ciągu. Ciągiem nazywa się wychodzącą treść formularza. Jest dla niej generowany MD5, SHA lub podobny jednostronny hash nazywany "outgoing form digest" dodawany do formularza jako dodatkowe ukryte pole.
    * Kiedy formularz zostaje odebrany przez serwer, pary nazw i wartości są ponownie łączone z tajnym kluczem tworząc przychodzącą treść formularza. Form digest przychodzącej treści formularza jest generowany i porównywany z zawartym w treści formularza. Jeżeli sumy kontrolne nie są identyczne, oznacza to, że ukryte pole zostało zmienione. Technika ta może być też stosowana w przypadku URL w celu uniemożliwienia manipulacji parametrami.

Manipulacja nagłówkiem http
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Nagłówki HTTP wykorzystywane są do przekazywania danych z sieci klienta do serwera dla żądań HTTP i odwrotnie dla odpowiedzi HTTP.

Istnieje możliwość wprowadzenia kontroli nadchodzących nagłówków, ale w takich przypadkach należy pamiętać, że jeśli pochodzą one od klienta mogą być zmienione przez napastnika.

Jako przykład można zastosować nagłówek referencyjny, który zwykle zawiera URL strony, z której pochodzi żądanie. Istnieje możliwość sprawdzenia takiego nagłówka w celu weryfikacji, czy żądanie pochodzi z wiarygodnego URL (np. własnego), tak, aby przeszkodzić napastnikom zapisanie stron sieci, zmodyfikowanie formularzy i przesłanie ich z innego komputera.

Nie jest to jednak bezpieczny mechanizm, gdyż napastnik może zmodyfikować nagłówek referencyjny HTTP tak, aby wyglądał na pochodzący z wiarygodnej strony.

:Środki kontrolno-zaradcze:

    * Nie należy polegać na nagłówkach bez dodatkowych mechanizmów ochronnych.

Manipulacje w URL
^^^^^^^^^^^^^^^^^
Formularze HTML mogą przedkładać swoje wyniki z zastosowaniem albo HTTP POST albo HTTP GET. W przypadku stosowania metody HTTP GET, wszystkie nazwy elementów i wartości formularza pojawiają się w ciągu zapytań URL, co daje szanse napastnikowi na łatwą manipulację wartościami lub próbę przekazania nieoczekiwanych danych.

:Środki kontrolno-zaradcze:

    * Należy unikać używania parametrów w ciągu zapytań.
    * Jeżeli parametry muszą być przedłożone do serwera, należy upewnić się czy towarzyszą im ważne tokeny sesji.
    * Jeżeli parametru nie można usunąć z ciągu zapytań, należy go chronić kryptograficznie z zastosowaniem silnych algorytmów kryptograficznych.

Jest to możliwe za pomocą następujących metod:

    * utajnianie całego ciągu zapytań,
    * dodanie dodatkowego parametru w ciągu pytań, będącego sumą SHA-1. Nie zapobiega to przeglądaniu ciągu przez użytkownika, ale jeżeli aplikacja sprawdzi zwrócony hash i nie spełni żądań, w których hash nie pasuje, uniemożliwi ich zmianę i przedłożenie, odrzucając dane wprowadzone przez użytkownika.


Ujawnianie informacji i prywatność użytkownika
----------------------------------------------
Napastnicy używają szeregu metod, aby uzyskać informacje, które mogłyby stanowić podstawę do przeprowadzenia ataku na witryny lub infrastruktury wspomagające.

Komendy po stronie klienta
^^^^^^^^^^^^^^^^^^^^^^^^^^
Dodawanie i utrzymywanie komentarzy w kodzie źródłowym było standardową praktyką, usprawniającą późniejszy serwis. Praktyka ta ma zastosowanie do stron HTML, co w zależności od charakteru komentarzy może powodować ujawnianie wrażliwych informacji o strukturze witryny, jej podległej infrastrukturze albo członkach personelu. Komentarze często pozostawiane na stronach HTML zawierają nazwy serwera, błędy, struktury katalogów, adresy IP, zdebugowane informacje, nazwiska programistów, numery telefonów czy adresy emailowe.

:Środki kontrolno-zaradcze:

    * Należy usuwać komentarze z kodu zanim zostaną przeniesione do usług produkcyjnych (oprócz dotyczących praw autorskich, licencji czy własności intelektualnej!).
    * Należy upewniać się czy w procedurach zapewnienia jakości istnieje możliwość usunięcia wszystkich komentarzy przed przeniesieniem do produkcji.

Komendy debugowania
^^^^^^^^^^^^^^^^^^^
Często umieszcza się włączniki debugowania w HTML, aby umożliwić ich włączanie na dodatkowych poziomach logowania lub zgłaszania. Umieszczanie tego kodu (i logiki od strony serwera w celu interpretacji) w usługach produkcyjnych powoduje poważne zagrożenie, które zapewnia napastnikowi zwiększone przywileje dotyczące usług i podległej infrastruktury.

:Środki kontrolno-zaradcze:

    * Należy usunąć wszelkie mechanizmy debugowania przed przeniesieniem aplikacji poza środowisko deweloperskie.
    * Przed przeniesieniem do produkcji należy wykonać test tak, aby zapewnić usunięcie układu debugowania po stronie serwera.

Kody błędów
^^^^^^^^^^^
Niewłaściwa obsługa błędnego kodu umożliwia napastnikowi uzyskanie informacji niezbędnych do podjęcia ataku na aplikację sieci lub infrastrukturę wspomagającą. Mogą one zawierać:

    * przepływ aplikacji,
    * dodatkową informację serwera sieciowego,
    * typ i wersję bazy danych,
    * typ i wersję systemu operacyjnego,
    * typ i wersję skryptu / języka programowania,
    * fizyczne ścieżki,
    * pliki otwarte do odczytu i do zapisu,
    * nazwy, wartości, typy i cele zmiennych,
    * segmenty kodu źródłowego skryptu i zapytań SQL,
    * struktury baz danych i tabeli.

:Środki kontrolno-zaradcze:

    * Należy unikać raportowania użytkownikowi komunikatów o błędach w systemach produkcji. Jeżeli są one jednak nieuniknione, muszą być odpowiednio zakodowane i nie mogą ujawniać informacji napastnikowi.
    * W celu wychwytywania błędów dla wewnętrznej obsługi należy zapewnić właściwą rejestrację i logowanie.

Wyliczenie pliku / aplikacji
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Jest to powszechna technika stosowana do identyfikacji aplikacji  i plików, które mogą być podatne na wykorzystanie lub mogą stanowić podstawę ataku. Napastnicy poszukują:

* plików lub aplikacji wrażliwych,
* plików lub aplikacji ukrytych lub bez odnośników
* kopii lub plików czasowych.

:Środki kontrolno-zaradcze:

    * Należy usuwać wszystkie pliki testowe z serwera sieci.
    * Należy usuwać niechciane lub nieużywane pliki z serwerów.
    * Należy wyszukiwać i usuwać kopie zapasowe i pliki tymczasowe.
    * Należy blokować dostęp z zewnątrz do plików, które powinny pozostać na serwerze, ale użytkownik nie powinien mieć do nich dostępu.

Cache przeglądarki
^^^^^^^^^^^^^^^^^^
Informacje wrażliwe często przechowywane są w pamięci cache przeglądarki i dostępne dla każdej osoby mającej dostęp do dysku twardego urządzenia (np. w komputerach biurowych, kawiarenkach internetowych czy w bibliotekach).

:Środki kontrolno-zaradcze:

    * Aplikacje muszą przekazywać informacje wrażliwe wyłącznie zamierzonemu odbiorcy, tylko w przypadku kiedy jest to absolutnie konieczne.
    * Jeśli to możliwe należy wcześniej wygaszać strony, które mogą zawierać wrażliwy materiał.
    * Komenda "Pragma No-cache" na wszystkich stronach mogących zawierać materiał wrażliwy, informuje przeglądarki, że nie powinny przechowywać kopii stron.

Historia przeglądarki
^^^^^^^^^^^^^^^^^^^^^
Przeglądarki często zachowują historię ostatnio odwiedzonych witryn, które są podpowiadane, kiedy użytkownik zaczyna wprowadzać podobne URL. Adresy URL mogą często zawierać parametry, wykorzystane później do ujawnienia informacji, wystarczających do rozpoczęcia ataku.

:Środki kontrolno-zaradcze:

    * Dane formularzy powinny być przekazywane z użyciem HTTP POST, ponieważ nie zostają dodane do URL. Nigdy z użyciem HTTP GET.

Autouzupełnianie
^^^^^^^^^^^^^^^^
Przeglądarki internetowe obsługują funkcję Autouzupełniania. Dzięki niej dane wejściowe użytkowników mogą być zachowane dla przyszłego użycia i prezentowane użytkownikowi komputera po kliknięciu na pole formularza sieciowego z tą samą nazwą.

Jeżeli funkcja ta jest uruchomiona na komputerach wspólnych (w bibliotekach, biurach, kawiarenkach internetowych), informacja wprowadzana przez klientów do pól wejściowych (mogąca też zawierać dane osobowe czy finansowe), może być widzialna dla innych użytkowników korzystających z komputera.

:Środki kontrolno-zaradcze:

    * Należy ostrzegać klientów o istnieniu funkcji i zalecać jej wyłączenie w przypadku korzystania z urządzeń wspólnych.
    * Należy informować klientów, że funkcja zostaje włączona na wspólnie użytkowanych urządzeniach na ich własne ryzyko.
    * Należy wyłączać funkcję w polach hasła/PIN.
    * Należy wyłączać funkcję w polach kart i danych kont bankowych.
    * Istnieje również możliwość całkowitego wyłączenia funkcji.
    * Przechowywanie hasła i hasła zakodowane sprzętowo
    * Poważne zagrożenie bezpieczeństwa powodować może włamanie do bazy danych, która przechowuje hasła.

:Środki kontrolno-zaradcze:

    * Należy unikać przechowywania haseł, kodów PIN , itp. w postaci czystego tekstu, natomiast przechowywać hash hasła z użyciem jednostronnych algorytmów szyfrujących z użyciem pseudolosowej soli.
    * Aby uniemożliwić przeglądarkom zapisywanie haseł, kodów PIN itp należy stosować formularze uwierzytelnienia (GAS)
    * Jeżeli hasła bądź PINy muszą być przechowywane, w postaci umożliwiającej odtworzenie, należy zapewnić ich szyfrowanie przy użyciu silnych algorytmów szyfrujących, oraz zagwarantować bezpieczeństwo klucza szyfrującego.
    * Edukacja użytkownika
    * Nie każdy użytkownik komputera i Internetu jest ekspertem od bezpieczeństwa komputerów, w związku z tym wielu z nich nie rozumie, dlaczego bezpieczeństwo jest tak istotne.

:Środki kontrolno-zaradcze:

    * Należy udzielać przemyślanych porad zatwierdzonych przez wydzielone komórki firmy oraz wykorzystywać aktualne informacje dostępne na stronach internetowych firmy.

Ukryte pola
^^^^^^^^^^^
Ukryte pola mogą być przydatne, jednak mogą też stanowić znaczące ryzyko dla aplikacji, jeżeli zostaną niewłaściwie wykorzystane do przechowywania wrażliwych informacji. Mogą być łatwo przejrzane, zmodyfikowane i odesłane przez napastnika.

:Środki kontrolno-zaradcze:

    * Wartości, które mogą zostać użyte przez napastnika do uzyskania nieoczekiwanej odpowiedzi (względnie do otrzymania danych innej osoby albo wygenerowania warunku błędu mogącego stanowić podstawę do ataku) powinny być zawsze kodowane albo haszowane.
    * Należy unikać przechowywania identyfikatorów sesji w tych polach.
    * Nigdy nie należy przechowywać haseł ani PINów w ukrytych polach.
    * Wszelkie dane osobowe (zdefiniowane w ustawie o ochronie danych osobowych) i informacje finansowe powinny być kodowane i przesyłane w szyfrowanej sesji SSL.
    * Pola te powinny być zawsze rygorystycznie sprawdzane, po stronie serwera.
    * Nigdy nie należy używać ukrytych pól do komend kontrolnych serwera sieci.

Historia konta
^^^^^^^^^^^^^^
Użytkownicy aplikacji nie mogą sprawdzać, czy nieupoważnione osoby uzyskały dostęp do ich konta lub czy posługiwały się nim w sposób niewłaściwy.

:Środki kontrolno-zaradcze:

    * Należy stosować wyświetlanie czasu ostatniego logowania, daty i adresu IP źródła po prawidłowym uwierzytelnieniu.
    * Należy stworzyć szczegółową sekcję historii konta dla uwierzytelnionych użytkowników, obejmującą:
    * odnotowany czas i datę,
    * modyfikacje konta np. zmiana hasła,
    * transakcje finansowe, itp.

Zgłaszanie incydentu
^^^^^^^^^^^^^^^^^^^^
W przypadku pojawienia się podejrzanych zmian na koncie lub stronie użytkownika, musi on wiedzieć w jaki sposób zgłosić incydent firmie. Brak przejrzystej i prostej instrukcji niesie ryzyko nie zgłoszenia problemów.

:Środki kontrolno-zaradcze:

    * Dostawcy powinni zachęcać użytkowników do zgłaszania incydentów oraz informować o sposobach kontaktu.
    * Incydent powinien zostać zgłoszony do przełożonego liniowego, a ten powinien zgłosić go zgodnie ze ścieżką formalną do kierownika projektu lub/i stosownego dyrektora.

Informacje wrażliwe i kod źródłowy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Kod źródłowy od strony klienta jest łatwo zauważalny dla użytkowników. Wprowadzanie wrażliwych informacji zakodowanych sprzętowo do kodu źródłowego, może udostępnić napastnikowi informacje, które może on wykorzystać do przeprowadzenia ataku lub popełnienia oszustwa.

:Środki kontrolno-zaradcze:

    * Nie należy kodować sprzętowo po stronie klienta informacji wrażliwych (identyfikatorów, haseł itp.).

Informacje wrażliwe i pliki cookie
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Pliki cookie mogą być przeglądane i modyfikowane. Jeżeli zawierają informacje wrażliwe, mogą być wykorzystane do przeprowadzenia ataku lub popełnienia oszustwa.

:Środki kontrolno-zaradcze:

    * Nie należy przechowywać danych osobowych ani informacji finansowych w plikach cookie.
    * Nie należy przechowywać szczegółów uwierzytelnienia w plikach cookie.
    * Jeżeli identyfikator sesji jest przechowywany w plikach cookie - należy zapewnić jego haszowanie.
    * Zawartość plików cookie należy zabezpieczać przy pomocy bezpiecznych algorytmów szyfrujących.
    * Aby zapobiec wysyłaniu przez przeglądarkę plików cookie przez nieszyfrowane połączenie - należy przeanalizować użycie etykiety bezpieczeństwa.

Kryptografia
^^^^^^^^^^^^
Kryptografia służy do zapewnienia:

    * poufności (dane są rozumiane wyłącznie przez upoważnione osoby)
    * integralności (dane nie są zmienione w trakcie przesyłania)
    * uwierzytelniania (dane pochodzą od określonej osoby)

Należy jednak pamiętać, że nie jest ona ostatecznym rozwiązaniem dla ochrony danych, a skomplikowaną funkcją kontrolną. Do listy problemów należy m.in:

    * pozorne poczucie bezpieczeństwa,
    * własne, niesprawdzone procedury kodowania,
    * wykorzystanie niewiarygodnych i niepotwierdzonych procedur kodowania,
    * odzyskanie systemu / danych,
    * zarządzanie kluczami i ich odzyskiwanie,
    * typ / moc algorytmu,
    * długości kluczy,
    * generowanie liczb kluczowych / losowych.

:Środki kontrolno-zaradcze:

    Wdrażając kodowanie należy:

        * zapoznać się z wymaganiami firmy i bezpieczeństwa,
        * ściśle współpracować z technicznymi zespołami informatyki i bezpieczeństwa,
        * nie próbować samodzielnie opracowywać procedur kodowania,
        * nie wykorzystywać niezatwierdzonych lub niewiarygodnych procedur kodowania, tylko tych zaakceptowanych i zatwierdzonych,
        * dokumentować rozwiązania,
        * dokładnie testować rozwiązania (kodowanie, dekodowanie, odzyskiwanie),
        * zapewnić gruntowne sprawdzenie systemu zarządzania kluczami (manualnego lub informatycznego) oraz odpowiednie przeszkolenie personelu obsługi. Funkcjonować musi możliwość odzyskania zaszyfrowanych danych w celach dochodzeniowych,
        * stosować odpowiednie długości kluczy.

Kontrola dostępu
----------------
Podstawową kwestią ochrony systemów centralnych i końcowych oraz danych jest wprowadzenie odpowiedniej kontroli dostępu, którą należy stosować w celu:

    * Ograniczenia możliwości działania użytkowników,
    * Ograniczenia dostępu użytkowników do zasobów,
    * Definicji funkcji, które użytkownicy mogą stosować do danych.

Mechanizmy kontroli dostępu powinny uniemożliwiać nieuprawnionym: przeglądania, modyfikowania i kopiowania danych. Dodatkowo, mogą powstrzymać przed zastosowaniem złośliwego kodu lub nieuprawnionych działań przez napastnika, wykorzystującego zależności infrastruktury.

Dostęp do informacji w systemach oraz dokumentacji a informacja publiczna
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Udostępnieniu danych na podstawie "Ustawy o dostępie do informacji publicznym" nie podlegają informacje oraz kod źródłowy aplikacji zgromadzony w Bazie Wiedzy, Systemie Zgłoszeń, Repozytorium Kodu Źródłowego i w dokumentacji!

Wyżej wymienione repozytoria są objęte tzw. klauzulą informacji zastrzeżonej przedsiębiorstwa i nie powinny być udostępniane dla osób powołujących się na tą ustawę. W przypadku wstąpienia roszczącego na drogę sądową informacje te nie powinny zostać udostępnione bez prawomocnego wyroku sądu.

Użytkowanie sprzętu prywatnego
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Aby zapewnić bezpieczeństwo środowiska pracy w organizacji regulamin polityki bezpieczeństwa Firmy zabrania używania urządzeń prywatnych do wykorzystania w celu służbowym w Firmie.

Odstępstwo od tej reguły może mieć miejsce tylko i wyłącznie za zgodą kierownika, architekta lub stosownego zastępcy Dyrektora i musi być dobrze umotywowane. W powyższych i uzasadnionych przypadkach muszą zostać spełnione obowiązujące w Firmie standardy bezpieczeństwa, w stopniu nie niższym niż te, dotyczące pracy na służbowych komputerach.

Na szczególną uwagę należy zwrócić aby:

* dysk musi być szyfrowany bezpiecznie,
* firewall musi być skonfigurowany,
* praca na użytkowniku musi się odbywać na użytkowniku pozbawionym praw administratora,
* system musi być bezpieczny, aktualny, wspierany przez producenta,
* w systemie nie ma malware'u (oprogramowanie antywirusowe w systemie Windows, chrootkit/debsums w Linux/\*nix),
* nie przechowywanie danych/kopii zapasowych na zdalnych chmurach.

Klasyfikacja danych i autoryzacja dostępu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dane mogą zostać niewłaściwie skontrolowane, a w efekcie bezprawnie ujawnione, w sytuacji, kiedy nie użyjemy klasyfikacji albo w przypadku, kiedy będzie ona niewłaściwa.

Bez efektywnej procedury uwierzytelniania i autoryzacji dostęp do danych lub systemu może zostać nieodpowiednio przyznany bez wiedzy właściciela systemu lub danych.

:Środki kontrolno-zaradcze:

    * Wszystkie dane używane przez aplikacje muszą być sklasyfikowane zgodnie z zasadami stosowanymi przez grupę.
    * Procedura autoryzacji musi być wprowadzona, regularnie przeglądana i udokumentowana.

Nieoczekiwany dostęp do zasobów
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Napastnicy nie zawsze używają aplikacji w sposób zgodny ze sposobem ich funkcjonowania. Aby uzyskać dostęp do procedur, zasobów czy danych (zazwyczaj zamaskowanych przez układ logiczny aplikacji), próbują obejść wprowadzone zabezpieczenia aplikacji.

:Środki kontrolno-zaradcze:

    * Należy zidentyfikować i udokumentować role i uprawnienia dostępu.
    * Należy stosować zasadę najniższych możliwych uprawnień.
    * Każdy chroniony zasób, przed udzieleniem dostępu, musi uwierzytelniać sesję użytkownika. Kiedy użytkownik składa zapytanie przez aplikację, oprócz odpowiedniej kontroli danych wejściowych, procedura powinna sprawdzać czy konto użytkownika ma uprawnienia do wykonania operacji zarówno w aplikacji, jak i bazie danych.

Ukryte zagrożenia lub dane wykorzystane w niewłaściwym celu na skutek nieodpowiedniej kontroli dostępu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Działania ochronne kluczowych zasobów, procedur lub danych bazujących na prostych technikach, np. przyjęciu konwencji nazywania plików czy ukrywanie plików i folderów, nie stanowią przeszkody dla napastników przed uzyskaniem do nich dostępu, o ile nie istnieje dodatkowa autoryzacja i kontrola. Większość profesjonalnych napastników korzysta z technik, które ujawniają takie zasoby.

:Środki kontrolno-zaradcze:

    * Zawsze należy stosować odpowiednią kontrolę procedur, zasobów i danych oraz zadbać o stosowny poziom zabezpieczeń organizacyjnych.

Dostęp do kodu źródłowego
^^^^^^^^^^^^^^^^^^^^^^^^^
Ograniczenie dostępu do kodu źródłowego aplikacji rozwijanych w ramach Firmy ma na celu:

    * poprawę bezpieczeństwa,
    * zapewnienie braku możliwości wprowadzenia nieautoryzowanych zmian w kodzie źródłowym,
    * kontrolę autoryzowanych zmian,
    * możliwość śledzenia zmian w danych modułach i plikach.

:Środki kontrolno-zaradcze:

    * Centralne repozytorium kodu źródłowego znajduje się na serwerze do którego dostęp jest kontrolowany. Zarówno część systemowa jak i aplikacyjna serwera repozytorium jest chroniona hasłem lub/i kluczem a uprawnienia są nadawane na podstawie przynależności do odpowiedniej grupy w katalogu użytkowników.

Serwer powinien pozwalać na nadanie uprawnień na minimum trzech poziomach:

    * read-only - tylko do odczytu,
    * read-write - odczyt i zapis,
    * administrator - osoba nadająca uprawnienia, oraz kontrolująca proces.

Serwer powinien zapewniać separację pomiędzy projektami oraz repozytoriami i gałęziami  (ang. branch)  rozwojowymi w repozytoriach na podobnych zasadach jak powyżej.

Poszczególne projekty powinny odzwierciedlać strukturę projektową i być niedostępne dla osób nieprzydzielonych do danego projektu.

Dostęp fizyczny do kodu źródłowego
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Aby zabezpieczyć się przed nieautoryzowanym dostępem fizycznym do kodu źródłowego Firma podjęła decyzję o wprowadzeniu procedur bezpieczeństwa oraz wprowadzenia sposobów ich egzekucji specjalnym rozporządzeniem dyrektora.

Do najczęstszych naruszeń bezpieczeństwa w zakresie fizycznego dostępu należą:

    * publikacja w serwisach umożliwiających hostowanie kodu źródłowego tj. Github czy Bitbucket (nie dotyczy kodu objętego możliwością publikowania na Open Source - patrz odpowiedni załącznik),

    * publikacja fragmentów kodu źródłowego w serwisach do wymiany snippetów np. Pastebin, Github,
    * serwisy wymiany porad dotyczące kodu i problemów informatycznych tj. fora internetowe, Stackoverflow,
    * publiczne komunikatory, których serwery należą do firm trzecich, tj. Google Hangouts, Facebook Messenger, HipChat (nie dotyczy usługi hostowanej na serwerach Firmy),
    * wysyłanie fragmentów kodu źródłowego za pomocą poczty elektronicznej,
    * kopiowanie plików, całego repozytorium lub dokumentów na dyskach przenośnych,
    * fizyczne wynoszenie komputerów poza budynek firmy,
    * przetrzymywanie danych na nieszyfrowanym nośniku, bez względu na fakt czy jest zamontowany na stałe czy wymienny,
    * pozostawianie komputera na Open Space, lub w pomieszczeniach do których dostęp nie wymaga konieczności użycia karty dostępowej,
    * pozostawienie komputera bez zablokowania go hasłem,
    * automatyczna kopia zapasowa komputerów i składowanie danych na nieszyfrowanych dyskach.

:Środki kontrolno-zaradcze:

    Unikanie powyższych zagrożeń.
    Natychmiastowe zgłaszanie incydentów w wypadku zauważenia naruszenia, poprzez:

        * osobiste, telefoniczne lub elektroniczne poinformowanie przełożonego liniowego o zaistniałym incydencie,
        * zgłoszenie Incydentu w systemie ITSM Firmy,
        * osobiście, telefonicznie lub elektronicznie poinformować o wystąpieniu incydentu odpowiedni zespół ds. bezpieczeństwa fizycznego / sieciowego.
        * Egzekucja kary adekwatnej do naruszenia.

        W przypadku konieczności zobrazowania problemu i poparcia go stosownym fragmentem dopuszcza się możliwość wklejenia zanonimizowanego fragmentu kodu:

        * należy dołożyć wszelkich starań aby nie można było odczytać kontekstu kodu,
        * należy dołożyć wszelkich starań aby kod był w miarę najkrótszy, tj. obrazował tylko i wyłącznie problematyczną linijkę / linijki, a nie większy zakres.
        * kod przeznaczony do udostępnienia i który spełnia powyższe kryteria powinien być skonsultowany z kierownikiem projektu lub/i architektem.
        * Przez Internet przekazuję ZASZYFROWANE informacje - nie odszyfrowane.
        * Pracownicy Firmy powinni być świadomi, że użytkowanie tego zasobu jest monitorowane w celu ustalenia nieprawidłowych działań przy wykorzystaniu zasobów sieci.

Rejestracja zdarzenia
^^^^^^^^^^^^^^^^^^^^^
Rejestracja służy do zapisu zdarzeń podejmowanych przez użytkownika lub system, które później mogą zostać przejrzane oraz przeanalizowane. Rejestracją zdarzenia można posłużyć się do analizy problemu systemowego lub zagrożenia bezpieczeństwa. Rejestracja może:

* sygnalizować podejrzaną działalność,
* wykazać odpowiedzialność użytkownika poprzez śledzenie jego działań,
* dać możliwość rekonstrukcji zdarzeń po nieprawidłowym wykorzystaniu danych lub po wystąpieniu problemu,
* stanowić pomoc w postępowaniu sądowym.

Brak możliwości wykrycia i oceny skutków zagrożenia systemu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Brak należytych mechanizmów rejestracji zdarzenia w aplikacjach może powodować zmniejszenie możliwości weryfikacji obecności nieuprawnionej działalności i określania jej skutków dla systemów lub interesów firmy.

:Środki kontrolno-zaradcze:

    * Podczas tworzenia procedur rejestracji zdarzeń należy uwzględnić takie kwestie jak:
    * pliki rejestru muszą być sklasyfikowane według Polityki Bezpieczeństwa Systemów Teleinformatycznych,
    * próby uwierzytelnienia np. (wy)logowanie, nieudane logowanie,
    * próby autoryzacji, w tym czas, sukces/porażka, autoryzowany zasób lub funkcja, do których użytkownik żądający autoryzacji chciał uzyskać dostęp,
    * funkcje administracyjne, takie jak: przeglądanie danych użytkownika,  zarządzanie kontami, aktywacja lub deaktywacja rejestracji zdarzenia, itp.,
    * rejestracja informacji debugowych nie może prowadzić do zapisania wrażliwych danych prywatnego konta użytkownika w rejestrze zdarzeń (np. haseł, czy kodów PIN),
    * rejestry nie mogą usuwać istniejących zapisów bez ich skopiowania lub zarchiwizowania. Archiwa i kopie zapisów muszą być chronione i przechowane zgodnie z ich klasyfikacjami i celami,
    * zawartości rejestrów mogą być ujawniane w uzasadnionych przypadkach tylko osobom mającym odpowiednią autoryzację właściciela systemu lub danych, którego system lub baza jest monitorowana,
    * indywidualni użytkownicy nie mogą aktualizować ani usuwać pozycji w rejestrach zdarzeń. Pliki rejestru mogą być uaktualnione tylko przez serwis rejestracji zdarzenia,
    * komunikaty sieciowe.

W sytuacji kiedy ocena ryzyka wskazuje na potrzebę jednoznacznego potwierdzenia działań wykonanych przez podmiot lub osobę, przeznaczone dla nich mechanizmy i rejestry muszą spełniać normy, które mają niepodważalną moc dowodową przed sądem.


