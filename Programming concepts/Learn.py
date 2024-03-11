#All the basic Python concepts that are needed in the first semester university level college exams or basic Competitive Programming.

"""
Comments
#Python will not print this text
"""


"""
multi
vitamin
tablets
"""


"""
#Backslash usage
print("This is not what I imagined coding would be like \t " , "or was it", end="?")

print("\nWell, maybe.")
"""


"""
#Backslash Function
print("He said \"You should not talk to me like that.\"")

print("\\nevertheless")
"""


"""
#Variables
x="Someone"
y="idiot"
print(""+x+" is an "+y+"")

y="genius"
print(""+x+" is a "+y+"")
"""
"""
#Variable datatypes
x="Hello"
y=987
z=80.91
q="people"
t="76"
r="54"

print(type(x))
print(type(y))
print(type(z))

print(100*y + z)
print(x + " " + q)

print(t+r)
print(int(t) + int(r))

print(5*x)

print(10*str(int(t)+int(r)))

"""
"""
#Input function
print("Enter the value")
x = input()
print("You entered", x)

print("You entered", int(x)+100)
"""
"""
#Input addition
print("Enter first number")
x = input()
print("Enter second number")
y = input()

print("You entered", int(x) + int(y))
"""
"""
#String slicing and functions
x = "Akarshan is talented"

print(x[0:8])

print(len(x))

print(x[0:8:2])
print(x[0::8])

print(x[0:])
print(x[:5])
print(x[:])
print(x[::])
print(x[0:20:1])
print(x[-3:-1])
print(x[3:-1])
print(x[-3:])
print(x[::-1])
print(x[::-2])

print(type(x))
print(x.isalnum())
print(x.isalpha())

x="Akarshanistalented"
print(x.isalnum())
print(x.isalpha())

x="akarshan is talented"
print(x.endswith("talented"))
print(x.endswith("open"))

print(x.count("x"))
print(x.count("a"))

print(x.capitalize())

print(x.find("is"))

x="Akarshan is talented"
print(x.lower())
print(x.upper())

print(x.replace("is","are",))
"""
"""
#List
Band = ["Suraj","Puraskar","Bharat","Vishikh","Gaurav","Saraj",75]

print(Band)
print(Band[0])
print(Band[4])

print("\n")
numbers = [5,11,3,9,8]
numbers.sort()
numbers.reverse()

print("\n")
print(numbers)

print("\n")
print(numbers[:4])

print("\n")
print(len(numbers))

print("\n")
print(numbers)
print(numbers[::1])
print(numbers[0:5:1])
print(numbers[1:4:2])
print(numbers[::-1])
print(numbers[::-2])

print("\n")
print(max(numbers))
print(min(numbers))

print("\n \n")
nums = [5,11,3,9,8]
nums.append(7)
print(nums)

print("\n")
nums.insert(2,54)
print(nums)

print("\n")
nums.remove(9)
print(nums)

print("\n")
nums.insert(4,9)
print(nums)

print("\n")
nums.pop()
print(nums)

print("\n")
nums[1] = 32
print(nums)
nums[1] = 11
print(nums)

#Mutable = can change
#Immutable = cannot change

tp = (1, 2, 3)
print(tp)

a = 1
b = 7
temp = a
a = b
b = temp
print(a,b)
"""
"""
#Dictionary
t1 = ()
print(type(t1))

d1 = {}
print(type(d1))

d2 = {"Akarshan":"Analyst", "Aakanshu":"Drums", "Vaibhav":{"1":"Bass","2":"Guitar","3":"Chorus"}, "Shreshth":"Vocal"}
print(d2)
print(d2["Akarshan"])
print(d2["Vaibhav"]["1"])

d2["Utsav"] = "Percussions"
d2["Hemant"] = "Strings"
print(d2)

d3 = d2.copy()
del d3["Shreshth"]

print(d2)
print(d3)

print(d2.get("Akarshan"))

d2.update({"Shreshth":"Singing"})
print(d2)

print(d2.keys())
print(d2.items())
"""
"""
#Sets
x = set()

print(type(x))

y = set([1,2,3,4])
print(y)
print(type(y))

x.add(1)
x.add(1)
x.add(2)

x1 = x.union({1,2,3})
print(x,x1)

x2 = x.intersection({1,2,3})
print(x,x2)

print(x.isdisjoint(x1))
"""
"""
x = 6
y = 77

a = int(input("Number: "))

if a>y:
    print("Greater")

if a==y:
    print("Equal")

else:
    print("Lesser")

l1 = [1, 2, 3]
print(a in l1)
if a in l1:
    print("Yes, it's in the list.")

print(a not in l1)
if a not in l1:
    print("No, it's not in the list")

print("What is your age?")
b = int(input("My age is "))

if b<7 or b>95:
    print("Cannot perform task.")

elif b==7:
    print("You are physically required to qualify.")

else:
    print("You are qualified")
"""
"""
#For Loops

l1 = [["Akarshan",1],["Aditya",2],["Aakanshu",3],["Shreshth",4]]
d1 = dict(l1)
print(d1)

for item,num in d1.items():
    print(item,"and the number is", num)

l2 = [1, 77, "niawd", "dawd", 8,5,1,99]
print(l2)

for obj in l2:
    if str(obj).isnumeric() and obj > 6:
        print(obj)

l3 = ['dawd','ada',12312,2,2,45,6]
for num in l3:
    if str(num).isnumeric():
        print(num)

"""
"""
#While Loops

i = 0

while(i<45):
    print(i)
    i = i+2
"""
"""
#Break and Continue

i = 0

while (True):
    if i<5:
        i = i+1
        continue

    print(i, end=" ")
    if (i == 45):
        break

    i = i+1
"""
"""
while (True):
    x = int(input("Enter a number: "))
    if x > 100:
        print("Yes")
        break

    else:
        print("No")
        continue
"""
"""
#Operators

#Arithematic Operators are + - * / // **

#Assignment Operators

x=7
print(x)

x+=5
print(x)

x-=9
print(x)

x*=99
print(x)

x/=9
print(x)

x%=19
print(x)

#Comparison

i = 5
print(i==8)
print(i==5)
print(i!=5)

#Logical (Boolean Expressions)

a = True
b = False

print(a and b)
print(a or b)

print(a is b)
print(a is not b)

#Identity

print(5 is not 7)
print(5 is 7)

#Membership

l1 = [1,2,5,6,211,2,31]

print(1 in l1)
print(212 in l1)

#Bitwise

print(0 and 1)
print(0 or 1)
"""
"""
#Functions and docstrings

a = 9
b = 8
c = sum((a,b)) #built in function
print(c)

def f1(a,b):
    """Sum of two numbers."""
    sum = a + b
    print("you are in f1", sum)
    return sum

v=f1(5,7)
print(v)

print(f1.__doc__)
"""
"""
#Try except Handling
print("enter x ")
x = input()
print("enter y ")
y = input()
try:
    print("sum is", int(x)+int(y))
except:
    print("Nope")
"""
"""
#Test

x = input("Print table of: ")

y = 1

while str(x).isnumeric():
    print(int(x)*int(y))
    y = y+1

    if y>10:
        break

if str(x).isalpha():
    print("Invalid input.")
"""
"""
#Recursions

def fib(n):
    if(n==0):
        return 0
    
    elif n==1:
        return 1
         
    else:
        return (n-2) + fib(n-1)

x = int(input("Print fibonacci number till: "))
print(fib(x))


def factorial(n):
    if n<0:
        print("Invalid input")
    
    elif (n==0) or (n==1):
        return 1

    else:
        return n * factorial(n-1)

x = input("Print Factorial of: ")
print(factorial(int(x)))
"""
"""
#Nested Loops

for x in range(3):
    for y in range(1,10):
        print(y, end=" ")
    print()

for z in range(5):
    print(7)

a = 9
while (True):
    print(a)
    while (True):
        print(a)
        a = a+1

        if a > 10:
            break
    break
"""
"""
# File IO Basics

# "r" - Open file for reading.
# "w" - Open a file for writing.
# "x" - Creates file if doesn't exist.
# "a" - Add more content to a file.
# "t" - text mode.
# "b" - binary mode.
# "+" - read and write both.
"""


