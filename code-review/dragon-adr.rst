Architecture Design Records
===========================


Create Dragon
-------------
* Create dragon at x=50, y=120 position and name it "Wawelski"

>>> dragon = Dragon('Wawelski')

>>> dragon = Dragon(name='Wawelski')

>>> dragon = Dragon('Wawelski', 'img/dragon/alive.png', 50, 120)

>>> dragon = Dragon('Wawelski', 'img/dragon/alive.png', x=50, y=120)

>>> dragon = Dragon(name='Wawelski', x=50, y=120)

>>> dragon = Dragon(name='Wawelski', posx=50, posy=120)

>>> dragon = Dragon(name='Wawelski', position_x=50, position_y=120)  # good

>>> dragon = Dragon(name='Wawelski', positionx=50, positiony=120)

>>> dragon = Dragon(name='Wawelski', pos=(50, 120))

>>> dragon = Dragon(name='Wawelski', posxy=(50, 120))

>>> dragon = Dragon(name='Wawelski', pos_xy=(50, 120))

>>> dragon = Dragon(name='Wawelski', position=(50, 120))

>>> dragon = Dragon(name='Wawelski', pos={'x':50, 'y':120})

>>> dragon = Dragon(name='Wawelski', pos={'x':50, 'r':120})

>>> dragon = Dragon(name='Wawelski', posxy={'x':50, 'y':120})

>>> dragon = Dragon(name='Wawelski', position={'x':50, 'y':120})

>>> dragon = Dragon(name='Wawelski', pos=Point(50, 120))

>>> dragon = Dragon(name='Wawelski', posxy=Point(50, 120))

>>> dragon = Dragon(name='Wawelski', position=Point(50, 120))

>>> dragon = Dragon(name='Wawelski', pos=Point(x=50, y=120))

>>> dragon = Dragon(name='Wawelski', posxy=Point(x=50, y=120))

>>> dragon = Dragon(name='Wawelski', position=Point(x=50, y=120))  # good

>>> dragon = Dragon(name='Wawelski', position=Point(posx=50, posy=120))

>>> dragon = Dragon(name='Wawelski', position=Point(position_x=50, position_y=120))

>>> from collections import namedtuple
>>>
>>>
>>> Position = namedtuple('Position', ['x', 'y'])
>>> dragon = Dragon(name='Wawelski', position=Position(x=50, y=120))

>>> from typing import NamedTuple
>>>
>>>
>>> class Position(NamedTuple):
...     x: int
...     y: int
>>>
>>> dragon = Dragon(name='Wawelski', position=Position(x=50, y=120))

>>> from typing import TypedDict
>>>
>>>
>>> class Position(TypedDict):
...     x: int
...     y: int
>>>
>>> pt1 = Position(x=50, y=120)
>>> pt2: Position = {'x': 50, 'y': 120}


Set Position
------------
* Set new position to x=10, y=20

>>> dragon.set_position(10, 20)

>>> dragon.teleport(10, 20)

>>> dragon.fly(10, 20)

>>> dragon.set_position(x=10, y=20)  # good

>>> dragon.teleport(x=10, y=20)

>>> dragon.fly(x=10, y=20)

>>> dragon.set(position_x=10, position_y=20)

>>> dragon.position_x = 10

>>> dragon.position_y = 20

>>> dragon.position_x, dragon.position_y = 10, 20

>>> dragon.position = (10, 20)

>>> dragon.position @ (10, 20)

>>> dragon.position @ Point(10, 20)

>>> dragon.x, y.position_y = 10, 20

>>> dragon.x = 10

>>> dragon.y = 20


Change Position
---------------
* Move dragon left by 10 and down by 20

>>> dragon.move(left=10, down=20)  # good

>>> dragon.change_position(left=10, down=20)  # good

>>> dragon.move_left(10)

>>> dragon.move_right(10)

>>> dragon.move_upright(10)

>>> dragon.move_downright(10)

>>> dragon.move_downleft(10)

>>> dragon.move_upleft(10)

>>> dragon.move_left_down(10, 20)

