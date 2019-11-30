*****
Scrum
*****

Artefakty Scrum
===============
.. glossary::

    Product Roadmap
        Timeline

    Product Backlog
        List of items to do

Product Backlog
---------------
Product Backlog jest jedynym źródłem wymagań do projektu. Stanowi uporządkowaną, dostępną dla członków zespołu listę wszystkich elementów, które mogą być potrzebne w realizacji produkcji oprogramowania.

W szczególności, Product Backlog wymienia wszystkie:

    * Cechy produktu,
    * Wymagania,
    * Usprawnienia,
    * Poprawki.

Uporządkowanie elementów listy zależy od wartości, ryzyka, priorytetu oraz stopnia potrzeby realizacji danego elementu - im element jest wyżej na liście, tym szybciej rozpoczynają się prace nad nim. Większy nacisk kładziony jest na jego zrozumienie, zapewniany jest większy poziom szczegółowości oraz bardziej precyzyjnie szacowana jest przez zespół jego pracochłonność.

Product Backlog ewoluuje w trakcie trwania procesu wytwórczego w zakresie porządkowania, dodawania szczegółów, ponownego oszacowywania pracochłonności oraz aktualizowania elementów.

Nie rzadziej, niż co Sprint Review Meeting sprawdzane są w Product Backlogu postępy prac. Monitoruje się całkowitą pozostałą pracochłonność poszczególnych elementów Product Backlogu, porównując ją z wynikiem poprzednim oraz wyznacza się trend w pracy, prognozując datę końca produkcji.

SCRUM Team
----------
Osoby zaangażowane w projekt tworzą samoorganizujący i wielofunkcyjny zespół, tzw. SCRUM Team, który składa się z:

    * Product Owner - dba o maksymalizację wartości produktu i pracy Development Teamu, jest odpowiedzialny za zarządzanie Product Backlogiem, przygotowuje spotkania, ustala priorytety, prezentuje zadania Development Teamu, wyjaśnia wszelkie niejasności oraz ma prawo do anulowania Sprintu gdy np. jego cel stał się nieaktualny,

    * Development Team - jest odpowiedzialny za pracę, dostarcza przyrosty funkcjonalności; jest samoorganizujący, wielofunkcyjny, bez struktury i podzespołów, składa się z 3-9 osób,

    * SCRUM Master - wspiera organizację w dostosowaniu SCRUMa dla większej efektywności SCRUM Teamu oraz w pracy z innymi SCRUM Masterami, dba o SCRUM Team, czyli o rozumienie przez niego przebiegu procesu produkcji, długoterminowych planów i stosowania przyjętych zasad zwinnej produkcji. Wspiera Product Ownera w efektywnym zarządzaniu Product Backlogiem i przygotowywaniu spotkań. Wspiera Development Team w samoorganizacji, wielofunkcyjności i wytwarzaniu produktów o wysokiej wartości. Uczy go tworzyć elementy Product Backlogu, komunikuje wizje i cele tych elementów oraz usuwa wszelkie napotkane przeszkody.

Sprint
------
Sprint jest centralną częścią SCRUMa, trwającą poniżej miesiąca (zwykle od 5 do 10 dni). Stanowi zamknięty cykl wytwórczy, dający w wyniku działający prototyp produktu (wewnętrzny lub zewnętrzny), będący podzbiorem finalnego produktu, który rozrasta się z iteracji na iterację aż do produktu końcowego.

Ważne jest określenie celu danego Sprintu (tzw. Sprint Goal), który nadaje kierunek pracy zespołowi, pozostawiając jednocześnie elastyczność jeśli chodzi o sposób realizacji tego celu.

Członkowie zespołu powinni przestrzegać podstawowych zasad, tj.:

    * nie dokonywać zmian wpływających na Sprint Goal,
    * nie dokonywać zmian w Development Teamie,
    * nie dokonywać zmian w standardach jakości,
    * zakres prac może być uściślany i negocjowany tylko pomiędzy Product Ownerem a Development Teamem, i tylko na skutek przyrostu wiedzy.

Każdy Sprint dostarcza nowy, produkcyjnie gotowy przyrost funkcjonalności, a każdy przyrost tworzy całość ze wszystkim, co zostało dotychczas wytworzone.

