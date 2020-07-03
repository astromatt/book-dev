********
Git Tags
********


About Tags
==========
* ``.git/refs/tags/*``


Using
=====

Create Tag
----------
* ``-a``, ``--annotate`` - annotated tag, needs a message
* ``-m``, ``--message <message>`` - tag message

.. code-block:: console

    $ git tag -a <tag> -m <message>
    $ git tag -a "v1.0.0" -m "Released on 1970-01-01"

Show Tags
---------
.. code-block:: console

$ git show v1.0.0
tag v1.0.0
Tagger: Mark Watney <mark.watney@nasa.gov>
Date:   Thu Jan 1 00:00:00 1970 +0000

released on 1970-01-01

commit 55c83ab01f804a450f9e4d6b3550c87542703937 (HEAD -> master, tag: v1.0.0, origin/master, origin/HEAD)
Author: Mark Watney <mark.watney@nasa.gov>
Date:   Thu Jan 1 00:00:00 1970 +0000

    content from master branch

diff --git a/myfile.txt b/myfile.txt
index 046820b..08ac55e 100644
--- a/myfile.txt
+++ b/myfile.txt
@@ -1 +1 @@
-Some Old Content
+And Now for Something Completely Different

List Tags
---------
* ``-l``, ``--list`` - list tag names
* ``-n[<n>]`` - print <n> lines of each tag message

.. code-block:: console

    $ git tag -l

Delete Tag
----------
* ``-d``, ``--delete`` - delete tags

.. code-block:: console

    $ git tag -d <tag-name>


Signing
=======

Sign
----
* ``-s``, ``--sign`` - annotated and GPG-signed tag

.. code-block:: console

    $ git tag -s <key-path>

Verify Tag
----------
* ``-v``, ``--verify`` -  verify tags

.. code-block:: console

    $ git tag -v <tag-name>

Describe
========
.. code-block:: console

    $ git describe


Push
====
.. code-block:: console

    $ git push origin <tag-name>
    $ git push --tags
