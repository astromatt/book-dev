Filter Create
=============


Rationale
---------
* Subskrypcja


Demonstration
-------------
* Create subscription: Every Monday at 5 am
* Delete subscription (mention, not to delete filter)


Assignments
-----------

Filter Subscription Create
^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Przejdź do wyszukiwania zadań:

    * Cloud: Z menu `Filters` wybrać `Advanced Issue Search` w trybie `Switch to JQL`
    * Server: Z menu `Issues` wybrać `Search for Issues` w trybie `Advanced`

#. Wyszukaj ``assignee = currentUser() and statusCategory != Done``
#. Przycisk trójkąta w dół `⌄` obok `Save` -> wybieramy Save as `Imię Todo` (gdzie Imię, to Twoje imię)
#. Kliknij link `Details` i wybierz `New Subscription`
#. Wybieramy Schedule: Days per Week; Interval: `Once per day at 5:00 am` w dniu `Monday`
#. Upewnij się, że jest odznaczone `Email this filter, even if there are no issues found`
#. Kliknij `Subscribe`
#. Zmodyfikuj wyszukiwanie na:

    .. code-block:: sql

        assignee = currentUser()
            AND statusCategory != "Done"
            AND due <= 7d

#. Kliknij przycisk `Save`

.. note:: Zwróć uwagę, że przycisk trójkąta w dół `⌄` obok `Save` pojawi się tylko wtedy, kiedy edytujesz filtr oraz jego zapytanie `JSQ` jest zmodyfikowane. Jeżeli tworzysz nowy filtr, to przycisk trzech kropek się nie pojawi.

Filter Subscription Delete
^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Przejdź do wyszukiwania zadań:

    * Cloud: Z menu `Filters` wybrać `View All Filters`
    * Server: Z menu u góry `Issues` wybrać `Manage filters` (na dole)

#. Przefiltruj listę po filtrach należących do użytkownika
#. Wybierz filtr z aktywną subskrypcją
#. Kliknij na link `1 Subscription`
#. Wybierz Actions `Delete` (po prawej)
#. Uwaga: usuń tylko subskrypcję a nie filtr! - będziemy z niego jeszcze korzystać
