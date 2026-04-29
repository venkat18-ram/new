import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)
print(df)
# Access Bob's age
bob_age = df.loc[1, 'Age']
print(bob_age)
# Access the value in the first row, second column
val = df.iloc[0, 1]
print(val)
# Drop the 'City' column
df_new = df.drop('City', axis=1)
print(df_new)
# Drop the first row
df_new = df.drop(0, axis=0)
print(df_new)
# Sort by Age descending
df_sorted = df.sort_values(by='Age', ascending=False)
print(df_sorted)
# Sort by Age descending
df.reset_index(drop=True)
# print(df_sorted)