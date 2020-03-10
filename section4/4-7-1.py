from pandas import Series

# Series 선언
series1=Series([92600,92400,92100,94300,92300])

# 출력
print(series1)

# 총 개수
print('count',series1.count())

# 요약
print(series1.describe())

# 인스턴스 접근
print(series1[0])

# series2 선언
series2=Series([92600,92400,92100,94300,92300],index=['2018-02-19','2019-11-26','2020-06-08','2018-03-19','2018-04-19'])
print(series2)
