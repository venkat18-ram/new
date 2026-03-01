import pandas as pd
df=pd.DataFrame({
    'Name':['venkat','sadiq','shiva','suhail','vardhan'],
    'Age':[19,20,12,15,20],
    'marks':[90,43,78,57,87]
})
print(df)
print(df.groupby('Age')['marks'].mean())
print(df.groupby('Age')['Name'].count())
print(df.groupby(['Age','marks'])['Name'].count())