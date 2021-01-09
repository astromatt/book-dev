***********************
Environmental Variables
***********************

- ``/usr/bin/env``
- ``/etc/environment``

.. csv-table:: Environmental Variables
    :header-rows: 1
    :widths: 20, 80
    :file: ../_data/environmental-variables.csv

Environmental Variables
=======================

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
