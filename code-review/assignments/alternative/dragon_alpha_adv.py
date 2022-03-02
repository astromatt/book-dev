"""
>>> from random import randint, seed

Stwórz smoka w pozycji x=50, y=120 i nazwij go "Wawelski"
>>> seed(0); dragon = Dragon('Wawelski', position_x=50, position_y=120)

Ustaw nową pozycję na x=10, y=20
>>> dragon.position_set(x=10, y=20)

Przesuń smoka w lewo o 10 i w dół o 20
>>> dragon.position_change(left=10, down=20)

Przesuń smoka w lewo o 10 i w prawo o 15
>>> dragon.position_change(left=10, right=15)

Przesuń smoka w prawo o 15 i w górę o 5
>>> dragon.position_change(right=15, up=5)

Przesuń smoka w dół o 5
>>> dragon.position_change(down=5)

Smok zadaje obrażenia
>>> _ = dragon.make_damage()

>>> try:
...     dragon.take_damage(10)  # Zadaj 10 obrażeń smokowi
...     dragon.take_damage(5)  # Zadaj 5 obrażeń smokowi
...     dragon.take_damage(3)  # Zadaj 3 obrażeń smokowi
...     dragon.take_damage(2)  # Zadaj 2 obrażeń smokowi
...     dragon.take_damage(15)  # Zadaj 15 obrażeń smokowi
...     dragon.take_damage(25)  # Zadaj 25 obrażeń smokowi
...     dragon.take_damage(75)  # Zadaj 75 obrażeń smokowi
... except dragon.IsDead:
...     drop = dragon.get_drop()
...     print(f'{dragon.name} is dead')
...     print(f'Gold {drop["gold"]}')
...     print(f'Position {drop["position"]}')
Wawelski is dead
Gold 98
Position (20, 40)


>>> assert dragon.position_x == 20
>>> assert dragon.position_y == 40
"""
from enum import Enum
from random import randint
from typing import Final, TypedDict
from unittest import TestCase


def if_alive(method):
    def wrapper(dragon, *args, **kwargs):
        if dragon.is_alive():
            return method(dragon, *args, **kwargs)
    return wrapper


def if_dead(method):
    def wrapper(dragon, *args, **kwargs):
        if dragon.is_dead():
            return method(dragon, *args, **kwargs)
    return wrapper


Position = tuple[int,int]

class HasPosition:
    position_x: int
    position_y: int

    @if_alive
    def position_set(self, *, x, y) -> None:
        self.position_x = x
        self.position_y = y

    @if_alive
    def position_change(self, *, right: int = 0, left: int = 0,
                        down: int = 0, up: int = 0) -> None:
        current_x, current_y = self.position_get()
        self.position_set(
            x=current_x + right - left,
            y=current_y + down - up)

    def position_get(self) -> Position:
        return self.position_x, self.position_y


class Status(Enum):
    ALIVE: Final[str] = 'alive'
    DEAD: Final[str] = 'dead'

class Drop(TypedDict):
    gold: int
    position: Position


class Dragon(HasPosition):
    name: str
    health: int
    texture: str
    status: str
    DAMAGE_MAX: Final[int] = 20
    DAMAGE_MIN: Final[int] = 5
    HEALTH_MIN: Final[int] = 50
    HEALTH_MAX: Final[int] = 100
    GOLD_MIN: Final[int] = 1
    GOLD_MAX: Final[int] = 100
    TEXTURE_ALIVE: Final[str] = 'img/dragon/alive.png'
    TEXTURE_DEAD: Final[str] = 'img/dragon/dead.png'

    def __init__(self,
                 name: str,
                 /,
                 *,
                 position_x: int = 0,
                 position_y: int = 0) -> None:

        self.name = name
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.status = Status.ALIVE
        self.texture = self.TEXTURE_ALIVE
        self.position_set(x=position_x, y=position_y)

    class IsDead(Exception):
        pass

    def is_dead(self):
        return self.health <= 0

    def is_alive(self):
        return not self.is_dead()

    @if_alive
    def make_damage(self):
        return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    @if_alive
    def take_damage(self, damage, /):
        self.health -= damage
        if self.is_dead():
            self._make_dead()

    def _make_dead(self):
        self.status = Status.DEAD
        self.texture = self.TEXTURE_DEAD
        raise self.IsDead

    @if_dead
    def get_drop(self) -> Drop:
        gold, self.gold = self.gold, 0
        return Drop(gold=gold, position=self.position_get())



