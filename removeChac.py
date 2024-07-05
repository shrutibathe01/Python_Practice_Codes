import pandas as pd
data={'name':['riya','priya','sonal','tiya'],'age':[20,18,17,23]}
df=pd.DataFrame(data)
df1=df['name'].str.replace('sonal'," ")
df2=df['age'].replace(17,  0)
print(df,"\n")
print(df1)
print(df2)
