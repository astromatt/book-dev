Wstęp
=====

Zanim zaczniemy kodować
-----------------------

Development to nie tylko kod. Chociaż bardzo często o tym zapominamy to “kodzenie” jest wyłącznie jedną z części procesu wytwarzania oprogramowania. Development to narzędzia wpierające programowanie, to systemy kontroli wersji, to Continuous Integration i Delivery i w końcu to również ludzie i ich interakcje. Metodyki agile takie jak Scrum i Kanban na stałe zagościły w naszych projektach jako standardy komunikacji i usprawnienia pracy.

Niniejsza książka jest zaadresowana do developerów, testerów, adminów, analityków biznesowych, managerów i wreszcie coachów Agile na każdym poziomie zaawansowania. Procesy które tutaj opisuję pomagają sprawnie wytwarzać oprogramowanie w zadowalającym i przewidywalnym tempie. Pozwalają okiełznać chaos związany z prowadzeniem projektu informatycznego oraz zwiększyć satysfakcję klienta z oprogramowania, które zamówił. Zasady tutaj przedstawione są uniwersalne i można je zastosować do każdego projektu bez względu na dziedzinę oraz język programowania. Są to po prostu ogólnie przyjęte dobre praktyki wytwarzania oprogramowania skutecznie wdrożone w firmach zarówno małych jak i dużych na całym świecie.

Wszystko o czym będzie mowa w następnych rozdziałach jest dostępne w internecie w postaci audio, wideo lub jako artykuły i blogposty o poszczególnych elementach procesu. Nigdzie jednak nie znalazłem dobrego źródła przedstawiającego problem od początku do samego końca. Od wyjścia z inicjatywą projektową, przez realizację, programowanie i wdrożenie na środowisko produkcyjne włącznie. Choć coraz częściej w internecie znajduję oferty pracy dla tzw. Full Stack Developera to zrozumienie tematu i środowiska jest na niezbyt zadowalającym poziomie. Zamiast narzekać lepiej coś zrobić i zmienić. I ot takim sposobem właśnie czytasz książkę, która jest efektem moich doświadczeń oraz zbiorem dobrych praktyk wypracowanych przez największe autorytety świata IT i zarządzania projektami.

Development processes
---------------------

Rozpoczynając pracę jako Coach w nowej firmie zwykle proszę o wprowadzenie w aktualny stan procesów i produktów. Tego co najcenniejsze dla firmy. To co stanowi corowy biznes i innowacyjność przedsiębiorstwa na rynku. Wg. mnie jedyny sposób aby dobrze dopasować procesy do organizacji to postarać się wniknąć w jej codzienną egzystencję. Zdarza się, iż właściciele firm nieufnie podchodzą do tematu dzielenia się tajemnicami biznesowymi lecz w miarę postępu szkoleń jesteśmy w stanie znaleźć porozumienie a co najważniejsze zaufanie do siebie.

Jednym z najczęstszych problemów jakie spotykam w organizacjach szczególnie młodych i "zwinnych" jest brak jakichkolwiek procesów. Organizacje, w których u podstaw leży Agile dochodzą do ekstremum i "brzydzą" się ich wprowadzaniem. Uważają, że to jedynie spowolni development, spowoduje bariery komunikacyjne między ludźmi a przede wszystkim zniszczy ich luźną i zwykle młodzieżową atmosferę.

Nic bardziej mylnego. Każda filozofia nawet błędna i nieaktualna zawiera w sobie dobre przesłania. ITIL tak mocno i szeroko krytykowany w start-upowym środowisku jako ciężki zestaw procesów zaprzeczających zwinności organizacji jest zbiorem najlepszych praktyk IT wypracowanych przez liderów branży jako odpowiedź na najczęściej pojawiające się problemy podczas tworzenia organizacji i prowadzenia projektów.

Moim zdaniem nawet takie ciężkie metodyki jak Prince i PMBoK posiadają w sobie elementy, których odrzucenie skazuje naszą organizację na wynajdywanie koła na nowo i marnowanie czasu na już rozwiązane problemy.

Proszę nie zrozum mnie źle: jestem daleki od wprowadzania tych metodyk jako standardy wytwarzania oprogramowania. Zresztą nie na darmo Agile (Scrum i Kanban) stają się standardem i wypierają swoich starszych kolegów. Moim przesłaniem jest sugestia aby przyjrzeć się tym tworom i zaimplementować ich najlepsze strony w naszych projektach czyniąc je jeszcze lepszymi i bogatszymi o sprawdzone standardy, które do niedawna były jedynym słusznym podejściem.

Team management
---------------

Praktycznie nie zdarza się abym pracując z jakimś zespołem nie natrafił na problem komunikacyjny między członkami zespołu. Zwykle wynika to z niedojrzałości zespołu, sposobu jego pracy oraz po prostu z problemów z jego zarządzaniem.

Aby stać się dobrym managerem nie konieczne jest wieloletnie doświadczenie w wytwarzaniu oprogramowania. Nie każdy Senior czy Ekspert developer będzie nadawał się na kierownika projektu, lidera zespołu czy szefa działu. W zadziwiającej większości przypadków osoby techniczne, które awansują na kierownicze stanowisko po prostu nie sprawdzają się w tej roli. Czasami jest to związane z umiejętnościami interpersonalnymi, tzw. miękkimi, takimi jak np. charakter introwertyczny. Czasami problem jest trudniejszy do zlokalizowania i wynika z polityki, zwykłej zawiści lub innych bardzo często prozaicznych problemów.

