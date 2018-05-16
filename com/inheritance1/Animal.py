class Animal(object):
    'animal class'
    def __init__(self, name):
        print ("jalandhar animal")
        self.name = name

    def eat(self):
        print('Eating...from animal')
        super(Animal, self).__init__()


