*************
Jenkins About
*************


Devtools Ecosystem
==================
.. figure:: img/ecosystem-big-picture-01.png
    :scale: 50%
    :align: center

    Ecosystem Big Picture

.. figure:: img/ecosystem-big-picture-02.png
    :scale: 50%
    :align: center

    Ecosystem Big Picture

.. figure:: img/ecosystem-jenkins-tooling.png
    :scale: 50%
    :align: center

    Jenkins in Devtools Ecosystem


Architecture
============
- Local executors (default: 2)
- Remote workers via SSH and labels
- Docker build
- New UI (Blue Ocean) currently accessible as a plugin, but soon to be default
- Jenkins uses Groovy scripts in ``Jenkinsfile`` in repository main directory


Process
=======
- https://jenkins.io/
- https://jenkins.io/doc

.. figure:: img/cicd-loop.png
    :scale: 75%
    :align: center

    Continuous Integration -> Continuous Delivery -> Continuous Deployment


Notifications
=============
- Email
- Slack / HipChat
- IRC


Large repos
===========
- is a sign of git missuse, and should be tackled with Git LFS
- Use command line git rather than jGit
- command line git handles memory better
- Use reference repository (bare)
- Shallow clone (Git from 1.9+ can push from shallow clones)
- Don't fetch tags
- Narrow refspec - only clone specific branches (honor refspec on initial clone)
- Pipeline stash / unstash (sparse checkout on master node, and then stash checkout, and unstash on remotes)
- Sparse checkout (Subset of working tree - single directory [exclude or include on per file basis])
