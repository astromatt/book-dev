**********
Automation
**********


Atlassian Python API
====================
* https://github.com/atlassian-api/atlassian-python-api
* https://github.com/atlassian-api/atlassian-python-api/tree/master/examples/jira

.. code-block:: sh

    pip install atlassian-python-api

.. code-block:: python

    from atlassian import Jira


    jira = Jira(
        url='http://localhost:8080',
        username='admin',
        password='admin')

    jira.issue_create({
        'project': {'key': 'MYPROJECT'},
        'issuetype': {'name': 'Task'},
        'summary': 'My Issue Summary',
        'description': 'This is the issue description'})

.. code-block:: python

    from atlassian import Jira


    jira = Jira(
        url='http://localhost:8080',
        username='admin',
        password='admin')

    JQL = 'project = MYPROJECT AND status IN ("To Do", "In Progress") ORDER BY priority DESC'

    data = jira.jql(JQL)
    print(data)


GIT
===
.. code-block:: console

    $ git log --oneline
    ec68eec MYPROJECT-10 now working #time 69m
    60661f4 MYPROJECT-8 fix #time 13m
    1cb7c51 MYPROJECT-6 new feature #time 300m

    $ git log --oneline |awk -F'#time ' '{print $2}'
    69m
    13m
    300m

    $ git log --oneline |awk -F'#time ' '{print $2}' |sed 's/m//'
    69
    13
    300

    $ git log --oneline |awk -F'#time ' '{print $2}' |sed 's/m//' |addnum
    382

    $ cat ~/.profile |grep addnum
    alias addnum='python -c"import sys; print(sum(map(int, sys.stdin)))"'

.. code-block:: console

    $ cat ~/.gitconfig |grep -B1 since
    [alias]
    since = "!f() { ~/.bin/since; }; f"

    $ cat ~/.bin/since
    #!/usr/bin/env python3

    from datetime import datetime, timezone
    from subprocess import run

    SECOND = 1
    MINUTE = 60 * SECOND

    last = run('git log -1 --format="%ad" --date=iso', shell=True, capture_output=True).stdout.strip().decode()
    last = datetime.strptime(last, '%Y-%m-%d %H:%M:%S %z')
    print('Last commit:', last)

    delta = datetime.now(tz=timezone.utc) - last
    min = delta.total_seconds() / MINUTE
    min = round(min)

    print(f'Since: {min}m')

.. code-block:: console

    $ git log --format='"%ai", "%h", "%s"'
    "2020-10-14 01:04:38 +0200", "d5a4d6b", "MYPROJECT-10 git commit message #time 69m"

    $ git log --format='"%aI", "%h", "%an", "%ae", "%s"'
    "2020-10-14T01:04:38+02:00", "d5a4d6b", "Matt Harasymczuk", "matt@astrotech.io", "MYPROJECT-10 git commit message #time 69m"

    $ git log --format='"%aI", "%h", "%an", "%ae", "%s"' > ~/Desktop/git-log.csv

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
