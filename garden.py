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
        if self.seeds <= 30:
            self.vegetables.append(vegetable)
        else:
            self.seeds -= vegetable.seed
            print('The garden can not grow more than thirty seeds')
       
    def add(self, vegetable):
        return self._plant(vegetable) 








