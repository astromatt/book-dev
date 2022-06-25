Processes
=========
* ``&`` - Spawning


PID
---
* PID files
* ``pidof``
* ``/var/spool/pid``


Problems
--------
* Deadlock
* Starvation
* Race Condition


Killing
-------
* ``kill``
* ``kill -9``
* ``killall``


Keyboard Shortcuts
------------------
* ``ctrl+c``
* ``ctrl+d``
* ``^% - escape sequence``


Priorities
----------
* ``nice``


Commands
--------
.. csv-table:: Processes
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``htop``,       "(1)",      "interactive process viewer"
    ``jobs``,       "",         ""
    ``kill -9``,    "",         ""
    ``kill``,       "(1)",      "send a signal to a process"
    ``kill``,       "(2)",      "send signal to a process"
    ``killall``,    "(1)",      "kill processes by name"
    ``lxc``,        "",         ""
    ``memusage``,   "(1)",      "profile memory usage of a program"
    ``nice``,       "(1)",      "run a program with modified scheduling priority"
    ``nice``,       "(2)",      "change process priority"
    ``nohup``,      "(1)",      "run a command immune to hangups, with output to a non-tty"
    ``nproc``,      "(1)",      "print the number of processing units available"
    ``pidof``,      "(8)",      "find the process ID of a running program."
    ``pidwait``,    "(1)",      "look up, signal, or wait for processes based on name and other attributes"
    ``pkill``,      "(1)",      "look up, signal, or wait for processes based on name and other attributes"
    ``pkill``,      "(3pm)",    "Kill all instances of a process by pattern matching the command-line"
    ``pmap``,       "(1)",      "report memory map of a process"
    ``ps aux``,     "",         ""
    ``ps``,         "(1)",      "report a snapshot of the current processes."
    ``pslog``,      "(1)",      "report current logs path of a process"
    ``pstree``,     "(1)",      "display a tree of processes"
    ``renice``,     "(1)",      "alter priority of running processes"
    ``screen``,     "(1)",      "screen manager with VT100/ANSI terminal emulation"
    ``skill``,      "(1)",      "send a signal or report process status"
    ``time``,       "(1)",      "run programs and summarize system resource usage"
    ``time``,       "(2)",      "get time in seconds"
    ``time``,       "(7)",      "overview of time and timers"
    ``timeout``,    "(1)",      "run a command with a time limit"
    ``times``,      "(2)",      "get process times"
    ``top``,        "(1)",      "display Linux processes"
    ``wait``,       "(2)",      "wait for process to change state"
    ``watch``,      "(1)",      "execute a program periodically, showing output fullscreen"
    ``fork``,       "(3am)",    "basic process management"
    ``fg``,         "",         "move process to foreground"
    ``bg``,         "",         "move process to background"
    ``free``,       "(3)",      "allocate and free dynamic memory"
