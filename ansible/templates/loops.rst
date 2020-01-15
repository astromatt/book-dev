*****
Loops
*****


.. code-block:: jinja

    <ul>
    {% for item in seq %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>

.. code-block:: jinja

    {% for item in items %}
        {{ item }}
    {% else %}
        No items!
    {% endfor %}

.. csv-table:: Loops special variables

    "Variable", "Description"
    "``loop.index``", "The current iteration of the loop. (1 indexed)"
    "``loop.index0``", "The current iteration of the loop. (0 indexed)"
    "``loop.revindex``", "The number of iterations from the end of the loop (1 indexed)"
    "``loop.revindex0``", "The number of iterations from the end of the loop (0 indexed)"
    "``loop.first``", "True if first iteration."
    "``loop.last``", "True if last iteration."
    "``loop.length``", "The number of items in the sequence."
    "``loop.cycle``", "A helper function to cycle between a list of sequences. See the explanation below."
    "``loop.depth``", "Indicates how deep in a recursive loop the rendering currently is. Starts at level 1"
    "``loop.depth0``", "Indicates how deep in a recursive loop the rendering currently is. Starts at level 0"
    "``loop.previtem``", "The item from the previous iteration of the loop. Undefined during the first iteration"
    "``loop.nextitem``", "The item from the following iteration of the loop. Undefined during the last iteration"
    "``loop.change``", "True if previously called with a different value (or not called at all)"