>>> dragon.move(0, 10, 0, 20)

>>> dragon.move([
...     (0, 10, 0, 20),
...     (0, 10, 0, 20)])

>>> dragon.move(dx=10, dy=-20)

>>> dragon.move(vertical=10, horizontal=-20)

>>> dragon.move(x=10, y=-20)

>>> dragon.move_to(x=10, y=20)

>>> dragon.move_x(10)

>>> dragon.move_y(20)

>>> dragon.move_xy(10, 20)

>>> dragon.move({'x':50, 'y':120})

>>> dragon.move({'left':50, 'down':120})

>>> dragon.move([
...     {'left':50, 'down':120},
...     {'left':50, 'right':120},
...     {'down':50}])

>>> dragon.move([
...     (10, 20),
...     (50, 120),
...     (5)])

>>> dragon.move([
...     (10, 20),
...     (10, 15)])

>>> dragon.move([
...     {'x':10, 'y':20},
...     {'x':10, 'y':15}])

>>> dragon.move([
...     Point(x=10, y=20),
...     Point(x=10, y=15)])

>>> x = dragon.x
>>> y = dragon.y
>>> dragon.move(x=x-10, y=y+20)

>>> x = dragon.x - 10
>>> y = dragon.y + 20
>>> dragon.move(x=x, y=y)

>>> dragon.x -= 10
>>> dragon.y += 20

>>> dragon.position_x -= 10
>>> dragon.position_y += 20

>>> dragon.move(x=-10, y=+20)

>>> dragon.move(dx=-10, dy=+20)

>>> dragon.change_position(left=-10, down=20)
>>> dragon.change_position((-10, 20))

>>> dragon.move([
...     (-10, 20),
...     (-10, 20),
...     (-10, 20)])

>>> dragon.move([
...     {'dx': -10, 'dy': 20},
...     {'dx': -10, 'dy': 20},
...     {'dx': -10, 'dy': 20},])

>>> dragon.move([
...     {'left': -10, 'down': 20},
...     {'left': -10, 'right': 20},])

>>> dragon.move(direction='left', distance=20)

>>> dragon.move(direction='right', distance=5)

>>> LEFT = 61
>>> dragon.move(direction=LEFT, distance=20)

>>> class Direction(Enum):
...     LEFT = 61
>>>
>>> dragon.move(direction=Direction.LEFT, distance=5)

>>> dragon.move([
...     {'direction': 'left', 'distance': 20},
...     {'left': -10, 'right': 20},])

>>> KEY_BINDING = {
...     'ARROW_UP': dragon.move_up,
...     'ARROW_DOWN': dragon.move_down,
...     'ARROW_LEFT': dragon.move_left,
...     'ARROW_RIGHT': dragon.move_right}

>>> def action(key, time):
...     return KEY_BINDING.get(key)(time)
>>>
>>> action('ARROW_UP', 5)


Make Damage
-----------
* Dragon makes damage

.. code-block:: text

    dragon ---> enemy
    dragon -> enemy
    dragon <-> enemy
    dragon <- enemy
    dragon <--- enemy

>>> dragon.take_damage()

>>> dragon.hit()

>>> dragon.wound()

>>> dragon.make_damage()  # good

>>> dragon.attack()

>>> dragon.take_damage(enemy)

>>> dragon.hit(enemy)

>>> dragon.attack(enemy)

>>> dragon.wound(enemy)

>>> dragon.make_damage(enemy)

>>> dragon.hurt()

>>> dragon.damage()

>>> dragon.hurt_someone()

>>> dragon.deal_damage()


Take Damage
-----------
* Make DMG points damage to the dragon

>>> dragon.take_damage(DMG)  # good

>>> dragon.receive_damage(DMG)

>>> dragon.wound(DMG)

>>> dragon.hurt(DMG)

>>> dragon.hit(DMG)

>>> dragon.damage(DMG)

>>> dragon.hurt_self(DMG)

>>> dragon - DMG

>>> dragon.__sub__(DMG)

>>> dragon.receive_damage(DMG)
