Date
====


Paths
-----
* ``/etc/timezone``
* ``/etc/localtime``


Date
----
* https://python.astrotech.io/intermediate/datetime/format.html#parameters

.. code-block:: console

    $ date -I
    1969-07-21

    $ date -Iseconds
    1969-07-21T02:56:15+00:00

.. code-block:: console

    $ date +"%F %H:%M:%S %Z"
    1969-07-21 02:56:15 UTC

.. code-block:: console

    $ date +%s
    1234567890

    $ date -d @1234567890
    Sat Feb 14 00:31:30 CET 2009

.. code-block:: console

    $ date -u
    Mon Jul 21 02:56:15 UTC 1969

    $ date -d '-10 min'
    Mon Jul 21 02:46:15 UTC 1969

.. code-block:: console

    $ TZ=UTC date
    Mon Jul 21 02:56:15 UTC 1969

    $ TZ=CET date
    Mon Jul 21 04:56:15 CEST 1969

    $ TZ=GMT date
    Mon Jul 21 02:56:15 GMT 1969


Unix Timestamp
--------------
* Seconds since midnight of January 1st, 1970 (1970-01-01 00:00:00 UTC)
* Unix era, also known as "epoch"
* In most systems represented as 32-bit integer
* Max value is 2,147,483,647 (2038-01-19 03:14:07 UTC)
* Min value is -2,147,483,647 (1902-12-13 20:45:53 UTC)
* If you add 1 to max value, you will get overflow to min value
* Linux kernel 5.6 (released 29 March 2020) has a fix for this problem so that 32-bit systems can run beyond the year 2038
* https://itsfoss.com/linux-kernel-5-6/
* https://lore.kernel.org/lkml/CAHk-=wi9ZT7Stg-uSpX0UWQzam6OP9Jzz6Xu1CkYu1cicpD5OA@mail.gmail.com/

.. code-block:: console

    $ TZ=UTC date +%s
    1234567890

    $ TZ=CET date +%s
    1234567890

    $ TZ=GMT date +%s
    1234567890


Commands
--------
* ``tzconfig`` -
* ``tzselect`` - view timezones
* ``tzselect`` - select a timezone
* ``date`` - print or set the system date and time
* ``date +%F`` -
* ``date --iso-8601``
* ``date -Ins``
* ``date -I`` - ISO 8601  (YYY-MM-DD)
* ``date -Iseconds``
* ``date +%s`` - timestamp, seconds since: 1970-01-01T00:00:00.000000+00:00
* ``date -d @1234567890``
* ``date --date='-90 minute' -Iseconds``
* ``date --date='-10 min'`` -
