import requests, json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# Response 상태코드 첨부
s=requests.session()
r=s.get('http://httpbin.org/get')
print(r.status_code)
print(r.ok)
# if ok==True :
#     if status_code==200 :

r=s.get("https://jsonplaceholder.typicode.com/posts/1")
print(r.text)
print(r.json().keys())
print(r.encoding)
print(r.content)
print(r.row)
