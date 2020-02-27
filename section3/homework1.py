from bs4 import BeautifulSoup
import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

with requests.session() as s :
    login_req=s.post('https://movie.naver.com/movie/bi/mi/point.nhn?code=161967')
    # print('login_header : ',login_req.headers)

    # Response 정상 확인
    if login_req.status_code==200 and login_req.ok :
        # print("로그인 성공!")

        # 권한이 필요한 게시글 가져오기
        post_one=s.get('https://movie.naver.com/movie/bi/mi/point.nhn?code=161967')
        # print(post_one)

        # 예외처리
        # post_one.raise_for_status()
        # print(post_one.text)

        # BeautifulSoup 선언
        soup=BeautifulSoup(post_one.text,"html.parser")
        # print(soup.prettify())
        article=soup.select('.score_reple>p')
        # print(article)
        for i,a in enumerate(article,1) :
            print('{}번째 평론 : {}'.format(i,a.text))
