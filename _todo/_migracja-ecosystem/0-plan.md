Plan działania
==============


Plan Migracji
-------------
1. Backup bazy danych i katalogów domowych aplikacji JIRA i Bitbucket
2. Rsync bazy danuych i katalogów domowych aplikacji JIRA i Bitbucket
3. Przeniesienie konfiguracji nginx
4. Uruchomienie Jiry, Bitbucket i nginx na serwerze docelowym
5. Poprawki w dokumentacji (jeżli potrzeba)
6. Jeżeli wszystko działa, to wyłączenie kontenerów na hoście w cloud
   - jira, jiradb
   - bitbucket, bitbucketdb
7. Ustalić termin finalnego wyłączenia Jira i Bitbucket w sieci wewnętrznej
8. Komunikacja do ludzi o planach migracji
9. Jak nadejdzie termin, wyłączamy jira.example.com oraz bitbucket.example.com
10. Wykonujemy procedurę rsync (ponownie) z flagą ``--delete``
11. Włączamy jira.cloud.example.com praz bitbucket.cloud.example.com
12. Ustawiamy redirect (albo na DNS albo w Nginx):
    - z jira.example.com na jira.cloud.example.com
    - z bitbucket.example.com na bitbucket.cloud.example.com
13. Stara Jira oraz Bitbucket są backupowane i już więcej nikt jej nie podnosi (bo będzie desynchronizacja, tzn. część osób wprowadzi zmiany w starej, część w nowej) próba scalenia jest bardzo czasochłonna i ogólnie się nie opłaca


Podsumowanie wykonanych czynności
---------------------------------
Słowniczek:
- internal: serwer na którym są obecnie: jira.example.com oraz bitbucket.example.com
- cloud: serwer docelowy na którym będą jira.cloud.example.com oraz bitbucket.cloud.example.com


Executive summary:
- Jira i Bitbucket są gotowe do migracji
- Rsync najbezpieczniej robić na wyłączonych kontenerach po obu stronach (internal i cloud)
- Ważne: Po zrobieniu rsync, a przed uruchomieniem kontenerów trzeba zrobić chown
- Jira i Bitbucket internal nie mają dokumentacji, więc uwaga z wyłączaniem (natomiast powinno to być analogiczne co w mojej dokumentacji)
- Pilne i łatwe: migracja bazy danych Bitbucket z h2 do Postgres
- Pilne i trudne: wywalenie wszystkich kont z Jira Internal Directory

1. Jira jest posprzątana:
   - Pluginy
   - Nieużywane projekty
   - Licencja
   - Grupy w Jira Internal Directory
   - Permissions Schemes
   - Workflows i Workflow Schemes
   - Priorities
   - Boardy

2. Zostało do posprzątania:

a) można by scalić dwa permission scheme w jeden
https://jira.example.com/secure/admin/ViewPermissionSchemes.jspa
Nie zrobiłem tego, bo Jira dla projektów nie software zawsze będzie zakładać Default Permission Scheme a dla projektów Software - Default software scheme. Teraz macie przynajmniej dobrze skonfigurowane. Atlassian ostatnimi czasy bardzo dużo kombinuje w tych sprawach, to się czasami dużo zmienia z miesiąca na miesiąc

b) Jest kilka Custom Field, które można usunąć:
https://jira.example.com/secure/admin/ViewCustomFields.jspa
Natomiast to wymaga poświęcenia trochę czasu aby poszukać jakie dane w nich są trzymane i czy ktoś je potrzebuje
Te, które nie budziły wątpliwości usunąłem, ale zostały najtrudniejsze.

c) Można trochę zmniejszyć ilość Statusów:
https://jira.example.com/secure/admin/ViewStatuses.jspa
Może ingerować w validators, conditions albo postfunction w Workflow.

d) Rola tester
https://jira.example.com/secure/project/ViewProjectRoles.jspa
Może ingerować w validators, conditions albo postfunction w Workflow.

e) Workflow Schemes i Workflow
https://jira.example.com/secure/admin/ViewWorkflowSchemes.jspa
https://jira.example.com/secure/admin/workflows/ListWorkflows.jspa

