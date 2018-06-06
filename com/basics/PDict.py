class PDict:
    a = None
    c = True
    b = False

    def show(self):
        value = 'shyammohan'
        for char in value:
            print("prints each alphabet ", char)

        dictionary = {'name': 'charlie', 'id': 100, 'dept': 'it'}
        print(dictionary.keys())
        print(dictionary.values())

        for key in dictionary:
            print(key," ",dictionary.get(key))

        # for key in dictionary.keys():
        #     print("We are geting value ",dictionary.get(key))

        dict2 = {1: "aaa", 2: "bbb", 3: "ccc"}
        print(dict2.keys())
        print(dict2.get(2))
        print("hello\nuser")
        list = ['aman', 678, 20.4, 'saurav']
        i=0
        while (i<list.__len__()):
            print("Inwhile loop: ",list[i])
            i=i+1
        j=0
        while (j<list.__len__() and list[j]!=None):
            print("In second while loop: ", list[j])
            j = j + 1

        print(list)
        print(list[list.__len__()-1])
        list[0] = "amit"
        print(list[1:9])
        print(list)

    @staticmethod
    def main():
        obj = PDict ()
        obj.show ()




if __name__ == '__main__':
    PDict.main()


###########################IMP TIPS ##################################
# Tuple is similar to list where data is separated by commas.
# Only the difference is that list uses square bracket and tuple uses parenthesis.
# Tuples are enclosed in parenthesis and are immutable.
# Lists are mutable i.e., modifiable.
# The plus sign (+) is the list concatenation and asterisk(*) is the repetition operator.