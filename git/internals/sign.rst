***************
GIT Commit Sign
***************


.. code-block:: console
    :caption: Install GPG

    $ brew install gpg
    # Installs GPG on Mac

    $ sudo apt install gpg2
    # Installs GPG on Linux

.. code-block:: console
    :caption: Set environment variable

    $ echo 'export GPG_TTY=$(tty)' >> ~/.profile

.. code-block:: console
    :caption: Generate GPG key

    $ gpg --full-generate-key
    * Select RSA and DSA
    * Use 4096 bits
    * 0 = key does not expire

.. code-block:: console
    :caption: Add GPG key to GIT

    $ gpg --list-secret-keys --keyid-format LONG
    /Users/myuser/.gnupg/secring.gpg
    ------------------------------------
    sec   rsa4096/3AA5C34371567BD2 1970-01-01 [SC]
    uid                 [ultimate] Mark Watney <mark.watney@nasa.gov>
    ssb   rsa4096/42B317FD4BA89E7A 1970-01-01 [E]

    # In this example, the GPG key ID is 3AA5C34371567BD2

    $ git config --global user.signingkey 3AA5C34371567BD2
    $ git config --global commit.gpgsign true

.. code-block:: console
    :caption: Add GPG key to GitHub

    $ gpg --armor --export 3AA5C34371567BD2
    # Copy output of the GPG key ID, in ASCII armor format
    # Copy with -----BEGIN PGP PUBLIC KEY BLOCK----- and -----END PGP PUBLIC KEY BLOCK-----

    $ open https://github.com/settings/gpg/new
    # Paste GPG key ID, in ASCII armor format (from previous step)


.. code-block:: console
    :caption: Commit files using ``-S``. Commits should be signed automatically if ``git config commit.gpgsign`` is set to ``true`` (no need to use ``-S`` each time)

    $ git commit -S -am "My Commit Message"

.. note:: Some GPG installations on Linux may require you to use ``gpg2 --list-keys --keyid-format LONG`` to view a list of your existing keys instead. In this case you will also need to configure Git to use gpg2 by running ``git config --global gpg.program gpg2``.
