class ControlStatements:

    def ifExample(self):
        a = 10
        if a >= 20:
            print("Condition is True")
        else:
            if a >= 15:
                print("Checking second value")

            else:
                print("All Conditions are false")

    def ifExample1(self):
        a = 10
        if a >= 20:
            print("Condition is True")
        elif a >= 15:
                print("Checking second value")
        else:
                print("All Conditions are false")

        listNumbers=[range(1,6)]
        print(listNumbers)

    @staticmethod
    def show():
        obj = ControlStatements()
        obj.ifExample()
        obj.ifExample1()


if __name__ == '__main__':
    ControlStatements.show()
