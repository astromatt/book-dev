***********
Board Usage
***********


Rationale
=========

Manifesto for Agile Software Development
----------------------------------------
We are uncovering better ways of developing
software by doing it and helping others do it.
Through this work we have come to value:

- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan

That is, while there is value in the items on
the right, we value the items on the left more.

Source: [#agilemanifesto]_

Principles behind the Agile Manifesto
-------------------------------------
We follow these principles:

- Our highest priority is to satisfy the customer through early and continuous delivery of valuable software.

- Welcome changing requirements, even late in development. Agile processes harness change for the customer's competitive advantage.

- Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale.

- Business people and developers must work together daily throughout the project.

- Build projects around motivated individuals. Give them the environment and support they need, and trust them to get the job done.

- The most efficient and effective method of conveying information to and within a development team is face-to-face conversation.

- Working software is the primary measure of progress.

- Agile processes promote sustainable development. The sponsors, developers, and users should be able to maintain a constant pace indefinitely.

- Continuous attention to technical excellence and good design enhances agility.

- Simplicity--the art of maximizing the amount of work not done--is essential.

- The best architectures, requirements, and designs emerge from self-organizing teams.

- At regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly.

Source: [#agilemanifestoprinciples]_

Scrum
-----
Scrum is a lightweight framework that helps people, teams and organizations generate value through adaptive solutions for complex problems.

In a nutshell, Scrum requires a Scrum Master to foster an environment where:

1. A Product Owner orders the work for a complex problem into a Product Backlog.

2. The Scrum Team turns a selection of the work into an Increment of value during a Sprint.

3. The Scrum Team and its stakeholders inspect the results and adjust for the next Sprint.

4. Repeat

Scrum is simple. Try it as is and determine if its philosophy, theory, and structure help to achieve goals and create value. The Scrum framework is purposefully incomplete, only defining the parts required to implement Scrum theory. Scrum is built upon by the collective intelligence of the people using it. Rather than provide people with detailed instructions, the rules of Scrum guide their relationships and interactions.

Various processes, techniques and methods can be employed within the framework. Scrum wraps around existing practices or renders them unnecessary. Scrum makes visible the relative efficacy of current management, environment, and work techniques, so that improvements can be made.

* https://scrumguides.org/download.html
* https://scrumguides.org/revisions.html

Source: [#scrumguide]_


Project Management
==================
- Kanban
- Scrum
- Scrum + Kanban
- Portfolio
- Scrum vs. Kanban

    - Scrum -> Rozwój (Story)
    - Kanban -> Utrzymanie (Task)
    - Praca w Scrum i Kanban jednocześnie
    - Konstytucja zespołu i dobre praktyki

.. figure:: ../_img/jira-board-select.jpg
.. figure:: ../_img/agility-bigpicture-simple.png
.. figure:: ../_img/agility-bigpicture-advanced.png
.. figure:: ../_img/scrum-sprint-week-continuous.png
.. figure:: ../_img/scrum-daily-timer.png
.. figure:: ../_img/scrum-userstory.png


Scrum
=====
- Backlog
- Sprintlog
- Task board

.. figure:: ../_img/jira-board-backlog-scrum.png
.. figure:: ../_img/jira-board-sprint.png


Epic
====
- Brak worków (np. Poprawki błędów)
- Doważalne (określone w czasie, mają datę początku i końca)
- Wymagalność:

    - `Due Date`
    - `Start Date`
    - `Assignee`

- Optymalna długość
- Kategoryzowanie
- Timeline i roadmapa
- Planowanie kwartalne
- Przypisywanie Epiców do wersji
- Board epików
- Business Value epików


Planning and Refinement
=======================
.. figure:: ../_img/agile-decomposition-01-mindmapping.jpg
.. figure:: ../_img/agile-decomposition-02-epics.jpg
.. figure:: ../_img/agile-decomposition-03-epic.jpg
.. figure:: ../_img/agile-decomposition-04-epics.jpg
.. figure:: ../_img/agile-decomposition-05-ordering.jpg
.. figure:: ../_img/agile-decomposition-06-ordered.jpg
.. figure:: ../_img/agile-decomposition-07-todecompose.jpg
.. figure:: ../_img/agile-decomposition-08-decomposition.jpg
.. figure:: ../_img/agile-decomposition-09-ordering.jpg
.. figure:: ../_img/agile-decomposition-10-ordered.jpg
.. figure:: ../_img/agile-decomposition-11-estimation-resample.png
.. figure:: ../_img/agile-decomposition-12-estimation.jpg
.. figure:: ../_img/agile-decomposition-13-priorities.jpg
.. figure:: ../_img/agile-decomposition-14-sprints.jpg
.. figure:: ../_img/agile-decomposition-15-issues.jpg
.. figure:: ../_img/agile-decomposition-16-jira.jpg
.. figure:: ../_img/agile-decomposition-17-epicmaping.jpg
.. figure:: ../_img/agile-decomposition-18-board.jpg
.. figure:: ../_img/agile-decomposition-19-risk.jpg
.. figure:: ../_img/agile-decomposition-20-portfolio.jpg


Sprints
=======
- Wielkość (ilość zadań, capacity chart)
- Sprint Goal
- Sprint Duration (week)
- Sprint Name (YYYY-MM week N):

    * 2000-01 week 1
    * 2000-01 week 2
    * 2000-01 week 3
    * 2000-01 week 4
    * 2000-02 week 1
    * 2000-02 week 2
    * 2000-02 week 3

..   figure:: ../_img/scrum-capacity-sprint.png


Active Sprint
=============
- Open and close sprint
- Flag issues
- Scope changes


Estimation
==========
- Time Estimate
- Manday
- Story Point
- Business Value
- ``#NoEstimates`` and Monte Carlo simulation:

    * https://www.infoq.com/presentations/monte-carlo
    * https://docs.google.com/spreadsheets/d/1BmSuj1jA2ZfhUBzPtqDBqDjMjSXMqj3QoHZGR-TesOA/edit#gid=542217325


Metrics
=======
- Velocity
- Capacity
- Maturity

.. figure:: ../_img/scrum-capacity-backlog.png


Planning and Refinement
=======================
- Estimation
- How big your tasks should be?
- Estimation support systems
- Sprint goal
- Acceptance Criteria
- Definition of Done
- Time Tracking


Roadmap
=======
.. figure:: ../_img/jira-board-roadmap.png


Kanban
======
- What’s Kanban?
- Pull system
- JIT
- Context switching
- Kanban Board
- Improvement:

    - Muda
    - Jidoka
    - Kaizen
    - Bottlenecks
    - Metrics
    - Lean

- Workflow:

    - Columns
    - Swimlanes
    - Expedite
    - Priority
    - SLA

.. figure:: ../_img/jira-board-backlog-kanban.png


Demonstration
=============
* Estimate issue
* Add sprint: set name, set duration, set start date
* Add issues to sprint
* Start sprint: set goal
* Active sprint: move issues, add flag, print cards (on paper)
* Close sprint: drop issues to next sprint


Assignments
===========

Board Usage Estimation
----------------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` (w menu po lewej)
#. W detail view zadania `One` -> okienko `Estimate` ustaw 3 (lub pole `Story Point` przy edycji zadania)
#. W detail view zadania `Three` -> okienko `Estimate` ustaw 4 (lub pole `Story Point` przy edycji zadania)
#. W detail view zadania `Five` -> okienko `Estimate` ustaw 8 (lub pole `Story Point` przy edycji zadania)
#. Zwróć uwagę, że estymować można tylko zadania typu `Story`

.. note:: `Story Points` (jak sama nazwa wskazuje) domyślnie mogą być przyznawane tylko zadaniom typu `Story`. Można to zmienić w konfiguracji (wymaga uprawnień administratora) `Custom Field` -> `Story Points` -> Ikona trybiku (po prawej) -> `Configure` -> `Applicable contexts for scheme` -> `Edit Configuration`.

Board Usage Sprint Create
-------------------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` (w menu po lewej)
#. Dodaj pierwszy sprint:

    - `Name`: `2000-01 week 1`
    - `Duration`: `1 week`
    - `Start Date`: `1/Jan/00 09:00 AM`

#. Dodaj drugi sprint:

    - `Name`: `2000-01 week 2`
    - `Duration`: `1 week`
    - `Start Date`: `7/Jan/00 09:00 AM`

Board Usage Sprint Start
------------------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Backlog` (w menu po lewej)
#. Do sprintu `2000-01 week 1` dodaj zadania: `One`, `Two`, `Three`
#. Przejedź suwakiem i dodaj `Four`, `Five`, `Six`, zwróć uwagę na zmiany liczb w okienku `Issues` i `Estimate`
#. Wystartuj sprint ustawiając:

    - `Goal`: `Ukończenie szkolenia z Jiry`
    - `Duration`: `1 week`
    - `Start Date`: `1/Jan/00 09:00 AM`

#. Co oznaczają wartości z estymacjami w nagłówku sprintu: `To Do`, `In Progress`, `Done` (w rozpoczętym sprincie, na ekranie `Backlog` w prawym górnym rogu - trzy kolorowe owale).

Board Usage Sprint Work
-----------------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Active Sprints` (w menu po lewej)
#. Przenieś zadania:

    - `One` do `In Progress`
    - `Two` do `In Progress`
    - `Three` do `Done`

#. Dodaj flagę do zadania `Four`
#. Z menu `Board` prawy górny róg:

    - Wybierz `Hide detail view`
    - Wybierz `Print cards` i zmień `Card size` -> `small`

#. Zobacz jak zmieniły się wartości z estymacjami w nagłówku sprintu: `To Do`, `In Progress`, `Done` (w rozpoczętym sprincie, na ekranie `Backlog` w prawym górnym rogu - trzy kolorowe owale).

Board Usage Sprint Close
------------------------
#. Z menu u góry wybierz `Boards` -> Twój Board -> `Active Sprint` (w menu po lewej)
#. Zakończ aktualny sprint -> Prawy górny róg `Complete Sprint`
#. Zadania niezakończone mają `spaść` do sprintu następnego, tj. `2000-01 week 2`

    - Co się dzieje z otwartymi zadaniami?
    - Co się dzieje z zamkniętymi zadaniami?
    - Co się dzieje z zamkniętymi subtaskami, ale otwartym zadaniem?
    - Co się dzieje z otwartymi subtaskami ale zamkniętym zadaniem?


References
==========
.. [#agilemanifesto] Beck, Kent and Beedle, Mike and van Bennekum, Arie and Cockburn, Alistair and Cunningham, Ward and Fowler, Martin and Grenning, James and Highsmith, Jim and Hunt, Andrew and Jeffries, Ron and Kern, Jon and Marick, Brian and C. Martin, Robert and Mellor, Steve and Schwaber, Ken and Sutherland, Jeff and Dave Thomas. Manifesto for Agile Software Development. Year: 2001. URL Access Date: 2021-03-22. URL: https://agilemanifesto.org/iso/en/manifesto.html

.. [#agilemanifestoprinciples] Beck, Kent and Beedle, Mike and van Bennekum, Arie and Cockburn, Alistair and Cunningham, Ward and Fowler, Martin and Grenning, James and Highsmith, Jim and Hunt, Andrew and Jeffries, Ron and Kern, Jon and Marick, Brian and C. Martin, Robert and Mellor, Steve and Schwaber, Ken and Sutherland, Jeff and Dave Thomas. Principles behind the Agile Manifesto. Year: 2001. URL Access Date: 2021-03-22. URL: https://agilemanifesto.org/iso/en/principles.html

.. [#scrumguide] Schwaber, Ken and Sutherland, Jeff. The Scrum Guide, The Definitive Guide to Scrum: The Rules of the Game. Year: 2020. Accessed Date: 2021-03-22. URL: https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf
