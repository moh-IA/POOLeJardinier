# from tomato import Tomato
from potato import Potato
from garden import Garden
from jardiner import Jardinier



if __name__ == "__main__":
    
    # potato = Potato ()
    # potato.grow(6)
    # print(potato.seed)

    j = Jardinier()
    
    veg = j.planter()
    # veg.grow(5)
    g = Garden()

    g.add(veg)
    # print(g.seed)

    p = Potato()
    p.grow(8)
    # p2 = Potato()
    # p2.grow(8)



    g.add(p)
    # g.add(p2)
    print(g.seeds)
    print(len(g.vegetables))