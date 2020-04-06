import random

from model.Units.Unit import Unit


class Archer(Unit):
    price = 50
    ID = 0

    def __init__(self):
        super().__init__()
        self.healthPoints += int(random.random() * 100)
        self.maxHealthPoints = self.healthPoints
        self.arrows = 64
        self.damage += int(random.random() * 10) + 10 * self.bonus

    def fight(self, unit):
        if self.arrows < 1:
            print(self, "ran out of arrows! Buy him some new.")
            pass
        if self.stamina <= 10:
            print(self, " got too tired too shoot! Let him rest.")
            pass
        unit.alterHealth(-20)
        self.arrows -= 1

    def die(self):
        print(self, " died! Rest in Peace, hero.")
        super().die()

    def __str__(self):
        return "The Archer " + str(self.id)

    def serialize(self):
        list = super().serialize()
        list.append(self.arrows)
        list.append('archer')
        return list

    @staticmethod
    def deserialize(list: list):
        archer = Archer()
        archer.id = int(list[0])
        archer.healthPoints = int(list[1])
        archer.stamina = int(list[2])
        archer.maxHealthPoints = int(list[3])
        archer.bonus = int(list[4])
        archer.damage = int(list[5])
        archer.squadId = int(list[6])
        archer.arrows = int(list[7])
        return archer

    def printInfo(self):
        super().printInfo()
        print("Arrows:", self.arrows)