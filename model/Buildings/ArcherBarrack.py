from model.Buildings.Barrack import Barrack
from model.Units.Archer import Archer


class ArcherBarrack(Barrack):
    def __init__(self):
        super().__init__()
        self.type = 'archer'
        self.cost += Archer.price

    def recruit(self):
        return Archer()

    def __str__(self):
        return 'Archer Barrack'
