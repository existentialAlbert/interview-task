from model.Buildings.ArcherBarrack import ArcherBarrack
from model.Buildings.KnightBarrack import KnightBarrack
from model.Buildings.MageBarrack import MageBarrack


class BarrackFactory:
    @staticmethod
    def getInstance(type):
        if type == 'archer':
            return ArcherBarrack()
        elif type == 'knight':
            return KnightBarrack()
        elif type == 'mage':
            return MageBarrack()
