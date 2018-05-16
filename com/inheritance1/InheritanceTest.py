from com.inheritance1.BabyDog import BabyDog
from com.inheritance1.Dog import Dog


def main():
    d = Dog("sumit")
    d.eat()
    d.bark()
    d.name1 = "sujit"
    print (d.name," ",d.name1)
    d1 = BabyDog("Rajat")
    d1.eat()
    d1.bark()
    d1.weep()
    print(d1.name)


if __name__ == '__main__':
    main()