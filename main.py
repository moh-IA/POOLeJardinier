# from tomato import Tomato
from potato import Potato
from garden import Garden
from jardiner import Jardinier



if __name__ == "__main__":
    
    

    j = Jardinier()
    veg = j.planter()
    veg.grow(3)
    
    g = Garden()
    g.add(veg)
    

    p = Potato()
    p.grow(27)
    g.add(p)
    
    print(g.seeds)
    print(len(g.vegetables))