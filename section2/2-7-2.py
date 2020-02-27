from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url="https://finance.naver.com/sise/"
res=req.urlopen(url).read().decode('cp949')
soup=BeautifulSoup(res,"html.parser")

# print(soup)
# print('soup',soup.prettify())

top=soup.select("#siselist_tab_0>tr")

# for e in top:
#     print(e)

# for e in top:
#     if e.find("a") is not None:#
#         print(e.select_one(".tltle").string)
#         i+=1

print('Top10 종목명 출력')
a=0
for i,e in enumerate(top, 1):
    if e.find("a")!=None:
        print(i-a,".", e.select_one(".tltle").string)
    else:
        print("*")
        a= a+1

# print('Top10 현재가 출력')
# i=1
# for e in top:
#     if e.find("a") is not None:
#         print(i,e.select_one(".tltle").string,"=",\
#                 e.select_one("td:nth-of-type(5)").string)
#         i+=1
