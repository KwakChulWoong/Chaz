from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url="https://finance.naver.com/sise/"
res=req.urlopen(url).read().decode('cp949') #한글 깨짐 방지
soup=BeautifulSoup(res,"html.parser")

top=soup.select("#popularItemList > li")
# print(top)

print('네이버 주식 인기검색 종목 10위')
for i,e in enumerate(top, 1):
    print("순위 :",i,","" 이름 :",e.select_one("a").string)
