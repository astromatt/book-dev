Trap
====
* https://phoenixnap.com/kb/bash-trap-command
* `options` provide added functionality to the command.
* `arguments` are the commands trap executes upon detecting a signal. Unless the command is only one word, it should be enclosed with quotation marks (" "). If the argument contains more than one command, separate them with a semicolon (;).
* `signals` are asynchronous notifications sent by the system, usually indicating a user-generated or system-related interruption. Signals can be called by their name or number.

.. code-block:: text

    trap [options] "[arguments]" [signals]


Most Common
-----------
* SIGHUP (1) - Clean tidy-up
* SIGINT (2) - Interrupt
* SIGQUIT (3) - Quit
* SIGABRT (6) - Cancel
* SIGALRM (14) - Alarm clock
* SIGTERM (15) - Terminate


All
---
* ``trap -p`` - Displays signal commands
* ``trap -l`` - Prints a list of all the signals and their numbers

.. code-block:: console

    $ trap -l
     1) SIGHUP	 2) SIGINT	 3) SIGQUIT	 4) SIGILL
     5) SIGTRAP	 6) SIGABRT	 7) SIGEMT	 8) SIGFPE
     9) SIGKILL	10) SIGBUS	11) SIGSEGV	12) SIGSYS
    13) SIGPIPE	14) SIGALRM	15) SIGTERM	16) SIGURG
    17) SIGSTOP	18) SIGTSTP	19) SIGCONT	20) SIGCHLD
    21) SIGTTIN	22) SIGTTOU	23) SIGIO	24) SIGXCPU
    25) SIGXFSZ	26) SIGVTALRM	27) SIGPROF	28) SIGWINCH
    29) SIGINFO	30) SIGUSR1	31) SIGUSR2


Example
-------
.. code-block:: bash

    trap "echo The script is terminated; exit" SIGINT

    while true
    do
        echo Test
        sleep 1
    done

.. code-block:: bash

    $TRASH=$(mktemp -t tmp.XXXXXXXXXX)

    trap cleanup 1 2 3 6

    cleanup()
    {
      echo "Removing temporary files:"
      rm -rf "$TRASH"
      exit
    }

    ...
