from filecmp import cmp

str="Welcome to SSSIT"
substr1="come"
substr2="to"
substr3 = "Good"
print(str.find(substr1))
print(str.find(substr2))
print(str.find(substr1,3,10))
print(str.find(substr2,19))
print(str.find(substr3))

list1=[101,981,'abcd','xyz','m']
list2=['aman','shekhar',100.45,98.2]
list3=[101,981,'abcd','xyz','m']
print(cmp(list1,list2))
print(cmp[list2,list1])
print(cmp[list3,list1])

