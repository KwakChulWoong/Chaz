import datetime
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

#matplotlib_converters : 날짜(시간) 관련 warning 제거
register_matplotlib_converters()

# 조회 시작 날짜
start=datetime.datetime(2020,1,1)
# 조휘 마감 날짜
end=datetime.datetime(2020,3,9)

# 네이버 주식 정보
df_naver=fdr.DataReader('035420',start,end)

# 다음 주식 정보
df_kakao=fdr.DataReader('035720',start,end)

# 중간 출력
# print(df_kakao)
# print(df_naver)

# 윈도우 제목
fig=plt.figure('Chart Test')
# 차트 사이즈 설정
fig.set_size_inches(10,6,forward=True)
# 차트 설정1
plt.plot(df_naver.index,df_naver['Close'],'r',label="Naver")
# 차트 설정2
plt.plot(df_kakao.index,df_kakao['Close'],'b',label="Kakao")
# 범례
plt.legend(loc='upper left')
# 차트 제목
plt.title('Naver & Kakao')
# x축 레이블
plt.xlabel('Date')
# y축 레이블
plt.ylabel('Close')
# 차트 실행
plt.show()
