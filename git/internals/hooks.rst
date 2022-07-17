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
    # @author Matt Harasymczuk <matt@astrotech.io>
    # @since 2012-10-23
    # @updated 2022-07-17
    #
    # This simple hook gets Jira issue ID from the branch you are currently
    # committing to. If you used Jira development panel "Create Branch",
    # your branch name should be: "feature/MYPROJECT-69-some-issue-summary"
    # and in such case it would get "MYPROJECT-69". Then hook prepends issue
    # ID to your current commit message linking commit and Jira issue together.
    # You'll never forget about adding issue id to the commit message anymore!
    #
    # To install hook just paste following script (with this comment) in:
    # ``.git/hooks/prepare-commit-msg``
    #
    # On *nix machines (macOS, Linux, etc) add executable rights:
    # ``chmod +x .git/hooks/prepare-commit-msg``
    #
    # That's it. You can commit to test if it works.
    # Remember before committing to check out branch with proper name, such as:
    # ``feature/MYPROJECT-69-my-issue-summary``

    PATTERN='[A-Z]{2,10}-[0-9]{1,6}'

    currentBranch=$(git branch --show-current)
    issueKey=$(echo $currentBranch |egrep -o $PATTERN)

    commitMsgFile=$1
    commitMsgOld=$(cat $commitMsgFile)
    commitMsgNew="$issueKey $commitMsgOld"

    if [ -z "$issueKey" ]; then
        echo "You are currently on a branch without JIRA issue ID in its name."
        echo "Changes were not committed."
        echo ""
        echo "If you want to commit anyway, just remove executable rights for this hook:"
        echo "chmod -x .git/hooks/prepare-commit-msg"
        echo ""
        echo "But remember to re-enable it later on, by executing:"
        echo "chmod +x .git/hooks/prepare-commit-msg"
        exit 1
    else
        echo "Current Branch: $currentBranch"
        echo "Jira Issue Key: $issueKey"
        echo "Commit Msg Old: $commitMsgOld"
        echo "Commit Msg New: $commitMsgNew"
        echo ""

        echo $commitMsgNew > $commitMsgFile
        exit 0
    fi


Assignments
===========
#. Create Git hook which enforces JIRA issue key in commit message
#. Create Git hook which copies JIRA issue key from branch name to commit message
