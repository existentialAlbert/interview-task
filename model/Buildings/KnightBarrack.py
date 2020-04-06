from model.Buildings.Barrack import Barrack
from model.Units.Knight import Knight


class KnightBarrack(Barrack):
    def __init__(self):
        super().__init__()
        self.type = 'knight'
        self.cost += Knight.price

    def recruit(self):
        return Knight()

    def __str__(self):
        return 'Knight Barrack'
