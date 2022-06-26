About
=====


Variables
---------
.. csv-table:: Variables
    :header: "Command", "Description"
    :widths: 20, 80

    "``$PATH``",                        "path"
    "``$IFS``",                         "field separator"
    "``${varname:-}``",                 "default value for variable (if empty)"
    "``$0``",                           "program name"
    "``$1, $2, $3, ..., $n``",          "arguments"
    "``$@``",                           "current command"
    "``$?``",                           "exit status from previous command"
    "``$PS1``",                         "prompt"


Symbols
-------
* ` - tick mark
* ``"`` - double quote

.. csv-table:: Variables
    :header: "Command", "Description"
    :widths: 20, 80

    "``!``",     ""
    "``#``",     ""
    "``$()``",   ""
    "``&&``",    ""
    "``&``",     ""
    "``'``",     ""
    "``*``",     ""
    "``+``",     ""
    "``,``",     ""
    "``-``",     ""
    "``:``",     ""
    "``;``",     ""
    "``<<``",    ""
    "``<=``",    ""
    "``<``",     ""
    "``>=``",    ""
    "``>>``",    ""
    "``>``",     ""
    "``@``",     ""
    "``[]``",    ""
    "``\\``",    ""
    "``|``",     ""
    "``||``",    ""
    "``~``",     ""



Control Flow
------------
.. csv-table:: Control Flow
    :header: "Command", "Description"
    :widths: 20, 80

    ``for ... do ... done``,          ""
    ``case ... esac``,                ""
    ``if ... then ... else ... fi``,  ""
    ``cat > ... << EOF ... EOF``,     ""
    ``while``,                        ""
    ``until``,                        ""
    ``set``,                          ""
    ``unset``,                        ""
    ``return``,                       ""
    ``getopt``,                       ""
    ``getopts``,                      ""
    ``function``,                     ""
    ``for``,                          ""
    ``fi``,                           ""
    ``false``,                        ""
    ``true``,                         ""
    ``expr``,                         ""
    ``exec``,                         ""
    ``eval``,                         ""
    ``esac``,                         ""
    ``else``,                         ""
    ``elif``,                         ""
    ``do``,                           ""
    ``done``,                         ""
    ``continue``,                     ""
    ``case``,                         ""
    ``break``,                        ""


Commands
--------
.. csv-table:: Shell Programming
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``run-parts``, "(8)",   "run scripts or programs in a directory"
    ``seq``,       "(1)",   "print a sequence of numbers"
    ``unalias``,   "",      ""
    ``unset``,     "",      ""
    ``uuidgen``,   "(1)",   "create a new UUID value"
    ``xargs``,     "(1)",   "build and execute command lines from standard input"
    ``type``,      "",      ""
    ``trap``,      "",      ""
    ``test``,      "(1)",   "check file types and compare values"
    ``source``,    "",      ""
    ``set +e``,    "",      ""
    ``set -e``,    "",      ""
    ``set``,       "",      ""
    ``sleep``,     "(1)",   "delay for a specified amount of time"
    ``sleep``,     "(3)",   "sleep for a specified number of seconds"
    ``readonly``,  "",      ""
    ``exit 0``,    "",      ""
    ``exit 1``,    "",      ""
    ``exit``,      "(2)",   "terminate the calling process"
    ``exit``,      "(3)",   "cause normal process termination"
    ``crontab``,   "(1)",   "maintain crontab files for individual users (Vixie Cron)"
    ``crontab``,   "(5)",   "tables for driving cron"
    ``cron``,      "(8)",   "daemon to execute scheduled commands (Vixie Cron)"
    ``as``,        "(1)",   "the portable GNU assembler."
    ``alias``,     "",      "Creates user defined alias"
    ``awk``,       "(1)",   "pattern scanning and processing language"
    ``basename``,  "(1)",   "strip directory and suffix from filenames"
    ``basename``,  "(3)",   "parse pathname components"
