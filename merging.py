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
#inner merge
print('inner merge')
print(pd.merge(df1,df2,on='customer_id',how='inner'))
#outer merge
print('outer merge ')
print(pd.merge(df1,df2,on='customer_id',how='outer'))
# left merge
print('left merge')
print(pd.merge(df1,df2,on='customer_id',how='left'))
#right merge
print('right merge')
print(pd.merge(df1,df2,on='customer_id',how='right'))
