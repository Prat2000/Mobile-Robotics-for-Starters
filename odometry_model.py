import math
import matplotlib.pyplot as plt
from sampling import *

def sampling_odometry(x,u,alpha):
    std1 = alpha[0]*abs(u[0]) + alpha[1]*u[2]
    std2 = alpha[2]*u[2] + alpha[3]*(abs(u[0])+abs(u[1]))
    std3 = alpha[0]*abs(u[1]) + alpha[1]*u[2]

    del_rot_1 = u[0] + sampling_norm_dis(0,std1**2,1)[0]
    del_rot_2 = u[1] + sampling_norm_dis(0,std3**2,1)[0]
    del_trans = u[2] + sampling_norm_dis(0,std2**2,1)[0]

    x_ = x[0] + del_trans*math.cos(x[2]+del_rot_1)
    y_ = x[1] + del_trans*math.sin(x[2]+del_rot_1)
    theta_ = x[2] + del_rot_1 + del_rot_2

    return [x_,y_,theta_]

def plot(x,y):    
    plt.figure()
    plt.title('Odometry based Motion Modelling')
    plt.xlabel('x_coordinate')
    plt.ylabel('y_coordinate')
    plt.plot(x1[0],x1[1],'go',markersize=10)
    plt.plot(x,y,'ro',markersize=1)
    plt.savefig("Odometry Motion Modelling")

x1 = [2.0, 4.0, 0.0]
u1 = [(math.pi)/2, 0.0, 1.0]
alpha1 = [0.1, 0.1, 0.01, 0.01]
# pos = sampling_odometry(x1,u1,alpha1)
# print(pos)
samples = 5000
x = []
y = []
for _ in range(samples):
    pos=sampling_odometry(x1,u1,alpha1)
    x.append(pos[0])
    y.append(pos[1])

plot(x,y)




