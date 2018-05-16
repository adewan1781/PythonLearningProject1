from com.inheritance1.Animal import Animal
from com.inheritance1.FParent import FParent


class MultiDerived(Animal,FParent):

    def ___init__(self):
        print("i am Multiderived")
