class Student1:
    'simple class student'  # describes class characterstic
    s = 5
    rollno = 56
    empCount = 5.8

    def __init__(self, rollno, name):
        print(self.rollno)
        self.rollno = rollno
        self.name = name
        Student1.empCount += 1  # Student1.empCount = Student1.empCount+1

    def displayStudent(self):
        print("rollno : ", self.rollno, ", name: ", self.name)

    @staticmethod
    def showStudent1(arg1):
        arg1 += 5
        return arg1              #use of return statement in a method

    def calculate(self, no1):
        res = self.s+no1
        return res

    @classmethod
    def classLike(cls):
        print("%s classLike() called" % cls)
        return cls


##############Important Tips###########################################
## Variables are static in nature.
# self is a default object of class and passed in constructor along with other arguments.
# Python class can have only one constructor.
#static methods do not have 'self' whereas in instance methods 'self' is passed as argument
# @classmethod recieves one mandatory argument, class name it was called from.