from numpy import loadtxt,linspace,zeros
from pylab import plot,show,xlabel,ylabel,xlim

print("RUNNING AVERAGE")

xlim(0,1000)
r=5
b=loadtxt("sunspots.txt",float)
s=0
R=zeros([1000],float)

for n in range (5,1001):
	for i in range(-r,r):
		a=(b[i+n,1])
		s=s+a
	w=(s/11)
	R[n-1]=w
print(R)

xlabel("MES")
ylabel("MANCHAS")
plot(b[:,0],b[:,1],"b--")
plot(R)
show()               
