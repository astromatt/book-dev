Redirection Commands
====================


Descriptors
-----------
* 0 or ``/dev/stdin`` - standard input
* 1 or ``/dev/stdout`` - standard output
* 2 or ``/dev/stderr`` - standard error


Redirection
-----------
.. csv-table:: Redirection Commands [#1]_
    :widths: 20, 80
    :header: "Command", "Description"

    ``cmd > file``, "Output of cmd is redirected to file"
    ``cmd < file``, "Program cmd reads its input from file"
    ``cmd >> file``, "Output of cmd is appended to file"
    ``n > file``, "Output from stream with descriptor n redirected to file"
    ``n >> file``, "Output from stream with descriptor n appended to file"
    ``n >& m``, "Merges output from stream n with stream m"
    ``n >&-``, "Discards output from stream n"
    ``n <& m``, "Merges input from stream n with stream m"
    ``<< tag``, "Standard input comes from here through next tag at the start of line"
    ``|``, "Takes output from one program, or process, and sends it to another"


References
----------
.. [#1] Retrieved: 2021-11-10. URL: https://www.tutorialspoint.com/unix/unix-io-redirections.htm
