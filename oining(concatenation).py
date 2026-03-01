import pandas as pd
df1=pd.DataFrame({
    'customer_id':[1,2,3],
    'customer_name':['venkat','sadiq','shiva']
})
df2=pd.DataFrame({
    'customer_id':[2,3,4],
    'purchase_amount':[2000,1500,3000]
})
print(df1)
print(df2)
#vertical concat
print('vertical concatenation')
print(pd.concat([df1,df2],axis=0,ignore_index=True))
#horizontal concat
print('horizontal concatenation')
print(pd.concat([df1,df2],axis=1,ignore_index=True))