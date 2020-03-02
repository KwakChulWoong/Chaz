import simplejson as json
import pickle

#Dict (json) 선언
data={} # Dict{[],[],[],[]}
data['people']=[] #array
data['people'].append(
    {'name':'kim',
     'website':'naver.com',
     'from':'Seoul',
     'grade':[20,60,80]}
    )
data['people'].append(
    {'name':'Park',
     'website':'daum.net',
     'from':'Busan',
     'grade':[10,50,90]}
    )
data['people'].append(
    {'name':'Ju',
     'website':'nate.com',
     'from':'Incheon',
     'grade':[70,80,90]}
    )

# Dict -> Str(json) 직렬화
e=json.dumps(data, indent=4)
print(type(e))
print(e)

# Str -> Dict(json) 역직렬화
d=json.loads(e)
print(type(d))
print(d)

# 직렬화
with open('D:/atom_py/section4/member.json', 'w') as outfile:
    json.dump(data, outfile)

# 역직렬화
with open('D:/atom_py/section4/member.json', 'r') as infile:
    r=json.load(infile)

    for p in r['people'] :
        print('Name :'+p['name'])
        print('Website :'+p['website'])
        print('From :'+p['from'])

        t=p['grade']
        grade =''
        for g in t :
            grade = grade + ' ' + str(g)
        print('Grade :', grade.lstrip())
        print('')
