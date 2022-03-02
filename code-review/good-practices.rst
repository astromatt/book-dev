Good Practices
==============


Rationale
---------
* Zasady clean code
* Nazewnictwo zmiennych, długość nazw, funkcji, klas i pakietów
* Kod po polsku czy angielsku?
* Liczba paramterów, typy i wzorce konstrukcyjne
* Zasady SOLID
* Zmienne statyczne, do czego służą i kiedy stosować
* Importy wszystkiego czy wybiórcze
* Klasy abstrakcyjne vs Interfejsy, kiedy i jak
* Wzorce projektowe
* Długość klas
* Liczba metod
* Długość metod
* Modyfikatory dostępu: private, protected, public


Code Language
-------------
* ``import this`` - The Zen of Python, by Tim Peters
* Readability counts.
* Special cases aren't special enough to break the rules.
* Although practicality beats purity.
* If the implementation is hard to explain, it's a bad idea.
* In US: The states are **not administrative** divisions of the country, in that their powers and responsibilities are in no way assigned to them from above by federal legislation or the Constitution; rather they exercise all powers of government not delegated to the federal government by the Constitution.
* Political divisions of the United States are the various recognized governing entities that together form the United States – states, the District of Columbia, territories and Indian reservations.
* https://en.wikipedia.org/wiki/Administrative_division
* https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country
* https://en.wikipedia.org/wiki/Administrative_division

>>> class Obywatel:
...     def get_wojewodztwo(self):
...         pass
...
...     def get_powiat(self):
...         pass
...
...     def get_gmina(self):
...         pass

>>> class Citizen:
...     def get_voivodeship(self):
...         pass
...
...     def get_state(self):
...         pass
...
...     def get_county(self):
...         pass
...
...     def get_ceremonial_county(self):
...         pass
...
...     def get_metropolitan_county(self):
...         pass
...
...     def get_nonmetropolitan_county(self):
...         pass
...
...     def get_district(self):
...         pass
...
...     def get_civil_parish(self):
...         pass
...

>>> class Obywatel:
...     def get_PESEL(self):
...         pass
...
...     def get_NIP(self):
...         pass


>>> class Citizen:
...     def get_SSN(self):
...         ...
...
...     def get_VATEU(self):
...         pass

>>> class Obywatel:
...     def get_NIP(self):
...         pass
...
...     def get_PESEL(self):
...         pass

>>> class Citizen:
...     def get_VATEU(self):
...         pass

Stdnum https://github.com/arthurdejong/python-stdnum/tree/master/stdnum

Objects and instances
---------------------
Creating string instance:

``''`` is just a syntactic sugar:

>>> name1 = 'Mark Watney'
>>> name2 = str('Mark Watney')
>>> name1 == name2
True

>>> name = 'Mark Watney'
>>> name.upper()
'MARK WATNEY'

>>> str.upper('Mark Watney')
'MARK WATNEY'

Use case:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
...
...     def say_hello(self):
...         print(f'My name... {self.firstname} {self.lastname}')
>>>
>>>
>>> astro = Astronaut('Jose', 'Jimenez')
>>> astro.say_hello()
My name... Jose Jimenez
>>>
>>> Astronaut.say_hello()
Traceback (most recent call last):
TypeError: say_hello() missing 1 required positional argument: 'self'
>>>
>>> Astronaut.say_hello(astro)
My name... Jose Jimenez


Tell - don't ask
----------------
* Tell-Don't-Ask is a principle that helps people remember that object-orientation is about bundling data with the functions that operate on that data.
* It reminds us that rather than asking an object for data and acting on that data, we should instead tell an object what to do.
* This encourages to move behavior into an object to go with the data.

Bad:

>>> class Light:
...     status = 'off'
>>>
>>>
>>> light = Light()
>>> light.status = 'on'
>>> light.status = 'off'

Good:

>>> class Light:
...     status = 'off'
...
...     def switch_on(self):
...         self.status = 'on'
...
...     def switch_off(self):
...         self.status = 'off'
>>>
>>>
>>> light = Light()
>>> light.switch_on()
>>> light.switch_off()

Bad:

>>> class Hero:
...     health: int = 10
>>>
>>>
>>> hero = Hero()
>>>
>>> while hero.health > 0:
...     hero.health -= 2

Good:

>>> class Hero:
...     health: int = 10
...
...     def is_alive(self):
...         return self.health > 0
...
...     def take_damage(self, damage):
...         self.health -= damage
>>>
>>>
>>> hero = Hero()
>>>
>>> while hero.is_alive():
...     hero.take_damage(2)


Setters, Getters, Deleters
--------------------------
* Java way: setters, getters, deleters
* Python way: properties, reflection, descriptors
* More information in `Protocol Property`
* More information in `Protocol Reflection`
* More information in `Protocol Descriptor`
* In Python you prefer direct attribute access

Accessing class fields using setter and getter:

>>> class Astronaut:
...     _name: str
...
...     def set_name(self, name):
...         self._name = name
...
...     def get_name(self):
...         return self._name
>>>
>>>
>>> astro = Astronaut()
>>> astro.set_name('Mark Watney')
>>> result = astro.get_name()
>>> print(result)
Mark Watney

Problem with setters and getters:

>>> class Point:
...     _x: int
...     _y: int
...
...     def get_x(self):
...         return self._x
...
...     def set_x(self, value):
...         self._x = value
...
...     def del_x(self):
...         del self._x
...
...     def get_y(self):
...         return self._y
...
...     def set_y(self, value):
...         self._x = value
...
...     def del_y(self):
...         del self._y

Rationale for Setters and Getters:

>>> class Temperature:
...     kelvin: int
...
...     def set_kelvin(self, kelvin):
...         if kelvin < 0:
...             raise ValueError('Kelvin cannot be negative')
...         else:
...             self._kelvin = kelvin
...
>>>
>>> t = Temperature()
>>> t.set_kelvin(-1)
Traceback (most recent call last):
ValueError: Kelvin cannot be negative

Rationale for Setters and Getters `HabitatOS <https://www.habitatos.space>`_ Z-Wave sensor admin:


References
----------
* https://python.astrotech.io/oop/good-practices.html


Assignments
-----------
* Razem z trenerem omówcie filmik Uncle Boba dotyczący
