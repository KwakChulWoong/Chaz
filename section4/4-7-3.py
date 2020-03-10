import datetime
import FinanceDataReader as fdr
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# 조회 시작 날짜
start=datetime.datetime(2020,1,1)

# 조회 마감 날짜
end=datetime.datetime(2020,3,4)

# 한국거래소 상장종목 전체
# df_krx=fdr.StockListing('KRX')

# 리스트 10개 출력
# print(df_krx.head(10))

# 출력
# print(df_krx.index)
# print(df_krx['Symbol'])
# print(df_krx.describe())
# print(df_krx.iloc[0])

# 미국 apple 금융 정보 호출
# df_app=fdr.DataReader('AAPL',start,end)
# print(df_app.head(10))
# print(df_app.loc['2020-02-19'])
# print(df_app.describe())

df_ama=fdr.DataReader('AMZN',start,end)
print(df_ama.head(5))
print(df_ama.loc['2020-01-10'])
print(df_ama.describe())

print('=================================================================================================================================')

df_goo=fdr.DataReader('GOOGL',start,end)
print(df_goo.head(5))
print(df_goo.loc['2020-01-10'])
print(df_goo.describe())
