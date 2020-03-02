import pickle

# 파일 이름 데이터
bfilename = 'D:/atom_py/section4/test.bin'
tfilename = 'D:/atom_py/section4/test.txt'

data1 = 77
data2 = "Hello"
data3 = ['car', 'animal', 'house']

# 바이너리 쓰기 (객체 직렬화)
with open(bfilename, "wb") as f:
    pickle.dump(data1, f) #dumps(문자열) => loads / dump => load
    pickle.dump(data2, f)
    pickle.dump(data3, f)
    print('')

# 텍스트 쓰기
with open(tfilename, "wt") as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))
# 문서가 깨져서 읽어지면 위에 두 작업 바이너리 쓰기(객체 직렬화) 텍스트 쓰기 작업을 해야한다


# 바이너리로 읽기(역직렬화)
with open(bfilename, 'rb') as f:
    b=pickle.load(f)
    print(type(b),'Binary Read1 | ',b)
    b=pickle.load(f)
    print(type(b),'Binary Read2 | ',b)
    b=pickle.load(f)
    print(type(b),'Binary Read3 | ',b)

# 텍스트 읽기
with open(tfilename,"rt") as f:
    for i,line in enumerate(f,1):
        print(type(line),'Text Read'+str(i)+'|',line,end='')
