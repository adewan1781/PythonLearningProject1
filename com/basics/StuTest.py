from com.basics.Student1 import Student1

print(Student1.__doc__)                #default string depicting Class description
emp1 = Student1(121, "Ajeet")
emp2 = Student1(122, "Sonoo")
emp1.s =100
print("value is:- ", emp1.s)                #instance variable changes its value per object
print("value is:- ", emp2.s)
print("value is:- ", Student1.s)            #when used with class name, variable acts as static

Student1.s = 200
print("value11 is:- ", emp1.s)
print("value22 is:- ", emp2.s)              #if  emp2 object does nnot change the value of 's' it will take the
                                            #value of 's' from its static context.
print("value is:- ", Student1.s)

emp1.displayStudent()
emp2.displayStudent()
#  Student1.displayStudent()                      #method must be called with object
print(Student1.empCount)   #accessed with classname
print (emp2.empCount)       #accessed with object

res = emp2.calculate(15)
print("result is:- ",res)
print("result is:- %d" % res)

Student1.showStudent1(2)
a=Student1.showStudent1(5)                        #way to call static method
print(a)
emp1.showStudent1(34)

cls =Student1.classLike()
print(cls.s)                                     # sameas calling variable from static context
# print cls.displayStudent()                    #wrong can not call methods

print("Total Employee %d" % Student1.empCount)        #way to represent integer value in String
print("Total Employee: ", Student1.empCount)

# print Student1.calculate(10)                       #method must be called with object

