import simplejson as json

# Dictionary (json) 선언
data={} #Dictionary방 {[],[],[]}
data['people']=[] #array
data['people'].append(
    {'name':'kim',
    'website':'naver.com',
    'from':'Seoul'
    }
)
data['people'].append(
    {'name':'Park',
    'website':'google.com',
    'from':'Busan'
    }
)
data['people'].append(
    {'name':'Lee',
    'website':'daum.net',
    'from':'Incheon'
    }
)
# print(type(data))
# print(data) #Dictionary 상태

#직렬화 (Dictionary(json) > Str)
e=json.dumps(data,indent=4)
# print(type(e))
# print(e)

#역 직렬화 (Str > Dictionary(json))
d=json.loads(e)
# print(type(d))
# print(d)

with open('D:/atom_py/section4/member.json','w') as outfile :
    outfile.write(e)

with open('D:/atom_py/section4/member.json','r') as readfile :
    r=json.loads(readfile.read())
    print(type(r))
    print(r)

for p in r['people'] :
    print('Name / ' + p['name'])
    print('Website / ' + p['website'])
    print('From / ' + p['from'])
    print('')
