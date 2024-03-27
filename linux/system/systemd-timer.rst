Systemd Timer
=============
* https://carrondo.pt/en/posts/2021-08-29-create-cronjob-alternative-on-ubuntu-core/
* https://silentlad.com/systemd-timers-oncalendar-(cron)-format-explained

Ubuntu Core don't have `cron` and there is no `snap` to install it,
however it is possible to create a `systemd` user timer.


Cron to Timer
-------------

.. csv-table::
    :header: "Cron", "Systemd shorthand", "Systemd timer"

    "@reboot",   "",             "OnBootSec=1s"
    "@yearly",   "yearly",       "OnCalendar=*-01-01 00:00:00"
    "@annually", "yearly",       "OnCalendar=*-01-01 00:00:00"
    "",          "semiannually", "OnCalendar=*-01,07-01 00:00:00"
    "",          "quarterly",    "OnCalendar=*-01,04,07,10-01 00:00:00"
    "@monthly",  "monthly",      "OnCalendar=*-*-01 00:00:00"
    "@weekly",   "weekly",       "OnCalendar=Sun *-*-* 00:00:00"
    "@daily",    "daily",        "OnCalendar=*-*-* 00:00:00"
    "@hourly",   "hourly",       "OnCalendar=*-*-* *:00:00"
    "@minutely", "minutely",     "OnCalendar=*-*-* *:*:00"

.. csv-table::
    :header: "Systemd timestamp", "Systemd normalized form"

    "Sat,Thu,Mon..Wed,Sat..Sun",     "Mon..Thu,Sat,Sun *-*-* 00:00:00"
    "Mon,Sun 12-*-* 2,1:23",         "Mon,Sun 2012-*-* 01,02:23:00"
    "Wed *-1",                       "Wed *-*-01 00:00:00"
    "Wed..Wed,Wed *-1",              "Wed *-*-01 00:00:00"
    "Wed, 17:48",                    "Wed *-*-* 17:48:00"
    "Wed..Sat,Tue 12-10-15 1:2:3",   "Tue..Sat 2012-10-15 01:02:03"
    "*-*-7 0:0:0",                   "*-*-07 00:00:00"
    "10-15",                         "*-10-15 00:00:00"
    "monday *-12-* 17:00",           "Mon *-12-* 17:00:00"
    "Mon,Fri *-*-3,1,2 *:30:45",     "Mon,Fri *-*-01,02,03 *:30:45"
    "12,14,13,12:20,10,30",          "*-*-* 12,13,14:10,20,30:00"
    "12..14:10,20,30",               "*-*-* 12..14:10,20,30:00"
    "mon,fri *-1/2-1,3 *:30:45",     "Mon,Fri *-01/2-01,03 *:30:45"
    "03-05 08:05:40",                "*-03-05 08:05:40"
    "08:05:40",                      "*-*-* 08:05:40"
    "05:40",                         "*-*-* 05:40:00"
    "Sat,Sun 12-05 08:05:40",        "Sat,Sun *-12-05 08:05:40"
    "Sat,Sun 08:05:40",              "Sat,Sun *-*-* 08:05:40"
    "2003-03-05 05:40",              "2003-03-05 05:40:00"
    "05:40:23.4200004/3.1700005",    "*-*-* 05:40:23.420000/3.170001"
    "2003-02..04-05",                "2003-02..04-05 00:00:00"
    "2003-03-05 05:40 UTC",          "2003-03-05 05:40:00 UTC"
    "2003-03-05",                    "2003-03-05 00:00:00"
    "03-05",                         "*-03-05 00:00:00"
    "hourly",                        "*-*-* *:00:00"
    "daily",                         "*-*-* 00:00:00"
    "daily UTC",                     "*-*-* 00:00:00 UTC"
    "monthly",                       "*-*-01 00:00:00"
    "weekly",                        "Mon *-*-* 00:00:00"
    "weekly Pacific/Auckland",       "Mon *-*-* 00:00:00 Pacific/Auckland"
    "yearly",                        "*-01-01 00:00:00"
    "annually",                      "*-01-01 00:00:00"
    "*:2/3",                         "*-*-* *:02/3:00"
    "Fri 2012-11-23 11:12:13",       "Fri 2012-11-23 11:12:13"
    "2012-11-23 11:12:13",           "Fri 2012-11-23 11:12:13"
    "2012-11-23 11:12:13 UTC",       "Fri 2012-11-23 19:12:13"
    "2012-11-23T11:12:13Z",          "Fri 2012-11-23 19:12:13"
    "2012-11-23T11:12+02:00",        "Fri 2012-11-23 17:12:00"
    "2012-11-23",                    "Fri 2012-11-23 00:00:00"
    "12-11-23",                      "Fri 2012-11-23 00:00:00"
    "11:12:13",                      "Fri 2012-11-23 11:12:13"
    "11:12",                         "Fri 2012-11-23 11:12:00"
    "now",                           "Fri 2012-11-23 18:15:22"
    "today",                         "Fri 2012-11-23 00:00:00"
    "today UTC",                     "Fri 2012-11-23 16:00:00"
    "yesterday",                     "Fri 2012-11-22 00:00:00"
    "tomorrow",                      "Fri 2012-11-24 00:00:00"
    "tomorrow Pacific/Auckland",     "Thu 2012-11-23 19:00:00"
    "+3h30min",                      "Fri 2012-11-23 21:45:22"
    "-5s",                           "Fri 2012-11-23 18:15:17"
    "11min ago",                     "Fri 2012-11-23 18:04:22"
    "@1395716396",                   "Tue 2014-03-25 03:59:56"

You may also use these shorthand expressions: quarterly, or semiannually.


