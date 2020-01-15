******
Blocks
******


Example 1
=========
.. code-block:: jinja

    <title>{% block title %}{% endblock %}</title>
    <h1>{{ self.title() }}</h1>
    {% block body %}{% endblock %}

.. code-block:: jinja

    {% block body %}
        <h3>Table Of Contents</h3>
        ...
        {{ super() }}
    {% endblock %}


Example 2
=========
.. code-block:: jinja

    <!DOCTYPE html>
    <html lang="en">
    <head>
        {% block head %}
        <link rel="stylesheet" href="style.css" />
        <title>{% block title %}{% endblock %} - My Webpage</title>
        {% endblock %}
    </head>
    <body>
        <div id="content">{% block content %}{% endblock %}</div>
        <div id="footer">
            {% block footer %}
            &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.
            {% endblock %}
        </div>
    </body>
    </html>

.. code-block:: jinja

    {% extends "base.html" %}
    {% block title %}Index{% endblock %}

    {% block head %}
        {{ super() }}
        <style type="text/css">
            .important { color: #336699; }
        </style>
    {% endblock %}

    {% block content %}
        <h1>Index</h1>
        <p class="important">
          Welcome to my awesome homepage.
        </p>
    {% endblock %}

