***********
GIT Subtree
***********


Add subtree
===========
.. code-block:: console

    $ git log -1
    commit 945d1d8d300b1ceef3378b5520ebdaa337655eac
    Author: Matt Harasymczuk <matt@astrotech.io>
    Date:   Thu Nov 28 00:06:53 2019 +0100

        First Commit

.. code-block:: console

    $ git remote add revealjs https://github.com/hakimel/reveal.js.git

    $ git remote
    origin
    revealjs

.. code-block:: console

    $ git subtree add --prefix=contrib/ revealjs master
    git fetch revealjs master
    warning: no common commits
    remote: Enumerating objects: 11232, done.
    remote: Total 11232 (delta 0), reused 0 (delta 0), pack-reused 11232
    Receiving objects: 100% (11232/11232), 8.88 MiB | 2.15 MiB/s, done.
    Resolving deltas: 100% (6214/6214), done.
    From https://github.com/hakimel/reveal.js
     * branch            master     -> FETCH_HEAD
     * [new branch]      master     -> revealjs/master
    Added dir 'contrib'

.. code-block:: console

    $ git log -2
    commit d86741484366d84108f62f1e6120e7ed6613d8d3 (HEAD -> master)
    Merge: 945d1d8 33bed47
    Author: Matt Harasymczuk <matt@astrotech.io>
    Date:   Thu Nov 28 00:08:05 2019 +0100

        Add 'contrib/' from commit '33bed47daca3f08c396215415e6ece005970734a'

        git-subtree-dir: contrib
        git-subtree-mainline: 945d1d8d300b1ceef3378b5520ebdaa337655eac
        git-subtree-split: 33bed47daca3f08c396215415e6ece005970734a

    commit 945d1d8d300b1ceef3378b5520ebdaa337655eac
    Author: Matt Harasymczuk <matt@astrotech.io>
    Date:   Thu Nov 28 00:06:53 2019 +0100

        First Commit

.. code-block:: console

    $ ls contrib
    CONTRIBUTING.md         demo.html               package-lock.json
    LICENSE                 gruntfile.js            package.json
    README.md               index.html              plugin
    bower.json              js                      test
    css                     lib

Pull
====
.. code-block:: console

    $ git subtree pull --prefix=contrib/ revealjs master --squash
    From https://github.com/hakimel/reveal.js
     * branch            master     -> FETCH_HEAD
    Subtree is already at commit 33bed47daca3f08c396215415e6ece005970734a.


Push
====
.. code-block:: console

    $ git subtree push --prefix=contrib/ origin master
