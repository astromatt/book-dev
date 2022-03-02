Dragon (version beta)
=====================


About
-----
* Assignment: Dragon (version beta)
* Complexity: medium
* Lines of code: 120 lines
* Time: 60 min (±10 min), then 30 min live coding with instructor
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn


English
-------
.. todo:: English Translation


Polish
------
1. Zmodyfikuj smoka z pierwszej części
2. Smok nie może wyjść poza obszar ekranu (1024x768)
3. Jeżeli dojdzie do granicy ekranu, to przesuwając dalej, pozycja będzie ustawiona na maks
4. Zmień smokowi punkty życia na losowy ``int`` z zakresu 100 do 150
5. Stwórz bohatera "Pan Twardowski":

    a. losowe punkty życia (200-250)
    b. zadaje losowe obrażenia (1-15)
    c. klasa postaci (domyślnie "Warrior")
    d. Bohater może przyjmować obrażenia
    e. Bohater może zginąć
    f. Bohater może poruszać się po planszy

6. Wszystkie istoty mają statusy:

    a. "Full Health" - gdy punkty życia 100% (zastąp status "alive")
    b. "Injured" - gdy punkty życia 99% - 75%
    c. "Badly Wounded" - gdy punkty życia 74% - 25%
    d. "Near Death" - gdy punkty życia 24% - 1%
    e. "Dead" - gdy punkty życia poniżej lub równe 0%

7. Bohater przejmuje złoto smoka, jeżeli go zabije
8. Przeprowadź walkę, tak długo aż ktoś pierwszy nie zginie
9. Wymagania niefunkcjonalne:
    a. Zadanie jest symulacją procesu developmentu
    b. Trener zachowuje się jak Product Owner z niewielką techniczną wiedzą
    c. Ty jesteś inżynierem oprogramowania, który musi podejmować decyzje
       i ponosić ich konsekwencje
    d. Zadanie jest tylko narracją do demonstracji OOP i dobrych
       praktyk programowania
    e. Wyliczona pozycja Smoka na końcu gry powinna być x=20, y=40
    f. Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne, stałe,
       klasy, obiekty, co tylko chcesz
    g. Nie korzystaj z modułów spoza standardowej biblioteki Pythona
    h. Zadanie jest specyfikacją wymagań biznesowych, a nie dokumentacją
       techniczną, tj. "co Smok ma robić, a nie jak to ma robić"
    i. Nie musisz trzymać się kolejności punktów i podpunktów w zadaniu
    j. Jest to wersja `alpha` więc bez dodatkowych funkcjonalności
       (np. sprawdzanie koordynatów, wychodzenia poza planszę itp.)
    k. Możesz stworzyć testy, np. unittest lub doctest
    l. Nie przeglądaj rozwiązań ani treści kolejnych części zadania;
       jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę i naukę


Solution
--------
* EN: Note, that this will spoil your fun and learning
* PL: Zwróć uwagę, że to zepsuje Twoją zabawę i naukę
* :download:`Architecture Decision Records <assignments/dragon_api_adr.py>`
* :download:`Solution <assignments/dragon_beta.py>`
