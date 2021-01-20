from vegetable_factory import VegetableFactory
# from vegetable import Vegetable

class Jardinier():
    """
    docstring
    """
    def __init__(self):
        self.vf = VegetableFactory()

    
    def planter(self):
        veget_name = input("set the vegetable that want to plant")
        vegetable = self.vf.get_vegetable(veget_name)
        return vegetable