I tu jest największy problem. Są projekty, które korzystają z własnego workflow.
Te workflow mogą zawierać różne validators, conditions albo postfunction i inne reguły.
Usunięcie roli projektowej Tester (która raczej nie powinna być potrzebna w Jirze) może spowodować, że w niektórych workflow coś przestanie działać. Pozostałe projekty są bardzo proste, każda osoba która ma uprawnienia w projekcie może zmieniać na dowolny status. Proste łatwe i nie wymaga zastanawiania się. Natomiast w wymienionych projektach są specjalne reguły i jak ruszymy np. niektóre statusy, rolę to trzeba prześledzić wszystkie tranzycje czy np. da się je wykonać (gdyby był w Conditions, że tylko tester może np. wyjąć zadanie ze statusu In Test). Natomiast jakich przejść jest kilkadziesiąć i dla każdego trzeba przeglądnąć: Properties, Triggers, Conditions, Validators i Post Functions. Kupa czasu, a jak coś przeoczysz, bo źle klikniesz strzałkę na obrazku to wszystko od nowa.

f) Konta z Jira Internal Direcotry (wywalić wszystkie poza jira-administrator)
Aby to zrobić trzeba w bazie danych zrobić UPDATE i przepisać wszystkie akcje (komentarze, zakładane zadania, logowanie pracy, logi itp) osób na ich odpowiedniki w AD. To się da zrobić, ale jest to żmudne i łatwo się pomylić. Natomiast bez tego Jira nie pozwoli skasować kont.


Jako, że te osoby nie pracują u nas w firmie, to mają stworzone konta w AD, ale w innym OU niż to, które jest synchronizowane do Jiry dla pracowników (tak admini to wymyślili). Z tego powodu, aby nadać im dostęp trzeba było albo zmienić konfigurację LDAP w Jirze (nie było na to zielonego światła) lub stworzyć ich konta w tzw. Jira Internal Directory. Została zrobiona ta druga opcja, ale to nie jest dobre na przyszłość rozwiązanie.

Nad kontami w Jira Internal Directory zespół Helpdesk nie ma kontroli (np. nie może im resetować hasła). Ale jest większy problem. Jak te osoby przestaną móc mieć dostęp do Jiry (np. zerwiemy z nimi umowę, lub wygaśnie), to trzeba będzie pamiętać aby im ręcznie zabrać uprawnienia w Jirze!! Uwaga, samo zgłoszenie do Helpdesk wtedy nie wystarczy, bo helpdesk zrobi to tylko w AD a do administracji Jirą nie ma dostępu! Jak o tym się zapomni to otworzy lukę bezpieczeństwa/prawną.  Jak zwykle z Jirą, tematy nie są trudne i jak się wie jak zrobić to można szybko wykonać. Natomiast impakt decyzji i zmian jest bardzo duży.

Te cztery konta są obecnie jedynymi takimi, z którymi mamy powyższy problem.  Nie pozwolono mi zmieniać tych rzeczy na bazie danych i dlatego to jest niezrobione.

3. Wpisy w DNSie dla jira.cloud.example.com oraz bitbucket.cloud.example.com wskazują na adresy prywatne maszyn w cloud. Dzięki czemu rozwiązywanie nazw oraz nawiązywanie połączenia jest błyskawiczne. Wcześniej był problem z adresami publicznymi, ale zostało to rozwiązane.

4. Na  chwilę obecną można połączyć się po SSH do:
- jira.example.com
- jira.cloud.example.com
- pomiędzy jira.example.com i jira.cloud.example.com

Była chwila gdzie to zrobili, następnie nie działało a dzień później to zrobili. To było w momencie jak zgłaszałem porty na firewallu. Na chwilę obecną wszystko działa.

5. Rsync między jira.example.com a jira.cloud.example.com działa bez problemów.

6. Rsync można robić na stojących i działających instancjach po obu stronach, tj. jira.example.com i jira.cloud.example.com, ale... Nigdy nie wiadomo co może się stać (indeksowanie, cache, crony itp) i coś może się wysypać.

Rsynców katalogów domowych Postgresa bez kładzenia kontenerów w cloud bym nie próbował. Bazy danych generalnie trzymają dużo rzeczy w pamięci i do pliku zapisują rzadziej. Jeżeli trafi się na taką sytuację to można stracić spójność danych. Podmienianie im plików w locie może (ale nie musi) skończyć się źle. Natomiast nie warto, bo położenie kontenera rsync i uruchomienie to dwie minuty, a prawdopodobieństwo zniszczenia danych znacznie mniejsze.

