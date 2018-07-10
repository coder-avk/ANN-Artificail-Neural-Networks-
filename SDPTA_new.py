import numpy as np
import sys
E=0
flag =0
c=1
k=1
W = np.random.randn(3,1)
# print("initial weight vector "+str(W))
# sys.exit()
X = np.array([[1,0.8,4,4.1,0.8],[1,0.9,4,4.2,0.7],[1,1,1,1,1]])
print(X)
g = input()
d = np.array([-1,-1,1,1,-1])
# W = W.reshape(3,1)
while flag==0:
    E=0
    for i in range(0,5):
        l = np.array(X[:,i]).reshape(3,1)
        # print(X[:,i])
        # sys.exit()
        net = np.dot(np.transpose(W),l)
        # print(net)
        if net < 0:
            o=-1
        if net > 0:
            o=1
        if net == 0:
            o = -1 *d[i]
        W = W + 0.5*c*(d[i]-o)*l
        # print(W)
        # z = input()
        E = E + 0.5*(d[i]-o)*(d[i]-o)
        # print(E)
        k=k+1
    if E == 0 :
        break

print(W)
print(k)
