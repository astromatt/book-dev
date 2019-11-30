*****
Loops
*****

For
===
.. code-block:: bash

    for i in `seq 1 10`; do
        echo $i
    done

.. code-block:: bash

    for i in $( ls ); do
        echo item: $i
    done

.. warning:: IFS='\\n'

Inline for
----------
- ``for a in *; do echo $a; done``

While
=====
.. code-block:: bash

     COUNTER=0

     while [  $COUNTER -lt 10 ]; do
         echo The counter is $COUNTER
         let COUNTER=COUNTER+1
     done

.. code-block:: bash

    while [ $# -gt 0 ]; do    # Until you run out of parameters . . .
      case "$1" in
        -d|--debug)
              # "-d" or "--debug" parameter?
              DEBUG=1
              ;;
        -c|--conf)
              CONFFILE="$2"
              shift
              if [ ! -f $CONFFILE ]; then
                echo "Error: Supplied file doesn't exist!"
                exit $E_CONFFILE     # File not found error.
              fi
              ;;
      esac
      shift   # Check next set of parameters.
    done

Until
=====
.. code-block:: bash

     COUNTER=20

     until [  $COUNTER -lt 10 ]; do
         echo COUNTER $COUNTER
         let COUNTER-=1
     done