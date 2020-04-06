from model.Buildings.Barrack import Barrack
from model.Units.Mage import Mage


class MageBarrack(Barrack):
    def __init__(self):
        super().__init__()
        self.type = 'mage'
        self.cost += Mage.price

    def recruit(self):
        return Mage()

    def __str__(self):
        return 'Mage Barrack'
