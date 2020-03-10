import pandas as pd
import numpy as np # 과학 계산용 깊은 숫자를 분석할 때

# 랜덤으로 DataFrame 생성(100행 4열)
df=pd.DataFrame(np.random.randint(0,100,size=(100,4)),columns=list('ABCD')) #리스트로 선언하면 []로 하지 않아도 됨
df=pd.DataFrame(np.random.randint(0,100,size=(100,4)),columns=['ONE','TWO','THREE','FOUR'])
print(df)
