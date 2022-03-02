"""
>>> from random import randint, seed

Stwórz smoka w pozycji x=50, y=120 i nazwij go "Wawelski"
>>> seed(0); dragon = Dragon('Wawelski', position_x=50, position_y=120)

Ustaw nową pozycję na x=10, y=20
>>> dragon.set_position(x=10, y=20)

Przesuń smoka w lewo o 10 i w dół o 20
>>> dragon.move(left=10, down=20)

Przesuń smoka w lewo o 10 i w prawo o 15
>>> dragon.move(left=10, right=15)

Przesuń smoka w prawo o 15 i w górę o 5
>>> dragon.move(right=15, up=5)

Przesuń smoka w dół o 5
>>> dragon.move(down=5)

Smok zadaje obrażenia
>>> _ = dragon.make_damage()

Zadaj 10 obrażeń smokowi
>>> dragon.take_damage(10)

Zadaj 5 obrażeń smokowi
>>> dragon.take_damage(5)

Zadaj 3 obrażeń smokowi
>>> dragon.take_damage(3)

Zadaj 2 obrażeń smokowi
>>> dragon.take_damage(2)

Zadaj 15 obrażeń smokowi
>>> dragon.take_damage(15)

Zadaj 25 obrażeń smokowi
>>> dragon.take_damage(25)

Zadaj 75 obrażeń smokowi
>>> dragon.take_damage(75)
Wawelski is dead
Gold 6
Position 20, 40

>>> assert dragon.position_x == 20
>>> assert dragon.position_y == 40
"""
from random import randint
from unittest import TestCase


class Dragon:
    name: str
    health: int
    texture: str
    status: str
    position_x: int
    position_y: int

    def __init__(self,
                 name: str,
                 /,
                 *,
                 position_x: int = 0,
                 position_y: int = 0) -> None:
        self.health = randint(50, 100)
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.status = 'alive'
        self.texture = 'img/dragon/alive.png'

    def set_position(self, *, x, y) -> None:
        if self.status == 'alive':
            self.position_x = x
            self.position_y = y

    def move(self, *, right: int = 0, left: int = 0,
                      down: int = 0, up: int = 0) -> None:
        if self.status == 'alive':
            self.position_x += right - left
            self.position_y += down - up

    def make_damage(self):
        if self.status == 'alive':
            return randint(5, 20)

    def take_damage(self, damage, /):
        if self.status == 'alive':
            self.health -= damage
            if self.health <= 0:
                self.status = 'dead'
                self.texture = 'img/dragon/dead.png'
                print(f'{self.name} is dead')
                print(f'Gold {randint(1,100)}')
                print(f'Position {self.position_x}, {self.position_y}')


class DragonTest(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.status = None

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

    def test_position_set_kwargs(self):
        self.dragon.set_position(x=1, y=2)
        self.assertEqual(self.dragon.position_x, 1)
        self.assertEqual(self.dragon.position_y, 2)

    def test_position_set_args(self):
        with self.assertRaises(TypeError):
            self.dragon.set_position(1, 2)
        with self.assertRaises(TypeError):
            self.dragon.set_position(1, y=2)

    def test_move_left(self):
        self.dragon.move(left=1)
        self.assertEqual(self.dragon.position_x, -1)
        self.assertEqual(self.dragon.position_y, 0)

    def test_move_right(self):
        self.dragon.move(right=1)
        self.assertEqual(self.dragon.position_x, 1)
        self.assertEqual(self.dragon.position_y, 0)

    def test_move_down(self):
        self.dragon.move(down=1)
        self.assertEqual(self.dragon.position_x, 0)
        self.assertEqual(self.dragon.position_y, 1)

    def test_move_up(self):
        self.dragon.move(up=1)
        self.assertEqual(self.dragon.position_x, 0)
        self.assertEqual(self.dragon.position_y, -1)

    def test_damage_make(self):
        dmg = self.dragon.make_damage()
        self.assertIn(dmg, range(5,21))

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
        self.dragon.take_damage(1)
        self.assertEqual(self.dragon.health, 0)

    def test_damage_take_and_health_negative(self):
        self.dragon.health = 1
        self.dragon.take_damage(2)
        self.assertEqual(self.dragon.health, -1)

    def test_damage_take_and_dead_zero(self):
        self.dragon.health = 1
        self.dragon.take_damage(1)
        self.assertEqual(self.dragon.status, 'dead')

    def test_damage_take_and_dead_negative(self):
        self.dragon.health = 1
        self.dragon.take_damage(2)
        self.assertEqual(self.dragon.status, 'dead')

    def test_init_status_alive(self):
        self.assertEqual(self.dragon.status, 'alive')
