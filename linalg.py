import math
import numpy as np
import matplotlib.pyplot as plt  
scan=np.loadtxt('laserscan.dat.txt')
angle=np.linspace(-math.pi/2,math.pi/2,np.shape(scan)[0],endpoint='true')
x_cor=scan*np.cos(angle)
y_cor=scan*np.sin(angle)
plt.plot(x_cor,y_cor,'bo',markersize=2)
plt.title('Laser points wrt laser finder')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('laser_point_wrt_laser_finder.png')

#plot robot,sensor,laser scan in global coordinates
pi=math.pi
T_rg=[[math.cos(pi/4),-math.sin(pi/4),1],[math.sin(pi/4),math.cos(pi/4),0.5],[0,0,1]]
T_sr=[[math.cos(pi),-math.sin(pi),0.2],[math.sin(pi),math.cos(pi),0],[0,0,1]]
T_sg=np.dot(T_rg,T_sr)
R_cor=[1,0.5]
S_cor=[T_sg[0][2],T_sg[1][2]]
plt.plot(R_cor[0],R_cor[1],'go',markersize=10)
plt.plot(S_cor[0],S_cor[1],'ro',markersize=8)
T_ls=[]
T_lg=[]
L_cor=[]
for i in range(np.shape(scan)[0]):
    T_ls.append([[math.cos(angle[i]),-math.sin(angle[i]),x_cor[i]],[math.sin(angle[i]),math.cos(angle[i]),y_cor[i]],[0,0,1]])
    T_lg.append(np.dot(T_sg,T_ls[i]))
    L_cor.append([T_lg[i][0][2],T_lg[i][1][2]])
    plt.plot(L_cor[i][0],L_cor[i][1],'bo',markersize=2)
plt.savefig("World coordinates.png")

