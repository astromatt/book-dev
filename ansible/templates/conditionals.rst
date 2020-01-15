************
Conditionals
************


If
==
.. code-block:: jinja

    {% if loop.index is divisibleby 3 %}
    {% if loop.index is divisibleby(3) %}

.. code-block:: jinja

    {% if users %}
        <ul>
        {% for user in users %}
            <li>{{ user.username|e }}</li>
        {% endfor %}
        </ul>
    {% endif %}


If else
=======
.. code-block:: jinja

    {% if user.user_id is odd %}
        {{ user.username|e }} is odd
    {% else %}
        hmm. {{ user.username|e }} looks pretty normal
    {% endif %}


If elif else
============
.. code-block:: jinja

    {% if kenny.sick %}
        Kenny is sick.
    {% elif kenny.dead %}
        You killed Kenny!  You bastard!!!
    {% else %}
        Kenny looks okay --- so far
    {% endif %}
