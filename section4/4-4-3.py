import urllib.request as req
import os.path, random
import simplejson as json

#url
url="https://api.github.com/repositories"

# 경로 & 파일명
savename='D:/atom_py/section4/member.json'

if not os.path.exists(url) :
    req.urlretrieve(url,savename)

items=json.loads(open(savename, "r", encoding="utf-8").read())

for item in items :
    print(item["full_name"]+" - "+item["owner"]["url"])
