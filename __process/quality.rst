*******************
Zapewnienie jakości
*******************

W ramach projektu stworzono dokument opisujący standardy technologiczne rozwiązania. Uzyskano dzięki temu uporządkowanie i ograniczenie liczby wykorzystywanych narzędzi oraz szkieletów tworzenia aplikacji. Spowodowało to możliwość zapewnienia lepszego wsparcia narzędziowego i operacyjnego. Pozwala to również na łatwiejsze zrealizowanie założeń biznesowych.

W poniższym rozdziale przedstawiono metody zapewnienia jakości, tj.:

    - metody testów i walidacji aplikacji,
    - automatyzacja procesu zapewniania jakości oprogramowania,
    - testowanie automatyczne,
    - proces przeglądu kodu,
    - zarządzanie projektem oraz zadaniami.

Wykaz technologii użytych w każdym z elementów tego procesu został opisany w rozdziale ":ref:`Architektura systemu`".


Metody walidacji i testów aplikacji
===================================
Dbając o jakość wytworzonych rozwiązań w celu poprawy kodu aplikacji zdecydowano się na wprowadzenie nowoczesnych rozwiązań. Wprowadzone i kultywowane zostały standardy wytwarzania oprogramowania, tj.:

    - wykorzystanie systemu kontroli wersji,
    - wdrożenie systemów i metodyk zwinnych w zarządzaniu projektami i oprogramowaniem,
    - automatyzację procesu budowania projektu,
    - automatyczne zarządzanie zależnościami projektu,
    - automatyzacja procesu testowego, zarówno części warstwy logiki biznesowej jak i graficznego interfejsu użytkownika,
    - wprowadzenie warstwowej architektury rozwiązania,
    - zastosowanie języków oprogramowania oraz technologii powszechnie stosowanych na świecie.


Automatyzacja procesu zapewniania jakości oprogramowania
========================================================
Testowanie oprogramowania odbywa się nie tylko w sposób manualny. Ważnym procesem jest testowanie zautomatyzowane. Sposób ten polega na przygotowaniu odpowiednich narzędzi testowych, które autonomicznie wykonują zadany scenariusz i oceniają jego rezultaty.

Zaletami testowania automatycznego są m.in.:

    - możliwość szybkiej i wydajnej weryfikacji poprawek błędów,
    - możliwość odtworzenia testu,
    - możliwość kompleksowej analizy wyników testów,
    - szybsze i tańsze tworzenie sprawozdań,
    - nieomylność przy wprowadzaniu danych,
    - możliwość podania dużej liczby danych testowych,
    - szybsze wprowadzanie testów do aplikacji,
    - systematyczność i powtarzalność procesu testowania,
    - oszczędzenie czasu osób tworzących system,
    - unikniecie błędów związanych z czynnikiem ludzkim.


Testowanie automatyczne
=======================
W projekcie stosuje się testy jednostkowe dla poszczególnych komponentów oprogramowania. Ponadto zastosowanie mają również lekkie testy integracyjne, służące wykryciu błędów w interakcjach pomiędzy modułami, oraz testy interfejsu służące znajdywaniu błędów w warstwie klienckiej.

W procesie testowania pomocne są również narzędzia pozwalające budować, gromadzić i umieszczać na serwerze archiwa, a także zapewniające przykładowe dane dla testów do łatwego wykorzystania i ponownego użycia. Testy automatyczne są uzupełnieniem testów manualnych. Ogólny zestaw testów znacząco wpływa na poprawę wydajności wytwarzanych produktów. W trakcie przeprowadzania testów następuje wdrożenie demonstracyjne prototypu projektu powstałego w danej iteracji. Ponadto, testy są w pełni wspierane w zintegrowanym środowisku programistycznym (ang. *Integrated Development Environment*, *IDE*). Dzięki powyższym rozwiązaniom testowanie jest proste, szybkie i wydajne.

W ramach wymagań niefunkcjonalnych projektu, określono, że jednym z kluczowych elementów poprawnego działania aplikacji jest jego wydajność. Decyzja taka wynikła z faktu docelowego wykorzystywania systemu do codziennej równoległej pracy znacznej liczby użytkowników. W ramach sprawdzenia wydajności projektu przygotowano scenariusze testów obciążeniowych. Na ich podstawie wykonywane są testy mierzące zachowanie aplikacji przy przetwarzaniu zwiększonej ilości zapytań.

Aby utrzymać wysoki standard jakości oprogramowania został wdrożony system *SonarQube* oraz *SonarLint*. Oprogramowanie to pozwala na wyświetlanie wyników statycznej analizy kodu źródłowego w prostej i przejrzystej formie. Dzięki wykorzystaniu tych systemów twórcy oprogramowania dostają informację o najczęściej popełnianych błędach oraz sposobie ich rozwiązania.

Testy automatyczne są uzupełnieniem testów manualnych, a ogólny zestaw testów znacząco wpływa na poprawę wydajności kodu. W trakcie przeprowadzania testów następuje wdrożenie demonstracyjne prototypu projektu powstałego w danym Sprincie.


Proces przeglądu kodu
=====================
Kolejnym elementem, który znacząco przyczynia się do wysokiej jakości wytwarzanych rozwiązań jest tzw. system *Pull Request* w ramach oprogramowania do przeglądu kodu (ang. *Code Review*). Zarówno do przetrzymywania repozytoriów kodu źródłowego jak i obsługi procesu *Pull Request* wykorzystywane jest narzędzie przechowujące kod źródłowy systemu. Aplikacja ta pozwala w prosty i intuicyjny wprowadzać komentarze do kodu źródłowego co wspiera komunikację osób biorących udział w rozwoju oprogramowania.

W miarę zwiększania dojrzałości systemu oraz wzrostu osób tworzących aplikację istnieje możliwość konfiguracji, aby zmiana w kodzie źródłowym wymagała akceptacji przynajmniej dwóch innych programistów oraz pozytywnego wyniku budowania i testów w systemie *Continuous Integration*.


Zarządzanie projektem oraz zadaniami
====================================
W projekcie oprogramowanie jest wytwarzane w duchu metodyk zwinnych (*Agile*). Główny nacisk jest położony na współpracę z odbiorcami oraz jak najczęstsze udostępnianie aplikacji do testów. Dzięki takiemu rozwiązaniu liczba błędów jest mniejsza, a odbiorcy są w stanie swoje uwagi zgłosić na wczesnym etapie rozwoju systemu, gdzie koszt ich poprawy jest mniejszy.

Do systemów wspierających wytwarzanie oprogramowania w metodykach *Scrum* i *Kanban* wybrano system *Jira* wraz z dodatkiem *Jira Software*. W tym oprogramowaniu znajdują się tzw. rejestry produktów (ang. *backlog*) precyzyjnie opisujące zasady i kolejność tworzenia funkcjonalności i poprawek w systemie. Aplikacja ta pozwala na planowanie iteracji, szacowanie pracochłonności zadań oraz wyliczanie postępów prac na wykresie spalania, jak również prędkości zespołu na grafice *velocity chart*.