class DragonTest(TestCase):
    def setUp(self):
        self.dragon = Dragon('Wawelski', position_x=0, position_y=0)

    def test_init_name_noname(self):
        with self.assertRaises(TypeError):
            Dragon()

    def test_init_name_positional(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.name, 'Wawelski')

    def test_init_name_keyword(self):
        with self.assertRaises(TypeError):
            Dragon(name='Wawelski')

    def test_init_position_default(self):
        dragon = Dragon('Wawelski')
        self.assertEqual(dragon.position_x, 0)
        self.assertEqual(dragon.position_y, 0)

    def test_init_position_set_x(self):
        dragon = Dragon('Wawelski', position_x=1)
        self.assertEqual(dragon.position_x, 1)
        self.assertEqual(dragon.position_y, 0)

    def test_init_position_set_y(self):
        dragon = Dragon('Wawelski', position_y=1)
        self.assertEqual(dragon.position_x, 0)
        self.assertEqual(dragon.position_y, 1)

    def test_init_position_set_xy(self):
        dragon = Dragon('Wawelski', position_x=1, position_y=2)
        self.assertEqual(dragon.position_x, 1)
        self.assertEqual(dragon.position_y, 2)

    def test_damage_make(self):
        dmg = self.dragon.make_damage()
        self.assertIn(dmg, range(5, 21))

    def test_damage_take_keyword(self):
        with self.assertRaises(TypeError):
            self.dragon.take_damage(damage=1)

    def test_damage_take_positional(self):
        self.dragon.take_damage(1)

    def test_damage_take_and_health_positive(self):
        self.dragon.health = 2
        self.dragon.take_damage(1)
        self.assertEqual(self.dragon.health, 1)

    def test_damage_take_and_health_zero(self):
        self.dragon.health = 1
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(1)

    def test_damage_take_and_health_negative(self):
        self.dragon.health = 1
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)

    def test_is_alive(self):
        self.dragon.health = 1
        self.assertTrue(self.dragon.is_alive())

    def test_is_dead_zero(self):
        self.dragon.health = 0
        self.assertFalse(self.dragon.is_alive())
        self.assertTrue(self.dragon.is_dead())

    def test_is_dead_negative(self):
        self.dragon.health = -1
        self.assertFalse(self.dragon.is_alive())
        self.assertTrue(self.dragon.is_dead())

    def test_damage_take_and_dead_zero(self):
        self.dragon.health = 1
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(1)

    def test_damage_take_and_dead_negative(self):
        self.dragon.health = 1
        with self.assertRaises(self.dragon.IsDead):
            self.dragon.take_damage(2)

    def test_init_status_alive(self):
        self.assertEqual(self.dragon.status, Status.ALIVE)


class PositionTest(TestCase):
    def setUp(self):
        self.dragon = Dragon('Wawelski', position_x=0, position_y=0)

    def test_position_set_kwargs(self):
        self.dragon.position_set(x=1, y=2)
        self.assertEqual(self.dragon.position_x, 1)
        self.assertEqual(self.dragon.position_y, 2)

    def test_position_set_args(self):
        with self.assertRaises(TypeError):
            self.dragon.position_set(1, 2)
        with self.assertRaises(TypeError):
            self.dragon.position_set(1, y=2)

    def test_move_left(self):
        self.dragon.position_change(left=1)
        self.assertEqual(self.dragon.position_x, -1)
        self.assertEqual(self.dragon.position_y, 0)

    def test_move_right(self):
        self.dragon.position_change(right=1)
        self.assertEqual(self.dragon.position_x, 1)
        self.assertEqual(self.dragon.position_y, 0)

    def test_move_down(self):
        self.dragon.position_change(down=1)
        self.assertEqual(self.dragon.position_x, 0)
        self.assertEqual(self.dragon.position_y, 1)

    def test_move_up(self):
        self.dragon.position_change(up=1)
        self.assertEqual(self.dragon.position_x, 0)
        self.assertEqual(self.dragon.position_y, -1)
