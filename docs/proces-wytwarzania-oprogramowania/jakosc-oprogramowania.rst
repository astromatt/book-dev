*********************
Jakość oprogramowania
*********************

Testowanie oprogramowania w Firmie odbywa się nie tylko w sposób manualny. Ważnym procesem jest testowanie zautomatyzowane. Polega to na tym, że programista lub/i tester przygotowuje odpowiednie narzędzia testowe, które w sposób jak najbardziej autonomiczny wykonują zadany scenariusz i oceniają jego rezultaty.

Zaletami testowania automatycznego są m.in.:

* Możliwość szybkiej i wydajnej weryfikacji poprawek błędów,
* Możliwość odtworzenia testu, co jest bardzo przydatne zwłaszcza przy sprawdzaniu, czy wskazywane błędy zostały usunięte,
* Możliwość kompleksowej analizy wyników testów,
* Szybsze i tańsze tworzenie sprawozdań,
* Nieomylność przy wprowadzaniu danych,
* Możliwość podania dużej liczby danych testowych,
* Szybsze wprowadzanie testów,
* Umożliwienie systematyczności,
* Oszczędzenie czasu testerów,
* Unikniecie błędów związanych z czynnikiem ludzkim.

Firma stosuje testy jednostkowe dla poszczególnych jednostek oprogramowania, lekkie testy integracyjne, służące wykryciu błędów w interakcjach pomiędzy modułami, oraz testy interfejsu, służące wykryciu błędów w interfejsach użytkownika.

W procesie testowania pomocne są Firmie również narzędzia pozwalające budować, gromadzić i umieszczać na serwerze archiwa, a także zapewniające przykładowe dane dla testów do łatwego wykorzystania i ponownego użycia.

Testy automatyczne są zatem świetnym uzupełnieniem testów manualnych, a ogólny zestaw testów znacząco wpływa na poprawę wydajności wytwarzanych produktów. W trakcie przeprowadzania testów następuje wdrożenie demonstracyjne prototypu projektu powstałego w danym Sprincie.

Firma w ramach przygotowania Projektu, określiła, że jednym z kluczowych elementów poprawnego działania aplikacji jest jego wydajność.

Decyzja taka wynikła z faktu docelowego wykorzystywania systemu Projektu do codziennej równoległej pracy znacznej liczby użytkowników.

W ramach sprawdzenia testów wydajnościowych systemu Projektu przygotowano scenariusze testów wydajnościowych i obciążeniowych.

Na ich podstawie wykonywane są testy mierzące wydajność aplikacji.

Aby utrzymać wysoki standard jakości oprogramowania został wdrożony system SonarQube. Oprogramowanie to pozwala na wyświetlanie wyników statycznej analizy kodu źródłowego w prostej i przejrzystej formie. Dzięki jego wykorzystaniu deweloperzy mają możliwość zobaczenia najczęściej popełnianych błędów oraz ich rozwiązania.

Kolejnym elementem, który znacząco przyczynia się do wysokiej jakości wytwarzanych rozwiązań jest tzw. system Pull Requestów, tj. oprogramowanie do przeglądu kodu (ang. `Code Review`). Zarówno do przetrzymywania repozytoriów kodu źródłowego jak i obsługi procesu Pull Request wykorzystywane jest narzędzie Stash. Aplikacja ta pozwala w prosty i intuicyjny wprowadzać komentarze do kodu źródłowego co wspiera komunikację programistów. Wg. obecnych ustawień każda zmiana w kodzie źródłowym wymaga akceptacji przynajmniej dwóch innych programistów oraz pozytywnego wyniku budowania i testów w systemie Continuous Integration. 

Testowanie automatyczne
=======================

Testowanie oprogramowania w Firmie odbywa się nie tylko w sposób manualny. Ważnym procesem jest testowanie zautomatyzowane. Polega to na tym, że programista lub/i tester przygotowuje odpowiednie narzędzia testowe, które w sposób jak najbardziej autonomiczny wykonują zadany scenariusz i oceniają jego rezultaty.

Zaletami testowania automatycznego są m.in.:

* Możliwość szybkiej i wydajnej weryfikacji poprawek błędów,
* Możliwość odtworzenia testu, co jest bardzo przydatne zwłaszcza przy sprawdzaniu, czy wskazywane błędy zostały usunięte,
* Możliwość kompleksowej analizy wyników testów,
* Szybsze i tańsze tworzenie sprawozdań,
* Nieomylność przy wprowadzaniu danych,
* Możliwość podania dużej liczby danych testowych,
* Szybsze wprowadzanie testów,
* Umożliwienie systematyczności,
* Oszczędzenie czasu testerów,
* Uniknięcie błędów związanych z czynnikiem ludzkim.

Firma stosuje testy jednostkowe dla poszczególnych jednostek oprogramowania, lekkie testy integracyjne, służące wykryciu błędów w interakcjach pomiędzy modułami, oraz testy interfejsu, służące wykryciu błędów w interfejsach użytkownika.

Przykładem zastosowanych w Firmie testów integracyjnych są testy osadzone na kontenerze `Java EE`, wykonywane na innowacyjnych, rozszerzalnych platformach testowania, co umożliwia programistom łatwe tworzenie automatycznej integracji oraz testów funkcjonalnych dla middleware'u `Javy`.

W procesie testowania pomocne są Firmie również narzędzia pozwalające budować, gromadzić i umieszczać na serwerze archiwa, a także zapewniające przykładowe dane dla testów do łatwego wykorzystania i ponownego użycia. Ponadto, testy są w pełni zintegrowane z `IDE` (zintegrowanym środowiskiem programistycznym). Dzięki tym wszystkim rozwiązaniom testowanie jest proste, szybkie i wydajne.

Testy automatyczne są zatem świetnym uzupełnieniem testów manualnych, a ogólny zestaw testów znacząco wpływa na poprawę wydajności produktów wytwarzanych przez Firmę.

W trakcie przeprowadzania testów następuje wdrożenie demonstracyjne prototypu projektu powstałego w danym Sprincie.

System zapewnienia jakości kodu
===============================

Firma w ramach systemu zapewnienia jakości kodu, używa narzędzi umożliwiających regularne stosowanie cross-checków oraz `code review`. Wykorzystywany jest także system kontroli wersji służący do śledzenia zmian w kodzie źródłowym.
