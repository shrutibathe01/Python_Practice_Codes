import pandas as pd  
  
data = [{'x': 2, 'z':3}, {'x': 10, 'y': 20, 'z': 30}]  
  
dframe = pd.DataFrame(data, index =['first', 'second'])  
  
print(dframe)  