class ListTuple:

    def printTuple(self):
        tuple = ("ant",9,"rat",5,"sumit",15,"lalit",45,"sanjay")
        tuple1 = ("rajat", 8)
        tuple = tuple+tuple1
        for sampleObj in tuple:
            print("object value is ",sampleObj)
        print(tuple)
        print(tuple[2:7])       #index starts from zero, argument before colon is element at index
                                 # argumeent after colon is till element number
        print ("Value is", tuple[5])

    def printList(self):
        list = [1, "free", 23, "head", 55, "pint"]
        list1 = ["queen", "king"]
        list = list+list1
        print(list)
        print(list[2:5])
        list2 = list1*3
        print(list2)

    @staticmethod
    def show():
        obj = ListTuple()
        obj.printTuple()
        obj.printList()


if __name__ == '__main__':
   ListTuple.show()
