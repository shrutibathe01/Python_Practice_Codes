import pandas as pd
df=pd.DataFrame({'region':['east','west','north','south','center','north','east','south','center','west'],
                'manager':['jaydeep','rahesh','riya','yogita','jaydeep','ray','manoj','ray','jaydeep','riya'],
                'saleman':['ramu','raju','jiya','ram','dipti','mohan','mohini','ramu','jiya','raju'],
                'items':['tv','refrigrator','meachine','laptop','tab','phone','oven','table','iphones','phone'],
                'no_item':[2,3,1,4,5,2,1,3,1,4],
                'price':[30000,55000,60000,70000,30000,20000,65000,15000,120000,10000],
                'totalsaleamount':[60000,160000,60000,280000,150000,40000,65000,45000,120000,40000]})
print(df)
print("\n")
df1=pd.pivot_table(df,values='totalsaleamount',index=[],columns=['region','manager','saleman'])
print(df1)

