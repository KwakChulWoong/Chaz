import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randint(500,1000,size=(100,4)),columns=[2015,2016,2017,2018])
print(df)

# csv index,header(True,False)
# excel index(None),header(True,False)
data=df.to_excel('D:/atom_py/section4/excel_s2.xlsx',index=None,header=True)
print(data)
