#Basic numpy functions and classes


"""
#Array
import numpy as np

a = np.array([1,2,3,4])
print(a)
print(type(a)) #Types
print(a.ndim) #Dimensions

y = np.array([[1,2,3],[4,5,6]])
print(y)
print(y.ndim)

arn = np.array([1,2,3,4], ndnp.array([1,2,3,4],ndmin= 4)min = 10)
print(arn)
print(arn.ndim)
"""


"""
#Special Arrays
import numpy as np

ar_zero1 = np.zeros(4)
print(ar_zero1)

ar_zero2 = np.zeros((3,4))
print(ar_zero2)

ar_one1 = np.ones(4)
print(ar_one1)

ar_one2 = np.ones((3,4))
print(ar_one2)

ar_empty1 = np.empty(4)
print(ar_empty1) #This stores value of previous array in it

ar_rn = np.arange(4) #Array from 0-3
print(ar_rn)

ar_diag = np.eye(3,5)
print(ar_diag)

ar_lin = np.linspace(1,10,num = 5) #(x,y,z) from x to y with number of elements = z with automatic gap)
print(ar_lin)
"""


"""
#Arrays with random values

import numpy as np

arr = np.random.rand(5) #Generates random values
print(arr)

arr2 = np.random.rand(3,4)
print(arr2)

arrz = np.random.randn(6) #Generating numbers close to zero even negative
print(arrz)

arr_deci = np.random.ranf(5) #Array with intervals [0.0,1.0)
print(arr_deci)

arr_range = np.random.randint(2,9,4) #Generating array with a range and given elements (x,y,z) numbers from x to y generating z elements
print(arr_range)
"""


"""
#Bit size clarification
import numpy as np

myarr = np.array([[3,4,5,6]], np.int8) #Uses 8 bit integer
print(myarr)

# larr = np.array([3,4,5,312381273], np.int8) #Shows overflow error
# print(larr)

print(myarr[0,1])
print(myarr.dtype)
"""


"""
#Arithmetic Functions

import numpy as np

var1 = np.array([1,2,3,4,5])
var2 = np.array([1,2,3,4,5])

varadd = np.add(var1,5) #var1 + 5 #Same with -, *, / and % and np.reciprocal
varadd2 = np.add(var1,var2) #var1 + var2 #Same with - np.subtract
varmul = np.multiply(var1,var2) #var1 * var2 #Same with / and % np.divide and np.mod
varpow = np.power(var1,var2) #var1**var2

print(varadd)
print(varadd2)
print(varmul)
print(varpow)
"""


"""
#2D Array

import numpy as np

vard1 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
vard2 = np.array([[1,2,3,4,5],[1,2,3,4,5]])

vardadd = vard1 + vard2 #Same 1D array functions can apply here.

print(vardadd)
"""


