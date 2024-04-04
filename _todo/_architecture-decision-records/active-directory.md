Active Directory
================


Połączenie
----------
1. Do uwierzytelniania użytkowników korzystać tylko i wyłącznie z Active
   Directory
2. Połączenie do Active Directory wyłącznie za pomocą szyfrowanej wersji
   protokołu LDAP
3. Każde narzędzie ekosystemu musi mieć osobne konto tylko do odczytu danych z LDAPS

* gdyby hasło wypłynęło łatwo zmienić lub zablokować konto i stworzyć nowe w jednym narzędziu
* gdyby korzystać z tego samego konta w wielu narzędziach, to byłby to spory problem
* Jedna z dużych firm farmaceutycznych tak miała, jak hasło do LDAP ktoś
  "svn commit" na SourceForge (kilkanaście lat temu)
* Wszystkie aplikacje pisane przez ostatnie 10 lat trzeba było przerobić
  (a do niektórych już kompilatorów nie było)
* W dzisiejszych czasach obowiązywania przepisów RODO rozpłynięcie się hasła
  umożliwiającego odczyt danych osobistych użytkowników...


Użytkownicy
-----------
1. W narzędziu powinno być tylko jedno konto lokalne `jira-administrator`,
   które służy do konfiguracji połączenia z Active Directory
2. Zarówno wewnętrzni, jak i zewnętrzni użytkownicy (kontraktorzy, body
   leasing) powinni mieć konta w tym samym Active Directory
3. Użytkownicy wewnętrzni powinni być w Active Directory w osobnym `OU=users-internal`
4. Użytkownicy zewnętrzni powinni być w Active Directory w osobnym `OU=users-external`

* Gdy osoba odchodzi z pracy można zablokować konto w jednym miejscu
* Gdyby coś z użytkownikiem było nie tak, łatwo można sprawdzić, do czego
  ma i powinien mieć dostęp
* Zapytanie do LDAP wyciągające użytkowników z tych dwóch grup nie jest trudne
* Wyszukać po typie `sAMAcount` lub `userAccountControl` oraz w odpowiednim OU.

```ActiveDirectory
(&
    (objectCategory=Person)
    (objectCategory=User)
    (userAccountControl=512)
)
```


Grupy
-----
1. Grupy dostępu do narzędzia powinny nazywać się `jira-access` i `jira-administrators`
2. Każe narzędzie w ekosystemie ma swoje dwie grupy w Active Directory
3. Wszystkie narzędzia mają osobne grupy w Active Directory
4. Przynależność do `jira-administrators` nie skutkuje automatycznie
   posiadaniem dostępu do narzędzia lub/i projektów
5. Nie korzystać z zagnieżdżonych grup w AD - na początku może się to wydać
   fajne i łatwe, ale później przy wyjątkach trudne utrzymaniu)
6. Aby użytkownik dostał dostęp do narzędzia, musi mieć nadaną grupę
   `jira-access` w Active Directory
7. Grupa `jira-access` powinna znajdować się w `OU=ecosystem`
8. Do nadawania uprawnień do projektów stosować tylko grupy projektowe z
   Active Directory z `OU=projects`
9. Nie używać grup z Jiry do przydzielania uprawnień dostępowych do narzędzi
   ani projektów

* Dzięki temu łatwo wylistować, do jakich narzędzi i projektów człowiek ma dostęp
* W przypadku zwolnienia w jednym miejscu blokujemy wszystko
* W przypadku przejścia od nowego projektu łatwo nadać uprawnienia do
  wszystkiego, co osoby w danym projekcie robią
* W przypadku odejścia z projektu jednym ruchem można zabrać danej osobie
  uprawnienia w projekcie
* Osobne grupy dla narzędzi są zbawienne dla podczas np. audytu
* Wtedy konieczne jest nadanie np. audytorowi dostępu o Jiry do projektu
  ABC tylko jako użytkownik bez uprawnień admina systemu lub projektu


Domena
------
1. Maile z Jiry powinny wychodzić z konta `jira@example.com` (ułatwi to tworzenie filtrów i reguł)
2. Jira powinna być wystawiona na domenie `jira.example.com`
3. Dostęp do `jira.example.com` powinien być wycięty dla użytkowników ze świata
   za pomocą firewall (wpuszczać tylko z VPN)
4. Jira powinna korzystać z aktualnego i potwierdzonego certyfikatu wildcard
   SSL wystawionego na `*.example.com`
5. Dostęp do Jiry tylko przy użyciu HTTPS
6. Protokół DHCP powinien konfigurować search example.com w `/etc/resolv.conf`
   (opcja się nazywa Search Domains i dużo osób o niej nie wie, pozwala
   w przeglądarce wpisać tylko "jira" a system operacyjny sam dopełni example.com)

* Należy zwrócić uwagę, że nazwy domen są tożsame z emailem oraz grupami
  ostępowymi dla w Active Directory
* To znaczy, że dla jira.example.com zakładamy jira@example.com oraz grupy
  jira-access, jira-administrators ora jedno konto lokalne jira-administrator
* To znaczy, że dla todo.example.com zakładamy todo@example.com oraz grupy
  todo-access, todo-administrators ora jedno konto lokalne todo-administrator
* Ta konwencja powinna dotyczyć wszystkich systemów ekosystemu narzędziowego,
  nie tylko Jiry


Automatyzacja
-------------
1. Na Confluence stworzyć space o nazwie "Narzędzia Developerskie" (DEVTOOLS)
   lub Ekosystem narzędzi developerskich (ECO)
2. Za pomocą Atlassian Python API i crontab cyklicznie tworzyć/aktualizować
   stronę "Jira Administrators"
3. Na stronie powinni być wypisani wszyscy administratorzy Jiry
4. Strona jest aktualizowana codziennie o północy (Confluence trzyma diffy
   i wysyła powiadomienia do adminów, jak ktoś zostanie dopisany)
5. Strona na Confluence "Jira Project Leaders" z listą wszystkich liderów
   projektów (oraz osób, które mają administratora w projekcie)
6. Strona "Jira Project Leaders" ma spis projektów, ich liderów/adminów
   oraz linki mailto: do kontaktu z nimi
7. Linki mailto: mają możliwość przedefiniowania tytułu i treści ?title=...&body=...

* Atlassian Python API: https://github.com/atlassian-api/atlassian-python-api
* Dzięki "Jira Project Leaders" ludzie sami się zaczną obsługiwać
* Strony "Jira Project Leaders" oraz "Jira Administrators" powinny tworzyć,
  aktualizować codziennie o północy
* Osobny skrypt powinien codzienni sprawdzać Jirę, czy w którymś projekcie ktoś
  nie dostał ręcznie dopisany i usuwać
* Dzięki temu nie blokujemy komuś wystartowania z pracą (może zostać dopisany w
  dowolnym momencie)
* Mamy również porządek, bo wymusi to poprawne dodawanie użytkowników do
  odpowiednich grup w AD


Pluginy
-------
1. Bardzo restrykcyjnie podchodzić do instalacji pluginów do Jiry - jak się coś da użytkownikom, to ciężko później zabrać
2. Uwaga na darmowe pluginy, są często słabo, bądź wcale nie aktualizowane jak wyjdzie nowa Jira
