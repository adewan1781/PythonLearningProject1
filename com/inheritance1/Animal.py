class Animal(object):
    'animal class'
    def __init__(self, name):
        print ("jalandhar animal")
        self.name = name

    def eat(self):
        print('Eating...from animal')
        super(Animal, self).__init__()

#############################################INHERITANCE TIPS###############################################
# Inheriting object class is optional
# super is the object of superclass
# super() used with (self)delegate and __init__ is used as coonstructor call of parent.
# when constructor is created with two underscores, when called class own constructor runs
# when constructor is created with three underscores, when called super class constructor runs
