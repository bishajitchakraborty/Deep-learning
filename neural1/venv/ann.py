import numpy as np
x1=[0,0,1,1]
x2=[0,1,0,1]
yd=[0,1,1,1]
e=[0,0,0,0]

w1=0.4
w2=0.1
th=0.2
lr=0.1

def step(x):
    if x<=0