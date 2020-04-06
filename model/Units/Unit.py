from abc import abstractmethod


class Unit:
    price: None
    ID: 0

    def __init__(self):
        self.healthPoints = 100
        self.stamina = 100
        self.maxHealthPoints = None
        self.id = self.getID()
        self.bonus = 0
        self.damage = 20
        self.squadId = 0

    @classmethod
    def getID(cls):
        cls.ID += 1
        return cls.ID

    def alterHealth(self, value):
        self.healthPoints += value
        if self.healthPoints > self.maxHealthPoints:
            self.healthPoints = self.maxHealthPoints
        if self.healthPoints <= 0:
            self.die()

    @abstractmethod
    def fight(self, unit):
        pass

    def die(self):
        del self

    @abstractmethod
    def serialize(self):
        list = [self.healthPoints, self.stamina, self.maxHealthPoints, self.bonus, self.damage, self.squadId]
        return list

    @staticmethod
    def deserialize(list: list):
        pass

    @classmethod
    def getInstance(cls):
        return cls()

    @abstractmethod
    def __str__(self):
        pass

    def printInfo(self):
        print(self)
        print("HP:", self.healthPoints, '/', self.maxHealthPoints)
        print('Stamina:', self.stamina)
        print('id:', self.id)
        print('damage:', self.damage)
        print('bonus:', self.bonus)
        print('squad ID:', self.squadId)