Sprint Backlog
--------------
Sprint Backlog zawiera elementy Product Backlogu oraz plan dostarczenia przyrostu w Sprincie. Zarządza nim wyłącznie Development Team i aktualizuje go w czasie trwania Sprintu.

Tak jak w Product Backlogu, w Sprint Backlogu również sprawdzane są postępy prac, jednak nie rzadziej, niż co Daily SCRUM. Monitorowana jest całkowita pozostała pracochłonność poszczególnych elementów Sprint Backlogu i porównywana z wynikiem poprzednim oraz wyznaczany jest trend w pracy, szacujący prawdopodobieństwo osiągnięcia Sprint Goalu na koniec Sprintu.

Burndown Chart
--------------
Wykres takiego trendu określa się mianem Burndown (wykres wypalania). Zestawia on tempo pracy zespołu z pożądanym tempem pracy pozwalającym ukończyć Sprint lub cały projekt w terminie. Dzięki temu Burndown pozwala na pierwszy rzut oka ocenić sytuację dotyczącą realizacji zadań, w szczególności zdiagnozować ograniczenia.

:Zdrowy Burndown: Ponieważ wykres ma przedstawiać trend w pracy, na osi pionowej umieszcza się pozostałą do wykonania pracę, zaś na poziomej - czas. Pozostałą do wykonania pracę można mierzyć za pomocą sumy godzinowych oszacowań pozostałych zadań, liczby zadań lub w dowolny inny, odpowiedni do sytuacji sposób.

:Burndown prognozujący nie zdążenie w terminie: Jeśli na wykresie widać, że postępy pracy są wyraźnie wolniejsze, niż było to planowane, zespół powinien natychmiast poinformować o tym Właściciela Produktu i uzgodnić z nim, które zadania mają najwyższy priorytet, a które mogą zostać odłożone na później.

:Burndown świadczący o zbyt długim utknięciu na zadaniach: Jeśli wykres ma kształt "urwiska", czyli większość zadań jest domykana dopiero pod koniec Sprintu, może to świadczyć o tym, że praca dzielona jest na zbyt długie zadania. Redukuje to możliwość śledzenia aktualnej sytuacji w pracy nad projektem i stwarza zagrożenie, że zadanie się jeszcze bardziej wydłuży.

        Może też świadczyć to o tym, że zespół dostał zbyt wiele pracy do wykonania w danym czasie, co prowadzi do heroicznych wysiłków zespołu pod koniec Sprintu, a w rezultacie do natychmiastowej zapaści jakości i szybkiego wypalenia zespołu.

        W wyniku zastania powyższej sytuacji konieczne jest ustalenie priorytetów zadań.

:Burndown świadczący o wzroście zakresu prac: Jeśli wykres przez część Sprintu rośnie, zamiast maleć, może to świadczyć o:

            * braku dobrze określonego zakresu sprintu podczas planowania,
            * przypomnieniu sobie przez zespół o dodatkowych zadaniach,
            * otrzymuje dodatkowych zleceń w trakcie trwania Sprintu,
            * o napotkaniu nieprzewidzianych problemów technicznych.

            Ponadto dobrym rozwiązaniem byłoby stosowanie eksperymentów technicznych przed przystąpieniem do tworzenia produktu. Konieczne skrócenie zadań lub weryfikacja ilości pracy oraz konieczność zadbania o lepszą ochronę zespołu, by dać mu swobodę sprawnej realizacji ustalonych zadań.

Definition of Done
------------------
Definition of Done (DoD), czyli definicja ukończenia jest wykazem działań wymaganych do realizacji zadań w procesie produkcyjnym. Działaniami takimi mogą być np. napisanie kodu, skomentowanie kodu, testowanie jednostkowe, testowanie zintegrowane, sporządzenie notatek, zaprojektowanie dokumentów, itp.

Dzięki określeniu DoD, wszyscy członkowie zespołu jednoznacznie rozumieją, co oznacza stwierdzenie „zadanie wykonane” (Done). Ponadto, zespół produkcyjny może skupić się na konkretnych elementach, które muszą zostać wykonane, aby zadanie zostało uznane za zrealizowane. W rezultacie, DoD pozwala dodać produktowi weryfikowalnych wartości, nie zmieniając jego funkcjonalności.