"""
#Read a file
x = open("FIle.txt", "rt")

print(x.readlines())
# print(x.readline())
# print(x.readline())

# content = x.read(3)
# print(content)
#
# content = x.read(3)
# print(content)

# for line in x:
#     print(line, end='')
#
x.close()
"""
"""
#Writing and Appending to a file
x = open("FIle.txt", "a")
a = x.write("A demo output.\n")
x.close()
"""
"""
#Read and write both

f = open("FIle.txt", "r+")
print(f.read())
f.write("Thanks!")
"""
"""
#Input appending
x = input("What do you want to write in the file?\n")

y = open("FIle.txt", "a")

y.write(x)

y.close()
"""
"""
#Seek, Tell and Hide
#tell shows where the open statement in the program has reached.
#seek resets the open statement's place to the desired character.

x = open("FIle.txt")
#print(x.tell())
print(x.readline())
#print(x.tell())

x.seek(0)

print(x.readline())
#print(x.tell())

x.close()
"""
"""
#With block

with open("FIle.txt") as x:
    a = x.read(2)
    print(a)

"""
"""
#Scope, Global Variables and Global Keywords

l = 10 #Global variable

def func1(n):
    #l = 5 #Local Variable

    global l #allows permission to manipulate global variable

    l = l + 45

    print(l)
    print(n, "I have printed.")

    #Local variable is the priority. (Variable inside scope = Local, Outside = Global.
    #Global variable cannot gets it's value changed inside the function without 'global' keyword.
func1("awudbaw")
print(l)

def py():
    x = 90

    def txte():
        global x

        x = 88
        print(x)

    print(x) #Code will search for thiss instead of local variable inside a function.

py()
"""
"""
#Lambda functions (creates functions)

add = lambda x, y: x + y

print(add(8,4))

def i_first(i):
    return i[1]

i = [[1,22],[3,4],[6,8],[9,10]]
# i.sort(key=i_first)
i.sort(key=lambda x:x[1])
print(i)
"""
"""
#External and Built-in modules
    #Too many functions, no need to remember


import random

a = [1,2,3,4,5]

print(random.choice(a))

#Go to terminal, type example "pip install sklearn", to install sklearn
#Similarily, you can upgrade python by typing "python.exe -m pip install --upgrade pip" inside terminal.
"""
"""
#F strings & S strings

import math

any = "whatever"
op = "iawd"
b = "wygdw %s %s"%(any,op)
print(b)

wh = "wadjawd"
pn = 90
lpc = "kya hua {1} {0}"
q = lpc.format(wh,pn)
print(q)

#F string

z = f"why is {pn} {wh} {4*8} {math.cos(97)}"
print(z)
"""
"""
c
"""
"""
#*args and *kwargs

#def whatever(a,b,c,d):#Cannot add e
#    print(a,b,c,d)

def funargs(normal, *args, **kwargs): #normal argument always first
    print(normal)
    print(type(args)) #Always in tuple
    print(args[0])

    for item in args:
        print(item)

    print("\nDoubling some digits: ")

    for key,value in kwargs.items():
        print(f"{key} multipy 2 equals {value}")

harry = [1,2,3,4,5]
normal = 34561237
kw ={"6":12,"7":14,"8":16,"9":18,"0":0}
funargs(normal,*harry,**kw)
"""
"""
#Time module

import time

initial = time.time()
print(initial)

k = 0
while (k<2):
    print("Repeat this")
    time.sleep(2)
    k+=1

print("While loop: ", time.time() - initial, "seconds")
initial2 = time.time()

for i in range(2):
    time.sleep(2)
    print("Repeat this")
print("For loop: ", time.time() - initial2, "seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
"""
"""
#Enumarate Function

a1 = ["a","b","c","d"]

i = 1

for item in a1:
    if i%2 != 0:
        print(f"Please buy {item}")
    i += 1

for index, item in enumerate(a1):
    if index%2==0:
        print(f"Please buy {item}")
"""
"""
#Import

import panda
print(panda.a)
panda.p("lmao")


# This should be in Panda.py file
#
#     a = 7
#
#     def p(str):
#         print(f"This function is a joke {str}")

#from panda import a
#print(a)
"""
"""
#
import panda

print(panda.add(5,7))


# This must be written in TwoIndex.py file
# 
#     def pr(string):
#         return f"What is this {string}"
#     
#     def add(x,y):
#         return x + y + 5
#     
#     # print(pr("z"))
#     # q = add(5,7)
#     # print(q)
#     # print(pr(q))
#     print("and the name is", __name__)
#     
#     if __name__=='__main__':#Only executes when used in a seperate program (here)
#         print(pr("Python"))
#         yt = add(7,9)
#         print(yt)
"""
"""
#Join function
cop = ["What","is","This","Madness","no","idea"]

o = "and".join(cop)
print(o,"other words.")
"""
"""
#Map function

num = ["3","45","12"]
print(map(int, num))
num = list(map(int, num)) #object at memory location

num[1] = num[1] + 1
print(num[1])

square = list(map(lambda x: x**2, num))
print(square)

def add(a):
    return a+10

def minus(a):
    return a-10

func = [add, minus]

for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)
"""
"""
#Filter

l1 = [1,2,3,4,5,6,7]

def gr_than(x):
    return x>5

gr_than = list(filter(gr_than, l1)
print(gr_than)
"""
"""
#Reduce

from functools import reduce

l1 = [1,2,3,4]
num = reduce(lambda x,y:x*y, l1)
print(num)

# num = 0
#
# for i in l1:
#     num = num + i
# print(num)
"""
"""
#Decorators

def func(x):
    if x ==0:
        return print

    if x ==1:
        return int

    if x==2:
        return sum

a = func(0)
print(a)

b = func(1)
print(b)

c = func(2)
print(c)

def executor(funk):
    funk("this")

executor(print)

def dec1(func1):
    def now():
        print("Now.")
        func1()
        print("Done")
    return now

def wih():
    print("Harry is a good boy.")

wih = dec1(wih)
wih()
"""
"""
#Classes

class Employee:
    no_of_leaves = 8 #Class variable
    pass

harish = Employee()
rohan = Employee()

harish.name="Harish"
harish.salary = 455 #Instance variable
harish.role = "Teacher"

rohan.name="Rohan"
rohan.salary=7888
rohan.role = "Student"

print(rohan.__dict__)
print(harish.no_of_leaves)
print(Employee.no_of_leaves)
rohan.no_of_leaves = 9
print(rohan.no_of_leaves)
print(rohan.__dict__)
print(Employee.__dict__)
"""
"""
#Self and innit

class Employee:

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    no_of_leaves = 8

    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"

harish = Employee("Harish",455,"Instructor")
# harish = Employee()
# harish.name = "Harish"
# harish.salary = 455
# harish.role = "Teacher"
#
# rohan = Employee()
# rohan.name = "Rohan"
# rohan.salary = 7888
# rohan.role = "Student"

print(harish.printdetails())
"""
"""
#Class methods

class Employee:
    no_of_leaves = 8

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"

harish = Employee("Harish",455,"Instructor")
rohan = Employee("Rohan",4555,"Student")

rohan.change_leaves(34)

print(rohan.no_of_leaves)
print(Employee.no_of_leaves)
"""
"""
#Class methods as alternative constructors (Doubt)

class Employee:
    no_of_leaves = 8

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def from_str(cls, something):
        params = something.split("-")
        print(params)
        return cls.(params[0],params[1],params[2])


    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"

harish = Employee("Harish",455,"Instructor")
rohan = Employee("Rohan",4555,"Student")
karan = Employee.from_str("Karan-480-Student")
"""
"""
#Static methods (Doubt)

class Employee:
    no_of_leaves = 8

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"

    def printgood(self):
        print("This is good = " + self.name)
        return 89

harish = Employee("Harish",455,"Instructor")
rohan = Employee("Rohan",4555,"Student")

print(rohan.printgood())
"""
"""
#Abstraction and Encapsulation
"""
"""
#Single Inheritance

class Employee:
    no_of_leaves = 8

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"

    def printgood(self):
        print("This is good = " + self.name)

class Programmer(Employee):
    def __init__(self,name, salary,role,languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def printprog(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}. The languages are {self.languages}"

    pass

harish = Employee("Harish",455,"Instructor")
rohan = Employee("Rohan",4555,"Student")

shruti = Programmer("Shubham",8999,"Programmer",["Python"])
keshav = Programmer("Keshav",9000,"Programmer",["Java","C++"])
print(keshav.printdetails())
print(keshav.printprog())
"""
"""
#Multiple Inheritance

class Employee:
    no_of_leaves = 8
    var = 9
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"

    def printgood(self):
        print("This is good = " + self.name)

class Player:
    no_of_games = 4
    var = 8
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printgame(self):
        return f"The name is {self.name}. Salary is {self.game}"

class CoolProgrammer(Employee, Player):
    language = "C++"

    def printlang(self):
        print(self.language)

harish = Employee("Harish",455,"Instructor")
rohan = Employee("Rohan",4555,"Student")

shubh = Player("Shubh",["Cricket"])
karan = CoolProgrammer("Karan",90000,"Programmer")
det = karan.printdetails()

print(det)
print(karan.var) #Will run variable with first prefrence
"""
"""
#Multilevel Inheritance

class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance = 6

    def isdance(self): #Will overwrite son class function.
        return f"Jackson yeah!" \
            f" Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harish = Grandson()

print(harish.isdance())
print(harish.basketball)
"""
"""
#Public - Anyone can see this (outside a home)
#Protected - Selected people can see it (starts with underscore).
#Private - Only you can see it (double underscore)
#Done with nomenclature

class Employee:
    no_of_leaves = 8 #Public
    var = 9
    _this = 89 #Protected
    __praa = 21

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def printdetails(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"

    def printgood(self):
        print("This is good = " + self.name)

harry = Employee("Harry",9000,"erp")
print(harry.no_of_leaves) #Public calling
print(harry._this) #Protected calling
print(harry._Employee__praa) #Private calling
"""
"""
#Polymorphism (Different faces of two things.)
#Abstraction, Encapsulation, Decorators, Inheritance (class, abstract and static,etc methods)

print(8+7)
print("8" + "7")
"""
"""
#Decorators

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def who_is_harry():
    print("Harry is a good boy")

# who_is_harry = dec1(who_is_harry)

who_is_harry()
"""
"""

"""
