import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
#한글 아톰에서 인코딩

imgUrl="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRShGbPGgqlKFK0DghLfHYEGS_dKrYmKS6Z9cNbRU2dtsu1g2g0"
htmlURL="https://www.google.co.kr/"

savePath1="D:/atom_py/test1.jpg"
savePath2="D:/atom_py/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
