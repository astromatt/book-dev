Security
========
* ``libreSSL``
* ``uuid``


Random
------
* ``/etc/ca-certificates``
* ``/dev/random``
* ``/dev/urandom``
* ``/dev/null``
* ``/etc/sudoers.d``


/dev/random vs /dev/urandom
---------------------------
* Using ``/dev/urandom`` is preferred in the vast majority of cases
* Both are fed by the same ``CSPRNG`` to generate randomness
* ``/dev/urandom`` will never block
* ``/dev/random`` blocks when it runs out of entropy, so reading from it can halt process execution

The amount of entropy is conservatively estimated, but not counted.
In rare cases very shortly after boot, the CSPRNG may not have had
enough entropy to be properly seeded and ``/dev/urandom`` may not
produce high-quality randomness. Entropy running low is not a problem
if the ``CSPRNG`` was initially seeded properly. The ``CSPRNG`` is being
constantly re-seeded. In Linux 4.8 and onward, ``/dev/urandom`` does not
deplete the entropy pool (used by ``/dev/random``) but uses the ``CSPRNG``
output from upstream. [#stackexchangeRandomUrandom]_


Commands
--------
* ``head -c 100 /dev/urandom`` - read 100 bytes from ``/dev/urandom``
* ``dd count=100 bs=1 if=/dev/urandom 2>/dev/null``
* ``dd count=100 bs=1 if=/dev/urandom 2>&-``

.. csv-table:: Security, Crypt and Hashing
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``hash``,           "(3)",      "hash database access method"
    ``gpg``,            "(1)",      "OpenPGP encryption and signing tool"
    ``md5sum``,         "(1)",      "compute and check MD5 message digest"
    ``openssl``,        "(1ssl)",   "OpenSSL command line program"
    ``sha1sum``,        "(1)",      "compute and check SHA1 message digest"
    ``sha256sum``,      "(1)",      "compute and check SHA256 message digest"
    ``sha512sum``,      "(1)",      "compute and check SHA512 message digest"
    ``shasum``,         "(1)",      "Print or Check SHA Checksums"
    ``base64``,         "(1)",      "base64 encode/decode data and print to standard output"
    ``jacktheripper``,  "",         ""


References
----------
.. [#stackexchangeRandomUrandom] Hale, T. When to use /dev/random vs /dev/urandom. Year: 2016. Retrieved: 2022-06-28. URL: https://unix.stackexchange.com/a/324210
