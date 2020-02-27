from bs4 import BeautifulSoup
import requests
import sys
import io
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# 요청
URL='https://www.wishket.com/accounts/login/'

with requests.Session() as s :
    # URL 요청
    s.get(URL)
    ua=UserAgent()

    # print(ua.chrome)
    # print(ua.ie)
    # print(ua.random)
    # print(ua.firefox)

    # Login 정보를 담은 Payload
    LOGIN_INFO={
        'identification':'socratechnic',
        'password':'cjfdndqjvm0401-',
        'csrfmiddlewaretoken':s.cookies['csrftoken']
    }
    # print('token',s.cookies['csrftoken'])
    # print('headers',s.headers)

    # 요청
    response=s.post(URL,data=LOGIN_INFO,headers={'User-Agent':str(ua.chrome),'Referer':'https://www.wishket.com/accounts/login/'})

    # BeautifulSoup 선언
    soup=BeautifulSoup(response.text,"html.parser")
    # print(article.text)
    # article=soup.select('#wrap > div.page > div.sidebar > div > div.partners-history')

    if response.status_code == 200 and response.ok :
        soup=BeautifulSoup(response.text,'html.parser')
        project=soup.select('#wrap > div.page > div.sidebar > div > div.partners-history > div > table > tbody > tr')
        print(project)
        for i in project :
            print(i.text)
