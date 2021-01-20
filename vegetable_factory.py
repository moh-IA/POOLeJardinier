from tomato import Tomato
from potato import Potato
from pimiento import Pimiento


class VegetableFactory():
    """
    docstring
    """
    def get_vegetable(self, name):
        
        if  name == 'Tomato' :
            return Tomato()
        
        elif name == 'Potato':
            return Potato()
        
        elif name == 'Pimiento':
            return Pimiento()
    