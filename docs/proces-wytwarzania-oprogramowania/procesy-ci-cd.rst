*****************************************
Procesy Continuous Integration i Delivery
*****************************************

Proces ciągłej integracji polega na automatycznym uruchamianiu testów aplikacji tj. testów jednostkowych, testów integracyjnych, testów regresyjnych i funkcjonalnych dla każdej wprowadzonej zmiany. Dzięki zastosowaniu Continuous Integration (CI) programiści otrzymują̨ natychmiastową informację czy ich zmiany w kodzie nie destabilizują pracy systemu oraz negatywnie wpływają na całą aplikację.

W zależności od kategorii definiuje się inny zestaw testów uruchamianych dla budowania i sprawdzania aplikacji.

Proces ciągłego dostarczania polega na doprowadzeniu procedury wdrożenia oraz budowania aplikacji do poziomu pozwalającego na otrzymywanie gotowych do wdrożenia paczek po każdej integracji nowej funkcjonalności. Continuous Delivery (CD) jest rozwinięciem procesu CI o przygotowanie przetestowanej paczki wdrożeniowej. Każda paczka musi być gotowa do wdrożenia na środowisko produkcyjne w dowolnym momencie.

Continous Delivery jest sposobem dostarczania oprogramowania służącym zautomatyzowaniu i polepszeniu tego procesu.

Automatyczne testowanie, ciągłe scalanie i wdrażanie oprogramowania pozwalają̨ przygotować je w przejrzystej formie, aby mogły zostać poddane dalszym testom. To pozwala szybko, niezawodnie i wielokrotnie ulepszać produkt i naprawiać pojawiające się na różnych etapach produkcji błędy, uwzględniając opinie użytkowników, zmiany na rynku oraz zmiany w strategii biznesowej. Należy podkreślić, że zachowane jest przy tym minimalne ryzyko poważnej usterki oraz konieczność minimalnej poprawy instrukcji użytkowania.

Poszczególne mniejsze fragmenty wytwarzanego oprogramowania muszą przejść określone etapy walidacji na swojej drodze do publikacji. Kod jest kompilowany i pakowany za każdym razem, gdy dokonywana jest zmiana w systemie kontroli wersji. Następnie jest wielokrotnie testowany. Dopiero po tym może zostać wdrożony.

Wykorzystywanie metody Continuous Delivery w pracy Firmie jest skutkiem nastawienia na konkretne i dobre efekty. Dzięki niej oszczędza się także czas i pieniądze, które wykorzystuje się na dalszy, coraz bardziej zaawansowany rozwój.

Do procesu zarówno Continous Integration jak i Continous Delivery w Firmie wykorzystywany jest system Jenkins. Oprogramowanie to pozwala na automatyzację kroków procesu znacząco obniżając czas i koszt tworzenia kolejnych przyrostów. W kolejnych krokach działania tego narzędzia jest pobranie kodu źródłowego, jego kompilacja, poddanie go testom jednostkowym i funkcjonalnym a na samym końcu analiza statyczna kodu źródłowego i zbudowanie artefaktu gotowego do wdrożenia na środowisko testowe lub/i produkcyjne.

Continuous Integration
======================

Proces ciągłej integracji polega na automatycznym uruchamianiu testów aplikacji tj. testów jednostkowcyh, testów integracyjnych, testów regresyjnych i funkcjonalnych dla każdej wprowadzonej zmiany. Dzięki zastosowaniu Continuous Integration (CI) programiści otrzymują natychmiastową informację czy ich zmiany w kodzie nie destabilizują pracy systemu oraz negatywnie wpływają na całą aplikację.

Proces CI w ramach Firmy jest realizowany za pomocą systemu do automatycznego budowania - Jenkins. System ten periodycznie odpytuje repozytorium o zmiany w repozytorium i w przypadku wykrycia takowych uruchamia z góry zdefiniowane akcje, tj. wymienione powyżej.

