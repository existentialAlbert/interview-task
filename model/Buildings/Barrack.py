from abc import abstractmethod


class Barrack:
    def __init__(self):
        self.cost = 300

    @abstractmethod
    def recruit(self):
        pass

    def __str__(self):
        return 'barrack'
