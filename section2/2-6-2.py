from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

fp=open("D:/atom_py/section2/food-list.html",encoding="utf-8")
soup=BeautifulSoup(fp,"html.parser")

print(soup)

#양주 출력
print("1.",soup.select("li:nth-of-type(4)")[1].string)
print("2.",soup.select_one("#ac-list > li:nth-of-type(4)").string)
print("3.",soup.select("#ac-list > li[data-lo='cn']")[0].string)
print("4.",soup.select("#ac-list > li.alcohol.high")[0].string)
print('========================================================')
# 삼겹살 출력
print("5.",soup.select("li:nth-of-type(3)")[0].string)
print("6.",soup.select_one("#fd-list > li:nth-of-type(3)").string)
print("7.",soup.select("#fd-list > li[data-lo='ko']")[1].string)
print("8.",soup.select("#fd-list > li.food.hot")[1].string)
print("========================================================")
param={"data-lo":"cn","class":"alcohol"}
print("5.",soup.find("li", param).string)
#알콜이면서 cn이다
print("6.",soup.find(id="ac-list").find("li",param).string)

for ac in soup.find_all("li"):
    if ac['data-lo']=='us':
        print('data-lo==us',ac.string)
