import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

imgUrl="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRShGbPGgqlKFK0DghLfHYEGS_dKrYmKS6Z9cNbRU2dtsu1g2g0"
htmlURL="https://www.google.com/"

savePath1="D:/atom_py/test1.jpg"
savePath2="D:/atom_py/index.html"

# f=dw.urlopen(imgUrl).read()
f2=dw.urlopen(htmlURL).read()

# saveFile1=open(savePath1, 'wb')
# saveFile1.write(f)
# saveFile1.close()
with open(savePath2, 'wb') as savePath2 :
    savePath2.write(f2)

print("다운로드 완료!")
