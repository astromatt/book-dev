***
GIT
***

.. warning:: There's much more information at my slides https://www.slideshare.net/astrotech/git-training-course Those slides will be converted to the book format with time.


Wprowadzenie
============
* :cite:`GITDocumentation`

Opis dostępnych darmowych klientów gita
---------------------------------------

Podstawy git
============
- konfiguracja nazwy użytkownika, adresu e-mail i parametr autocrlf
- rozróżnienie konfiguracji globalnej i lokalnej
- zakładanie lokalnego repozytorium oraz jego wewnętrzna struktura

    * repozytorium bare
    * repozytorium normalne

- podstawowe operacje
- sprawdzenie statusu kopii roboczej
- obsługa git staging area (aka git index)
- zapisywanie zmian w repozytorium (commit)
- przeglądanie historii zmian w repozytorium
- ignorowanie zbędnych plików
- obsługa git diff (podgląd zmian wprowadzanych przez commit/commity oraz w kopii roboczej i staging area)
- obsługa git reset

Git Internals
-------------
#. Anatomia
#. jak git przechowuje informacje o wersjach
#. jak są one ze sobą powiązane
#. jak przechowywane są informacje o branchach i tagach,
#. co to są „referencje”)

Pojęcia zaawansowane
====================
- schowek – stash
- shelve
- moduły zależne -  submodule
- odnajdowanie „winnych” – blame
- ostatnia deska ratunku – reflog
- wyszukiwanie miejsca regresji – bisect
- cofanie pojedynczego commitu
- „zaawansowane” opcje konfiguracji
- pielęgnacja repozytorium – fsck, gc
- git fat i inne przydatne pluginy
- git hooks

Pozostałe
=========
git clean -f -d
git reset --hard HEAD
slajdy z .gitconfigiem

Przykłady praktyczne
====================
* https://learngitbranching.js.org

Jenkins + Git Bisect Run
------------------------

- plugin "Downstream-Ext"
- dodatkowy projekt "...-blame"
- email notyfikacje
- Build other projects (extended) -> Build result is FAILURE

.. code-block:: console

    $ git bisect start @                                # startujemy git bisect z obecnym commitem jako bad
    $ git bisect good `git rev-list --max-parents=0 @`  # dobry commit - początek repo, można przekazać inny commit żeby nie zaczynać zawsze od początku
    $ git bisect run ./test.sh                          # zestaw testów gdzie exit code > 0 oznacza bad commit
    $ git log --format="%ae"                            # wylistowanie emaila osoby która wprowadziła buga
    $ git bisect reset																	# zakończenie pracy z bisectem

Zadania praktyczne
==================

Praca na commitach
------------------
- inicializacja oraz sprawdzenie statusu repozytorium
- dodawanie oraz commitowanie zmian
- ignorowanie plików oraz katalogów
- resetowanie stanu repozytorium
- obsługa branch'y
- co to jest master, HEAD, HEAD~1, HEAD^1
- tworzenie, usuwanie oraz przełączanie między branchami
- rozróżnienie branchy lokalnych, lokalnych-zdalnych oraz zdalnych
- tworzenie branchy „śledzących” (tracking branches)
- co to jest 'detached HEAD'
- operacje merge, rebase, cherry-pick
- rozwiązywanie konfliktów
- edycja commitów (edycja commit message, łączenie commitów)

Manipulacja branchami
---------------------
- przeprowadzenie operacji merge (fast-forward i non fast-forward), rebase, cherry pick + rozwiązywanie konfliktów
- tworzenie branchy
- praca ze zdalnym repozytorium
- operacje clone, push, fetch, pull
- czym różni się fetch od pull
- tworzenie oraz usuwanie zdalnych branchy

Zarządanie remote
-----------------
- tworzenie oraz usuwanie zdalnych branchy
- pushowanie zmian
- pobieranie zmian

Submoduły
---------
#. Jako submoduł dodaj `Reveal.JS <https://github.com/hakimel/reveal.js>`_
#. Zainicjalizuj go
#. Zaciągnij najnowsze informacje

Hook: Pre-Commit - commit message
---------------------------------
Stwórz hook aby wymuszał w nazwie commita ID issues z Jiry

Hook: Pre-Commit - branche
--------------------------
Stwórz hook aby do commit message dodawał ID z nazwy brancha

Hook: Pre-Commit - Testy
------------------------
Stwórz hook aby przy każdym commicie uruchamiał testy dla `HabitatOS <https://github.com/AstroMatt/HabitatOS>`_

Hook: Post Commit
-----------------
Wyślij majla podsumowującego commita

Hook: Pre-Receive
-----------------
Zablokuj otrzymywanie danych, jeżeli w commit message nie znajduje się issue z Jiry

Subtree
-------
#. Jako subtree dodaj `Reveal.JS <https://github.com/hakimel/reveal.js>`_
#. Zainicjalizuj go
#. Zaciągnij najnowsze informacje
#. Wypushuj go do jako branch w swoim repozytorium
#. Zaktualizuj plik zdalnie
#. Zaciągnij lokalnie zmiany

fsck and gc
-----------
Przeprowadź pełne ``git fsck --full`` na repozytorium, a następnie uruchom ``git gc --aggressive --prune=now``


More information
================
.. warning:: There's much more information at my slides https://www.slideshare.net/astrotech/git-training-course Those slides will be converted to the book format with time.
