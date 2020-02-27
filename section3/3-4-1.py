from bs4 import BeautifulSoup
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# Session 생성, with구문 안에서 유지
with requests.session() as s:
    # 게시글 가져오기
    url=('https://bbs.ruliweb.com/news/board/11/read/1813?')
    post_one=s.get(url)

    # 예외 발생
    post_one.raise_for_status()

    # 예외 발생 print
    print(post_one.text)

    # BeautifulSoup 선언 및 확인
    soup=BeautifulSoup(post_one.text,"html.parser")

    # 문서만 추출 및 확인(select)
    # print(soup.text)
    top=soup.select("div.view_content > div > p")
    print(top)
    # string처리(for)
    for i in top :
        if i.string is not None and i.img==None:
            print(i.string)
