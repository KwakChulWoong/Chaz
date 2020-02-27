from bs4 import BeautifulSoup
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

html="""
<html><body>
    <ul>
        <li id="naver"><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a><//li>
        <li><a href="http://www.daum.com">daum</a><//li>
        <li><a href="http://www.google.com">daum</a><//li>
        <li><a href="http://www.tistory.com">daum</a><//li>
    </ul>
</body></html>
"""
soup=BeautifulSoup(html,"html.parser")
naver=soup.find(id="naver").string #select_one과 동일하게 바로 string처리 가능
print('naver : ', naver)

li=soup.find_all(href=re.compile(r"^https://"))
print e ('li : ',li)
for e in li:
    print(e.attrs['href'])
li2=soup.kind_all(hf=re.compile(r"da"))
print e ('li : ',li')

for e in li:
    print(e.attrs['href'])
