import requests, json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# r=requests.get('https://api.github.com/event')
# r.raise_for_status() #raise : 에러 시 장애발생코드 출력(확인용)
# print(r.text)

# jar=requests.cookies.RequestsCookieJar()
# jar.set('name','kim',domain='httpbin.org',path='/cookies')
# jar.set('name','kim')

# r=requests.get('https://httpbin.org/cookies',cookies=jar)
# r.raise_for_status()
# print(r.text)

# r=requests.get('https://github.com',timeout=3)
# print(r.text)

# Fake Rest : test에 성공하면 메시지로 변환(실제로 처리되지 않음)
# r=requests.post('https://httpbin.org/post',data={'name':'kim'},\
#                 cookies=jar)
# print(r.text)

# payload1={'key1':'name1','key2':'name2'} #dict(보편적 이거 씀)
# payload2=(('key1','name1'),('key2','name2')) #tuple(보안우수 > 증권에서  씀)
# r=requests.post('https://httpbin.org/post',data=payload2)
# print(r.text)

payload3={'some':'nice'}
r=requests.post('https://httpbin.org/post',data=json.dumps(payload3))
print(r.text)
