Crontab
=======
* Execute scheduled commands
* Can redirect Stderr and Stdout
* Cron will email you not redirected output
* https://cron.help/


Files
-----
* ``/etc/crontab``
* ``/etc/cron.allow`` - Allow User-Level Cron
* ``/etc/cron.deny`` - Deny User-Level Cron
* ``cat /var/log/syslog`` - Logs


Directories
-----------
* ``/etc/cron.d/``
* ``/etc/cron.daily/``
* ``/etc/cron.hourly/``
* ``/etc/cron.monthly/``
* ``/etc/cron.weekly/``
* ``/var/spool/cron/crontabs/``


Output Redirect
---------------
* ``1 > /dev/null`` - stdout to ``/dev/null``
* ``2 > /dev/null`` - stderr to ``/dev/null``
* ``1>/dev/null 2>&1`` - stdout to ``/dev/null`` and stderr to the same as stdout


Commands
--------
* ``crontab -e``
* ``crontab -l``

.. code-block:: console

    $ export EDITOR=/usr/bin/vim
    $ crontab -e


Variables
---------
.. code-block:: sh

    PATH=/usr/sbin:/usr/bin:/sbin:/bin


Syntax
------
* https://cron.help/
* ``*`` any value
* ``,`` value list separator
* ``-`` range of values
* ``/`` step values


Time
----
* minute: 0-59
* hour: 0-23
* day of month: 0-31
* month: JAN-DEC / 0-12
* day of week: SUN-SAT / 0-7 (Sunday = 0 or 7)


Recurrence
----------
* ``@hourly`` - Run once an hour ``0 * * * *``
* ``@daily`` - Run once a day ``0 0 * * *``
* ``@weekly`` - Run once a week ``0 0 * * 0``
* ``@monthly`` - Run once a month ``0 0 1 * *``
* ``@yearly`` - Run once a year, ``0 0 1 1 *``
* ``@reboot`` - Run once, at startup
* ``@midnight`` - Same as ``@daily``
* ``@annually`` - Same as ``@yearly``


Example
-------
.. code-block:: text

    SHELL=/bin/sh
    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

    # Example of job definition:
    # .---------------- minute (0 - 59)
    # |  .------------- hour (0 - 23)
    # |  |  .---------- day of month (1 - 31)
    # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
    # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
    # |  |  |  |  |
    # *  *  *  *  * user-name command to be executed
    17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
    25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
    47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
    52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )


Use Case - 0x01
---------------
* ``/var/spool/cron/crontabs/``
* ``crontab -e``

.. code-block:: text

    @midnight       /bin/echo 'at midnight'
    @daily          /bin/echo 'at midnight'
    @weekly         /bin/echo 'at midnight on Sunday'


Use Case - 0x02
---------------
* ``/var/spool/cron/crontabs/``
* ``crontab -e``

.. code-block:: text

    00 5 * * * /usr/bin/updatedb


Use Case - 0x03
---------------
* ``/var/spool/cron/crontabs/``
* ``crontab -e``

.. code-block:: text

    05 4 * * *       /bin/echo 'five past four a.m.'
    */10 * * * *     /bin/echo 'every ten minutes'
    05-10 4 * * *    /bin/echo 'every minute from 5-10 past four a.m.'
    * 4 * * *        /bin/echo 'every minute at 4 a.m.'
    00 14 * * *      /bin/echo 'at 2 p.m.'
    00 0 1 * *       /bin/echo 'at midnight of first day of month'
    00 0 1 JAN *     /bin/echo 'at midnight of first day of January'
    00 0 1 1 *       /bin/echo 'at midnight of first day of January'
    00 0 * * SAT,SUN /bin/echo 'at midnight on weekends'
    00 0 * * 0,6     /bin/echo 'at midnight on weekends'


Use Case - 0x04
---------------
* ``/var/spool/cron/crontabs/``
* ``crontab -e``

.. code-block:: text

    # Book Python
    00  * * * * *     /Users/mwatney/book-python/.venv-py310/bin/python /Users/mwatney/book-python/bin/make-notes.py 1>/dev/null 2>&1
    05  * * * * *     /Users/mwatney/book-python/.venv-py310/bin/python /Users/mwatney/book-python/bin/make-assignments.py 1>/dev/null 2>&1
