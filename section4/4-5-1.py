import pandas as pd
import csv

# 기본 읽기
# df=pd.read_csv('D:/atom_py/section4/csv_s1.csv')
# print(df)

df2=pd.read_csv('D:/atom_py/section4/csv_s2.csv',sep=';',skiprows=[0],header=None,names=["First name","Test1","Test2","Test3","Final","Grade"]) #skiprows 원래는 줄을 생략하고 읽겠다
# print(df)

# 원본 columns 변경
# print(df2['Grade'])
df2['Grade']=df2['Grade'].str.replace('"','')
# print(df2)

# 평균 컬럼 추가
df2['AVG']=df2[['Test1','Test2','Test3']].mean(axis=1)
# print(df2)

# 합계 컬럼 추가
df2['SUM']=df2[['Test1','Test2','Test3']].sum(axis=1)
print(df2)
