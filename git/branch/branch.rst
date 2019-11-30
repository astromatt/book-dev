************
Git Branches
************


.. epigraph::

    Branching is not the issue, the merging is... -- Linus Torvalds


Branche
=======
#. Default branch: ``master``
#. Branch can have any names
#. ``/`` in name make branch folder in ``.git/refs/heads/``
#. Typically use Git Flow naming convention
#. After merging no need to delete branch
#. Branches are only commit hashes to the most recent commit
#. Branch weights 40 bytes + null terminator (in fact one file system sector)
#. Can :ref:`merge <Git Merge>` and :ref:`rebase <Git Rebase>` branches


Local storage of branches
=========================
.. code-block:: text

    .git/HEAD
    .git/refs/heads/master
    .git/refs/heads/*
    .git/refs/remotes/*
    .git/refs/tags/*
    (HEAD detached at 44d11b0)

.. code-block:: console

    $ cat .git/HEAD
    ref: refs/heads/master

.. code-block:: console

    $ cat .git/refs/heads/master
    8192e9663597d1a58bb89d09b882372763395175

Working with branches
=====================

List branches
-------------
.. code-block:: console

    $ git branch
    * master

.. code-block:: console

    $ git branch -a
    * master
      remotes/origin/HEAD -> origin/master
      remotes/origin/master

.. code-block:: console

    $ git branch -avv
    * master                8192e96 [origin/master] DevOps: CI/CD #time 15m
      remotes/origin/HEAD   -> origin/master
      remotes/origin/master 8192e96 DevOps: CI/CD #time 15m

Create branch
-------------
.. code-block:: console

    $ git branch [name]

.. code-block:: console

    $ git checkout -b [name]

.. code-block:: console

    $ git checkout -tb origin/master

Change branch
-------------
.. code-block:: console

    $ git checkout [name]

Delete branch
-------------
.. code-block:: console

    $ git branch -d [name]

.. code-block:: console

    $ git branch -D [name]
