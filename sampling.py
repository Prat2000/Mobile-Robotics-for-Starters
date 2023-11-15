import time
import math
from scipy.stats import norm
import numpy as np
from numpy.random import uniform
import matplotlib.pyplot as plt

def sampling_norm_dis(mean, variance, samples):
    gen = []
    std = math.sqrt(variance)
    time1 = time.time()
    for _ in range(samples):
        sum = 0
        i=0
        while i<12:
            sum += uniform(-std,std)
            i = i+1
        sum = mean + sum/2
        gen.append(sum)
    time2 = time.time()
    # print("Time : {}".format(time2-time1))
    return gen

def max_norm_dis(mean,variance):
    n=100000
    y=[]
    std=math.sqrt(variance)
    for _ in range(n):
        x = mean + uniform(-std,std)
        val = (1/math.sqrt(2*math.pi*variance))*math.exp(-math.pow(x-mean,2)/(2*variance))
        y.append(val)
    return max(y)

def norm_dis(x,mean,variance):
    val = (1/math.sqrt(2*math.pi*variance))*math.exp(-math.pow(x-mean,2)/(2*variance))
    return val


def rejection_norm_dis(mean,variance,samples):
    std=math.sqrt(variance)
    max = max_norm_dis(mean,variance)
    gen=[]
    time1=time.time()
    for _ in range(samples):
        x=mean + uniform(-5*std,5*std)
        val=norm_dis(x,mean,variance)
        y=uniform(0,max)
        if(val>=y):
            gen.append(x)
    time2=time.time()
    # print("Time : {}".format(time2-time1))
    return gen

def box_muller(mean,variance,samples):
    std=math.sqrt(variance)
    gen=[]
    time1=time.time()
    for _ in range(samples):
        u1=uniform(0,1)
        u2=uniform(0,1)
        x=math.cos(2*math.pi*u1)*math.sqrt(-2*math.log(u2))
        x=std*x+mean
        gen.append(x)
    time2=time.time()
    # print("Time : {}".format(time2-time1))
    return gen 

def plot(sample):
    plt.hist(sample,bins=500)
    plt.title("Normal Distribution")
    plt.savefig("Box Muller Method")

# samples = box_muller(5,0.8,1000000)
# plot(samples)



        
