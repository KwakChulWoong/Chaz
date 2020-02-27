import sys
import io
import urllib.request as dw
import urllib.parse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

imgUrl="https://ssl.pstatic.net/tveta/libs/1260/1260649/19aabf7c9a09e0d9ed84_20200211140438611.jpg"
mp4="https://tvetamovie.pstatic.net/libs/1260/1260649/24e0cefb7bd741f2d0ec_20200211143216244.mp4-pBASE-v0-f98576-20200211143324330.mp4"

savePath1="D:/atom_py/homework1.jpg"
savePath2="D:/atom_py/homework2.mp4"

f1=dw.urlopen(imgUrl).read()
f2=dw.urlopen(mp4).read()

with open(savePath1, 'wb') as savePath1 : #w : write 저장 r:read 읽기 a:add append개념과 동일
    savePath1.write(f1)
with open(savePath2, 'wb') as savePath2 : #w : write 저장 r:read 읽기 a:add append개념과 동일
    savePath2.write(f2)

print("다운로드 완료!")
