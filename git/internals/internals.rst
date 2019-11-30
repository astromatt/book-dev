*************
Git Internals
*************


Objects
=======
* ``.git/objects/*``
* ``.git/objects/pack/``

.. code-block:: console

    $ ls .git/objects
    09      14      49      7b      94      b4      d8      pack
    0c      41      6d      8b      a4      c5      info

    $ git show

gc
==
.. code-block:: console

    $ git gc --aggressive --prune=now
    $ ls .git/objects/*
    $ ls .git/objects/pack/

fsck
====
* Verifies the connectivity and validity of the objects in the database

.. code-block:: console

    $ git fsck --full
    Checking object directories: 100% (256/256), done.
    Checking objects: 100% (10063/10063), done.
    dangling blob 47160601b85c1fbc4d0a89f23064f993fe9221cf

    $ git gc --aggressive --prune=now
    Counting objects: 10239, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (9708/9708), done.
    Writing objects: 100% (10239/10239), done.
    Total 10239 (delta 6175), reused 3763 (delta 0)

    $ git fsck --full
    Checking object directories: 100% (256/256), done.
    Checking objects: 100% (10239/10239), done.
