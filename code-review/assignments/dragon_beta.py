from enum import Enum
from dragon_alpha_advanced import Dragon, Status, Point, Direction


class Status(Enum):
    ALIVE: str = 'alive'
    DEAD: str = 'dead'
    FULL_HEALTH: str = 'Full Health'
    INJURED: str = 'Injured'
    BADLY_WOUNDED: str = 'Badly Wounded'
    NEAR_DEAD: str = 'Near Death'


class Config:
    BORDER_X_MAX = 1024
    BORDER_X_MIN = 0
    BORDER_Y_MAX = 768
    BORDER_Y_MIN = 0


class Character(Dragon):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._items = []
        self._health_full = self._health

    def update_status(self):
        if not hasattr(self, '_health_full'):
            self._health_full = self._health

        percent = self._health / self._health_full * 100

        if percent == 100:
            self.status = Status.FULL_HEALTH
        elif 75 <= percent < 100:
            self.status = Status.INJURED
        elif 25 <= percent < 75:
            self.status = Status.BADLY_WOUNDED
        elif 0 < percent < 25:
            self.status = Status.NEAR_DEAD
        else:
            self.status = Status.DEAD

    def __matmul__(self, position: Point = Point()) -> None:
        """
        >>> dragon = Character(name='Red', position_x=0, position_y=0)
        >>> dragon >> Direction(right=1)
        >>> dragon.position
        Point(x=1, y=0)
        >>> dragon >> Direction(down=1)
        >>> dragon.position
        Point(x=1, y=1)
        >>> dragon >> Direction(left=2)
        >>> dragon.position
        Point(x=0, y=1)
        >>> dragon >> Direction(up=2)
        >>> dragon.position
        Point(x=0, y=0)
        """
        x = position.x
        y = position.y

        if x > Config.BORDER_X_MAX:
            x = Config.BORDER_X_MAX

        if x < Config.BORDER_X_MIN:
            x = Config.BORDER_X_MIN

        if y > Config.BORDER_Y_MAX:
            y = Config.BORDER_Y_MAX

        if y < Config.BORDER_Y_MIN:
            y = Config.BORDER_Y_MIN

        super().__matmul__(Point(x, y))


class CharacterClass(Enum):
    WARRIOR = 'Warrior'
    DRAGON = 'Dragon'


class Dragon(Character):
    HIT_POINTS_MIN = 100
    HIT_POINTS_MAX = 150
    CHARACTER_CLASS = CharacterClass.DRAGON


class Hero(Character):
    HIT_POINTS_MIN = 200
    HIT_POINTS_MAX = 250
    DAMAGE_MIN = 1
    DAMAGE_MAX = 15
    GOLD_MIN = 0
    GOLD_MAX = 0
    CHARACTER_CLASS = CharacterClass.WARRIOR


def run():
    dragon = Dragon(name='Wawelski')
    hero = Hero(name='Jan Twardowski')

    turn = 1

    while dragon.is_alive() and hero.is_alive():
        print(f'\nTurn: {turn}')

        dmg = dragon.make_damage()
        hero.take_damage(dmg)

        if hero.is_alive():
            dmg = hero.make_damage()
            dragon.take_damage(dmg)

        if dragon.is_dead():
            drop = dragon.get_drop()
            hero.gold += drop['gold']
            print(f'{hero.name} now has: {hero.gold} gold')

        turn += 1


if __name__ == '__main__':
    run()
