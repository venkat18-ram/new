import pandas as pd
data={
    'reg id':['24FH1A05F5','24FH1A05H3','24FH1A05I8','24FH1A05J6','24FH1A05H8','24FH1A05G8','24FH1A05J6','24FH1A05G1','24FH1A05F7','24FH1A05F3','24FH1A05H0','24FH1A05I9','24FH1A05F4','24FH1A05F6'],
    'Name':['venkat','suhail','jahash','shiva','bansi','Vardhan','khaiser','mahesh','sethu sai','sai teja','affan','junaid','govardhan','kishore'],
    'age':[20,20,20,20,20,20,20,20,20,20,20,20,20,20],
}
df=pd.DataFrame(data)
print(df)
df.to_csv('new/CSE-C details.csv',index=False)
# df.to_json('new/CSE-Cdetails.json',index=True)
# df.to_excel('new/CSE-Cdetails.xlsx',index=False)