Najbezpieczniej jest:
- położyć instancje w cloud (docker stop jira jiradb),
- usunąć je (docker rm jira jiradb)
- a następnie zrobić rsync i podnieść poleceniami z dokumentacji (odnośniki poniżej)

Wielokrotnie testowałem rsync z działającą Jirą oraz Bitbucket na jira.example.com oraz położonymi instancjami w Cloud i nigdy nie było problemu. Najbezpieczniej jest jednak zawsze położyć instancje po obu stronach (internal oraz w cloud) zarówno bazy danych jak i aplikacji, a dopiero później robić rsync. Wtedy prawdopodobieństwo błędów jest najmniejsze

7. Ale chciałbym zwrócić uwagę na:
- Obecna instalacja jira.example.com i bitbucket.example.com nie ma dokumentacji
- To powoduje, że w sumie to nie ma nigdzie zapisanego jednego polecenia jak uruchomić kontener
- Przed położeniem, a już napewno przed docker rm trzeba prześledzić opcje konfiguracyjne docker inspect i przygotować polecenie docker do postawienia kontenera
- Zarówno kontenery dla Bitbucket jak i Jira obecnie nie mają flagi restart=always więc gdyby padł prąd, host się zrestartował... to byłoby szukanie w logach jak to podnieść... niefajnie
- Uruchamianie kontenerów powinno być analogiczne do tych z mojej dokumentacji (tylko trzeba podmienić na named volumes, z których korzysta jira i bitbucket na hoście na maszynie internal)

8. Ważne! Pamiętajcie proszę, aby po rsync, a przed uruchomieniem kontenerów (jira, jiradb, bitbucket, bitbucketdb) zmienić uprawnienia:
- chown -R 999:999 /home/bitbucket/database
- chown -R 2003:2003 /home/bitbucket/home
- chown -R 2001:2001 /home/jira/home

To jest wpisane w dokumentacji. Jak tego nie zrobicie, to procesy nie będą mogły zapisywać danych. Trzeba zmieniać uprawnienia, bo rsync synchronizuje pliki jako root. Każdy z kontenerów działa z userem, który ma inny UID. Odpowiedników tych userów nie ma w systemie Docker0 (czyli na jira.cloud.example.com).

9. Dlaczego nie named volumeny na hoście w Cloud (bo rozmawialiśmy o tym)
- Wszystko jest w jednym miejscu: dane aplikacji, dane bazy danych, skrypty startowe, toole i dokumentacja
- W katalogach w home stworzyłem skrypty startowe do uruchamiania Jiry, Bitbucket i ich baz danych, np. /home/jira/run-jira.sh
- Rsync jest dużo łatwiejszy jak wszystko jest w jednym miejscu i nie trzeba szukać gdzie to jest
- Backup jest dużo łatwiejszy jak wszystko jest w jednym miejscu i nie trzeba szukać gdzie to jest
- Przywracanie z backup jest dużo łatwiejsze jak wszystko jest w jednym miejscu i nie trzeba szukać gdzie to jest
- Gdybyście jednak chcieli przejść na named volumes, to bardzo łatwo można to zrobić (przy pierwszym uruchomieniu podmontować zarówno named volume jak i katalog, skopiować dane, a później już nie montować katalogu)

10. Wymagająca poświęcenia chwili jest sytuacja z Bitbucket, gdzie baza danych jest w h2. Samo przeniesienie tego do Postgres to kwestia kilku minut (Bitbucket ma wbudowany migrator https://bitbucket.example.com/admin/db). Dwukrotnie testowałem migrację bazy z h2 do Postgresa i nie było żadnych problemów. Ale nigdy nie było na to zielonego światła aby zrobić to na "produkcji".

11. Certyfikaty do HTTPS. Obecnie jest self signed i są to te same certyfikaty co dla jira.example.com i bitbucket.example.com. Natomiast docelowo powinny to być certyfikaty wystawione dla tych hostów. Przed wystawieniem certyfikatów trzeba przemyśleć nazwy domen. Czy iść w łatwiejsze dla ludzi jira.example.com (tylko zmienić w DNS aby wskazywało na cloud) czy skorzystać z jira.cloud.example.com. Na wygenerowanie certyfikatu jest zlecenie
