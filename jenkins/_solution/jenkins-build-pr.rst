**************************
Jenkins Build Pull Request
**************************

Dashboard -> New Item -> "Freestyle project"

======================== ======================== =======================================================
Section                   Key                      Value
======================== ======================== =======================================================
                         Project name             Pull Request
Source Code Management   Source Code Management   Git
Source Code Management   Repository URL           ssh://git@localhost:7999/eco/workshop.git
Source Code Management   Credentials              jenkins
Source Code Management   [Advanced] -> Refspec    +refs/pull-requests/*/from:refs/remotes/origin/pr/*
Source Code Management   Branch Specifier         \**/pr/*
Build Triggers           Schedule                 * * * * *
Post-build Actions       Notify Stash Instance
======================== ======================== =======================================================
