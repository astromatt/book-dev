*****************
GIT Filter Branch
*****************


Remove file from history
========================
* Remove sensitive data
* Remove
* http://help.github.com/remove-sensitive-data/

.. code-block:: console

    $ FILENAME="secret.txt"

    $ git filter-branch \
        --index-filter 'git rm --cached --ignore-unmatch $FILENAME' \
        --prune-empty -- \
        --all

    $ git gc --aggressive --prune=now
    Enumerating objects: 3720, done.
    Counting objects: 100% (3720/3720), done.
    Delta compression using up to 12 threads
    Compressing objects: 100% (3519/3519), done.
    Writing objects: 100% (3720/3720), done.
    Total 3720 (delta 2090), reused 1006 (delta 0)
    Computing commit graph generation numbers: 100% (463/463), done.


Change user or email
====================
.. code-block:: sh

    git filter-branch --commit-filter '

        if [ "$GIT_COMMITTER_NAME" = "mharasymczuk" ]; then
            GIT_COMMITTER_NAME="Matt Harasymczuk";
            GIT_COMMITTER_EMAIL="matt@astrotech.io";
        fi

        if [ "GIT_AUTHOR_NAME" = "mharasymczuk" ]; then
            GIT_AUTHOR_NAME="Matt Harasymczuk";
            GIT_AUTHOR_EMAIL="matt@astrotech.io";
        fi

        git commit-tree "$@";
        ' HEAD
