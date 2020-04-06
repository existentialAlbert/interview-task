import random

from model.Units.Unit import Unit


class Mage(Unit):
    price = 125
    ID = 2000000
    spells = ({'type': 'fire', 'cost': 15}, {'type': 'freeze', 'cost': 20}, {'type': 'electricity', 'cost': 25})

    def __init__(self):
        super().__init__()
        self.healthPoints += int(random.random() * 75)
        self.maxHealthPoints = self.healthPoints
        self.mana = 100 + int(random.random() * 100)

    def fight(self, unit):
        self.spell('fire', unit)

    def spell(self, type, unit):
        spell = 0
        for i in self.spells:
            if type == i['type']:
                spell = i
        if self.mana >= spell['cost']:
            self.mana -= spell['cost']
            print(spell['type'], 'magic spelled by the Mage', self.id, '!')
            unit.alterHealth(-self.damage - spell['cost'])

    def __str__(self):
        return "The Mage " + str(self.id)

    def die(self):
        print(self, 'died! Rest in Peace, master')
        super().die()

    def serialize(self):
        list = super().serialize()
        list.append(self.mana)
        list.append('mage')
        return list

    @staticmethod
    def deserialize(list: list):
        mage = Mage()
        mage.id = int(list[0])
        mage.healthPoints = int(list[1])
        mage.stamina = int(list[2])
        mage.maxHealthPoints = int(list[3])
        mage.bonus = int(list[4])
        mage.damage = int(list[5])
        mage.squadId = int(list[6])
        mage.mana = int(list[7])
        return mage


    def printInfo(self):
        super().printInfo()
        print("mana:", self.mana)
