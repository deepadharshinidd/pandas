import pandas as pd
#Create Dataframe from values
print('\nCreate Dataframe from values')
df=pd.DataFrame([['deepa',10],['dharshini',20],['kala', 40]],columns=['name','age'],index=['I','II','III'])
print(df)    

#Create Dataframe from Lists
print('\nCreate Dataframe from Lists')
li1=[1,2]
li2=[3,4]
li3=[5,6]
df=pd.DataFrame([li1,li2,li3],columns=['id','val'],index=['I','II','III'])
print(df)  

print('\nCreate Dataframe from Lists')
li1=[1,'ruby']
li2=[3,'maala']
li3=[5,'kala']
df=pd.DataFrame([li1,li2,li3],columns=['id','name'],index=['I','II','III'])
print(df)  


#Create Dataframe from Tuple
print('\nCreate Dataframe from Tuple') 
tp1=(1,2)
tp2=(3,4)
tp3=(5,6)
pd.DataFrame([tp1,tp2,tp3],columns=['id','val'],index=['I','II','III'])
print(df) 

#Create Dataframe from Tuple
print('\nCreate Dataframe from Tuple') 
tp1=(1,'rice')
tp2=(2,'wheat')
tp3=(3,'pizaa')
pd.DataFrame([tp1,tp2,tp3],columns=['id','menu'],index=['I','II','III'])
print(df) 

#Create Dataframe from np.array
import numpy as np
print('Create Dataframe from np.array')
ar1=np.array([1,2])
ar2=np.array([3,4])
ar3=np.array([5,6])
pd.DataFrame([ar1,ar2,ar3],columns=['id','val'],index=['I','II','III'])
print(df) 


#Create Dataframe from np.array
import numpy as np
print('Create Dataframe from np.array')
ar1=np.array([10,'meal'])
ar2=np.array([30,'briyani'])
ar3=np.array([50,'f.rice'])
pd.DataFrame([ar1,ar2,ar3],columns=['id','val'],index=['I','II','III'])
print(df) 



#Create Dataframe from dictionary
print('\nCreate Dataframe from dictionary') 
dic={'id':[1,2,3],'name':['kumar','selva','raj']}
df=pd.DataFrame(dic)
print(df) 


dic={'id':[10,20,30],'name':['Chennai','Bangalore','kerala']}
df=pd.DataFrame(dic)
df
