from com.basics.Dog import Dog


def main():
    print(Dog.breed)
    obj1 = Dog(4, "labrador", 5)
    obj1.requiredFood()
    obj1.printAge()

if __name__ == '__main__':
    main()