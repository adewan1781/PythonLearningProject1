

class Dog:
    'Dog class'

    legs = 0
    breed= ""
    count = 0

    def __init__(self,legs,breed,count):
        self.legs = legs
        self.breed = breed
        self.count = count

    def requiredFood(self):
        print("Total number of bones required", self.count*4)

    def printAge(self):
        print("There are ",self.count, " dogs of breed ", self.breed, " with age 3")


