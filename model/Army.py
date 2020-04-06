from model.Squad import Squad
from model.Units.Archer import Archer
from model.Units.Knight import Knight
from model.Units.Mage import Mage
from model.Units.Unit import Unit


class Army:

    def __init__(self):
        self.units = {}
        self.squads = {}

    def setArmy(self, units, squads):
        un = []
        for i in units:
            unit = None
            if i[-1] == 'archer':
                unit = Archer.deserialize(i)
            elif i[-1] == 'knight':
                unit = Knight.deserialize(i)
            elif i[-1] == 'mage':
                unit = Mage.deserialize(i)
            un.append(unit)
        sq = []
        if None not in squads:
            for i in squads:
                sq.append(Squad.restoreSquad(i))
        if None not in un:
            for restoredSquad in sq:
                for restoredUnit in un:
                    if restoredUnit.squadId == restoredSquad.id:
                        restoredSquad.addUnit(restoredUnit)
        if None not in squads:
            for i in range(len(sq)):
                for index in range(i, len(sq)):
                    if sq[i] != sq[index] and sq[i].parent == sq[index].id:
                        sq[i].addSquad(sq[index])
        for i in range(len(sq)):
                self.addSquad(sq[i])
        for i in un:
            if i.squadId == 0:
                self.add(i)

    def unite(self, ids: list):
        squad = Squad()
        for id in ids:
            if id > 3000000:
                squad.addSquad(self.squads.pop(id))
            else:
                squad.addUnit(self.units.pop(id))
        self.squads[squad.id] = squad

    def add(self, unit: Unit):
        self.units[unit.id] = unit

    def addSquad(self, squad: Squad):
        self.squads[squad.id] = squad

    def buff(self):
        for i in range(len(self.units)):
            self.units[i].buff += 1

    def fight(self, otherSquad):
        pass

    def getAllUnits(self):
        list = []
        for id in self.units:
            list.append(self.units[id])
        for squadId in self.squads:
            list.extend(self.squads[squadId].getUnits())
        return list

    def getAllSquads(self):
        squads = []
        for squadId in self.squads:
            squads.append(self.squads[squadId])
            squads.extend(self.squads[squadId].getSquads())
        return squads

    def __str__(self):
        units = ''
        for i in self.units:
            units += str(self.units[i]) + " "
        squads = ''
        for i in self.squads:
            squads += str(self.squads[i])
        return units + "\n" + squads
