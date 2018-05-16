from com.inheritance1.Animal import Animal


class Dog(Animal):
    def ___init__(self, name1):                 # constructor with three underscores
        print("constructor from dog")
        self.name1 = name1

    def bark(self):
        print('dog Barking...')
        super(Dog, self).eat()



def eat(self):
    print("eating from dog")
    Animal("lkl").eat()
