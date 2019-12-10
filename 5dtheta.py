import numpy as np
from scipy import interpolate
import matplotlib.pyplot as ml


file="5data.txt"
theta=np.loadtxt(file,usecols=[0])
d=np.loadtxt(file,usecols=[1])

x=theta
y=d
print(x,y)

ml.plot(x,y)
ml.show()
