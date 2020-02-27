import sys
import io
import urllib.request
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url="http://www.encar.com/"

mem=urllib.request.urlopen(url)
# print(type(mem))
# print("geturl : ",mem.geturl())
# print("status : ",mem.status)
# if status==403 :
#     print("5분 후에 다시 접속하세요")
# elif :
# print('headers : ',mem.getheaders())
# print('info : ',mem.info())
# print("getcode : ",mem.getcode())
# print("read : ",mem.read(10))

print(urlparse("http://www.encar.com/").query)
