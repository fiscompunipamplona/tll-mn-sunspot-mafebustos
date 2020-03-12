from numpy import loadtxt,linspace
from pylab import plot,show,xlabel,ylabel

print("MANCHAS SOLARES DESDE 1749")

x=linspace(0,1000,1)
		
b=loadtxt("sunspots.txt",float)
xlabel("MES")
ylabel("MANCHAS")
plot(b[:,0],b[:,1],"b--")
show()

