import pandas as pd
import matplotlib.pyplot as plt
data={
    'reg id':['24FH1A05F5','24FH1A05H3','24FH1A05I8','24FH1A05J6','24FH1A05H8','24FH1A05G8','24FH1A05J6','24FH1A05G1','24FH1A05F7','24FH1A05F3','24FH1A05H0','24FH1A05I9','24FH1A05F4','24FH1A05F6'],
    'Name':['venkat','suhail','jahash','shiva','bansi','Vardhan','khaiser','mahesh','sethu sai','sai teja','affan','junaid','govardhan','kishore'],
    'age':[20,20,31,9,19,18,15,10,21,12,20,30,20,19],
}
df=pd.DataFrame(data)
print(df)
plt.bar(df['Name'],df['age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age Distribution')
plt.xticks(rotation=45)
plt.savefig('C:/Users/LENOVO/Desktop/folder/trails/new/age_distribution.png')
plt.show()
df.to_csv('new/CSE-C details.csv',index=False)
# df.to_json('new/CSE-Cdetails.json',index=True)
# df.to_excel('new/CSE-Cdetails.xlsx',index=False)