Plany w Jenkinsie dzielą się na różne kategorie:

* budowanie gałęzi stabilnej (master),
* budowanie gałęzi rozwojowej (develop),
* budowanie Pull Requestów,
* budowanie zmian w gałęziach z nowymi funkcjonalnościami (feature),
* budowanie zmian w gałęziach z poprawkami błędów (bugfix),
* plan wdrożeniowy.

W zależności od kategorii definiuje się inny zestaw testów uruchamianych dla budowania i sprawdzania aplikacji. Powyższy podział ma na celu umożliwienie uzyskania natychmiastowych i szybkich informacji po wprowadzeniu zmian (feature, bugfix). Dla Pull Requestów uruchamiane są testy integracyjne informujące czy wprowadzone zmiany nie destabilizują działania aplikacji. Natomiast dla zmian w gałęzi rozwojowej (zmiany po wprowadzeniu funkcjonalności) oraz gałęzi stabilnej (wdrożenia) uruchamiana jest dogłębna i długotrwała statyczna analiza kodu wraz z odpowiednim procesem.

Continuous Delivery
===================

Proces ciągłego dostarczania polega na doprowadzeniu procedury wdrożenia oraz budowania aplikacji do poziomu pozwalającego na otrzymywaniu gotowych do wdrożenia paczek po każdej integracji nowej funkcjonalności. Continuous Delivery (CD) jest rozwinięciem procesu CI o przygotowanie przetestowanej paczki wdrożeniowej. Każda paczka musi być gotowa do wdrożenia na środowisko produkcyjne w dowolnym momencie.

Proces Continuous Delivery w Firmie jest realizowany za pomocą systemu automatyzacji budowania - Jenkins. System ten po przetestowaniu zmian w repozytorium generuje binarny artefakt, tj. skompilowaną paczkę kodu gotową do wdrożenia na środowisko produkcyjne i umieszcza ją w systemie Artifactory uprzednio nazywając ją odpowiednio stosownie do zbudowanych zmian.

Continous Delivery jest sposobem dostarczania oprogramowania służącym zautomatyzowaniu i polepszeniu tego procesu.

Automatyczne testowanie, ciągłe scalanie i ciągłe wdrażanie oprogramowania pozwalają przygotować je w przejrzystej formie, aby mogły zostać poddane dalszym testom. To pozwala szybko, niezawodnie i wielokrotnie ulepszać produkt i naprawiać pojawiające się na różnych etapach produkcji błędy, uwzględniając opinie użytkowników, zmiany na rynku oraz zmiany w strategii biznesowej. Należy podkreślić, że zachowane jest przy tym minimalne ryzyko poważnej usterki oraz konieczność minimalnej poprawy instrukcji użytkowania.

Poszczególne mniejsze fragmenty wytwarzanego oprogramowania muszą przejść określone etapy walidacji na swojej drodze do publikacji. Kod jest kompilowany i pakowany za każdym razem, gdy dokonywana jest zmiana w systemie kontroli wersji. Następnie jest wielokrotnie testowany. Dopiero po tym może zostać wdrożony.

.. figure:: ../../_static/img/cicd-loop.png

    Koncepcja metody Continuous Delivery. Poszczególne kroki procesu zapętlają się tworząc niekończącą się pętlę.

Wykorzystywanie metody Continuous Delivery w pracy Firmy jest skutkiem nastawienia na konkretne i dobre efekty. Dzięki niej Firma również oszczędza czas i pieniądze, które wykorzystuje na dalszy, coraz bardziej zaawansowany rozwój.

Continuous Deployment
=====================

Proces produkcji oprogramowania charakteryzujący się wdrażaniem zmian na środowisko produkcyjne po każdej wprowadzonej poprawce lub nowej funkcjonalności. Proces ten charakteryzuje dojrzałe oprogramowanie oraz 100% zaufanie testom automatycznym. Continuous Deployment jest rozwinięciem ideii Continuous Delivery.
