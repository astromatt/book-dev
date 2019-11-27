**********
Git Config
**********

Config File
===========

Global Config
-------------
* ``~/.gitconfig``

Local Config
------------
* ``.git/config``
* ``git config multiple url``

Configuration
-------------
.. code-block:: ini

    [i18n]
        commitencoding = UTF-8
        logoutputencoding = UTF-8

.. code-block:: ini

    [core]
        eol = 'lf'
        autocrlf = input
        excludesfile = /Users/matt/.gitignore_global

.. code-block:: ini

    [branch "master"]
        rebase = true

.. code-block:: ini

    [branch]
        #autosetuprebase = always

.. code-block:: ini

    # git config --global color.diff.meta "blue black bold"

    [color]
        ui = true

.. code-block:: ini

    [merge]
      tool = extMerge

    [mergetool "extMerge"]
      cmd = extMerge "$BASE" "$LOCAL" "$REMOTE" "$MERGED"
      trustExitCode = false

.. code-block:: ini

    [diff]
      external = extDiff


Notable
=======
* receive.fsckObjects
* receive.denyNonFastForwards
* receive.denyDeletes
* core.autocrlf
* color.branch
* color.diff
* color.interactive
* color.status
* user.signingkey
* commit.template
* core.editor

Aliases
=======
.. code-block:: text

    l = log --pretty=format:"%C(yellow)%h %ad%Cred%d %Creset%s%Cblue [%cn]" --decorate --date=short

.. code-block:: text

    again = "!f() { git add -A && git status && git commit -m \"$(git log -1 --format='%s')\" && git push && git l -1; }; f"

.. code-block:: text

    d = diff --cached HEAD^

.. code-block:: text

    csv = log --pretty=format:'"%h", "%an", "%ae", "%ad", "%s"'


Gitignore
=========
