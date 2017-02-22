*************************
Proces zarządzania zmianą
*************************

.. figure:: ../../_static/img/processes.png

    Procesy zarządzania zmianą.

Procesy wejścia dla zarządzania zmianą
======================================

Wejściem do procesu zmiany jest zgłoszenie otrzymane poprzez określony kanał kontaktowy. Pierwszym zadaniem związanym ze zgłoszeniem jest określenie jego typu (incydent, wniosek o usługę lub inne).

Przyjmuje się jednolity tryb nadsyłania zgłoszeń incydentów i wniosków o usługę w ramach prac nad aplikacją. W praktyce sposób postępowania z incydentami oraz wnioskami o usługę jest podobny, dlatego inicjalnie oba są zawarte w zakresie procesu Zarządzania Incydentem.

Wnioski o usługę realizowane są w trybie indywidualnym ale powtarzalnym (związanym z analiza ryzyka, czasochłonności, możliwości wprowadzenia zmiany w aktualnym stadium zaawansowania prac), natomiast w przypadku stwierdzenia incydentu, następują działania związane z Zarządzaniem Incydentem. 

Przyczyna wystąpienia incydentu może okazać się oczywista, co skutkuje w szybkim rozwiązaniu i zamknięciu incydentu. W identyfikacji przyczyny przydatna jest Baza Wiedzy dotycząca istniejących rozwiązań. W przypadku, gdy nie jest możliwa szybka identyfikacja przyczyny i rozwiązanie zgłoszenia, następuje uruchomienie procesu Zarządzania Problemem.

Incydent (błąd w funkcjonalności aplikacji)
===========================================

Incydent to każde zdarzenie, które nie jest częścią normalnego działania usługi, zakłóca tę usługę, które powoduje lub może powodować przerwę w dostarczaniu usługi, względnie obniżenie jej jakości.

Wniosek o usługę (zmiana funkcjonalności)
=========================================

Wnioski o usługę mają charakter powtarzalny, obsługiwane są zawsze w ten sam sposób, dla których możliwe jest zagwarantowanie przez Firmę czasu realizacji. 

Zarządzanie incydentem
======================

Celem procesu Zarządzania Incydentem jest przywrócenie normalnego działania aplikacji i usług tak szybko, jak to możliwe oraz minimalizowanie niekorzystnego wpływu Incydentu na działanie aplikacji w przyszłości, tak by zapewnić najwyższy możliwy poziom jakości i dostępności świadczonych przez Projekt usług.

Przez "normalne działanie usług" należy rozumieć działanie usług określone w ustalonej z zamawiającym dokumentacji. Wszystkie zgłoszenia użytkowników, czyli incydenty i wnioski o usługę, powinny zostać zarejestrowane w Bazie Zgłoszeń. Jest to pierwsza czynność procesu Zarządzania Incydentem wykonywana przez I linię wsparcia tzw. Service Desk.

Użytkownik przy rejestracji swojego zgłoszenia otrzymuje unikalny numer referencyjny (nr zgłoszenia), na który może powołać się przy kolejnym kontakcie w sprawie danego zgłoszenia.

Następnym krokiem jest klasyfikacja incydentu.

Klasyfikacja obejmuje następujące czynności:

* identyfikację usługi, której dotyczy incydent i wybór odpowiedniej kategoryzacji,
* identyfikację komponentu usługi związanej z incydentem,
* identyfikację fragmentu kodu, którego dotyczy incydent,
* przypisanie priorytetu na podstawie wpływu danego incydentu na funkcjonowanie usług i aplikacji, użytkownik zgłaszając incydent może zażądać nadania konkretnego priorytetu zgłoszeniu przy czym w przypadku rozbieżności pomiędzy oceną zgłaszającego i Service Desk, priorytet jest uzgadniany przez Firmę z Klientem w późniejszym terminie, a w trakcie obsługi przypisywany jest priorytet określony przez zgłaszającego,
* konfrontacja danego incydentu z Bazą Wiedzy w celu znalezienia gotowego rozwiązania lub rozwiązania zastępczego,
* próba rozwiązania incydentu na podstawie gotowego rozwiązania lub własnego doświadczenia,
* jeśli rozwiązania nie ma lub jest nieskuteczne – wybór i przypisanie kompetentnej grupy wsparcia, mogącej rozwiązać incydent.

Kolejnym krokiem jest zamknięcie incydentu, polegające na zapewnieniu: 
* (jeżeli zastosowano rozwiązanie zastępcze nieznajdujące się dotychczas w Bazie Wiedzy) poprawności wpisu w Bazie Wiedzy dotyczącego zastosowanego rozwiązania (czy wpis jest zwięzły i zrozumiały?),
* poprawnej klasyfikacji incydentu ze względu na przyczynę jego wystąpienia,
* sprawdzenia czy zastosowane rozwiązanie jest uzgodnione i zatwierdzone przez Klienta,
* wszystkie istotne informacje dotyczące incydentu są zarejestrowane, a w szczególności rejestrowane są:
* czas poświęcony na rozwiązanie incydentu,
* osoba zamykająca incydent,
* data i czas zamknięcia incydentu.

Zarządzanie problemem
=====================

