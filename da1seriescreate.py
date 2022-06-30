import pandas as pd
#Create series from values
print('\nCreate series from values')
ser=pd.Series(data=[10,20,30,40],index=['a','b','c','d'])
print(ser)


#Create series from values
print('\nCreate series from values')
ser=pd.Series(data=[1,2,3,4],index=['ab','cd','ef','gh'])
print(ser)



#Create series from list
print('\nCreate series from list')
li=[10,20,30,40]
ser=pd.Series(li,index=['1','2','3','4']) # list with user defined index
print(ser)

print('list with default index')
ser=pd.Series(li) # list with default index
print(ser)


#Create series from tuple
print('\nCreate series from tuple')
tup=(10,20,30,40)
ser=pd.Series(tup,index=['a','b','c','d']) # tuple with user defined index
print(ser)
print('tuple with default index')
ser=pd.Series(tup) # tuple with default index
print(ser)


print('\nCreate series from tuple')
data=(10,20,30,40)
ser=pd.Series(data,index=['a','b','c','d']) # tuple with user defined index
print(ser)

#Create series from np array
print('\nCreate series from np array')
import numpy as np
npa=np.array([10,20,30,40])
ser=pd.Series(npa,index=['a','b','c','d']) # array with user defined index
print(ser)
print('array with default index')
ser=pd.Series(npa) # array with default index
print(ser)

#Create series from Dictionary
print('\nCreate series from Dictionary')
dic={'a':10,'b':20,'c':30,'d':40}
ser=pd.Series(dic)
print(ser)


print('\nCreate series from Dictionary')
dic={1:'a',2:'b',3:'c'}
ser=pd.Series(dic)
print(ser)