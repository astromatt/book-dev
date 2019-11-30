*******
Crontab
*******

.. code-block:: console

    $ crontab -e
    $ crontab -l
    $ sudo crontab -e

Przykładowy crontab
===================
.. code-block:: text

    5 4 * * *       /bin/echo 'five past four a.m.'
    */10 * * * *    /bin/echo 'every ten minutes'
    5-10 4 * * *    /bin/echo 'every minute from 5-10 past four a.m.'
    * 4 * * *       /bin/echo 'every minute at 4 a.m.'
    0 14 * * *      /bin/echo 'at 2 p.m.'
    0 0 1 * *       /bin/echo 'at midnight of first day of month'
    0 0 1 JAN *     /bin/echo 'at midnight of first day of January'
    0 0 1 1 *       /bin/echo 'at midnight of first day of January'
    0 0 * * SAT,SUN /bin/echo 'at midnight on weekends'
    0 0 * * 0,6     /bin/echo 'at midnight on weekends'

    @midnight       /bin/echo 'at midnight'
    @daily          /bin/echo 'at midnight'
    @weekly         /bin/echo 'at midnight on Sunday'

    45 04 * * * /usr/bin/updatedb
    45 04 * * * /usr/sbin/chkrootkit && /usr/bin/updatedb
    00 06 * * * env DISPLAY=:0.0 gui_appname
    00 01 * * * ubuntu /home/ubuntu/script.sh


Editing ``crontab``
===================
.. code-block:: console

    export EDITOR=/usr/bin/vim


Variables
---------
.. code-block:: console

    PATH=/usr/sbin:/usr/bin:/sbin:/bin

Special characters
------------------
- ``*`` any value
- ``,`` value list separator
- ``-`` range of values
- ``/`` step values

Crontab formatting
------------------
- minute: 0-60
- hour: 0-23
- day of month: 0-31
- month: JAN-DEC / 0-12
- day of week: SUN-SAT / 0-7 (Sunday = 0 or 7)

Short notation
--------------
.. csv-table:: Short notation
    :file: data/crontab.csv
    :widths: 20, 80
    :header-rows: 1

Allowing/Denying User-Level Cron
================================
- /etc/cron.allow
- /etc/cron.deny

Files and Directories
=====================
- /etc/crontab
- /var/spool/crontab/
- /etc/cron.d/
- /etc/cron.daily/
- /etc/cron.hourly/
- /etc/cron.weekly/
- /etc/cron.monthly/

Other
=====
- z jakiego użytkownika są uruchamiane
- przekierowanie outputu stdout i stderr
- dostawanie maili
