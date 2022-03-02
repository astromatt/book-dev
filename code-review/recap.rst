Recap
=====


1. Praktyki developerskie a praktyki projektowe:

    * Praktyki projektowe (Scrum, Kanban, XP, Lean)
    * Praktyki developerskie (TDD, S.O.L.I.D., CI/CD, Code Review/Pull Request, DevOps)
    * Dlaczego coraz więcej zespołów odchodzi od Scrum i idzie w Kanban?
    * Połączenie Scrum i Kanban
    * Lean Startup: Build, Measure, Learn loop
    * Praktyki deweloperskie a wartości biznesowe
    * Wykres agility
    * Agile vs agility

2. Ekosystem narzędziowy:

    * Architektura
    * Skalowanie
    * Ekosystem wewnętrzny i zewnętrzny

3. System kontroli wersji:

    * Rozproszony vs scentralizowane systemy kontroli wersji
    * GIT i jego zalety
    * Koncept Feature Branch relacja z User Story
    * Rozwiązywanie konfliktów w systemie kontroli wersji
    * Hotfix vs bugfix
    * Pull Request vs Merge Request
    * Merge vs Rebase
    * Relacja branchy i zadań z backlog
    * Podział repozytoriów pod względem technicznym i produktowym
    * Strategia Fork
    * Strategia Centralnego Repozytorium
    * Strategia Monorepo
    * Strategia wszystko do Main
    * Strategia Git Flow
    * Strategia budowania branchy
    * Statyczna analiza kodu Pull Requestów
    * Scalanie Pull Request (merge, rebase, squash+merge, squash+rebase)

4. Dług techniczny:

    * Definicja długu technicznego
    * Czym w praktyce jest dług techniczny
    * Rozpoznawanie długu technicznego
    * Programistyczny dług techniczny
    * Dług techniczny architektury systemowej
    * Dług techniczny infrastruktury
    * Dług techniczny organizacji
    * Kryteria oceny długu technicznego
    * Wychodzenie z długu technicznego
    * Monolit vs. mikro-usługa

5. Dokumentacja projektu:

    * Code review i dokumentacja
    * Architectural Decision Records
    * Składnia Markdown i reStructuredText
    * Systemy generowania dokumentacji
    * Code Review jako mechanizm przekazywania wiedzy
    * OpenAPI i SwaggerUI

6. Proces Code Review:

    * Systemy do Code Review, ich wady i zalety
    * Code Review blokujące, nieblokujące i post-factum
    * Unified diff vs side-by-side
    * Komentarze: co komentować, jak politycznie komunikować problem
    * Taski: blokowanie zmian
    * Liczba linii w Code Review
    * Pair programming vs Code Review
    * Dobre praktyki Code Review
    * Czy cały kod musi być poddawany Code Review?
    * Kogo zapraszać do Code Review?
    * Skuteczność notyfikacji
    * Czy PO powinien być w Code Review?
    * Co oznacza akceptacja Code Review?

7. Automatyzacja Code Review:

    * Włączenie procesu CI/CD do Code Review
    * Statyczna analiza kodu źródłowego
    * Pipeline as a Code
    * Code Review dla provisioning
    * Quality Gates
    * Triggerowanie statusów w Jira
    * Automatyzacja narzędzi Atlassian (Atlassian Python API)

8. Podstawy optymalizacji i wydajności systemów:

    * Złożoność obliczeniowa
    * Złożoność pamięciowa
    * Złożoność cyklometryczna

9. Jakość kodu:

    * SonarQube i SonarLint
    * Wyciąganie wniosków z analizy statycznej
    * Quality Gates
    * Czym jest Spaghetti code
    * Zależności w kodzie i między modułami
    * Zasady S.O.L.I.D.
    * Refactoring legacy systemów i legacy code
    * Budowanie bazy wiedzy jako wynik Code Review
    * Code Review jako element Collective Code Ownership
    * Emerging architecture

10. Dobre praktyki:

    * Zasady clean code
    * Nazewnictwo zmiennych, długość nazw, funkcji, klas i pakietów
    * Liczba paramterów, typy i wzorce konstrukcyjne
    * Zasady SOLID
    * Zmienne statyczne, do czego służą i kiedy stosować
    * Importy wszystkiego czy wybiórcze
    * Klasy abstrakcyjne vs Interfejsy, kiedy i jak
    * Długość klas
    * Liczba metod
    * Długość metod
    * Modyfikatory dostępu: private, protected, public

11. Testy:

    * TDD: test first vs test last development
    * Złożoność cyklometryczna vs liczba testów
    * Mierzenie pokrycia testami
    * Idealne pokrycie?
    * Testy mutacyjne
    * Rodzaje testów

12. SonarQube:

    * Definicja Quality Gates
    * API Key i uprawnienia w projekcie
    * SonarLint
    * SonarScanner
    * Wpięcie SonarQube do CI/CD

13. Logowanie:

    * Czytelne komunikaty błędów
    * Dobieranie poziomów logowania
    * Kody błędów
    * Identyfikacja miejsc w kodzie, gdzie wystąpił wyjątek
    * Spooling logów do pliku i bazy danych
    * Strategie rotowania logów
    * Dane wrażliwe - logowanie i przechowywanie, udostępnianie

14. Zależności:

    * Systemy śledzenia podatności w zależnościach

15. Podsumowanie:

    * Kto powinien być zaangażowany w Code Review?
    * Ile czasu poświęcić na Code Review?
    * Czy Code Review jest potrzebne przy TDD?
    * Jak wielkość elementów w backlog wpływa na Code Review?
    * Jak uniknąć wąskiego gardła w postaci Code Review?
    * Czy zawsze należy robić Code Review?
    * Czy można zautomatyzować proces Code Review?
    * Na co warto zwrócić uwagę w Code Review?
    * Jakiej wielkości zmiany poddawać Code Review?
    * Jak komunikować problem z kodem?
    * Jak blokować scalenie kodu, który zawiera błędy?
    * Jak robić Code Review na żyjącym branchu?
    * Notyfikacje i jak pozostać na bieżąco ze zmianami?
    * Jak unikać silosów kompetencyjnych za pomocą Code Review?
