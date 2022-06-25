Manuals
=======
* ``man``
* ``-h`` or ``--help``
* Kernel Documentation [#kerneldoc]_

.. code-block:: text

    1   Executable programs or shell commands
    2   System calls (functions provided by the kernel)
    3   Library calls (functions within program libraries)
    4   Special files (usually found in /dev)
    5   File formats and conventions, e.g. /etc/passwd
    6   Games
    7   Miscellaneous  (including macro packages and conventions),
       e.g. man(7), groff(7), man-pages(7)
    8   System administration commands (usually only for root)
    9   Kernel routines [Non standard]

Conventional section names include NAME, SYNOPSIS,  CONFIGURA‐
TION, DESCRIPTION, OPTIONS, EXIT STATUS, RETURN VALUE, ERRORS,
ENVIRONMENT, FILES, VERSIONS, CONFORMING TO, NOTES, BUGS,  EX‐
AMPLE, AUTHORS, and SEE ALSO.


Commands
--------
.. csv-table:: Documentation
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``man``,                        "(1)",              "an interface to the system reference manuals"
    ``man``,                        "(7)",              "macros to format man pages"
    ``apropos``,                    "(1)",              "search the manual page names and descriptions"
    ``whatis``,                     "(1)",              "display one-line manual page descriptions"
    ``whereis``,                    "(1)",              "locate the binary, source, and manual page files for a command"
    ``which``,                      "(1)",              "locate a command"


References
----------
.. [#kerneldoc] Linux Kernel Organization, Inc. The Linux Kernel documentation. Year: 2019. Retrieved: 2019-01-23. URL: https://www.kernel.org/doc/html/latest/
