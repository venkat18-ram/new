import pandas as pd
df=pd.DataFrame({
    'Name':['venkat','sadiq','shiva','suhail','vardhan'],
    'Age':[19,20,12,15,20]
})

print(df)
df.sort_values(by="Age",ascending=False,inplace=True)
print(df)
print(df['Age'].mean())
print(df['Age'].sum())
print(df['Age'].std())