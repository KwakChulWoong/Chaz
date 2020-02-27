import sys
import io
import urllib.request
import urllib.parse


sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

API="https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

values={'ctxCd' : '1001'}

print('before',values)
params=urllib.parse.urlencode(values)

print('after',params)

#요청 url 생성
url=API+"?"+params
print("요청 url = ",url)

#읽기
data=urllib.request.urlopen(url).read()
text=data.decode('utf-8')
print(text)
