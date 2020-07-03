**********
Git Bisect
**********

.. code-block:: console

    $ git log --oneline README.rst
    8b3440a (HEAD -> master) Change Readme file
    d84da13 Book: Refactor #time 79m
    19cc5df Book: Theme #time 30m
    d84ac63 Book: README #time 5m
    e5c6727 Book: README #time 5m
    b730202 Book: README #time 2m
    8aecc59 Book: Requirements #time 10m
    af231bc Book: Readme #time 2m
    51a11d7 Book: Readme #time 1m
    5de098a Book: Readme #time 15m
    89d7dd1 CI/CD: Docker #time 2m
    3827f93 Update README.rst
    2f7b146 Update README.rst
    0cf6c38 Unified book format #time 3h
    050a0e5 Requrements #time 6m
    d93ea7a Restructure #time 41m
    9b9e000 Documentation #time 2h
    76ce5b6 README
    0ce393d Requirements update
    a3a0415 Adding information about time to start the service.
    11bc71d Merge branch 'master' of https://github.com/MattAgile/ecosystem-workshop
    dfe5ede Added information about ports.
    298fd09 Updated README.rst-vagrant up issue
    bc71467 Dodanie informacji o ecosystem.box
    03066ec Update README.rst
    34bae76 Ecosystem vagrant up
    a848376 Ecosystem vagrant up

.. code-block:: console

    $ git bisect start

    $ git bisect good a3a0415

    $ git bisect bad 19cc5df
    Bisecting: 197 revisions left to test after this (roughly 8 steps)
    [2f4b69b765de68964ae96d275cf61398df21540d] Merge pull request #2 from wasikuss/master

.. code-block:: console

    $ git log -1
    commit 2f4b69b765de68964ae96d275cf61398df21540d (HEAD)
    Merge: e1a7747 535067e
    Author: Matt Harasymczuk <github.com@haras.pl>
    Date:   Fri Aug 4 05:19:09 2017 +0200

        Merge pull request #2 from wasikuss/master

        Expand use case of `Jenkins + Git Bisect Run`

    $ git bisect good
    Bisecting: 98 revisions left to test after this (roughly 7 steps)
    [2161b50d6c0258c43e55cc82f0cd6bd9a71d04dd] Virtualization: Vagrant #time 15m

    $ git bisect good
    Bisecting: 49 revisions left to test after this (roughly 6 steps)
    [112762124c2fbedc3a0b3a98b9f0754a9a7d9eb5] Quality: Sonar-Scanner #time 1m

    $ git bisect bad
    Bisecting: 24 revisions left to test after this (roughly 5 steps)
    [f97417fc401216da9c6beb5800bdd9becd5a7ec8] Virtualization: Docker #time 5m

    $ git bisect bad
    Bisecting: 11 revisions left to test after this (roughly 4 steps)
    [0480826f327beadddb6e3f00599a212bd62b701f] CI/CD: Jenkins, Sonar, Gitlab, Docker #time 60m

    $ git bisect good
    Bisecting: 5 revisions left to test after this (roughly 3 steps)
    [f404055c7d930a3319f8fc6e72e2f0640bda0ddb] Virtualization: Docker #time 75m

    $ git bisect good
    Bisecting: 2 revisions left to test after this (roughly 2 steps)
    [4f08f621ed61602ce70b187f73a2d07df3442ed1] Virtualization: Docker #time 5m

    $ git bisect bad
    Bisecting: 0 revisions left to test after this (roughly 1 step)
    [854ae8aec05bc77d4f55dc16255452167385302c] Virtualization: Docker #time 60m

.. code-block:: console

    $ git log -1
    commit 854ae8aec05bc77d4f55dc16255452167385302c (HEAD)
    Author: Matt Harasymczuk <book@astronaut.center>
    Date:   Wed Oct 24 02:16:57 2018 +0200

        Virtualization: Docker #time 60m

    $ git blame README.rst
    0cf6c38c (Matt Harasymczuk 2018-01-04 22:59:47 +0100  1) ######################################
    0cf6c38c (Matt Harasymczuk 2018-01-04 22:59:47 +0100  2) DevOps and Development Tools Ecosystem
    0cf6c38c (Matt Harasymczuk 2018-01-04 22:59:47 +0100  3) ######################################
    0cf6c38c (Matt Harasymczuk 2018-01-04 22:59:47 +0100  4)
    0cf6c38c (Matt Harasymczuk 2018-01-04 22:59:47 +0100  5) **Author**
    0cf6c38c (Matt Harasymczuk 2018-01-04 22:59:47 +0100  6)     :name: `Matt Harasymczuk <https://www.astronaut.center>`_
    0cf6c38c (Matt Harasymczuk 2018-01-04 22:59:47 +0100  7)     :email: book@astronaut.center
    [...]

.. code-block:: console

    $ git bisect reset
    Previous HEAD position was 854ae8a Virtualization: Docker #time 60m
    Switched to branch 'master'
    Your branch is up-to-date with 'origin/master'.

Idea
====

Jenkins + git bisect run
------------------------
#. If Jenkins fails build, it triggers "search for person to blame"
#. Bisect over all changes since last green build
#. Run automatic tests and mark ``git bisect good`` or ``git bisect bad``
#. When found bad commit, ``git blame`` and send email to everyone
