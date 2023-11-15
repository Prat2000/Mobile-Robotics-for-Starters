import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-2*np.pi,2*np.pi,0.1)
f=np.cos(x)*np.sin(x)
plt.plot(x,f)
plt.xlabel("x")
plt.ylabel("f(x)=cos(x)*sin(x)")
plt.savefig("plot1.png")


