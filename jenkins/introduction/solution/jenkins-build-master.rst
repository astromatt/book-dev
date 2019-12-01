Dashboard -> New Item -> "Freestyle project"

======================== ======================== =============================================
Section                  Key                      Value
======================== ======================== =============================================
                         Project name             Master
Source Code Management   Source Code Management   Git
Source Code Management   Repository URL           ssh://git@localhost:7999/eco/workshop.git
Source Code Management   Credentials              jenkins
Source Code Management   Branch Specifier         **/master
Build Triggers           Schedule                 * * * * *
Post-build Actions       Notify Stash Instance
======================== ======================== =============================================
