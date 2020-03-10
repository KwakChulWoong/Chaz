import matplotlib.pyplot as plt

# figure 객체 생성
fig=plt.figure()

# 서브 슬롯 생성(2행 1열)
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)

x=[0,256]
# x축
y=[v*v for v in x]

# y축2 v*v*2
z=[v*v*2 for v in x]

# 멀티 라인(1행 1열)
ax1.plot(x,y,'b',z,'r--')

# 멀티 라인(2행 2열)
ax2.bar(x,y)

# 출력
plt.show()
