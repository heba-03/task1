import pandas as pd  # type: ignore


df= pd.read_excel("E.xlsx")


df.drop_duplicates(inplace=True)
#print(df.isnull().sum()) -> only exit date
#print(df.describe()) -> no outliers 

#df.info()



df.loc[0, 'Full Name'] = "Robert Butler"
df.loc[1, 'Department'] = "Marketing"
df.loc[2, 'Bonus %'] = 20
df.loc[3, 'Age'] = 20
df.loc[4, 'Ethnicity'] = "Latino"

print("Maximum Salary: ")
max=df.idxmax()
print(df.loc[max["Annual Salary"]])

df.to_excel('EmployeeSample.xlsx', index=False)
