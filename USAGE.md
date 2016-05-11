# Usage

Read `README.md` to se how to download and setup environment

## Run Selected Tool

If you set small amount of RAM, your machine might be killed.
Remember that each tool while running takes around `700 MB` of RAM.
Please run only one/two selected services for small RAM sizes.
`8196 MB RAM` should be enough to handle load for each of this machines run simultaneously.

    $ vagrant ssh -c 'sudo service confluence start'
    $ vagrant ssh -c 'sudo service jenkins start'
    $ vagrant ssh -c 'sudo service jira start'
    $ vagrant ssh -c 'sudo service sonar start'
    $ vagrant ssh -c 'sudo service stash start'

If you have a `Windows` operating system you might not have `SSH` installed.
Go ahead and download [Putty](http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe) and then connect to:

- host: `127.0.0.1`
- port: `2222`
- username: `vagrant`
- password: `vagrant`

First thing you do after connecting to the new host might be to switch to the `root`:

    $ sudo su -

Then you do not need to run commands with `sudo` prefix.
To run services type one of the following:

    $ service confluence start
    $ service jenkins start
    $ service jira start
    $ service sonar start
    $ service stash start

## Ports and Services

| Service    | HTTP | SSH  |
|:-----------|:-----|:-----|
| Confluence | 8090 | n/a  |
| Jenkins    | 8081 | n/a  |
| Jira       | 8080 | n/a  |
| SonarQube  | 9000 | n/a  |
| Stash      | 7990 | 7999 |
| PostgreSQL | 5432 | n/a  |

## Access

You may access your started service at:

    http://localhost:PORT/

Where PORT is an value from table.

## Stop Service

When you do not need the service anymore you may kill the instance to save some RAM for other tools.

    $ vagrant ssh -c 'service confluence stop'
    $ vagrant ssh -c 'service jenkins stop'
    $ vagrant ssh -c 'service jira stop'
    $ vagrant ssh -c 'service sonar stop'
    $ vagrant ssh -c 'service stash stop'

Be patient, service should start in around 60 sek. (per service)

# Stop Guest Machine

This will preserve state of the machine.

    $ vagrant halt

This will destroy the machine and free some space from your hard drive.

    $ vagrant destroy
