from pandas import Series

# Series 선언
series1=Series([92600,92400,92100,94300,92300])

# 출력
print(series1)

# 총 개수
print('count',series1.count())

# 요약
series1.describe()
