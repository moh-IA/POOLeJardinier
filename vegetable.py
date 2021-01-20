from abc import ABC, abstractmethod

class Vegetable(ABC):
    """
    docstring
    """
    
    
    @abstractmethod
    def grow(self, seed = 0):
        pass


