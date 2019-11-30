**********************
Git Interactive Rebase
**********************


Run
===
* old version problem with rebase of first commit

.. code-block:: console

    $ git rebase -i HEAD^^^
    $ git rebase -i HEAD~3
    $ git rebase -i HEAD~~~
    $ git rebase -i --root

Carret vs Tilde
---------------
* ``HEAD~2`` - 2 commits older than HEAD
* ``HEAD^2`` - the second parent of HEAD, if HEAD was a merge, otherwise illegal
* ``HEAD@{2}`` - refers to the 3rd listing in the overview of git reflog
* ``HEAD~~`` - 2 commits older than HEAD
* ``HEAD^^`` - 2 commits older than HEAD

Commands
========
.. csv-table:: Interactive Rebase Commands
    :header: "Short", "Long", "Description"

    "p", "pick",    "use commit"
    "r", "reword",  "use commit, but edit the commit message"
    "e", "edit",    "use commit, but stop for amending"
    "s", "squash",  "use commit, but meld into previous commit"
    "f", "fixup",   "like 'squash', but discard this commit's log message"
    "x", "exec",    "run command (the rest of the line) using shell"
    "b", "break",   "stop here (continue rebase later with 'git rebase --continue')"
    "d", "drop",    "remove commit"
    "l", "label",   "label current HEAD with a name"
    "t", "reset",   "reset HEAD to a label"
    "m", "merge",   "create a merge commit using the original merge commit's message"


Squash
======
* When?
* Good practice?


Reword
======
* When?


Push
====
* Rebase on public repos
* Rebase on pushed commits

.. code-block:: console

    $ git push --force
