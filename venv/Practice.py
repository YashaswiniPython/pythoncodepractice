#Class example
'''class Student:
    print("first class program")
    def __init__(self):
        self.name = "yashu"
        self.age = 26
        self.marks = 80
    def talk(self):
        print("Student name is:",self.name)
        print("Student age is:", self.age)
        print("Student marks is:", self.marks)

obj=Student()
obj.talk()#'''

'''class Animals:
    print("second program on animals")
    name_of_forest = "Bandipur"
    no_of_Tigers = 12
    no_of_lions = 20
    def Tigers(self):
        print("total no of tigers", self.no_of_Tigers)
    def lions(self):
        print("total no of lions", self.no_of_lions)

o=Animals()
o.Tigers()
o.lions()'''

'''class Student:
    def __init__(self,name,age,marks):
        print("Program with constructor")
        self.name=name
        self.age=age
        self.marks=marks
    def report(self):
        print("my name is",self.name)
        print("my age is",self.age)
        print("my marks is",self.marks)
obj=Student("Anu",25,100)
obj.report()
obj2=Student("Yashu",27,100)
obj2.report()'''

#constructor example

'''class Student:
    def __init__(self,name,age): # self variable will be declared by python itself
        self.name=name # instance variable
        self.age=age # instance variable
        print("my name is", self.name)
        print("my age :", self.age)
s=Student("teju",10)
print("my name is",s.name) # we cannot call self outside the class so we use obj for reference
print("my age :",s.age)'''

'''class Test:
    def __init__(self):
        print("constructor overloading is not possible")
    def __init__(self,x):
        print("construtor o is possible")
o=Test(10)'''

# Hierarcheal Inheritance
'''class A:
    print("inheritance example")
    def Tigers(self):
        print("carnivoros")
class B(A):
    def Deer(self):
        print("Herbivoros")
class C(A):
    def Zebra(self):
        print("i am also herbivoros")
obj=C()
obj.Tigers()'''

#Multi level inheritance

'''class A:
    print("inheritance example")
    def Tigers(self):
        print("carnivoros")
class B(A):
    def Deer(self):
        print("Herbivoros")
class C(B):
    def Zebra(self):
        print("i am also herbivoros")
obj=C()
obj.Tigers()'''

#Multiple inheritance.

'''class A:
    print("inheritance example")
    def Tigers(self):
        print("carnivoros")
class B:
    def Tigers(self):
        print("Herbivoros")
class C(A,B):
    pass
    #def Zebra(self):
        #print("i am also herbivoros")
obj=C()
obj.Tigers()'''

#function example

'''def calculate(a,b):
    print("addition is ",a+b)
    print("differnece is ", a-b)
    print("Multiplication is ", a*b)
calculate(20,10)
calculate(200,100)'''

#Factorial

'''import math
print(math.factorial(5))'''

'''a=11
if (a==12):
    print("True")
elif (a==11):
    print("exactly")
else:
    print("Exit")'''

'''a=12
b=20
def addition():
    print("addition of : a+b", a+b)
addition()'''

#Exception
'''a=(int(input("value of a")))
b=(int(input("value of b")))
try:
    c=a/b
    print("result",c)

except ZeroDivisionError:
    print("dont divide by 0")

finally:
    print("Program executed")'''

a=10
b=120
c=1
print(min(a,b,c))
'''if (a>b>c):
    print("a is greater")
if(a<b>c):
    print("b is greater")
if(a<b<c):
    print("c is greater")
else:
    print("exit from program")'''

f = open("yashu.txt","r")
f.read()
print(f.readline(1))
#def addition():
    #a=10
    #b=12
    #print("Sum is",a+b)
#addition()"
