DoD określa się biorąc pod uwagę, jakie czynności realistycznie mogą zostać przez zespół wykonane. Z czasem lista tych czynności ulega zmianom i staje się bardziej rygorystyczna.

Skalowalność
------------
SCRUM jest skalowalny, tzn. może być zastosowany w projektach, w których bierze udział duża ilość pracowników. Skalowanie zespołu powinno się odbywać ze względu na wymogi dotyczące funkcjonalności produktu, nie zaś ze względu na umiejętności członków zespołu.

Podział systemu na moduły i całego zespołu na mniejsze zespoły

Produkcja dużego systemu wymaga podzielenia jego architektury na mniejsze moduły (podsystemy). Podział ten odbywa się zgodnie z tym, jakie Klient dostrzega wartości w poszczególnych częściach systemu oraz zgodnie z możliwościami technologicznymi. Cały zespół również jest dzielony na mniejsze zespoły (Scrum Teamy),  które zajmują się pracą nad przypisanymi im modułami systemu. Oprócz tych zespołów wydziela się również zespół poziomu systemu, w skład którego wchodzą architekci, liderzy zespołów, menedżerowie produktów oraz zespół zapewnienia jakości, który zajmuje się myśleniem, działaniem i wdrażaniem SCRUMa na poziomie systemu oraz uzupełnianiem Product Backlogu o testy integracyjne i demonstracje na poziomie systemu, punkty kontroli jakości oraz dystrybucje testowe.

W przypadku SCRUMa wprowadzanego na dużą skalę, pojawia się wymagany element w DoD: pomyślny wynik testów integracyjnych.


Wydarzenia Scrumowe
===================

Backlog Refinement
------------------
Definicją tego spotkania jest wszelkiego rodzaju praca na backlogu, tj. np jego priorytetyzacja, dekompozycja zadań oraz czyszczenie rejestru zmian produktu. Podczas Refinementu zespół wraz z Product Ownerem, układa sobie pracę pod następne iteracje oraz dokonuje wstępnego oszacowania wielkości zadań oraz określenia kryteriów akceptacyjnych poszczególnych zadań.

Aby skutecznie przeprowadzić refinement należy ustalić co będzie produkowane - potrzeba uporządkowanego Product Backlogu, zrozumienia jego elementów, zrozumienia aktualnego stanu produktów, wyliczonej pojemności zespołu oraz wiedzy na temat historycznej wydajności zespołu.

Sprint Planning
---------------
Podczas planowania zespół wraz z właścicielem produktu podejmuje decyzję, które zadania będą wchodziły w skład następnej iteracji a co za tym idzie jakie funkcjonalności zostaną oddane po kolejnym przyroście.

W Sprint Planning Meetingu bierze udział cały SCRUM Team. Trwa, w zależności od czasu trwania Sprintu, od 2 do 4 godzin.

Celem tego spotkania jest zaplanowanie pracy na cały Sprint (w szczególności ustalenie Sprint Goalu), a więc ustalenie w jaki sposób zostanie to wyprodukowane - precyzuje się dużo drobnych zadań, członkowie zespołu sami wybierają zadania dla siebie i na każde z nich przeznacza się maksymalnie 2 dni.

Każdy etap projektu w każdym kolejnym Sprincie poddawany jest analizie szczegółowej, opartej o szeroki zakres informacji. Najważniejszym zadaniem tej analizy jest rozwiązywanie trudności i problemów. Jest to proces pracochłonny, lecz w wielu przypadkach konieczny do skutecznego usprawniania produkcji.

Sprint Review
-------------
Podczas spotkania Review zespół oddaje wykonane zadania właścicielowi produktu udowadniając spełnienie kryteriów akceptacyjnych każdego z zadań. Spotkanie to powinno zakończyć się akceptacją przyrostu oraz decyzją biznesową o wdrożeniu wytworzonych zmian.

Uczestnicy tego spotkania to SCRUM Team oraz interesariusze. Ma ono charakter nieformalny i trwa, w zależności od czasu trwania Sprintu, od 1 do 2 godzin.

Celem jest uzyskanie informacji zwrotnej od interesariuszy na temat zaprezentowanego przyrostu funkcjonalności (produktów).

