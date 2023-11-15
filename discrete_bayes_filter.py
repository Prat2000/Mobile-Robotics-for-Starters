import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from celluloid import Camera

'''
action space:
move forward = 1
move backward = 0
'''
bel = np.hstack((np.zeros(9),1,np.zeros(10)))
world = np.arange(20)
action = np.hstack((np.ones(9),np.zeros(3)))

# Algorithm for discrete bayes filter:

def discrete_bayes_filter(bel,u):
    bel_p = np.zeros(20)
    if u==1:
        for x in range(20):
            if x==0:
                bel_p[x] = 0.25*bel[x]
            elif x==1:
                bel_p[x] = 0.25*bel[x] + 0.5*bel[x-1]
            elif x==19:
                bel_p[x] = 1*bel[x] + 0.75*bel[x-1]
            else:
                bel_p[x] = 0.25*bel[x] + 0.5*bel[x-1] + 0.25*bel[x-2]
    elif u==0:
        for x in range(20):
            if x==19:
                bel_p[x] = 0.25*bel[x]
            elif x==18:
                bel_p[x] = 0.25*bel[x] + 0.5*bel[x+1]
            elif x==0:
                bel_p[x] = 1*bel[x]+0.75*bel[x+1]
            else:
                bel_p[x] = 0.25*bel[x] + 0.5*bel[x+1] + 0.25*bel[x+2]            
    return bel_p

def plot_belief(belief):
    fig = plt.figure()
    camera = Camera(fig)
    t = plt.bar(world,belief)
    plt.legend(t, [f'action -'])
    bel_p = belief
    for u in action:
        bel_p = discrete_bayes_filter(bel_p,u)
        t = plt.bar(world,bel_p)
        plt.legend(t, [f'action {u}'])
        camera.snap()
    animation = camera.animate()
    animation.save('discrete_bayes_algo.gif')

plot_belief(bel)

        


