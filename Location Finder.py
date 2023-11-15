import math

h=[6,3]
u=[10,8]
t1=[5,7]
t2=[12,4]
v1=1
v2=1.5
d0=3.9
d1=4.5

Zh_exp1=math.sqrt((h[0]-t1[0])**2 + (h[1]-t1[1])**2)
Zh_exp2=math.sqrt((h[0]-t2[0])**2 + (h[1]-t2[1])**2)
Zu_exp1=math.sqrt((u[0]-t1[0])**2 + (u[1]-t1[1])**2)
Zu_exp2=math.sqrt((u[0]-t2[0])**2 + (u[1]-t2[1])**2)

def norm(z,z_exp):
    p = (1/math.sqrt(2*math.pi*v1))*math.exp(-1*(z-z_exp)**2/2*v1)
    return p

P_h = norm(d0,Zh_exp1)*norm(d1,Zh_exp2)
P_u = norm(d0,Zu_exp1)*norm(d1,Zu_exp2)

if P_h > P_u:
    print("She is more likely in her house.")
elif P_h == P_u:
    print("She is equally likely to be in her house or at the university.")
else:
    print("She is more likely at the university.")

