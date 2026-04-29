import pandas as pd
fruits={
    'Apple':4.5,
    'Banana':1.05,
    'orange':3.2,
    'kiwi':6.87,
    'cherry':8.34,
    'Avacado':12.3
}
s=pd.Series(fruits,name='Fruits_vitamins')
print(s)
print("labeled indexing\ns")
print(s.loc['kiwi'])
print('position based indezing\n')
print(s.iloc[3])
print(' labeled slicing \n')
print(s['Apple':'kiwi'])
print('positioned slicing\n')
print(s[3:5])
#comditional indexing
print('conditional indexing\n')
print(s[s>2.0])
#modifying a series 
print('Modifying a series\n')
print('1. updating\n')
s['Apple']=9.0
print(s)
s['Grapes']=5.4
print(s)
s=s.drop('kiwi')
print(s)