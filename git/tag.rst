********
GIT Tags
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

    $ git tag -a -m <message>
    $ git tag -a -m "v1.0.0"

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
