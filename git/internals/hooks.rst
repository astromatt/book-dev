*********
Git Hooks
*********


About Hooks
===========
* ``.git/hooks/pre-commit``
* ``chmod +x .git/hooks/pre-commit``
* ``#!/bin/sh``
* ``set +e`` - Print an error to but the script will continue
* ``set -e`` - Exit immediately if a command exits with a non-zero status
* ``trap``
* ``exit 0`` (success) - allows to commit
* ``exit 1`` (error) - prevents commit


Possible Hooks
==============
* applypatch-msg
* commit-msg
* fsmonitor-watchman
* post-update
* pre-applypatch
* pre-commit
* pre-merge-commit
* pre-push
* pre-rebase
* pre-receive
* prepare-commit-msg
* update


Branch Hook
===========
.. code-block:: sh

    #!/bin/sh
    #
    # @author Matt Harasymczuk <matt@astrotech.io>
    # @since 2012-10-23
    #
    # This hook message should go to .git/hooks/commit-msg
    # Remember to add (*nix machines) executable rights: chmod +x .git/hooks/commit-msg
    # Hook checks branch you're currently on and add its name to commit message.
    # It adds commit message as a comment in jira connected with this issue.
    # Moreover it creates a Code Review in Crucible.
    #
    # You'll never forget about this things anymore :}
    # The only thing you should do is to create an issue for each branch you have.
    # For example if you are working on issue DEMO-123 create a branch called DEMO-123
    # Each commit on this branch would have DEMO-123 in the commit message and Code Review process attached to it.
    #

    issuekey=$(git symbolic-ref HEAD |egrep --only-matching '[A-Z]{2,10}-[0-9]{1,6}')
    commitmsgFile="$1"
    commitmsg=$(cat "$1")

    if [ -z "$issuekey" ]; then
       echo "You're not working on issue branch!"
       echo "Please create a branch named after https://jira.example.com issue."
       echo "Commit message will be updated accordingly in order to contain branch/issuekey in the commit message."
       exit 1
    else
       echo "$issuekey #comment $commitmsg +review" > $commitmsgFile
    fi


Assignments
===========
#. Stwórz hook aby wymuszał w nazwie commita ID z Jiry
#. Stwórz hook aby do commit message dodawał ID z nazwy brancha
