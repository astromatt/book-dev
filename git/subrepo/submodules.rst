**************
Git Submodules
**************


Clone with submodules
=====================
.. code-block:: console

    $ git clone --recursive


Add submodule
=============
.. code-block:: console

    $ git submodule add https://github.com/AstroTech/workshop-git.git contrib/
    Cloning into '/home/devops/contrib'...
    remote: Enumerating objects: 29, done.
    remote: Counting objects: 100% (29/29), done.
    remote: Compressing objects: 100% (25/25), done.
    remote: Total 377 (delta 4), reused 26 (delta 2), pack-reused 348
    Receiving objects: 100% (377/377), 40.81 MiB | 3.77 MiB/s, done.
    Resolving deltas: 100% (141/141), done.

    $ ls contrib
    LICENSE.rst             _references             requirements.txt
    README.rst              _static                 setup.cfg
    _img                    conf.py                 setup.py
    _new_img                index.rst               versioning

.. code-block:: console

    $ git status
    On branch master
    Your branch is up-to-date with 'origin/master'.

    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            new file:   .gitmodules
            new file:   contrib

.. code-block:: console

    $ cat .gitmodules
    [submodule "contrib"]
            path = contrib
            url = https://github.com/AstroTech/workshop-git.git


Update
======
.. code-block:: console

    $ cd contrib

    $ git pull
    Already up to date.
    Current branch master is up to date.

    $ cd ..

    $ git status
    On branch master
    Your branch is up-to-date with 'origin/master'.

    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            new file:   .gitmodules
            new file:   contrib

    $ git commit
    Aborting commit due to empty commit message.

    $ git commit -am "Add submodule"
    [master 4140967] Add submodule
     2 files changed, 4 insertions(+)
     create mode 100644 .gitmodules
     create mode 160000 contrib

    $ git push

Remove
======
.. code-block:: console

    $ git rm -fr contrib .gitmodules
    rm 'contrib'

    $ git status
    On branch master
    Your branch is ahead of 'origin/master' by 2 commits.
      (use "git push" to publish your local commits)

    Changes to be committed:
      (use "git restore --staged <file>..." to unstage)
            deleted:    .gitmodules
            deleted:    contrib
