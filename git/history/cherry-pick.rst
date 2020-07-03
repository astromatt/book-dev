***************
Git Cherry Pick
***************


About Cherry Pick
=================
* Copy commit from one branch to another
* Copy has different commit hash


Workflow
========
.. code-block:: console

    $ git branch
    * master

    $ git checkout -b temporary
    Switched to a new branch 'temporary'

    $ git branch
      master
    * temporary

.. code-block:: console

    $ echo 'some text' > README.rst

    $ git commit -am "Change Readme file"
    [temporary 09c25aa] Change Readme file
     1 file changed, 1 insertion(+), 35 deletions(-)
     rewrite README.rst (100%)

.. code-block:: console

    $ git checkout master
    Switched to branch 'master'
    Your branch is up to date with 'origin/master'.

    $ git branch
    * master
      temporary

    $ git log -2
    commit 8192e9663597d1a58bb89d09b882372763395175 (HEAD -> master, origin/master, origin/HEAD)
    Author: Matt Harasymczuk <book@astronaut.center>
    Date:   Fri Nov 22 13:33:39 2019 +0100

        Commit Two

    commit dafb4249e41e88bf367f326d575efa19ea888955
    Author: Matt Harasymczuk <book@astronaut.center>
    Date:   Fri Nov 22 13:19:58 2019 +0100

        Commit One

.. code-block:: console

    $ git cherry-pick 09c25aa
    [master 8b3440a] Change Readme file
     Date: Wed Nov 27 23:13:05 2019 +0100
     1 file changed, 1 insertion(+), 35 deletions(-)
     rewrite README.rst (100%)

.. code-block:: console

    $ git log -2
    commit 8b3440aca849c4783069625ce4aada27e8007f8c (HEAD -> master)
    Author: Matt Harasymczuk <book@astronaut.center>
    Date:   Wed Nov 27 23:13:05 2019 +0100

        Change Readme file

    commit 8192e9663597d1a58bb89d09b882372763395175 (origin/master, origin/HEAD)
    Author: Matt Harasymczuk <book@astronaut.center>
    Date:   Fri Nov 22 13:33:39 2019 +0100

        Commit Two
