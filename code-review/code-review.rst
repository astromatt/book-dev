Code Review
===========


Rationale
---------
* Systemy do Code Review, ich wady i zalety
* Code Review blokujące, nieblokujące i post-factum
* Unified diff vs side-by-side
* Komentarze: co komentować, jak politycznie komunikować problem
* Feed-forward a nie feedback
* Taski: blokowanie zmian
* Commit zmieniający linię, gdzie był komentarz, w wielu systemach powoduje ukrycie komentarza, bo jest to traktowane jako rozwiązanie dyskusji
* Liczba linii w Code Review
* Pair programming vs Code Review
* Dobre praktyki Code Review
* Code Review robiony zdalnie, gdzie autor prezentuje zmiany, a ludzie mogą się podpytać jest najskuteczniejszy w przekazywaniu informacji i budowaniu wiedzy zespołu
* Czy cały kod musi być poddawany Code Review?
* Kogo zapraszać do Code Review?
* Normalnie nie zapraszamy Frontendowców i mobilnych, chyba że zmiana dotyczy API dla nich
* Code review default reviewers problem
* Skuteczność notyfikacji, ale tylko wtedy, kiedy ktoś nie jest zalewany bo należy default reviewer
* Czy Product Owner powinien być w Code Review?
* Co oznacza akceptacja Code Review?
* Czytelność wyrażeń regularnych

>>> scheme = r'(?:(?<scheme>[^:/?#]+):)?'
>>> authority = r'(?://(?<authority>[^/?#]*))?'
>>> path = r'(?<path>[^?#]*)'
>>> query = r'(?:\?(?<query>[^#]*))?'
>>> fragment = r'(?:#(?<fragment>.*))?'
>>>
>>> pattern = f'^(?=[^&]){scheme}{authority}{path}{query}{fragment}'
>>>
>>> print(pattern)
^(?=[^&])(?:(?<scheme>[^:/?#]+):)?(?://(?<authority>[^/?#]*))?(?<path>[^?#]*)(?:\?(?<query>[^#]*))?(?:#(?<fragment>.*))?


Pair Programming
----------------
* Pair Programming to Code Review prowadzone w realtime
* Code with Me
* Zabrać ze sobą notatnik, pisać temat dyskusji i numer linii i nazwę pliku / klasy / metody
* Nie stosować Pair Programming by default (nawet do prostych rzeczy)
* Zostawić to tylko trudnych miejsc w kodzie i problemów o dużym impakcie
* Stratą dla firmy jest jak dwóch koderów siedzi i dobiera kolorki i odcienie tekstu w HTML


Use Cases
---------
* CR dla IaaS
* CR dla programów szkoleń
* CR dla książki astro
