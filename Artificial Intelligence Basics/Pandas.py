#Some basic Pandas Functions and Classes.
"""
#Series
import pandas as pd

#List Series
x = [1,2,3,4,5]

var = pd.Series(x,index=['a','b','c','d','e'],dtype='float',name='Python')

print(var)
print(type(var))
print(var[2])

#Dictionary Series
dic = {"Name":[1,2,3,4],"Pos":[2,3,4,5],"Rope":[3,4,1,2]}

var1 = pd.Series(dic)

print(var1)
print(type(var1))

#Tuples
tup = pd.Series(12,index=[1,2,3,4,12])

print(tup)
print(type(tup))

#Arithmetic Operations
x1 = pd.Series([1,2,3,4,5])
x2 = pd.Series([1,2,3,4,5])

print(x1 - x2) #Can do same with Addition Mul and Div
"""
"""
#Dataframes
import numpy as np
import pandas as pd

dic = {"Name":['a','b','c','d'],"Pos":[2,3,4,5],"Rope":[3,4,1,2]}

df = pd.DataFrame(dic) #Creates a dataframe like excel

print(df)

df.to_csv('ex.csv') #Copying the content to a csv excel file
df.to_csv('ex_noind.csv',index=False) #Without index starting with 0

print(df.head(2)) #Starting elements
print(df.tail(2)) #Ending elements
print(df.describe()) #Describing various status
"""
"""
#Indexing and inserting values
import pandas as pd

exo = pd.read_csv('ex.csv')

print(exo)

print(exo['Pos'])
print(exo['Pos'][2])

exo['Pos'][0] =  50 #Can change value using this

print(exo)

exo.to_csv('ex.csv') #Have to transfer the current value to the specified value

exo.index = ['1','2','3','4a']

exo.to_csv('ex.csv')

print(exo)
"""
"""
#Resetting the values
import pandas as pd

dic = {"Name":['a','b','c','d'],"Pos":[2,3,4,5],"Rope":[3,4,1,2]}

df = pd.DataFrame(dic) #Creates a dataframe like excel

df.index = ['1a','2b','3c','4d']

df.to_csv('ex.csv')

print(df)
"""
"""
#Functions
import numpy as np
import pandas as pd

newdf = pd.DataFrame(np.random.rand(55,5), index=np.arange(55))

print(type(newdf))
print(newdf)
print(newdf.describe())

# newdf[0][0] = "Harry"

print(newdf.dtypes)

print(newdf.to_numpy()) #converts into numpy array

print(newdf.T) #Transposing the DataFrame

print(newdf.sort_index(axis=0, ascending=False)) #Will sort index, axis 0 = column, axis 1 = row, ascending false means descending.

print(type(newdf[0]))


#drop function with axis will remove the particular column or row
#loc function gets the location

newdf.columns = list("ABCDE")
print(newdf)
print(newdf.head(2))
print(newdf.loc[[1,2],['C','D']]) #Row and column syntax, can write : for all possible values in the particular area.
#Can insert conditions in the loc function as required

print(newdf.loc[(newdf['A']<0.3) & (newdf['C']>0.1)])
"""
