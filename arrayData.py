import pandas as pd
df=pd.DataFrame(range(5,4),index='ABCD'.split(),columns='wxyz'.split())
df1=df.assign(rstu=55)                             
print(df1)
