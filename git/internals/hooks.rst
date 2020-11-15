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
.. code-block:: console

    $ git log --format='"%ai", "%h", "%an", "%ae", "%s"' > ~/Desktop/git-log.csv
    "2020-10-14 01:04:38 +0200", "d5a4d6b", "Matt Harasymczuk", "matt@astrotech.io", "MYPROJECT-10 git commit message #time 69m"

    $ git log --format='"%aI", "%h", "%an", "%ae", "%s"' > ~/Desktop/git-log.csv
    "2020-10-14T01:04:38+02:00", "d5a4d6b", "Matt Harasymczuk", "matt@astrotech.io", "MYPROJECT-10 git commit message #time 69m"

.. code-block:: sh
    :caption: .git/hooks/prepare-commit-msg

    #!/bin/sh
    #
    # @author Matt Harasymczuk <book@astronaut.center>
    # @since 2012-10-23
    # @updated 2020-07-03
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

    COMMIT_MSG_FILE=$1
    COMMIT_SOURCE=$2
    SHA1=$3

    issuekey=$(git symbolic-ref HEAD |egrep --only-matching '[A-Z]{2,10}-[0-9]{1,6}')
    message=$(cat $1)


    if [ -z "$issuekey" ]; then
        echo "Please work on branch with JIRA issue key in the branch name"
        echo "Changes were not committed"
        exit 1
    else
       echo "$issuekey $message" > $COMMIT_MSG_FILE
    fi



Assignments
===========
#. Create Git hook which enforces JIRA issue key in commit message
#. Create Git hook which copies JIRA issue key from branch name to commit message
