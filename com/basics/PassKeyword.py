class PassKeyword:

    def show(self):
        for i in [1, 2, 3, 4, 5]:
            if i == 3:
                pass
                print( "Pass when value is", i)
            print(i)

    def show1(self):
        string1='pythonvsjava'
        print(string1[4])
        print(string1[-4])
        count = string1.__len__()
        count1=len(string1)
        print(count,' ',count1)
        print("Pass when value is", 12)     #: when concatenated with '+' operator, Both the operands passed for concatenation
                                            # must be of same type, else it will show an error.


if __name__ == '__main__':
    obj = PassKeyword()
    obj.show1()