from vegetable import Vegetable


class Garden():
    """
    docstring
    """
    def __init__(self):
        self.seeds = 0
        self.vegetables = []

    def _plant(self, vegetable):
        self.seeds += vegetable.seed
        self.vegetables.append(vegetable)
       
    def add(self, vegetable):
        return self._plant(vegetable) 








