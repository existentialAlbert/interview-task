import random

from model.Units.Unit import Unit


class Knight(Unit):
    price = 75
    ID = 1000000

    def __init__(self):
        super().__init__()
        self.healthPoints += int(random.random() * 150)
        self.maxHealthPoints = self.healthPoints
        self.armour = int((1 - random.random() / 2) * 100) / 100
        self.damage = int(random.random() * 10) + 30 * self.bonus * 10

    def fight(self, unit):
        if self.stamina > 0:
            unit.alterHealth(-self.damage)
            self.stamina -= 20
        else:
            print(self, 'is out of energy!')
        self.alterHealth(-unit.damage)

    def alterHealth(self, value):
        super().alterHealth(int(value * self.armour))

    def die(self):
        print(self, "has fallen! Rest In Peace, sir")
        super().die()

    def __str__(self):
        return "The Knight " + str(self.id)

    def serialize(self):
        list = super().serialize()
        list.append(self.armour)
        list.append('knight')
        return list

    @staticmethod
    def deserialize(list: list):
        knight = Knight()
        knight.healthPoints = int(list[1])
        knight.stamina = int(list[2])
        knight.maxHealthPoints = int(list[3])
        knight.id = int(list[0])
        knight.bonus = int(list[4])
        knight.damage = int(list[5])
        knight.squadId = int(list[6])
        knight.armour = float(list[7])
        return knight

    def printInfo(self):
        super().printInfo()
        print("Armour:", self.armour)
