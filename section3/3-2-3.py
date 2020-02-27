import requests, json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

s=requests.session()
r=s.get('http://httpbin.org/stream/20')
# print(r.encoding)

if r.encoding is None:
    r.encoding='utf-8'
# print(r.encoding)

for line in r.iter_lines(decode_unicode=True):
    print(line)
    b=json.loads(line)
    # c=b.keys() #키값 확인
    # print(c)
    for e in b.keys():
        print("key: ",e,"values : ",b[e])
