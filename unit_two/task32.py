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


class Player: # класс игрока
    def __init__(self, ids, name, health, race, charac_type, damage):
        self.ids = ids
        self.name = name
        self.health = health
        self.race = race
        self.charac_type = charac_type
        self.damage = damage


    def __repr__(self):
        return f"User(name={self.name},id={self.ids},health={self.health}, race={self.race},type={self.charac_type}," \
               f" damage={self.self.damage}"


    def strike(self, opposite):
        self.damage = randint(5, 12)
        opposite.health -= self.damage
        if opposite.health < 0:
            opposite.health = 0
        self.health += 0
        print(self.name, "hit", opposite.name, 'силой', self.damage)
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
            self.result = self.player2 + " Winner!"

    def who_winner(self):
        print(self.result)


id = randint(1000, 9999)
my_character = Player(id, 'Max', 100, 'Nigga', 'Barbarian', 10)
enemy = Player(id, 'Goblin', 100, 'Nigga', 'Barbarian', 10)

battle = Fight(my_character, enemy)
battle.fight()
battle.who_winner()

print(my_character.__repr__())
print(enemy.__repr__())
