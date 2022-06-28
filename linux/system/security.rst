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
