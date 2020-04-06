from threading import Thread

import pandas

from model.Army import Army
from model.Buildings.BarrackFactory import BarrackFactory
from model.Units.Archer import Archer
from model.Units.Knight import Knight
from model.Units.Mage import Mage


class Player(Thread):
    help = "work - get gold" \
           "barrack [type] - build barrack to buy units of [type] kind" \
           "save - save your army" \
           "load - restore your army" \
           "buy [type] [amount] - buy some units" \
           "unite - unite your squads and units in a new squad" \
           "print - get info about your army"

    def __init__(self):
        super().__init__()
        self.gold = 1000
        self.__army = Army()
        self.__buildings = []

    def run(self):
        while True:
            try:
                command = input()
                if command == 'exit':
                    break
                self.execute(command)
            except SyntaxError:
                print('Unknown command! Type "help" for the list of commands')
                continue

    def alterGold(self, value):
        if self.gold + value < 0:
            print('Not enough gold! You have ' + str(self.gold))
            return
        else:
            self.gold += value
        label = 'increased' if value > 0 else 'decreased'
        print('Your amount of gold', label, 'on', abs(value), end=".\n")
        print('Now it is', self.gold)

    def execute(self, command):
        command = str.split(command, " ")
        c = command[0]
        try:
            if c == 'help':
                print(self.help)
            elif c == 'buy':
                for i in self.__buildings:
                    if i.type == command[1]:
                        for j in range(int(command[2])):
                            self.__army.add(i.recruit())
                        self.alterGold(-i.recruit().price * int(command[2]))
                        print('Recruited', command[2], 'new', command[1] + 's')
                        break
                else:
                    print('You have not such barrack!')
            elif c == 'print':
                print(self.__army)
                for i in range(len(self.__buildings)):
                    print(self.__buildings[i], end=" ")
                print()
            elif c == 'barrack':
                building = BarrackFactory.getInstance(command[1])
                self.alterGold(-building.cost)
                self.__buildings.append(building)
                print('Built new', building)
            elif c == 'work':
                self.alterGold(500)
            elif c == 'save':
                allUnits = self.__army.getAllUnits()
                allSquads = self.__army.getAllSquads()
                data = {}
                data1 = {}
                data2 = {}
                for i in allUnits:
                    data[i.id] = i.serialize()
                for i in allSquads:
                    data1[i.id] = i.parent
                for i in self.__buildings:
                    data2[i.type] = [True]
                data2['gold'] = [self.gold]
                pandas.DataFrame(data).to_csv('units.csv')
                pandas.DataFrame(data1).to_csv('squads.csv')
                pandas.DataFrame(data2).to_csv('barracks.csv')
                print('Saved!')
            elif c == 'load':
                data = pandas.read_csv('units.csv')
                data1 = pandas.read_csv('squads.csv')
                data2 = pandas.read_csv('barracks.csv')
                restoredUnits = Player.fromCSVtoList(data)
                restoredSquads = Player.fromCSVtoList(data1)
                restoredMeta = Player.fromCSVtoList(data2)
                if not None in restoredMeta:
                    self.gold = int(restoredMeta[-1][1])
                    for i in restoredMeta:
                        if i[0] == 'mage':
                            self.__buildings.append(BarrackFactory.getInstance('mage'))
                        if i[0] == 'knight':
                            self.__buildings.append(BarrackFactory.getInstance('knight'))
                        if i[0] == 'archer':
                            self.__buildings.append(BarrackFactory.getInstance('archer'))
                self.__army.setArmy(restoredUnits, restoredSquads)
                print("Army restored!")
            elif c == 'unite':
                args = [int(i) for i in command[1:]]
                self.__army.unite(args)
            elif c == 'info':
                list = self.__army.getAllUnits()
                for i in list:
                    if i.id == int(command[1]):
                        i.printInfo()
                        break
            else:
                raise SyntaxError
        except IndexError:
            print("Incorrect amount of arguments!")

    @staticmethod
    def fromCSVtoList(csv):
        if str(csv).find("Empty") > -1:
            return [None]
        dataStringified = str(csv).split(" ")
        dataCleaned = []
        for i in dataStringified:
            if i != '' and i != 'Unnamed:':
                if i.find("\n") > 0:
                    l = i.replace("\n", " ").split(" ")
                    dataCleaned.append(l[0])
                    dataCleaned.append("\n")
                    dataCleaned.append(l[1])
                else:
                    dataCleaned.append(i)
        rows = ' '.join(dataCleaned).split("\n")
        data = []
        for i in range(len(rows)):
            if i == 0:
                data.append(rows[i].strip()[2:])  # ХАРДКОД!!!!
            else:
                data.append(rows[i].strip()[4:])
        list = []
        for i in range(len(data[0].split(" "))):  # 6
            row = []  # 10
            for j in range(len(data)):  # 10
                row.append(data[j].split(" ")[i])
            list.append(row)
        return list

    def fight(self):
        pass