Minutely
--------
.. code-block:: console

    $ sudo tee /etc/systemd/system/run-minutely.service << EOF

    [Unit]
    Description=Run all scripts in /home/cron/minutely
    AssertPathExists=/home/cron/minutely

    [Service]
    ExecStart=/usr/bin/find /home/cron/minutely/ -type f,l -print -exec {} \;
    Type=simple
    User=root

    EOF

.. code-block:: console

    $ sudo tee /etc/systemd/system/run-minutely.timer << EOF

    [Unit]
    Description=Run all scripts in /home/cron/minutely

    [Timer]
    OnCalendar=minutely
    Unit=run-minutely.service

    [Install]
    WantedBy=timers.target

    EOF

.. code-block:: console

    $ sudo mkdir -p /home/cron/minutely
    $ sudo systemctl start run-minutely.service
    $ sudo systemctl enable --now run-minutely.timer
    $ sudo systemctl status run-minutely
    $ sudo systemctl list-timers


Hourly
------
.. code-block:: console

    $ sudo tee /etc/systemd/system/run-hourly.service << EOF

    [Unit]
    Description=Run all scripts in /home/cron/hourly
    AssertPathExists=/home/cron/hourly

    [Service]
    ExecStart=/usr/bin/find /home/cron/hourly/ -type f,l -print -exec {} \;
    Type=simple
    User=root

    EOF

.. code-block:: console

    $ sudo tee /etc/systemd/system/run-hourly.timer << EOF

    [Unit]
    Description=Run all scripts in /home/cron/hourly

    [Timer]
    OnCalendar=hourly
    Unit=run-hourly.service

    [Install]
    WantedBy=timers.target

    EOF

.. code-block:: console

    $ sudo mkdir -p /home/cron/hourly
    $ sudo systemctl start run-hourly.service
    $ sudo systemctl enable --now run-hourly.timer
    $ sudo systemctl status run-hourly
    $ sudo systemctl list-timers


Daily
-----
.. code-block:: console

    $ sudo tee /etc/systemd/system/run-daily.service << EOF

    [Unit]
    Description=Run all scripts in /home/cron/daily
    AssertPathExists=/home/cron/daily

    [Service]
    ExecStart=/usr/bin/find /home/cron/daily/ -type f,l -print -exec {} \;
    Type=simple
    User=root

    EOF

.. code-block:: console

    $ sudo tee /etc/systemd/system/run-daily.timer << EOF

    [Unit]
    Description=Run all scripts in /home/cron/daily

    [Timer]
    OnCalendar=daily
    Unit=run-daily.service

    [Install]
    WantedBy=timers.target

    EOF

.. code-block:: console

    $ sudo mkdir -p /home/cron/daily
    $ sudo systemctl start run-daily.service
    $ sudo systemctl enable --now run-daily.timer
    $ sudo systemctl status run-daily
    $ sudo systemctl list-timers


Weekly
------
.. code-block:: console

    $ sudo tee /etc/systemd/system/run-weekly.service << EOF

    [Unit]
    Description=Run all scripts in /home/cron/weekly
    AssertPathExists=/home/cron/weekly

    [Service]
    ExecStart=/usr/bin/find /home/cron/weekly/ -type f,l -print -exec {} \;
    Type=simple
    User=root

    EOF

.. code-block:: console

    $ sudo tee /etc/systemd/system/run-weekly.timer << EOF

    [Unit]
    Description=Run all scripts in /home/cron/weekly

    [Timer]
    OnCalendar=weekly
    Unit=run-weekly.service

    [Install]
    WantedBy=timers.target

    EOF

.. code-block:: console

    $ sudo mkdir -p /home/cron/weekly
    $ sudo systemctl start run-weekly.service
    $ sudo systemctl enable --now run-weekly.timer
    $ sudo systemctl status run-weekly
    $ sudo systemctl list-timers


Monthly
-------
.. code-block:: console

    $ sudo tee /etc/systemd/system/run-monthly.service << EOF

    [Unit]
    Description=Run all scripts in /home/cron/monthly
    AssertPathExists=/home/cron/monthly

    [Service]
    ExecStart=/usr/bin/find /home/cron/monthly/ -type f,l -print -exec {} \;
    Type=simple
    User=root

    EOF

.. code-block:: console

    $ sudo tee /etc/systemd/system/run-monthly.timer << EOF

    [Unit]
    Description=Run all scripts in /home/cron/monthly

    [Timer]
    OnCalendar=monthly
    Unit=run-monthly.service

    [Install]
    WantedBy=timers.target

    EOF

.. code-block:: console

    $ sudo mkdir -p /home/cron/monthly
    $ sudo systemctl start run-monthly.service
    $ sudo systemctl enable --now run-monthly.timer
    $ sudo systemctl status run-monthly
    $ sudo systemctl list-timers


Remove Service and Timers
-------------------------
.. code-block:: console

    $ NAME="myservice"

    $ sudo systemctl stop $NAME.timer
    $ sudo systemctl disable $NAME.timer
    $ sudo rm /etc/systemd/system/$NAME.timer
    $ sudo rm /etc/systemd/system/$NAME.timer
    $ sudo rm /usr/lib/systemd/system/$NAME.timer
    $ sudo rm /usr/lib/systemd/system/$NAME.timer
    $ sudo rm rm ~/.config/systemd/$NAME.timer

    $ sudo systemctl stop $NAME.service
    $ sudo systemctl disable $NAME.service
    $ sudo rm /etc/systemd/system/$NAME.service
    $ sudo rm /etc/systemd/system/$NAME.service
    $ sudo rm /usr/lib/systemd/system/$NAME.service
    $ sudo rm /usr/lib/systemd/system/$NAME.service
    $ sudo rm rm ~/.config/systemd/$NAME.service

    $ sudo systemctl daemon-reload
    $ sudo systemctl reset-failed
