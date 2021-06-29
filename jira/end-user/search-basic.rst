Search Basic
============


Rationale
---------
#. Przejdź do wyszukiwania zadań:

    * Cloud: Z menu `Filters` wybrać `Advanced Issue Search` w trybie `Switch to JQL`
    * Server: Z menu `Issues` wybrać `Search for Issues` w trybie `Advanced`

* `Basic`
* `Detail View` -> `List View`
* Select columns


Where is used?
--------------
* Searching Issues
* Board Configuration
* Filters for Dashboard
* Filters for Subscriptions


Demonstration
-------------
* Change: list view, add headers, sort headers, order data
* Change: basic -> advanced
* Show: export CSV, bulk change
* Basic: select project, status, other fields, due date range


Assignments
-----------

Search Basic Columns
^^^^^^^^^^^^^^^^^^^^
#. Z menu u góry wybierz `Issues` -> `Search for Issues`
#. `Change View` [przycisk po prawej stronie] zmień na `List View`
#. `Columns` [przycisk po prawej stronie]: Odznaczyć: `Created`, `Updated`, `Development`
#. Columns: zaznaczyć: `Summary`, `Issue Type`, `Due Date`, `Fix Version/s`, `Epic Link`
#. Chwytając nagłówek kolumny, przenieś `Issue Type` (T) jako pierwsza kolumna
#. Ustawić kolumny w kolejności: `Issue Type`, `Issue Key`, `Epic Link`, `Fix Version/s`, `Due Date`, `Status`, `Summary`
#. Dodać kolumny: `Original Estimate`, `Remaining Estimate`, `Time Spent`
#. Z menu po prawej stronie u góry wybieramy `Export` -> `CSV (Current Fields)` -> `Delimiter` -> `Comma (,)`

.. note:: Gdyby któraś kolumna (np. `issue type`) mimo zaznaczenia nie była widoczna, odśwież ekran Jiry (nawet kilka razy). Zwróć też uwagę, że kolumna `issue type` jest widoczna jako literka ``T`` i są w niej tylko ikony typów zadań.

Search Basic Query
^^^^^^^^^^^^^^^^^^
#. Przejdź do wyszukiwania zadań:

    * Cloud: Z menu `Filters` wybrać `Advanced Issue Search`
    * Server: Z menu `Issues` wybrać `Search for Issues`

#. Upewnij się, że jesteś w trybie wyszukiwania: `Basic`
#. `Project` -> swój projekt
#. Kliknij na nazwę kolumny `Due Date` dwukrotnie aby posortować rosnąco
#. `Status` -> `In Progress` oraz `Blocked`
#. More -> `Due Date` -> `Now Overdue`
#. Zmień zakres `Due Date` -> od `1/Jan/00` do `31/Jan/00`
#. Zmień zakres `Due Date` -> `Due in next 8 hours or is overdue`
#. Zmień zakres `Due Date` -> `In range -7d to ...`` [pozostaw niewypełnione]
