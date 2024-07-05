import pandas as pd
data=pd.Series(['empid','empname','empsalary','empdesignation'])
df=pd.Series([1,'Jay',55000,'Pune'],index=data)   
print("Dataframe before append:\n",df)
df2=df.append(pd.Series([2,'Geeta',20000,'Mumbai'],index=data) )
print()
print("DataFrame Affter Append: \n",df2)

