***********
GIT Remotes
***********


About Remotes
=============
#. Default remote: ``origin`` (cloned from)
#. Any repository can be remote
#. Can fetch and push to any remote
#. Pull Requests are branches too
#. `.git/config` section ``[remote "origin"]`` can have multiple urls

Using Remotes
=============
.. code-block:: console

    usage: git remote [-v | --verbose]
       or: git remote add [-t <branch>] [-m <master>] [-f] [--tags | --no-tags] [--mirror=<fetch|push>] <name> <url>
       or: git remote rename <old> <new>
       or: git remote remove <name>
       or: git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
       or: git remote [-v | --verbose] show [-n] <name>
       or: git remote prune [-n | --dry-run] <name>
       or: git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
       or: git remote set-branches [--add] <name> <branch>...
       or: git remote get-url [--push] [--all] <name>
       or: git remote set-url [--push] <name> <newurl> [<oldurl>]
       or: git remote set-url --add <name> <newurl>
       or: git remote set-url --delete <name> <url>

        -v, --verbose         be verbose; must be placed before a subcommand

.. code-block:: console

    $ git remote
    origin

    $ git remote -v
    origin	https://github.com/AstroMatt/book-devops.git (fetch)
    origin	https://github.com/AstroMatt/book-devops.git (push)

    $ ls .git/refs/remotes
    origin

    $ git ls-remote
    From https://github.com/AstroMatt/book-devops.git
    8192e9663597d1a58bb89d09b882372763395175	HEAD
    8192e9663597d1a58bb89d09b882372763395175	refs/heads/master
    328c3ea571acda37a2d0f4673ab8af44ee0371d8	refs/pull/1/head
    535067e2c1b261e4ef1f5ae0d1c579fab7822bba	refs/pull/2/head
    ad0d7c95d9a14cdc5eac36d3b48bfcd76fbe8fd9	refs/pull/3/head



Updating / Fetching
===================
.. code-block:: console

    $ git remote update --prune
    Fetching origin

.. code-block:: console

    $ git fetch
    Fetching origin


Pull
====
.. code-block:: console

    $ git fetch
    $ git merge

Or:

.. code-block:: console

    $ git fetch
    $ git rebase


Push
====

Push to the default
-------------------
.. code-block:: console

    $ git push

Push all branches
-----------------
.. code-block:: console

    $ git push --all

Push to specific remote
-----------------------
.. code-block:: console

    $ git push origin
    $ git push origin master

Push to other name in the remote
--------------------------------
.. code-block:: console

    $ git push origin master:other

Delete branch in the remote
---------------------------
.. code-block:: console

    $ git push origin :other

Push Tags
---------
* Not pushed by default

.. code-block:: console

    $ git push --tags
