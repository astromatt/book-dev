"""
>>> import sys; sys.tracebacklimit = 0
>>> from random import seed; seed(0)

>>> wawelski = Dragon(name='Wawelski', position_x=50, position_y=120)
>>> wawelski.set_position(x=10, y=20)
>>> wawelski.move(left=10, down=20)
>>> wawelski.move(left=10, right=15)
>>> wawelski.move(right=15, up=5)
>>> wawelski.move(down=5)
>>> assert wawelski.make_damage() in range(5, 20)
>>> wawelski.take_damage(10)
>>> wawelski.take_damage(5)
>>> wawelski.take_damage(3)
>>> wawelski.take_damage(2)
>>> wawelski.take_damage(15)
>>> wawelski.take_damage(25)
>>> wawelski.take_damage(75)
Wawelski is dead
{'gold': 98, 'position': (20, 40)}
"""

from random import randint


# Solution
class Status:
    ALIVE = 'alive'
    DEAD = 'dead'


class Dragon:
    HEALTH_MIN = 50
    HEALTH_MAX = 100
    DAMAGE_MIN = 5
    DAMAGE_MAX = 20
    GOLD_MIN = 1
    GOLD_MAX = 100
    TEXTURE_ALIVE = 'img/dragon/alive.png'
    TEXTURE_DEAD = 'img/dragon/dead.png'

    def __init__(self, name, position_x=0, position_y=0):
        self.name = name
        self.current_health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.update_status()
        self.texture = self.TEXTURE_ALIVE
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.set_position(position_x, position_y)

    def set_position(self, x, y):
        if self.is_alive():
            self.position_x = x
            self.position_y = y

    def get_position(self):
        return self.position_x, self.position_y

    def move(self, left=0, down=0, right=0, up=0):
        x, y = self.get_position()
        x += right - left
        y += down - up
        self.set_position(x, y)

    def make_damage(self):
        if self.is_alive():
            return randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

    def make_drop(self):
        drop = {'gold': self.gold,
                'position': self.get_position()}
        self.gold = 0
        return drop

    def make_dead(self):
        self.status = Status.DEAD
        self.texture = self.TEXTURE_DEAD
        drop = self.make_drop()
        print(f'{self.name} is dead')
        return drop

    def is_alive(self):
        return not self.is_dead()

    def is_dead(self):
        return self.status == Status.DEAD

    def take_damage(self, damage):
        if self.is_dead():
            return None

        self.current_health -= damage
        self.update_status()

        if self.is_dead():
            return self.make_dead()

    def update_status(self):
        if self.current_health > 0:
            self.status = Status.ALIVE
        else:
            self.status = Status.DEAD
