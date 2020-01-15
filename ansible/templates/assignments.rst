***********
Assignments
***********


.. code-block:: jinja

    {% set navigation = [('index.html', 'Index'), ('about.html', 'About')] %}
    {% set key, value = call_something() %}

.. code-block:: jinja

    {% set navigation %}
        <li><a href="/">Index</a>
        <li><a href="/downloads">Downloads</a>
    {% endset %}

.. code-block:: jinja

    {% set reply | wordwrap %}
        You wrote:
        {{ message }}
    {% endset %}
