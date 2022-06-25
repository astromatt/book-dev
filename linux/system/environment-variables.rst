Environment Variables
=====================


Paths
-----
* ``/etc/environment``
* ``/etc/profile``
* ``/etc/bashrc``
* ``~/.bashrc``
* ``~/.profile``
* ``/etc/alternatives/``


Variables
---------
* ``$HOME`` - User Home Directory
* ``$HOSTNAME`` - Hostname
* ``$IFS`` - Inter Field Separator
* ``$LANG`` - System Language
* ``$PATH`` - Executable Search Path
* ``$PS1`` - Prompt
* ``$PWD`` - Present Working Directory
* ``$SHELL`` - Current Shell
* ``$TERM`` - Current Terminal (character mapping)
* ``$UID`` - User ID
* ``$UMASK`` - Permission mask for new files
* ``$USER`` - Username
* ``$LANG`` -
* ``$LS_COLORS`` -
* ``$_`` -


PS1
---
.. figure:: ../_img/bash-colors.png
    :align: center
    :scale: 50%

    Bash colors

.. code-block:: console

    ## Prompt
    red='\[\033[00;31m\]'
    green='\[\033[00;32m\]'
    blue='\[\033[00;36m\]'
    white='\[\033[00;39m\]'

    export PS1="\n${green}$ ${white}"

    [ $SSH_CONNECTION ] && export PS1="\n${green}\h $ ${white}"
    [ $UID == 0 ] && export PS1="\n${red}# ${white}"


Commands
--------
.. csv-table:: Env
    :header: "Command", "Type", "Description"
    :widths: 20, 5, 75

    ``env``,                    "",     "Show all environmental variables"
    ``env``,                    "(1)",  "run a program in a modified environment"
    ``update-alternatives``,    "(8)",  "maintain symbolic links determining default commands"
    ``export``,                 "",     "Set environment variable"
