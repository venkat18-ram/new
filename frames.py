import pandas as pd
data={
    'Name':['venkat','sadiq','shiva','suhail','vardhan'],
    'Age':[19,20,12,15,20],
    'marks':[90,43,78,57,87]
}
df=pd.DataFrame(data)
print(df)
print('shape of data frame')
print(df.shape)
print('columns')
print(df.columns)
print('data types')
print(df.dtypes)
print('first row')
print(df.iloc[0])
print('2 to 5 rows')
print(df.iloc[1:5])
print('name column')
print(df['Name'])
print('Name and marks')
print(df[['Name','marks']])
df['Grade']=['pass' if marks>45 else 'fail' for marks in df['marks']]
print(df)
df.drop('Grade', axis=1, inplace=True)
print(df)
print('students of age > 18')
print( df[df['Age']>18])
print('students between marks 60 and 90')
print(df[df['marks'].between(60,90)])
print('student name starts with s')
print(df[df['Name'].str.startswith('s')])