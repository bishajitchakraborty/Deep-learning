

          #ARTIFICIAL NEURAL NETWORK(ANN)
          #A SINGLE LAYER PERCEPTRON

import numpy as np
x1=[0,0,1,1]   #input 1
x2=[0,1,0,1]   #input 2
yd=[0,1,1,1]   #desired output
e=[0,0,0,0]    #total error

w1=0.4      #weight 1
w2=0.1      #weight 2
th=0.2      #threshold
lr=0.1      #learning rate
#yp=calculated output
def step(x):  #x=yp
  if x<=0:
    return 0
  else :
      return 1


def checkForError(values):
  for element in values:
    if element is not 0:
      return False
  return True

def NN(x1,w1,x2,w2,th):
  return step(x1*w1+x2*w2-th)

epoch = 1
while True:
  for i in range(4):
    yp=NN(x1[i],w1,x2[i],w2,th)
    e[i]=yd[i]-yp
    w1+=lr*x1[i]*e[i]
    w2+=lr*x2[i]*e[i]
    result=checkForError(e)

  if(result):
    break;
  epoch+=1

print("epoch=",epoch,"and weight w1=",w1,"w2=",w2)
p1=1
p2=0
print("output for p1=",p1,"p2=",p2,"and result:",NN(p1,w1,p2,w2,th))