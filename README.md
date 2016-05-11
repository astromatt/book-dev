# Developer Tools Ecosystem Workshop

## Hardware Requirements

Minimum:
- 2 CPU Cores
- 4 GB RAM
- 10 GB free disk space

Optimal:
- 4 CPU Cores
- 8 GB RAM
- 20 GB free disk space

## Clone the Repository with Submodules

    $ git clone --recursive https://github.com/MattAgile/ecosystem-workshop.git

## Install Dependencies

- Download and install [Virtualbox](https://www.virtualbox.org/wiki/Downloads) == 5.0
- Download and install [Vagrant](https://www.vagrantup.com/downloads.html) == 1.8

## Configure Guest Environment

Edit `Vagrantfile` and adjust number of CPUs and RAM for your new host.
Remember that each tool while running takes around 700MB of RAM.
If you have one or two Cores in your laptop, adjust number of Guest OS cores.

Default settings are:
- CPU = 2
- RAM = 8196

## Test your configuration and run

At the workshop you'll receive an Developer Tools Ecosystem already set-up and configured!
All you need is cloned git repository and `ecosystem.box` image in root folder (`./ecosystem-workshop`).
Otherwise you can set up your own ecosystem-workshop.

For that check documentation in `./docs` folder and follow those instructions for each service you want to install.

Be sure that no services on the host machine is running on those ports:

- 8088
- 8443
- 7990 (Stash)
- 7999 (SSH Stash)
- 8080 (Jira)
- 8081 (Jenkins)
- 8090 (Confluence)
- 9000 (SonarQube)
- 5432 (PostgreSQL)
- 3306 (MySQL)

Otherwise you will not be able to run Guest Ecosystem or you have to change `Vagrantfile`.

Then to run this you have to simply type:

    $ vagrant up

Warning: if you see warning message like this: `Warning: Authentication failure. Retrying...` exit the process(`ctrl+c` on `Linux/Windows` or `cmd+c` on `OS X`) and start `ssh` connection by:

    $ vagrant ssh

If you want to setup your own ecosystem from scratch, read the following instructions in `docs/how-to-setup-new-box.md` file.
