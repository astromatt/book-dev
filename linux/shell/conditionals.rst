************
Conditionals
************

``if``
======
.. code-block:: bash

    name="José Jiménez"

    if [ $imie == "José Jiménez" ]; then
        echo "My name José Jiménez"
    fi

``if`` and ``else``
===================
.. code-block:: bash

    name="José Jiménez"

    if [ $imie == "José Jiménez" ]; then
        echo "My name José Jiménez"
    else
        echo "I am someone else"
    fi

Short version - ``&&`` and ``||``
=================================
.. code-block:: console

    $ name="José Jiménez"
    $ [ $imie == "José Jiménez" ] && echo "My name José Jiménez" || echo "I am someone else"
    My name José Jiménez

Case (A.K.A. switch)
====================
.. code-block:: bash

    case $( arch ) in   # $( arch ) returns machine architecture.
                        # Equivalent to 'uname -m' ...
      i386 ) echo "80386-based machine";;
      i486 ) echo "80486-based machine";;
      i586 ) echo "Pentium-based machine";;
      i686 ) echo "Pentium2+-based machine";;
      *    ) echo "Other type of machine";;
    esac

    exit 0

.. code-block:: bash

    echo; echo "Hit a key, then hit return."
    read Keypress

    case "$Keypress" in
      [[:lower:]]   ) echo "Lowercase letter";;
      [[:upper:]]   ) echo "Uppercase letter";;
      [0-9]         ) echo "Digit";;
      *             ) echo "Punctuation, whitespace, or other";;
    esac      #  Allows ranges of characters in [square brackets],
              #+ or POSIX ranges in [[double square brackets.