Dobry manager to taki, który przewidywalnie dowozi oraz charyzmatycznie ciągnie ludzi za sobą. Dobry manager to osoba, która jest "key-opinion leaderem" czyli jest uznawany za eksperta w swojej dziedzinie. Którego ludzie się słuchają nie dlatego, że jest nad nimi w strukturze hierarchicznej, a dlatego, że jest uznanym specjalistą i dobrym człowiekiem stanowiącym wzór dla innych jak postępować.

Choć rzadko się to zdarza to można spotkać takie osoby na swojej ścieżce życiowej. Zwykle idziemy za nimi nawet w ogień i nigdy tego nie żałujemy. Ich decyzje mocno wpływają zarówno na nasze życie prywatne jak i zawodowe. A praca z takimi osobami to czysta przyjemność.

"Bardzo fajnie się to czyta, ale rzeczywistość jest inna." Całkowicie zgadzam się z tą ideą. Jednakże spotkałem na swojej drodze taką osobę i wiem, że można i się da. Wystarczy tylko trochę dobrej woli.

Jeżeli jesteś managerem, bądź takim człowiekiem za którym inni będą chcieli pójść. Jeżeli testujesz albo wytwarzasz oprogramowanie to pomagaj swoim kolegom, ubogacaj ich i cierpliwie tłumacz podczas code review dlaczego takie a nie inne rozwiązanie jest odpowiednie. Jeżeli natomiast jesteś coachem, to w Twoją rolę jest wpisane takie zachowanie i powinno należeć to do Twoich obowiązków służbowych. Pamiętaj: spędzasz z kolegami z pracy 1/3 doby. Wszyscy wspólnie budujemy atmosferę w projekcie, który stanowi bardzo istotną część naszego dnia. To w jaki sposób się między sobą komunikujemy bezpośrednio przekłada się na jakość naszego produktu ale przede wszystkim na satysfakcję i przyjemność z pracy.

Team technical skills
---------------------

Czasami niestety dobra wola nie wystarcza. Czasami brak doświadczenia daje we znaki i projekt mimo iż dobrze się zapowiadał zaczyna być, tym "kroczącym ku klęsce". Ten brak doświadczenia i umiejętności jest charakterystyczny dla młodych firm, których nie stać na zatrudnienie wysoko się ceniących specjalistów.

Firmy tego typu nie są jednak skazane na niepowodzenie. Wręcz przeciwnie: mają ogromny potencjał innowacji, która dobrze ukierunkowana i wyegzekwowana z należytą starannością może urosnąć w niebotyczne przedsięwzięcie przerastające swym ogromem nawet najśmielsze wyobrażenia założycieli. Pamiętaj, że takie potęgi jak Google, Microsoft, Amazon, Apple ale również i te nie związane z IT jak Boeing, Lockheed Martin, Wall Mart też zaczynały od niewielkich, niedoświadczonych przedsięwzięć. Dobre sterowanie, odpowiedni ludzie i trafione decyzje spowodowały, że dziś możemy tylko pozazdrościć ich potędze.

Umiejętności techniczne są ważne prawie tak ważne jak umiejętność pojawienia się z właściwym produktem we właściwym czasie. Umiejętności techniczne w firmach informatycznych są podstawową, integralną i nierozerwalną częścią egzystencji firm.

Jest powiedzenie: "jest jedna gorsza rzecz od pracownika, któremu zapłaciliśmy za szkolenie i od nas odszedł, taki którego na szkolenie nie wysłaliśmy i z nami został". Inwestycja w ludzi jest dobra i chyba nie muszę nikogo do tego przekonywać, jednakże zdarza się, iż managerowie przewrażliwieni na tym punkcie podejmują złe decyzje nierzadko skutkujące obniżeniem morale i zadowolenia z pracy wszystkich osób pracujących przy projekcie.

Technical debt analysis
-----------------------

Z pozoru wydaje się, że nasze oprogramowanie go nie posiada. To projekty innych ludzi są narażone na dług techniczny. To inni mają z tym problem nie ja… Tak niewiele potrzeba aby się przekonać, że ten problem dotyczy nawet naszego kodu i projektu. Zwykle przez brak pokory tkwimy w fałszywym przekonaniu.

Narzędzia, które pozwolą nam przeanalizować nasze oprogramowanie pod kątem występowania, a raczej określania wielkości długu technicznego są darmowe i dostępne od zaraz dla wszystkich popularnych języków programowania. W celu przybliżenia metod statycznej analizy kodu oraz liczenia długu zapraszam do kolejnych rozdziałów książki związanych z narzędziami developerskimi takimi jak SonarQube, Checkstyle, PMD i Findbugs.

Scrum/Kanban implementation maturity
------------------------------------

Ileż to razy miałem doczynienia z zespołami, które twierdziły, że ich proces jest w pełni dojrzały, że robią SCRUMa, a problem leży gdzieś indziej...
