Redirection Commands
====================


Descriptors
-----------
* 0 is normally standard input (STDIN),
* 1 is standard output (STDOUT),
* 2 is standard error output (STDERR).


Redirection
-----------
.. csv-table:: Redirection Commands [#1]_
    :widths: 5, 15, 80
    :header: "Sr.No.", "Command", "Description"

    "1", `pgm > file`, "Output of pgm is redirected to file"
    "2", `pgm < file`, "Program pgm reads its input from file"
    "3", `pgm >> file`, "Output of pgm is appended to file"
    "4", `n > file`, "Output from stream with descriptor n redirected to file"
    "5", `n >> file`, "Output from stream with descriptor n appended to file"
    "6", `n >& m`, "Merges output from stream n with stream m"
    "7", `n <& m`, "Merges input from stream n with stream m"
    "8", `<< tag`, "Standard input comes from here through next tag at the start of line"
    "9", `|`, "Takes output from one program, or process, and sends it to another"


References
----------
.. [#1] Retrieved: 2021-11-10. URL: https://www.tutorialspoint.com/unix/unix-io-redirections.htm
