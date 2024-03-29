Good Practices
==============


Rationale
---------
* Zasady clean code
* Nazewnictwo zmiennych, długość nazw, funkcji, klas i pakietów
* Kod po polsku czy angielsku?
* Liczba parametrów, typy i wzorce konstrukcyjne
* Zasady SOLID
* Zmienne statyczne, do czego służą i kiedy stosować
* Importy wszystkiego czy wybiórcze
* Klasy abstrakcyjne vs Interfejsy, kiedy i jak
* Wzorce projektowe
* Długość klas
* Liczba metod
* Długość metod
* Modyfikatory dostępu: private, protected, public


Komentarze
----------
* Kiedy komentować
* Co komentować
* Zakomentowany kod
* TODO i FIXME
* JavaDoc w komentarzach


Code Language
-------------
* ``import this`` - The Zen of Python, by Tim Peters
* Readability counts.
* Special cases aren't special enough to break the rules.
* Although practicality beats purity.
* If the implementation is hard to explain, it's a bad idea.


Case Study - Administrative Divisions
-------------------------------------
* In US: The states are **not administrative** divisions of the country, in that their powers and responsibilities are in no way assigned to them from above by federal legislation or the Constitution; rather they exercise all powers of government not delegated to the federal government by the Constitution.
* Political divisions of the United States are the various recognized governing entities that together form the United States – states, the District of Columbia, territories and Indian reservations.
* https://en.wikipedia.org/wiki/Administrative_division
* https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country
* https://en.wikipedia.org/wiki/Administrative_division

.. code-block:: python

    class Obywatel:
        getWojewodztwo()
        getPowiat()
        getGmina()

.. code-block:: python

    class Citizen:
        getVoivodeship()
        getState()
        getCounty()
        getCeremonialCounty()
        getMetropolitanCounty()
        getDistrict()
        getCivilParish()


Identification Numbers
----------------------
* https://github.com/arthurdejong/python-stdnum/tree/master/stdnum

.. code-block:: python

    class Obywatel:
        getPESEL()
        getNIP()

.. code-block:: python

    class Citizen:
        getSSN()
        getVATEU()


Tell - don't ask
----------------
* Tell-Don't-Ask is a principle that helps people remember that object-orientation is about bundling data with the functions that operate on that data.
* It reminds us that rather than asking an object for data and acting on that data, we should instead tell an object what to do.
* This encourages to move behavior into an object to go with the data.

Bad:

.. code-block:: python

    class Light:
        status = 'off'


    light = Light()
    light.status = 'on'
    light.status = 'off'

Good:

.. code-block:: python

    class Light:
        status = 'off'

        def switch_on(self):
            self.status = 'on'

        def switch_off(self):
            self.status = 'off'


    light = Light()
    light.switch_on()
    light.switch_off()

Bad:

.. code-block:: python

    class Hero:
        health: int = 10


    hero = Hero()

    while hero.health > 0:
        hero.health -= 2

Good:

.. code-block:: python

    class Hero:
        health: int = 10

        def is_alive(self):
            return self.health > 0

        def take_damage(self, damage):
            self.health -= damage


    hero = Hero()

    while hero.is_alive():
        hero.take_damage(2)


Setters, Getters, Deleters
--------------------------
* Java way: setters, getters, deleters
* Python way: properties, reflection, descriptors
* More information in `Protocol Property`
* More information in `Protocol Reflection`
* More information in `Protocol Descriptor`
* In Python you prefer direct attribute access

Accessing class fields using setter and getter:

.. code-block:: python

    class Astronaut:
        _name: str

        def set_name(self, name):
            self._name = name

        def get_name(self):
            return self._name


    astro = Astronaut()
    astro.set_name('Mark Watney')
    result = astro.get_name()


Problem with setters and getters:

.. code-block:: python

    class Point:
        _x: int
        _y: int

        def get_x(self):
            return self._x

        def set_x(self, value):
            self._x = value

        def del_x(self):
            del self._x

        def get_y(self):
            return self._y

        def set_y(self, value):
            self._x = value

        def del_y(self):
            del self._y

Rationale for Setters and Getters:

.. code-block:: python

    class Temperature:
        kelvin: int

        def set_kelvin(self, kelvin):
            if kelvin < 0:
                raise ValueError('Kelvin cannot be negative')
            else:
                self._kelvin = kelvin


    t = Temperature()
    t.set_kelvin(-1)
    # Traceback (most recent call last):
    # ValueError: Kelvin cannot be negative


References
----------
* https://python.astrotech.io/oop/good-practices.html


Assignments
-----------
* Razem z trenerem omówcie filmik Uncle Boba dotyczący hidden classes
* Razem z trenerem oglądnijcie filmik Ruby i JS (opcjonalnie)