Podczas Sprint Review Meetingu Product Owner prezentuje co zostało zrobione i co nie zostało zrobione, omawia Product Backlog oraz prezentuje prognozowane daty ukończenia produkcji, zaś Development Team przedstawia przebieg pracy - co nie sprawiło problemów, gdzie zostały napotkane problemy, jak te problemy zostały rozwiązane i jaki jest przyrost funkcjonalności oraz odpowiada na zadawane pytania. Wszyscy wspólnie uzgadniają temat dalszego planu działania, co jest wkładem do następnego Sprint Planning Meetingu.

Retrospective
-------------
Zamknięte spotkanie zespołu, który omawia problemy napotkane podczas właśnie zakończonej iteracji. Po retrospektywie zespół wyciąga wnioski z sukcesów oraz porażek. Planuje także eksperymenty, tj. nowe podejście do pracy lub zmiany w organizacji zespołu w przyszłej iteracji mające na celu usprawnienie procesu. Wnioski z takiego spotkania powinny być spisane i poddane do wiadomości członkom zespołu, ale nie ujawniane innym.

Udział w tym spotkaniu bierze cały SCRUM Team. Trwa ono, w zależności o czasu trwania Sprintu, od 1 do 2 godzin.

Cel spotkania to spojrzenie wstecz na wykonywaną pracę w celu jej polepszenia - praca powinna być coraz bardziej efektywna, a także dająca pracownikom satysfakcję. Cały zespół analizuje, jak przebiegał proces wytwórczy, jak ten proces usprawniały wykorzystywane narzędzia oraz jak kształtowały się relacje między pracownikami. Wszyscy dążą do konkluzji, jakie elementy pracy warto powtórzyć, a jakie można usprawnić. Sprawdzane jest też, czy wytworzone w Sprincie elementy oprogramowania należy zmodyfikować.

Daily Scrum
-----------
Do jednego z najważniejszych spotkań należy codzienny Scrum, tj. krótkie maksymalnie 15 minutowe zebranie zespołu podczas, którego członkowie opowiadają o problemach napotkanych przy realizacji zadań z poprzedniego dnia oraz o zamiarach na kolejną dobę.
Na tym spotkaniu powinno się skupić na zadaniach przybliżających zespół do osiągnięcia tzw. celu sprintu, tj. najważniejszego motywu przewodniego iteracji.

W spotkaniach tych uczestniczy Development Team. Odbywają się one codziennie o tej samej porze, w tym samym miejscu i trwają 15 minut.

Daily SCRUMs mają na celu synchronizowanie pracy zespołu oraz ustalanie planu działania na następne 24h. Odbywa się to poprzez udzielenie odpowiedzi przez każdego członka zespołu na 3 pytania:

    * co zrobił wczoraj aby przybliżyć zespół do osiągnięcia celu sprintu,
    * co będzie robił dzisiaj aby przybliżyć zespół do osiągnięcia celu sprintu,
    * jakie ma problemy, które uniemożliwiają osiągnięcie celu sprintu.

Zaletą tych spotkań jest usprawnienie komunikacji, wykluczenie straty czasu na nieproduktywne, czasochłonne rozmowy oraz usunięcie potencjalnych przeszkód w pracy. Ponadto, Daily SCRUM promuje samodzielność i szybkie podejmowanie decyzji oraz wpływa na poprawienie świadomości postępu prac projektowych w zespole.

SCRUM of SCRUMs
===============
Duża liczba SCRUM Teamów jest wyzwaniem koordynacyjnym i komunikacyjnym. Potrzeba też zapewnienia zintegrowania poszczególnych modułów, tak aby tworzyły jednolity docelowy system. W celu zapewnienia dobrej organizacji pracy wielu zespołów, organizowane są Eventy o nazwie SCRUM of SCRUMs. Uczestniczą w nich liderzy poszczególnych SCRUM Teamów.

Spotkania te odbywają się codziennie, najlepiej po zespołowych Daily SCRUMach. Każdy uczestnik odpowiada wtedy na 3 pytania:
co zespół zrobił wczoraj,
co zespół będzie robił dzisiaj,
jakie zespół ma problemy.
