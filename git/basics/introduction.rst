****************
GIT Introduction
****************


About Version Control
=====================
* :cite:`GITDocumentation`

Why we have Version Control?
----------------------------

Centralized vs. Decentralized
-----------------------------
#. Centralized:

    * Single truth
    * Simple revision numbers
    * Timeline is always straight
    * Single point of failure
    * Simpler branches
    * Small number of branches

#. Decentralized

    * Unable to use incremented int as revision numbers
    * Use hashes
    * All repositories are equal
    * Any repository can have different history
    * More diverged branches
    * Can have many branches


Design Philosophy
=================
#. Tracking file permissions
#. Tracking file renames and moves
#. Key-Value Storage of Immutable Objects
#. Working Offline
#. Efficient Storage


Assignments
===========

SSH key
-------
#. Create and login to Github account
#. If you don't have ``.ssh/id_rsa`` lub ``.ssh/id_rsa.pub`` run command ``ssh-keygen``
#. Add ``your.email@example.com/hostname`` to the end of your public key ``~/.ssh/id_rsa.pub`` (as a comment)
#. Add ``ssh`` public key ``~/.ssh/id_rsa.pub`` to Github profile

Repository Hosting
------------------
#. create accounts
#. create repo
#. protect branches
#. add collaborators
#. clone & touch .gitignore & push
#. pull-request