Celem procesu Zarządzania Problemem realizowanego przez Firmę jest minimalizowanie niekorzystnego wpływu incydentów oraz zabezpieczenie przed ponownym pojawieniem się incydentów związanych z tą samą przyczyną.

W pierwszym kroku procesu pracownik obsługujący problem jest zobowiązany do zarejestrowania nowego Problemu w Bazie Wiedzy. Następnie dokonuje klasyfikacji problemu zgodnie z przyjętymi zasadami. Klasyfikacja dokonywana jest w celu odpowiedniej alokacji zasobów, tak aby problemy o najwyższym priorytecie (poziomie negatywnego wpływu na realizację celów funkcjonowania aplikacji i usług) były rozwiązywane w pierwszej kolejności.

W kolejnym kroku ten sam pracownik lub zespół diagnozuje problem oraz proponuje jego rozwiązanie. Po tym etapie, czyli w momencie gdy znana jest już przyczyna wystąpienia, problem staje się znanym błędem. Kolejne czynności zmierzające do trwałego wyeliminowania przyczyny zwane są Kontrolą błędu.

Rezultatem procesu Zarządzania Problemem musi być wpis do Bazy Wiedzy dokonany przez pracownika obsługującego problem, identyfikujący rozwiązanie lub akceptujący rozwiązanie zastępcze. Dany wpis powinien być na tyle zrozumiały i szczegółowy, aby kolejne zgłoszenia tego samego typu, nie wymagały ponownego uruchomiania procesu Zarządzania Problemem i mogły być rozwiązane przez Specjalistów.

Może wystąpić sytuacja, w której rozwiązanie problemu będzie wymagało od pracowników obsługujących problem  wprowadzenia zmian. Zmiany są realizowane w procedurze Zarządzania Zmianą i w takim przypadku dopiero zastosowanie (przygotowanie, przetestowanie i wprowadzenie) zmiany pozwala zamknąć rozwiązany problem oraz wszelkie incydenty z nim powiązane.

Proces zarządzania zmianą
=========================

Zmiana, to dodanie, modyfikacja lub usunięcie czegokolwiek, co mogłyby mieć wpływ na działanie aplikacji i świadczone przez nią usługi. W ten sposób ogólna definicja zmiany obejmuje swym zakresem każdą zmianę w architekturze, procesach, narzędziach i innych elementach konfiguracji. 

Celem procesu jest zapewnienie, aby na każdym etapie cyklu życia aplikacji i jej usług, wszelkie zmiany kontrolowane były poprzez standardowe metody i procedury, które pozwalają minimalizować zakłócenia w jakości świadczonych usług. Za proces zarządzania zmianą jest odpowiedzialna Firma.

Ogólny sposób obsługi zmian przedstawiony jest na schemacie poniżej. 
Wejściem do procesu jest zgłoszenie Incydentu, lub złożony przez ITSM wniosek o zmianę (RFC, z ang. Request of Change). 

Na etapie tworzenia aplikacji, większość zmian wynika ze zgłoszonych Incydentów, natomiast wniosek o zmianę dotyczy tylko procesu wdrożeniowego i może być zgłoszony tylko przez wskazanych pracowników Firmy (w szczególności dotyczy to zmian standardowych, dla których decyzja jest preautoryzowana). 

Obsługa zadania zmiany rozpoczyna się od klasyfikacji i przypisania odpowiedniego priorytetu. Jeśli zmiana zostanie sklasyfikowana jako zmiana standardowa realizowana jest w uproszczony sposób. Zmiana standardowa jest określona wcześniej i decyzja o jej wdrożeniu jest automatycznie autoryzowana. Szczegóły dotyczące zmian standardowych i procedurze ich obsługi zostały określone w dokumentach roboczych dotyczących budowy i eksploatacji aplikacji i jej środowiska. 

Jeśli zmiana nie jest zmianą eksploatacyjną następuje ocena zmiany. Każda taka zmiana przed wprowadzeniem musi zostać zatwierdzona. Z punktu widzenia procesu zarządzania zmianą bardzo istotne jest określenie trybu, w jakim zmiana ma być zatwierdzona. Tryb ten wynika bezpośrednio z charakteru zmiany. Ze względu na to, że sposób autoryzacji może trwać długo (potrzebne jest zwołanie zespołu wewnątrz Firmy, wymagana jest konsultacja z Klientem lub użytkownikami końcowymi) w pewnych sytuacjach może być to nieakceptowalne. 

Dotyczy to szczególnie zmian, które wiążą się np. z krytycznymi poprawkami bezpieczeństwa, które powinny być wdrażane możliwie szybko, a jednocześnie proces musi zapewnić decyzję o wdrożeniu takiej zmiany. Dlatego też zmiany te klasyfikowane są jako pilne i decyzja o ich wdrożeniu leży w kompetencji.

Po autoryzacji planowanej zmiany kolejnym krokiem jest przygotowanie i realizacja zatwierdzonej zmiany. Zakres przeprowadzanej zmiany zawiera dokumentacja związana z obsługa Incydentu, lub dokument RFC. Dokumenty te w szczególności muszą uwzględniać przygotowanie planu implementacji zmiany oraz aktualizacji dokumentacji oraz systemu zarządzania konfiguracją.
