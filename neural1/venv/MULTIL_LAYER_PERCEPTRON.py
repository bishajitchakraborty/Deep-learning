
#MULTI LAYER PERCEPTRON

import  numpy as np
import time

#define input features
input_features=np.array([[0,0],[0,1],[1,0],[1,1]])

#define target output
target_output=np.array([[0,1,1,0]])

#Reshaping out target output into vector
target_output=target_output.T

#Define weights, thresholds randomly

w13=0.5
w23=0.4
w14=0.9
w24=1.0
w35=-1.2
w45=1.1
theta3=0.8
theta4=-0.1
theta5=0.3

print("Value of w13, w23, w14, w24 , w35, w45, theta3, theta4, theta5")
print("Randomly initialized", w13, w23, w14, w24, w35, w45, theta3, theta4,theta5)

lr=0.1 #learning rate

#sigmoid function

def sigmoid(x):
    return 1/(1+np.exp(-x))


#main logic for neural network:
inputs=input_features
y3=y4=y5=del3=del5=0
error=[0]*4

#Running bour code 10000 times
epoch=0
tic =time.time()
while True:
    for i in range(4):
        y3=sigmoid(inputs[i][0]*w13+inputs[i][1]*w23-theta3)
        y4 = sigmoid(inputs[i][0] * w14 + inputs[i][1] * w24 - theta4)
        y5 = sigmoid(y3 * w35 + y4* w45- theta5)
        error[i]=target_output[i]-y5

        #error gradient for neuron 5

        del5=y5*(1-y5)*error[i]

        #weight traning
        dw35=lr*y3*del5
        dw45=lr*y4*del5
        dTheta5=lr*-1*del5

        #error gradiant for neuron 3,4
        del3=y3*(1-y3)*del5 *w35
        del4=y4*(1-y4)*del5*w45


        #weight training
        dw13=lr*inputs[i][0]*del3
        dw23 = lr * inputs[i][1] * del3
        dTheta3=lr*-1*del3
        dw14 = lr * inputs[i][0] * del4
        dw24 = lr * inputs[i][1] * del4
        dTheta4 = lr * -1 * del4

        #update the weights and threshold

        w13+=dw13
        w14 += dw14
        w23 += dw23
        w24 += dw24
        w35 += dw35
        w45 += dw45

        theta3+=dTheta3
        theta4 += dTheta4
        theta5 += dTheta5

sum=0
for i in range(4):
 sum+=error[i]*error[i]
 if(sum<=0.001):
  break;
if epoch % 1000 is 0:
    print("epoch",epoch)
epoch+=1

print("epoch=",epoch)
toc=time.time()
print("time is",(toc-tic)*1000,"ms")
print("value of : w13, w23, w14, w24, w35, w45,theta3,t6heta4,theta5")
print("Final update",w13, w23, w14, w24, w35, w45,theta3,theta4,theta5)


