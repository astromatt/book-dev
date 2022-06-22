************
Git Workflow
************


Initialize repository
=====================
.. code-block:: console

    $ git init
    Initialized empty Git repository in /home/devops/.git/

    $ git init --bare
    Initialized empty Git repository in /home/devops/.git/

.. code-block:: console

    $ find .
    ./config
    ./objects
    ./objects/pack
    ./objects/info
    ./HEAD
    ./info
    ./info/exclude
    ./description
    ./hooks
    ./hooks/commit-msg.sample
    ./hooks/pre-rebase.sample
    ./hooks/pre-commit.sample
    ./hooks/applypatch-msg.sample
    ./hooks/fsmonitor-watchman.sample
    ./hooks/pre-receive.sample
    ./hooks/prepare-commit-msg.sample
    ./hooks/post-update.sample
    ./hooks/pre-merge-commit.sample
    ./hooks/pre-applypatch.sample
    ./hooks/pre-push.sample
    ./hooks/update.sample
    ./refs
    ./refs/heads
    ./refs/tags

Clone repository
================
* Protocols:

    * local filesystem
    * ssh
    * http
    * https

* Sometimes ssh port is blocked (especially in public wifi)
* HTTP is unsafe
* HTTPS is the most robust option

.. code-block:: console

    $ git clone URL [dest dir]
    $ git clone file:///...
    $ git clone ssh://...
    $ git clone https://...
    $ git clone --recursive URL

.. code-block:: console

    $ git clone https://github.com/AstroMatt/book-devops.git

Pull
====
.. code-block:: console

    $ git pull --rebase

Add
===
.. code-block:: console

    $ git add .

Move
====
.. code-block:: console

    $ git mv [source] [destination]

Remove
======
.. code-block:: console

    $ git rm
    $ git rm -fr
    $ git rm --cached


Status
======
.. code-block:: console

    $ git status


Commit
======
* ``-a``, ``--all`` - commit all changed files
* ``--amend`` - amend previous commit
* ``-C``, ``--reuse-message <commit>`` - reuse message from specified commit
* ``--reset-author`` - the commit is authored by me now (used with ``-C/-c/--amend``)
* ``-S``, ``--gpg-sign[=<key-id>]`` - GPG sign commit

.. code-block:: console

    $ git commit --all --message "ID-10 fix, now working"
    $ git commit -a -m "ID-10 fix, now working"
    $ git commit -am "ID-10 fix, now working"

Revert
======
* Undo committed file

.. code-block:: console

    $ git reset --soft HEAD^
    $ git reset HEAD <file-path>
    $ git commit -c ORIG_HEAD


Push
====
.. code-block:: console

    $ git push


Further Reading
===============
* https://www.gitops.tech


Assignments
===========

Clone, Push and Pull
--------------------
#. Clone repository via ``ssh``
#. Add file ``lastname_firstname.txt``
#. Edit ``.git/config`` and add following ``[user]`` section

    .. code-block:: text

        [user]
            name = Your Name
            email = your.email@example.com

#. Commit using ``git commit``
#. Push commit ``git push``

Advanced Options
----------------
#. Set branch permissions
#. Make pull request
#. Squash and merge pull request
