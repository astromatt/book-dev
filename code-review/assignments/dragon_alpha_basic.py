from random import randint


class Dragon:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.health = randint(50, 100)
        self.texture = 'img/dragon/alive.png'
        self.x = x
        self.y = y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move(self, left=0, down=0, right=0, up=0):
        self.x += right - left
        self.y += down - up

    def make_damage(self):
        return randint(5, 20)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.status = 'dead'
            self.texture = 'img/dragon/dead.png'
            print(f'{self.name} is dead')
            print(f'Gold {randint(1, 100)}')
            print(f'Position x={self.x} y={self.y}')
