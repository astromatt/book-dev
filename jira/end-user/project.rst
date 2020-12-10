*******
Project
*******


Rationale
=========
- Project Lead
- Categories

    - Department
    - Team
    - Project
    - Product

- Project vs. Boards
- Issue Collector


Issue key
=========
- krótki i zwięzły
- łatwy do zapamiętania
- 2-10 liter


Project Configuration
=====================
- Versions
- Components
- Users and Roles
- Application Links


Versions
========
* Semantic Versioning: major.minor.bugfix - (1.2.3, 3.9.1)
* Konwencja nazewnicza YYYY-MM (2000-01, 2000-02, 2000-03)
* Konwencja nazewnicza YYYY-QX - (2000-Q1, 2000-Q2, 2000-Q3, 2000-Q4)
* Konwencja nazewnicza YYYY - (2000, 2001, 2002, 2003)
* Roadmap
* Releases (with Bamboo)
* Time Tracking Report by Version


AffectsVersion vs FixVersion
============================
Affects Version/s:

    * MyApp 1.0 (assume this is unsupported)
    * MyApp 2.0
    * MyApp 3.0

Fix Version/s:

    * MyApp 2.0.1
    * MyApp 3.0.5


Assignments
===========


Project Details
---------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` -> `Project Settings` (przycisk koła zębatego w menu na dole po lewej)
#. Zakładka `Details` -> zmień awatar swojego projektu na rakietę
#. Zakładka `Details` -> zmień nazwę swojego projektu na `Imię N.` (z kropką na końcu)

Project Components
------------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` -> `Project Settings` (przycisk koła zębatego w menu na dole po lewej)
#. Przejdź na zakładkę `Components`
#. Dodaj: `Frontend`, `Backend`, `Database`
#. Aby przycisk `Add` stał się aktywny musisz:
    * dodać komponent należy wpisać jego nazwę (w polu po lewej)
    * z ostatniej listy rozwijanej (po prawej przy zaraz koło przycisku add) wybrać jedną z opcji np. `Unassigned`

Project Versions
----------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` -> `Project Settings` (przycisk koła zębatego w menu na dole po lewej)
#. Przejdź na zakładkę `Versions`
#. Dodając wersje w tym zadaniu nie musisz ustawiać dat rozpoczęcia i zakończenia
#. Możesz dodać wersje z dzisiejszą datą, ale dla uproszczenia w zadaniach, a później w JQL i filtrach będę stosował konwencję z rokiem `2000`
#. Dodaj: `2000-07`, `2000-08`, `2000-09`, `2000-10`, `2000-11`, `2000-12`
#. Dodaj: `2001-Q1`, `2001-Q2`, `2001-Q3`, `2001-Q4`
#. Dodaj: `2002`, `2003`, `2004`

Project Roles
-------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` -> `Project Settings` (przycisk koła zębatego w menu na dole po lewej)
#. Przejdź na zakładkę `Users and roles`
#. Dodaj siebie do roli `Administrators`
#. Dodaj użytkownika `admin` do roli `Developers`

Project Fields
--------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` -> `Project Settings` (przycisk koła zębatego w menu na dole po lewej)
#. Przejdź na zakładkę `Issue Types`:
#. Wybierz `Task` -> przycisk `Fields` (górny prawy róg) -> dodaj pole `Due Date`, usuń pole `Labels`
#. Wybierz `Story` -> przycisk `Fields` (górny prawy róg) -> dodaj nową zakładkę `Estimate` , dodaj na niej pole `Time Tracking` oraz `Story Points`; pasek z zakładkami jest u góry tam gdzie jest `Field Tab` i ikonka ołówka; dodaje się poprzez kliknięcie na znak `(+)`
#. Zwróć uwagę, że ta zakładka pojawiła się w prawie każdym `Issue Type` (poza `Bug`)
