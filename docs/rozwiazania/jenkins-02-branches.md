# Pull Requests builds

Connect Jenkins with Stash
1. Install Stash Notifier Plugin in Jenkins
2. In Configure System - Global Jenkins System Configuration set:

| Key            | Value                  |
|:---------------|:-----------------------|
| Stash Root Url | http://localhost:7990/ |
| Stash User     | jenkins                |
| Stash Password | jenkins                |


## Pull Request Build Configuration

Dashboard -> New Item -> "Freestyle project"

| Section                | Key                    | Value                                               |
|:-----------------------|:-----------------------|:----------------------------------------------------|
|                        | Project name           | Pull Request                                        |
| Source Code Management | Source Code Management | GIT                                                 |
| Source Code Management | Repository URL         | ssh://git@localhost:7999/eco/workshop.git           |
| Source Code Management | Credentials            | jenkins                                             |
| Source Code Management | [Advanced] -> Refspec  | +refs/pull-requests/*/from:refs/remotes/origin/pr/* |
| Source Code Management | Branch Specifier       | **/pr/*                                             |
| Build Triggers         | Schedule               | * * * * *                                           |
| Post-build Actions     | Notify Stash Instance  |                                                     |


## Master Branch Build Configuration

Dashboard -> New Item -> "Freestyle project"

| Section                | Key                    | Value                                     |
|:-----------------------|:-----------------------|:------------------------------------------|
|                        | Project name           | Master                                    |
| Source Code Management | Source Code Management | GIT                                       |
| Source Code Management | Repository URL         | ssh://git@localhost:7999/eco/workshop.git |
| Source Code Management | Credentials            | jenkins                                   |
| Source Code Management | Branch Specifier       | **/master                                 |
| Build Triggers         | Schedule               | * * * * *                                 |
| Post-build Actions     | Notify Stash Instance  |                                           |

## Feature Branch Build Configuration

Dashboard -> New Item -> "Freestyle project"

| Section                | Key                    | Value                                     |
|:-----------------------|:-----------------------|:------------------------------------------|
|                        | Project name           | Feature                                   |
| Source Code Management | Source Code Management | GIT                                       |
| Source Code Management | Repository URL         | ssh://git@localhost:7999/eco/workshop.git |
| Source Code Management | Credentials            | jenkins                                   |
| Source Code Management | Branch Specifier       | */feature/*                               |
| Build Triggers         | Schedule               | * * * * *                                 |
| Post-build Actions     | Notify Stash Instance  |                                           |

# Bugfix Branch Build Configuration

Dashboard -> New Item -> "Freestyle project"

| Section                | Key                    | Value                                     |
|:-----------------------|:-----------------------|:------------------------------------------|
|                        | Project name           | Feature                                   |
| Source Code Management | Source Code Management | GIT                                       |
| Source Code Management | Repository URL         | ssh://git@localhost:7999/eco/workshop.git |
| Source Code Management | Credentials            | jenkins                                   |
| Source Code Management | Branch Specifier       | */bugfix/*                                |
| Build Triggers         | Schedule               | * * * * *                                 |
| Post-build Actions     | Notify Stash Instance  |                                           |
