from vegetable import Vegetable

class Tomato(Vegetable):
    """
    docstring
    """
    def __init__(self, seed=0):
        self.seed = seed

    def grow(self, seed = 0):
        self.seed = seed 
        return self.seed
#