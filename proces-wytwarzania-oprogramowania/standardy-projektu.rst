********************************
Technologie i standardy projektu
********************************

W ramach prowadzenia swojej działalności należy wybrać standardy technologii prowadzenia projektów. Wybór ten ma na celu uporządkowanie i zmniejszenie liczby wykorzystywanych technologii. Dzięki czemu wsparcie narzędziowe oraz operacyjne może zostać zapewnione w najlepszy możliwy sposób. Dla każdego projektu wybierane są stosowne technologie zapewniające jak najlepsze zrealizowanie założeń biznesowych. Wykaz technologii znajduje się w załączniku do dokumentu.

Firma jest organizacją dbającą o jakość wytworzonych rozwiązań. Dla poprawy kodu aplikacji stworzonych w ramach działań operacyjnych Firmy zdecydowano się na wprowadzenie nowoczesnych rozwiązań, w ramach czego wprowadzone i kultywowane zostały standardy wytwarzania oprogramowania, tj.:

* wykorzystanie systemu kontroli wersji,
* wdrożenie systemów i metodyk zwinnych w zarządzaniu projektami i oprogramowaniem,
* automatyzacja procesu budowania projektu,
* automatyczne zarządzanie zależnościami projektu,
* automatyzacja procesu testowego, zarówno części warstwy logiki biznesowej jak i graficznego interfejsu użytkownika,
* wprowadzenie warstwowej architektury rozwiązania,
* zastosowanie języków oprogramowania oraz technologii powszechnie stosowanych na świecie.

Języki programowania
====================

Dostrzegając, iż na świecie Java de facto stała się standardem podjęliśmy decyzję aby projekty informatyczne były wytwarzane są w tym języku. Firma wytwarza oprogramowanie wykorzystując Javę po stronie serwerowej oraz w język Java Script po stronie klienta. Do pomniejszych zadań, skryptów lub narzędzi wykorzystywane są języki tj. Python, Ruby, Shell Script.

Dopuszcza się zwiększenie procentu wykorzystania innych języków lub zastosowanie technologii niewymienionych w powyższym zestawieniu jeżeli tylko jest to uzasadniona biznesowo lub informatycznie zmiana. W takim przypadku ma zastosowanie procedura wprowadzania nowych technologii w projektach.

Dokładną listę technologii precyzuje stosowny załącznik do dokumentu.

Procedury wprowadzania nowych technologii w projektach
======================================================

W przypadku zapotrzebowania na zmianę technologii, architektury lub podziału aplikacji zgodnie z innym schematem przewidziana jest następująca procedura:

1. Wniosek zgłaszany jest do przełożonego liniowego lub lidera zespołu,
2. Lider lub przełożony wydaje opinię czy zmiana jest uzasadniona i czy należy ją rozważyć na szczeblu projektowym
3. Jeżeli zmiana jest uzasadniona lider przedstawia ją na cyklicznym spotkaniu projektowym pozostałym liderom lub kierownikom.
4. Jeżeli zmiana zostanie określona jako istotnie i pozytywnie wpływająca na jakość, szybkość wytwarzania lub działania aplikacji, ewentualnie znacząco przyczyni się do zwiększenia wartości biznesowych dopuszcza się możliwość jej wprowadzenia po uprzednim skonsultowaniu się z architektami aplikacji oraz poinformowaniu kierownika projektu i stosownego dyrektora działu. Stosowna zmiana wraz z uzasadnieniem powinna również znaleźć się w dokumentacji technicznej projektu.

System kontroli wersji
======================

Firma jako standard systemu kontroli wersji wybrała rozwiązanie GIT. Aplikacja ta jest narzędziem pozwalającym na śledzenie zmian oraz ich autorów. GIT został wybrany, jako że na chwilę obecną jest najpopularniejszym oprogramowaniem tego typu na rynku i ma największe wsparcie wśród narzędzi deweloperskich. Ponadto w sieci Internet zgromadzone są duże zasoby wiedzy dotyczącej korzystania z tego oprogramowania, a społeczność chętnie pomaga rozwiązywać najczęściej spotykane problemy.

Zastosowanie GITa w projekcie wiąże się z przestrzeganiem odpowiednich konwencji nazewniczych oraz procesu wprowadzania funkcjonalności w aplikacji. Informacje te są zamieszczone w oddzielnym paragrafie “Konwencja nazewnicza w systemie kontroli wersji”.

Zarządzanie projektem oraz zadaniami
====================================

W Firmie oprogramowanie jest wytwarzane w duchu metodyk zwinnych (Agile). Główny nacisk jest położony na współpracę z klientem oraz jak najczęstsze udostępnianie aplikacji do testów. Dzięki takiemu rozwiązaniu ilość błędów jest mniejsza a klient jest w stanie swoje uwagi zgłosić na wczesnym etapie rozwoju systemu dzięki czemu koszt ich wprowadzenia jest mniejszy. Metodyki zarządzania projektami i zespołami są przedstawione w osobnym rozdziale.

Do systemów wspierających wytwarzanie oprogramowania w metodykach Scrum i Kanban wybraliśmy system Jira wraz z dodatkiem Jira Agile. W tym oprogramowaniu znajdują się tzw. rejestry produktów (backlogi) precyzyjnie opisujące zasady i kolejność tworzenia funkcjonalności i poprawek w systemie.

Budowanie projektu i zarządzanie zależnościami
==============================================

Do automatyzacji budowania projektu oraz zarządzania jego zależnościami zostały wybrane rozwiązania Maven i Gradle.

Dla aplikacji zbudowanych przy użyciu innego języka programowania niż Java przewiduje się użycie odmiennych, specyficznych dla danej technologii rozwiązań.

Warstwowa architektura rozwiązań
================================

Wśród aplikacji wytwarzanych w ramach projektów można wyróżnić co najmniej trzy główne warstwy, w ramach których zastosowanie mają różne technologie:

* warstwa widoku (frontendu),
* warstwa logiki biznesowej (backendu),
* warstwa persystencji (bazy danych).

Podział ten przyjął się jako standard na świecie. Dzięki wykorzystaniu takiego rozróżnienia Firma jest w stanie skutecznie tworzyć niezależne od siebie elementy aplikacji, które później stanowią całość oprogramowania.
