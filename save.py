import pandas as pd
data={
    'Name':['venkat','sadiq','suhail','jahash','shiva','Vardhan','khaiser'],
    'age':[20,20,20,20,20,20,20],
    'collage':['KVSRIT','ST.Joseph','KVSRIT','KVSRIT','KVSRIT','KVSRIT','KVSRIT'],
    'phone Number':[6304256292,9494141891,6304667801,8639917686,6305153274,8074764478,8919821748]
}
df=pd.DataFrame(data)
print(df)
df.to_csv('CSE-C details.csv',index=False)
