Date
====


Paths
-----
* ``/etc/timezone``
* ``/etc/localtime``


Date Formatting
---------------
.. csv-table:: Date and time parsing parameters
    :widths: 5, 35, 60
    :header: "Directive", "Example", "Meaning"

    "``%a``", "Sun, Mon, ..., Sat", "Weekday as locale's abbreviated name"
    "``%A``", "Sunday, Monday, ..., Saturday (en_US)", "Weekday as locale's full name"
    "``%w``", "0, 1, ..., 6", "Weekday as a decimal number, where 0 is Sunday and 6 is Saturday"
    "``%d``", "01, 02, ..., 31", "Day of the month as a zero-padded decimal number"
    "``%b``", "Jan, Feb, ..., Dec (en_US)", "Month as locale's abbreviated name"
    "``%B``", "January, February, ..., December (en_US)", "Month as locale's full name"
    "``%m``", "01, 02, ..., 12", "Month as a zero-padded decimal number"
    "``%y``", "00, 01, ..., 99", "Year without century as a zero-padded decimal number"
    "``%Y``", "0001, 0002, ..., 2013, 2014, ..., 9998, 9999", "Year with century as a decimal number"
    "``%H``", "00, 01, ..., 23", "Hour (24-hour clock) as a zero-padded decimal number"
    "``%I``", "01, 02, ..., 12", "Hour (12-hour clock) as a zero-padded decimal number"
    "``%p``", "AM, PM (en_US)", "Locale's equivalent of either AM or PM"
    "``%M``", "00, 01, ..., 59", "Minute as a zero-padded decimal number"
    "``%S``", "00, 01, ..., 59", "Second as a zero-padded decimal number"
    "``%f``", "000000, 000001, ..., 999999", "Microsecond as a decimal number, zero-padded on the left"
    "``%z``", "(empty), +0000, -0400, +1030", "UTC offset in the form +HHMM or -HHMM (empty string if the object is naive)"
    "``%Z``", "(empty), UTC, EST, CST", "Time zone name (empty string if the object is naive)"
    "``%j``", "001, 002, ..., 366", "Day of the year as a zero-padded decimal number"
    "``%U``", "00, 01, ..., 53", "Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0"
    "``%W``", "00, 01, ..., 53", "Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0"
    "``%c``", "Tue Aug 16 21:30:00 1988 (en_US)", "Locale's appropriate date and time representation"
    "``%x``", "08/16/1988 (en_US); 16.08.1988 (de_DE)", "Locale's appropriate date representation"
    "``%X``", "21:30:00", "Locale's appropriate time representation"
    "``%%``", "%", "A literal ``%`` character"
    "``%G``", "0001, 0002, ..., 2013, 2014, ..., 9998, 9999", "ISO 8601 year with century representing the year that contains the greater part of the ISO week (``%V``)"
    "``%u``", "1, 2, ..., 7", "ISO 8601 weekday as a decimal number where 1 is Monday"
    "``%V``", "01, 02, ..., 53", "ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4"

.. csv-table:: Leading Zero
    :widths: 70, 15, 15
    :header: "Meaning", "With", "Without"

    "day",                          ``%d``, ``%-d``
    "hour 24h",                     ``%H``, ``%-H``
    "hour 12h",                     ``%I``, ``%-I``
    "day of a year",                ``%j``, ``%-j``
    "month",                        ``%m``, ``%-m``
    "minute",                       ``%M``, ``%-M``
    "second",                       ``%S``, ``%-S``
    "week number (Sunday first)",   ``%U``, ``%-U``
    "week number (Monday first)",   ``%W``, ``%-W``
    "weekday (Sunday first)",       ``%w``, ``%-w``
    "year short",                   ``%y``, ``%-y``
    "year long",                    ``%Y``, ``%-Y``


Date
----
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
