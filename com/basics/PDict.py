class PDict:
    a = None
    c = True
    b = False

    def show(self):
        dictionary = {'name': 'charlie', 'id': 100, 'dept': 'it'}
        print(dictionary.keys())
        print(dictionary.values())
        dict2 = {1:"aaa",2:"bbb",3:"ccc"}
        print(dict2.keys())
        print(dict2.get(2))
        print("hello\nuser")
        list = ['aman', 678, 20.4, 'saurav']
        list[0] = "amit"
        print(list[1:3])
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