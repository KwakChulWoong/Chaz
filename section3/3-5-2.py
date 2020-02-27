import sys
import io
import json
import urllib.request as req
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url="https://finance.daum.net/api/search/ranks?limit=10"

# URL 요청
ua=UserAgent()

# header 선언
headers={
    'User-Agent':str(ua.chrome),
    'Referer':'https://finance.daum.net/'
}

# 다음 주식 요청 URL
url="https://finance.daum.net/api/search/ranks?limit=10"

# 요청
res=req.urlopen(req.Request(url,headers=headers)).read().decode('utf-8')

# 응답 데이터 확인(Json Data)
print('res',res)

# 응답 데이터 str => json 변환 및 data 값 저장
rank_json=json.loads(res)['data']

# 중간 확인
print('중간 확인 : ', rank_json, '\n')
for elm in rank_json :
    #print(type(elm)) Type 확인
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'],\
    elm['tradePrice'], elm['name']), )
