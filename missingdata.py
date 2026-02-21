import pandas as pd
data={
    'Name':['venkat','sadiq','shiva',None,'vardhan'],
    'Age':[19,20,12,None,20],
    'marks':[90,43,78,None,87]
}
df=pd.DataFrame(data)
print(df)
# finding missing value
print(df.isnull())
#finding no of missing values in data
print(df.isnull().sum())
#droping entire row where missing value occurs
# print(df.dropna()) 
#filling with default value inplace of missing value 
# print(df.fillna(0))
#filling with specified valu in place of missing value  
# print(df['Age'].fillna(df['Age'].mean(),inplace=True))
# print(df['marks'].fillna(df['marks'].mean(),inplace=True))
# print(df)
#interpolate()
print(df['Age'].interpolate(method='linear'))
print(df['marks'].interpolate(method='linear'))
print(df)