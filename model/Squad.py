class Squad:
    ID = 3000000

    def __init__(self):
        self.units = {}
        self.squads = {}
        self.parent = 0,
        self.id = Squad.getId()

    @classmethod
    def getId(cls):
        cls.ID += 1
        return cls.ID

    def addUnit(self, unit):
        self.units[unit.id] = unit
        unit.squadId = self.id
        self.buff()

    def addSquad(self, squad):
        self.squads[squad.id] = squad
        squad.parent = self.id
        squad.buff()

    def buff(self):
        for id in self.units:
            self.units[id].bonus += 1
        for id in self.squads:
            self.squads[id].buff()

    def getUnits(self):
        list = []
        for unit in self.units:
            list.append(self.units[unit])
        for squad in self.squads:
            list.extend(self.squads[squad].getUnits())
        return list

    def getSquads(self):
        list = []
        for id in self.squads:
            list.append(self.squads[id])
            list.extend(self.squads[id].getSquads())
        return list

    @staticmethod
    def restoreSquad(data):
        a = Squad()
        a.parent = int(data[1])
        a.id = int(data[0])
        return a

    def __str__(self):
        units = ''
        for i in self.units:
            units += str(self.units[i]) + " "
        squads = ''
        for i in self.squads:
            squads += str(self.squads[i])
        if squads == '':
            squads = 'no'
        return 'Squad ' + str(self.id) + ':\n\tUnits:\n\t' + units + '\n\tSquads:\n\t\t' + squads
