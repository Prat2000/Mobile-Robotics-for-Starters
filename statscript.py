from scipy.stats import norm,uniform
import numpy as np
import matplotlib.pyplot as plt 

v1=norm.rvs(loc=5.0, scale=2.0, size=100000, random_state=0)
v2=uniform.rvs(loc=0,scale=10,size=100000,random_state=0)
mean1=np.mean(v1)
std1=np.std(v1)
mean2=np.mean(v2)
std2=np.std(v2)
print(f'Normal Distribution: Mean {mean1} Standard Deviation {std1}')
print(f'Uniform Distribution: Mean {mean2} Standard Deviation {std2}')
plt.hist(v1)
plt.savefig("Normal distribution")
plt.hist(v2)
plt.savefig("Uniform distribution")