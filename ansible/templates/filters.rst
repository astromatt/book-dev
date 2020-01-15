*******
Filters
*******


Filters
=======
* http://jinja.pocoo.org/docs/2.10/templates/#list-of-builtin-filters

.. code-block:: jinja

    {{ items|join(', ') }}

.. code-block:: jinja

    {% filter upper %}
        This text becomes uppercase
    {% endfilter %}


Cycle
=====
.. code-block:: jinja

    {% for user in users %}
        <li class="{{ loop.cycle('odd', 'even') }}">{{ user }}</li>
    {% endfor %}
