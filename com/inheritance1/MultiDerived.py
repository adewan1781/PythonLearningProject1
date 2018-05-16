from com.inheritance1.Animal import Animal
from com.inheritance1.FParent import FParent


class MultiDerived(Animal,FParent):             # In multiple inheritance first super-class constructor runs

    def ___init__(self):                 # here Animal class constructor runs first because it is paarent no 1
        print("i am Multiderived")