"""
#Arithmetic functions
import numpy as np

var = np.array([1,2,3,4,5,23,2,3])

print(np.min(var), np.argmin(var)) #min/max = value argmin/argmax = position
print(np.max(var), np.argmax(var))

var1 = np.array([[2,1,3],[3,2,4]]) #axis = 0 is column and axis = 1 is row

print(np.min(var1, axis = 1)) #Minimum from all row
print(np.min(var1, axis = 0)) #Minimum from all column

print(np.sqrt(var1)) #Square root and same functions like np.sin() and np.cos()

print(np.cumsum(var1)) #Community sum technique must learnN
"""
"""
#Shaping (Matrix 2X2 vs array(2,2))
import numpy as np

var = np.array([[1,2],[1,2]])
print(var)
print(var.shape) #Gives shape of array (no. in 1st box, 2nd box)

varn = np.array([1,2,3,4],ndmin= 4)

print(varn)
print(varn.ndim)
print(varn.shape)

#Reshaping

varr = np.array([1,2,3,4,5,6])
print(varr)

varrn = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

x = varr.reshape(3,2)
y = varr.reshape(6,1) #ValueError will be generated if indexing is not possible

print(x)
print(x.ndim)

print(y)
print(y.ndim)

x1 = varrn.reshape(2,3,2)

print(x1)
print(x1.ndim)

one = x1.reshape(-1) #Reducing dimensions
print(one)
"""
"""
#Broadcasting

import numpy as np

var1 = np.array([1,2,3,4])
print(var1.shape)
print(var1)

var2 = np.array([[1],[2],[3]])
print(var2.shape)
print(var2)

print(var1 + var2) #Cannot be done in same shape but different size, but this will generate a 2D array (a,b) + (c,d) = max(a or c), max(b,d)
"""
""""
#Indexing

import numpy as np

var = np.array([[1,2,3],[1,2,3]])

print(var[0,2]) #Prints like [First,Second....last dimension index bracket]

#Slicing {Syntax = Start : Stop : Step} (Stop will do -1)

#1D
var1 = np.array([1,2,3,4,5,6,7,8,9])

print(var1[3:6])
print(var1[3:6:2])
print(var1[2:])
print(var1[:5])
print(var1[::2])

#2D (Same Syntax instead with indexing)

print(var[0,0:3])
print(var[0,0:])
print(var[0,0:2])
print(var[0,0::2])
"""
"""
#Iteration

import numpy as np

var = np.array([1,2,3,4,5,6,7,8,9])

for i in var:
    print(i)

var1 = np.array([[1,2,3,4],[1,2,3,4]])

for j in var1:
    print(j)
    for k in j:
        print(k) #Same with any dimensional array

var2 = np.array([[[1,2,3,4],[1,2,3,4]]])

for i in np.nditer(var2): #Breaks without multiple loops
    print(i)

for i in np.nditer(var2,flags=['buffered'],op_dtypes=["S"]): #Buffered creates extra space S converts string Flag creates conditions and op_details is data types
    print(i)

for i,d in np.ndenumerate(var2): #Will iterate dimensions as well while showing dimension as well as item
    print(i,d)
"""
"""
#Copy and Views (Must see theoritical difference)

import numpy as np

var = np.array([1,2,3,4,5])

cop = var.copy()
#Changing Copy will not affect the original array

var[1] = 4000
cop[3] = 12

print(var)
print(cop)

x = np.array([2,3,4,5,6,7,8])

viw = x.view()
#Changing view will affect original array

x[1] = 4120
viw[3] = 90

print(x)
print(viw)
"""
"""
#Joining

import numpy as np

var = np.array([1,2,3,4,5,6,7])
var1 = np.array([1,2,3,4,5,6,7])

jo = np.concatenate((var,var1))

print(jo)

va = np.array([[1,2,3],[4,5,6]])
va1 = np.array([[1,2,3],[4,5,6]])

joi = np.concatenate((va,va1),axis = 1) #rows axis = 0, columns axis = 1 (out bracket = lower number)
jon = np.concatenate((va,va1),axis=0)

print(joi)
print(jon)


var1 = np.array([1,2,3,4,5,6,7])
var11 = np.array([1,2,3,4,5,6,7])

new = np.stack((var1,var11),axis=0) #Creates new dimensional joint arrays
new1 = np.stack((var1,var11),axis=1)
new2 = np.hstack((var1,var11)) #Row H = horizontal
new3 = np.vstack((var1,var11)) #Column V = vertical
new4 = np.dstack((var1,var11)) #Height

print(new)
print(new1)
print(new2)
print(new3)
print(new4)
"""
"""
#Splitting

import numpy as np

ar = np.array([1,2,3,4,5,6])

new = np.array_split(ar, 1)
new1 = np.array_split(ar, 2)

print(new)
print(new1) #Can do same with multiple dimensions also with axis with shape and dtype outputs
"""
"""
#Functions

import numpy as np

ar = np.array([1,2,3,4,6,9,10,10])

print(np.where(ar == 2)) #Syntax = np.where(condition element) and creates an array of the fulfilled condition elements

print(np.where((ar/2) == 2))

print(np.where((ar/2) == 0))

print(np.where((ar%2) == 0))

print(np.searchsorted(ar,5,side='right')) #Binary search on the array for the index Syntax = (array,element,side=right or left)

print(np.searchsorted(ar,5,side='left'))

print(np.searchsorted(ar, [7,8],side='right')) #Index array is output

ar1 = np.array([1,3,2,45,6]) #Can do it with multi dimensional arrays but the smallest dimension being sorted
print(np.sort(ar1))

alp = np.array(['a','e','d','f'])
print(np.sort(alp))

des = np.sort(ar1)
print(des[::-1]) #Sorting in descending order

f = [True,False,True,True]

new_var = alp[f] #This is filtering with bool functions array
print(new_var)

np.random.shuffle(ar)

print(ar)

x = np.unique(ar, return_index=True,return_counts=True) #Returns unique elements deleting duplicates

print(x)

var2 = np.array([1,2,3,4,5,6,7,8])

y = np.resize(var2,(4,2))

print(y)

#See Flatten and Ravel functions
#Insert and delete work same way like list but see syntax insert = np.insert(array, position, element) positions can be multiple and with multi dimensions but with axis as after 3rd comma
#Delete syntax = np.delete(array, position)
"""
"""
#MATRIX

import numpy as np

var = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
var1 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
var2 = np.matrix([[1,2],[3,4]])

print(var)
print(var + var1)
#Addition and Subtraction work just the same as arrays

print(var*var1) #dot multiplication
#Multiplaction like in maths with minors matrix like multiplying row with column order is (aXb)*(cXd) = aXd

print(var/var1) #Division just like add and sub

print(var.dot(var1))

#Other matrix functions also applicable must check

print(var.transpose())
print(var.T) #transpose function

print(np.swapaxes(var,0,1)) #Swapping, wierd syntax

print(np.linalg.inv(var2)) #Inverse


# Power = np.linalg.Matrix_Power(array,n)
# n = 0 then identity
# n > 0 then simple power
# n < 0 then inverse power

print(np.linalg.matrix_power(var2,2))
print(np.linalg.matrix_power(var2,0))
print(np.linalg.matrix_power(var2,-1))
print(np.linalg.matrix_power(var2,-2))

print(np.linalg.det(var2)) #Determinant function
print(np.linalg.det(var)) #Same as in maths
"""
