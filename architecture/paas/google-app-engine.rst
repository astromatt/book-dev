Google App Engine
=================

Tworzenie aplikacji w oparciu o platformę Google App Engine
-----------------------------------------------------------

-  Tworzenie aplikacji
-  Storage
-  Cache
-  Bazy danych

Tworzenie aplikacji
^^^^^^^^^^^^^^^^^^^

.. code:: sh

    app.yaml
    git clone https://github.com/GoogleCloudPlatform/appengine-guestbook-python.git
    dev_appserver.py .

-  http://localhost:8000 - admin console
-  http://localhost:8080 - app

App.yaml for static pages
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: yaml

    runtime: php55
    api_version: 1
    threadsafe: true

    handlers:
     - url: /
       static_files: www/index.html
       upload: www/index.html

     - url: /(.*)
       static_files: www/\1
       upload: www/(.*)
