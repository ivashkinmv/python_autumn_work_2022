# todo: Реализовать класс "Игровой персонаж".
#  Класс должен содержать атрибуты(свойства): Идентификатор, Имя, Здоровье, Раса, Тип персонажа, урон.
#  Инициализация атрибутов(состояние объекта) должна происходить в конструкторе.
#  В классе реализовать метод изменения здоровья по нанесенному урону(параметр функции).
#  Заложить логику: При достижении порога здоровья персонаж погибает
#  В классе реализовать метод получения значения атрибута урона
#  При достижении порога здоровья персонаж погибает
#  Реализовать дандер __repr__ для отладки персонажа
#  Реализовать дандер вычитания __sub__()  написав логику "боя" которая срабатывает
#  в момент вычитания объектов класса obj1 - obj2 и заключается в вычитании из
#  здоровья первого объекта урона наносимого вторым объектом

from random import randint


class Player:  # класс игрока
    def __init__(self, name, health, race, charac_type, damage, ids):
        # ids = randint(1000, 9999)
        self.ids = ids
        self.name = name
        self.health = health
        self.race = race
        self.charac_type = charac_type
        self.damage = damage

    def __repr__(self):
        return f"User(id={self.ids}, name={self.name}, health={self.health}, " \
               f"race={self.race},type={self.charac_type}, damage={self.damage})"

    def strike(self, opposite):
        a = ['с вертушки ударил', 'двоичкой по']
        b = randint(0, 1)
        self.damage = randint(0, 12)
        opposite.health -= self.damage
        if opposite.health < 0:
            opposite.health = 0
        self.health += 0
        if b == 0 and self.damage > 0 and self.damage != 12:
            print(self.name, a[b], opposite.name, 'силой', self.damage)
            print(f"У {opposite.name} осталось энергии {opposite.health}")
        elif b == 1 and self.damage > 0 and self.damage != 12:
            print(self.name, a[b], opposite.name, 'силой', self.damage)
            print(f"У {opposite.name} осталось энергии {opposite.health}")
        elif b == 0 and self.damage == 12:
            print(self.name, a[b], opposite.name, 'силой', self.damage)
            print(f"{opposite.name} пропустил критический удар" )
            print(f"У {opposite.name} осталось энергии {opposite.health}")
        elif b == 1 and self.damage == 12:
            print(self.name, a[b], opposite.name, 'силой', self.damage)
            print(f"{opposite.name} пропустил критический удар")
            print(f"У {opposite.name} осталось энергии {opposite.health}")
        else:
            print(self.name, a[b], opposite.name, 'силой', self.damage)
            print(opposite.name, "увернулся от", self.name)
            print(f"У {opposite.name} осталось энергии {opposite.health}")
        # print('%s = %d' % (opposite.name, opposite.health))


class Fight:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = "Round One, Fight"

    def fight(self):
        while self.player1.health > 0 and self.player2.health > 0:
            n = randint(1, 2)
            if n == 1:
                self.player1.strike(self.player2)
            else:
                self.player2.strike(self.player1)
        if self.player1.health > self.player2.health:
            self.result = self.player1.name + " Winner"
        elif self.player2.health > self.player1.health:
            self.result = self.player2.name + " Winner!"

    def who_winner(self):
        print(self.result)


# idx = randint(1000, 9999)
my_character = Player('Max', 100, 'Nigga', 'Barbarian', 10, ids=randint(1000, 9999))
enemy = Player('Goblin', 100, 'Nigga', 'Barbarian', 10, ids=randint(1000, 9999))

battle = Fight(my_character, enemy)
battle.fight()
battle.who_winner()

print(my_character.__repr__())
print(enemy.__repr__())
