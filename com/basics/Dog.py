

class Dog:
    'Dog class'

    legs = 0
    breed= ""
    count1 = 0

    def __init__(self,legs,breed,count):
        self.legs = legs
        self.breed = breed
        count1 = count
        print(Dog.count1)
        print(count1)
        print(self.count1)

    def requiredFood(self):
        print("Total number of bones required", self.count*4)

    def printAge(self):
        print("There are ",self.count, " dogs of breed ", self.breed, " with age 3")


obj = Dog(4,"lll",700)