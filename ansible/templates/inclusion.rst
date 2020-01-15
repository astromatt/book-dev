*********
Inclusion
*********


.. code-block:: jinja

    {% include 'header.html' %}
        Body
    {% include 'footer.html' %}

.. code-block:: jinja

    {% for box in boxes %}
        {% include "render_box.html" %}
    {% endfor %}
