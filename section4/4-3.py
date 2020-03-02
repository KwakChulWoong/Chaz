import sys
import io
import os.path
import urllib.request as req
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url="http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1135059500"
savename="D:/atom_py/section4/forecast2.xml"
if not os.path.exists(savename) :
    req.urlretrieve(url,savename)

# BeautifulSoup로 분석
xml=open(savename,'r',encoding='utf-8').read()
soup=BeautifulSoup(xml,"html.parser")
# print(soup)
info={} # {"서울":2,7,20}
for location in soup.find_all("data") :
    loc=location.find("hour").string
    print(loc)
    weather=location.select_one("temp").string
    print(weather)
    # if not (loc in info):
    #     info[loc]=[] #keys (서울)
    # for temp in weather :
    #     info[loc].append(temp.string) #values
# print(info)
# print(list(info.keys()))
# print(info.values())
with open('D:/atom_py/section4/cast2.txt',"wt",encoding="utf-8") as f:
    for loc in sorted(info.keys()) :
        print("시간 : ",loc) #console
        f.write(str(loc)+'\n') #file
        for num in info[loc] :
            print("기온 : ",num)
            f.write('\t'+str(num)+'\n')
