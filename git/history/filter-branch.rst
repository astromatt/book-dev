*****************
Git Filter Branch
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
* ``git config user.name "Mark Watney"``
* ``git config user.email "mwatney@nasa.gov"``
* ``git config --global user.name "Mark Watney"``
* ``git config --global user.email "mwatney@nasa.gov"``

.. code-block:: sh

    git filter-branch --commit-filter '

        if [ "$GIT_COMMITTER_NAME" = "Mark W." ]; then
            GIT_COMMITTER_NAME="Mark Watney";
            GIT_COMMITTER_EMAIL="mwatney@nasa.gov";
        fi

        if [ "GIT_AUTHOR_NAME" = "Mark W." ]; then
            GIT_AUTHOR_NAME="Mark Watney";
            GIT_AUTHOR_EMAIL="mwatney@nasa.gov";
        fi

        git commit-tree "$@";
        ' HEAD

    git push --force
